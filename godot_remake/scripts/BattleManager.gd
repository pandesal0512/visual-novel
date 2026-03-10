extends Node
class_name BattleManager

# --- Signals ---
signal turn_started(turn_count: int)
signal execution_started()
signal execution_finished()
signal player_hp_changed(new_hp: int)
signal enemy_hp_changed(enemy_index: int, new_hp: int)
signal battle_won()
signal battle_lost()

# --- Runtime Classes ---
class Buff:
	var type: String
	var value: int
	var duration: int

	func _init(_type: String, _value: int, _duration: int):
		type = _type
		value = _value
		duration = _duration

class EnemyInstance:
	var data: EnemyData
	var hp: int
	var barrier: int = 0
	var buffs: Array[Buff] = []
	var slots: Array = [] # Can hold SkillData or EnemyIntentData
	var unlocked_intents_count: int = 2
	var skill_exp: int = 0
	var is_dead: bool = false
	var dodge_active: bool = false
	var dodge_expires_at_slot: int = -1
	var collapsed: bool = false
	var still_standing_triggered: bool = false

	func _init(_data: EnemyData):
		data = _data
		hp = data.max_hp

# --- State ---
@export var player_max_hp: int = 200
@export var player_max_energy: int = 20
@export var starting_energy: int = 10

var player_hp: int
var player_energy: int
var player_barrier: int = 0
var player_buffs: Array[Buff] = []

var enemies: Array[EnemyInstance] = []
var player_skills: Array[SkillData] = []
var full_skill_pool: Array[SkillData] = []
var chaos_pool: Array[SkillData] = []

var turn_count: int = 0
var current_max_slots: int = 2
var skill_exp: int = 0
var skill_exp_max: int = 100

var is_chaos: bool = false
var kare_shuffle_mode: bool = false
var used_skills_this_turn: Array[SkillData] = []
var skills_used_last_turn_types: Array[String] = []
var skills_used_this_turn_types: Array[String] = []

var rolled_one_last_turn: bool = false
var rolled_one_this_turn: bool = false
var total_skills_used_this_battle: int = 0

# --- Initialization ---
func setup_battle(_enemies_data: Array[EnemyData], _skill_pool: Array[SkillData], _is_chaos: bool = false):
	is_chaos = _is_chaos
	player_hp = player_max_hp
	player_energy = starting_energy
	full_skill_pool = _skill_pool

	enemies.clear()
	for data in _enemies_data:
		enemies.append(EnemyInstance.new(data))

	# Initial skills (first 2)
	player_skills = [full_skill_pool[0], full_skill_pool[1]]

	start_turn()

# --- Turn Logic ---
func start_turn():
	turn_count += 1
	skills_used_last_turn_types = skills_used_this_turn_types.duplicate()
	skills_used_this_turn_types.clear()
	rolled_one_last_turn = rolled_one_this_turn
	rolled_one_this_turn = false

	# Growth: starts at 2, +1 every 4 turns, max 6.
	current_max_slots = min(6, 2 + (turn_count - 1) / 4)

	player_energy = min(player_max_energy, player_energy + 2)
	used_skills_this_turn.clear()

	for enemy in enemies:
		if not enemy.is_dead:
			enemy.dodge_active = false
			enemy.collapsed = false
			enemy.slots.resize(current_max_slots)
			enemy.slots.fill(null)

			var num_enemy_intents = current_max_slots / 2
			var available_indices = range(current_max_slots)
			available_indices.shuffle()

			var possible_intents = enemy.data.intents.slice(0, enemy.unlocked_intents_count)
			# Filter by special logic (like RECIDIVISM) if needed
			possible_intents.shuffle()

			for i in range(num_enemy_intents):
				if possible_intents.is_empty(): break
				var idx = available_indices.pop_back()
				enemy.slots[idx] = possible_intents.pop_back()

	turn_started.emit(turn_count)

func add_skill_to_slot(skill: SkillData, enemy_idx: int, slot_idx: int) -> bool:
	if skill in used_skills_this_turn: return false
	if player_energy < skill.cost: return false

	var enemy = enemies[enemy_idx]
	if enemy.slots[slot_idx] is EnemyIntentData: return false

	# Replace existing player skill if any
	if enemy.slots[slot_idx] is SkillData:
		player_energy += enemy.slots[slot_idx].cost
		used_skills_this_turn.erase(enemy.slots[slot_idx])

	enemy.slots[slot_idx] = skill
	player_energy -= skill.cost
	used_skills_this_turn.append(skill)
	return true

func execute_turn():
	execution_started.emit()

	for slot_idx in range(current_max_slots):
		for enemy_idx in range(enemies.size()):
			var enemy = enemies[enemy_idx]
			if enemy.is_dead: continue

			var action = enemy.slots[slot_idx]
			if action == null: continue

			if action is SkillData:
				await resolve_player_skill(action, enemy_idx, slot_idx)
			elif action is EnemyIntentData:
				await resolve_enemy_intent(action, enemy_idx, slot_idx)

			if check_battle_end(): return

	# End of turn cleanup
	update_buffs()
	start_turn()
	execution_finished.emit()

# --- Resolution Helpers ---
func resolve_player_skill(skill: SkillData, enemy_idx: int, slot_idx: int):
	total_skills_used_this_battle += 1
	skills_used_this_turn_types.append(skill.skill_type)

	var value = calculate_skill_value(skill)
	if value == 1: rolled_one_this_turn = true

	match skill.skill_type:
		"attack":
			var enemy = enemies[enemy_idx]
			if enemy.dodge_active:
				# Trigger dodge animation/visuals
				enemy.dodge_active = false
			else:
				apply_damage(value, "enemy", enemy_idx)
				gain_exp(value * 5, "player")
		"barrier":
			player_barrier += value
		"buff":
			add_buff(skill.buff_type, value, skill.buff_duration, "player")
		"energy":
			player_energy = min(player_max_energy, player_energy + value)
		# Add other Chaos skill types here...

	await get_tree().create_timer(0.5).timeout # Placeholder for animation duration

func resolve_enemy_intent(intent: EnemyIntentData, enemy_idx: int, slot_idx: int):
	var enemy = enemies[enemy_idx]
	if enemy.collapsed:
		enemy.collapsed = false
		return

	match intent.intent_type:
		"attack":
			var damage = max(0, intent.damage + get_total_buff_value("damage", "enemy", enemy_idx))
			apply_damage(damage, "player")
		"barrier":
			enemy.barrier += intent.damage
		"buff":
			add_buff(intent.buff_type, intent.damage, intent.buff_duration, "enemy", enemy_idx)

	await get_tree().create_timer(0.5).timeout

# --- Core Mechanics ---
func apply_damage(amount: int, target: String, enemy_idx: int = 0):
	if target == "player":
		if player_barrier > 0:
			var absorbed = min(player_barrier, amount)
			player_barrier -= absorbed
			amount -= absorbed
		player_hp = max(0, player_hp - amount)
		player_hp_changed.emit(player_hp)
	else:
		var enemy = enemies[enemy_idx]
		if enemy.barrier > 0:
			var absorbed = min(enemy.barrier, amount)
			enemy.barrier -= absorbed
			amount -= absorbed
		enemy.hp = max(0, enemy.hp - amount)
		enemy_hp_changed.emit(enemy_idx, enemy.hp)
		if enemy.hp <= 0:
			enemy.is_dead = true

func add_buff(type: String, value: int, duration: int, target: String, enemy_idx: int = 0):
	var new_buff = Buff.new(type, value, duration)
	if target == "player":
		player_buffs.append(new_buff)
	else:
		enemies[enemy_idx].buffs.append(new_buff)

func update_buffs():
	var update_list = func(list: Array[Buff]):
		var i = list.size() - 1
		while i >= 0:
			list[i].duration -= 1
			if list[i].duration <= 0:
				list.remove_at(i)
			i -= 1

	update_list.call(player_buffs)
	for enemy in enemies:
		update_list.call(enemy.buffs)

func get_total_buff_value(type: String, target: String, enemy_idx: int = 0) -> int:
	var total = 0
	var list = player_buffs if target == "player" else enemies[enemy_idx].buffs
	for b in list:
		if b.type == type:
			total += b.value
	return total

func calculate_skill_value(skill: SkillData) -> int:
	if not is_chaos and not skill.is_chaos_skill:
		return skill.damage

	# Chaos logic translation
	match skill.skill_type:
		"attack":
			return randi_range(1, 20) + get_total_buff_value("damage", "player")
		"barrier", "buff", "energy":
			return randi_range(1, 50)
	return skill.damage

func gain_exp(amount: int, target: String, enemy_idx: int = 0):
	if target == "player":
		skill_exp += amount
		while skill_exp >= skill_exp_max:
			if player_skills.size() < full_skill_pool.size():
				skill_exp -= skill_exp_max
				player_skills.append(full_skill_pool[player_skills.size()])
			else:
				skill_exp = skill_exp_max
				break
	# Add enemy exp logic if needed

func check_battle_end() -> bool:
	if player_hp <= 0:
		battle_lost.emit()
		return true

	var all_dead = true
	for enemy in enemies:
		if not enemy.is_dead:
			all_dead = false
			break

	if all_dead:
		battle_won.emit()
		return true
	return false
