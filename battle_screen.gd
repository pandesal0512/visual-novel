extends Control

## ═══════════════════════════════════════════════════════
##  BattleScreen.gd — main controller
##  Attach to the root BattleScreen (Control) node
## ═══════════════════════════════════════════════════════

# ── Enums ───────────────────────────────────────────────
enum BattleMode { KARE, CHAOS }
enum EnemyMode  { SINGLE, MULTI }

# ── State ───────────────────────────────────────────────
var battle_mode   : BattleMode = BattleMode.KARE
var enemy_mode    : EnemyMode  = EnemyMode.SINGLE
var selected_card : int        = -1
var is_shuffling  : bool       = false
var is_exec       : bool       = false
var chaos_hand    : Array      = []

# ── Card data ───────────────────────────────────────────
const KARE_CARDS : Array[Dictionary] = [
	{ "name": "punch",           "cost": 4,  "dmg": 13, "cd": 2, "on_cd": false, "type": "attack",  "icon": "👊", "desc": "Powerful punch." },
	{ "name": "slap",            "cost": 2,  "dmg": 6,  "cd": 0, "on_cd": false, "type": "attack",  "icon": "🖐",  "desc": "Standard strike." },
	{ "name": "evade",           "cost": 4,  "dmg": 0,  "cd": 4, "on_cd": false, "type": "dodge",   "icon": "💨", "desc": "Dodges next attack." },
	{ "name": "Defense",         "cost": 3,  "dmg": 8,  "cd": 2, "on_cd": true,  "type": "barrier", "icon": "🛡",  "desc": "Gain 8 Defense." },
	{ "name": "yummers",         "cost": 0,  "dmg": 0,  "cd": 2, "on_cd": true,  "type": "energy",  "icon": "🍔", "desc": "Recover 10 energy.", "nrg": 10 },
	{ "name": "super cool kick", "cost": 6,  "dmg": 20, "cd": 6, "on_cd": false, "type": "ultimate","icon": "💥", "desc": "kick. that's it." },
]

const CHAOS_CARD_POOL : Array[Dictionary] = [
	{ "name": "interitus",     "cost": 3,  "dmg": 0, "cd": 0, "on_cd": false, "type": "attack",  "icon": "〜〜", "desc": "1–20 damage... probably" },
	{ "name": "Embrace",       "cost": 5,  "dmg": 0, "cd": 2, "on_cd": false, "type": "barrier", "icon": "◎",   "desc": "1–50 Defense. who knows" },
	{ "name": "Entropy",       "cost": 0,  "dmg": 0, "cd": 3, "on_cd": false, "type": "energy",  "icon": "∿",   "desc": "everything falls apart eventually." },
	{ "name": "Cataclysm",     "cost": 7,  "dmg": 0, "cd": 3, "on_cd": false, "type": "attack",  "icon": "⚡",  "desc": "1–30 damage... maybe" },
	{ "name": "dissolutum",    "cost": 6,  "dmg": 0, "cd": 2, "on_cd": false, "type": "dodge",   "icon": "⊘",   "desc": "Shift out of reality." },
	{ "name": "playing rough", "cost": 6,  "dmg": 0, "cd": 3, "on_cd": false, "type": "buff",    "icon": "R",   "desc": "1–50 Damage Buff. or 1. who knows." },
	{ "name": "??????",        "cost": 25, "dmg": 0, "cd": 4, "on_cd": false, "type": "ultimate","icon": "????","desc": "1–60 damage... ??? ?????" },
	{ "name": "Unravel",       "cost": 4,  "dmg": 0, "cd": 3, "on_cd": false, "type": "buff",    "icon": "U",   "desc": "Strips all buffs from the enemy." },
	{ "name": "Fracture",      "cost": 5,  "dmg": 0, "cd": 3, "on_cd": false, "type": "attack",  "icon": "X",   "desc": "Destroys barrier or deals 1–10 damage." },
	{ "name": "Corrode",       "cost": 5,  "dmg": 0, "cd": 2, "on_cd": false, "type": "attack",  "icon": "C",   "desc": "Reduces enemy damage for 2–3 attacks." },
	{ "name": "Inversion",     "cost": 6,  "dmg": 0, "cd": 3, "on_cd": false, "type": "buff",    "icon": "I",   "desc": "Flips enemy damage buff to a penalty." },
	{ "name": "Collapse",      "cost": 8,  "dmg": 0, "cd": 3, "on_cd": false, "type": "barrier", "icon": "L",   "desc": "Nullifies enemy's very next action." },
	{ "name": "Leech",         "cost": 6,  "dmg": 0, "cd": 3, "on_cd": false, "type": "buff",    "icon": "H",   "desc": "Steal a buff from the enemy." },
	{ "name": "Overload",      "cost": 7,  "dmg": 0, "cd": 3, "on_cd": false, "type": "attack",  "icon": "O",   "desc": "Deals damage equal to enemy barrier." },
]

# ── Enemy data ──────────────────────────────────────────
const ENEMY_SINGLE : Dictionary = {
	"name": "Butter", "hp": 90, "max_hp": 200, "chips": ["RECKONING"]
}
const ENEMY_BUTTER : Dictionary = {
	"name": "Butter", "hp": 175, "max_hp": 500, "chips": ["RECKONING"]
}
const ENEMY_AVA : Dictionary = {
	"name": "Ava", "hp": 220, "max_hp": 400, "chips": ["STILL STANDING", "MONUMENT (4)"]
}

# ── Default slot configs ────────────────────────────────
const SINGLE_SLOTS : Array[Dictionary] = [
	{ "owner": "player", "name": "punch",    "val": "13",
	  "intent": "SENTENCE — 25 damage", "intent_desc": "the verdict has been decided. there is no appeal." },
	{ "owner": "enemy",  "name": "SENTENCE", "val": "25",
	  "intent": "SENTENCE — 25 damage", "intent_desc": "the verdict has been decided. there is no appeal." },
	{ "owner": "player", "name": "evade",    "val": "—",  "intent": "", "intent_desc": "" },
	{ "owner": "empty",  "name": "",         "val": "",   "intent": "", "intent_desc": "" },
]
const BUTTER_SLOTS : Array[Dictionary] = [
	{ "owner": "player", "name": "punch",    "val": "13",    "intent": "Butter: SENTENCE — 25 dmg", "intent_desc": "the verdict has been decided." },
	{ "owner": "enemy",  "name": "SENTENCE", "val": "25",    "intent": "Butter: SENTENCE — 25 dmg", "intent_desc": "the verdict has been decided." },
	{ "owner": "player", "name": "evade",    "val": "—",     "intent": "", "intent_desc": "" },
	{ "owner": "empty",  "name": "",         "val": "",      "intent": "", "intent_desc": "" },
	{ "owner": "enemy",  "name": "VERDICT",  "val": "+def",  "intent": "Butter: VERDICT — defense",  "intent_desc": "law does not bend. gains 5 Defense." },
	{ "owner": "empty",  "name": "",         "val": "",      "intent": "", "intent_desc": "" },
]
const AVA_SLOTS : Array[Dictionary] = [
	{ "owner": "empty",  "name": "",         "val": "",      "intent": "", "intent_desc": "" },
	{ "owner": "enemy",  "name": "DRAIN",    "val": "33k",   "intent": "Ava: DRAIN — 33,333 dmg",   "intent_desc": "the city crumbles. once per turn." },
	{ "owner": "player", "name": "Embrace",  "val": "???",   "intent": "", "intent_desc": "" },
	{ "owner": "empty",  "name": "",         "val": "",      "intent": "", "intent_desc": "" },
	{ "owner": "enemy",  "name": "MONUMENT", "val": "barrier","intent": "Ava: MONUMENT — barrier",   "intent_desc": "gains barrier equal to turns passed." },
	{ "owner": "empty",  "name": "",         "val": "",      "intent": "", "intent_desc": "" },
]

# ── Taunts ──────────────────────────────────────────────
const TAUNTS_SINGLE : Array[Array] = [
	["Butter", "haha!! no way you are surviving this"],
	["Butter", "is that really all you've got?"],
	["Butter", "okay but like... you tried"],
]
const TAUNTS_MULTI : Array[Array] = [
	["Butter", "sorry, Kare."],
	["Ava",    "every civilization must fall."],
	["Butter", "we're not even trying yet."],
	["Ava",    "resistance is statistically futile."],
]

# ── Node references (mark each as Unique Name in owner) ─
@onready var screen_bg      : ColorRect      = %ScreenBG
@onready var player_name_lb : Label          = %PlayerName
@onready var player_hp_bar  : ProgressBar    = %PlayerHPBar
@onready var player_hp_num  : Label          = %PlayerHPNum
@onready var player_en_bar  : ProgressBar    = %PlayerEnBar
@onready var player_en_num  : Label          = %PlayerEnNum
@onready var chip_row       : HBoxContainer  = %ChipRow
@onready var turn_badge     : Label          = %TurnBadge
@onready var team_label     : Label          = %TeamLabel
@onready var enemy_stats    : VBoxContainer  = %EnemyStats
@onready var intent_bar     : PanelContainer = %IntentBar
@onready var intent_title   : Label          = %IntentTitle
@onready var intent_desc_lb : Label          = %IntentDesc
@onready var taunt_bubble   : Control        = %TauntBubble
@onready var taunt_speaker  : Label          = %TauntSpeaker
@onready var taunt_text     : Label          = %TauntText
@onready var slots_inner    : HBoxContainer  = %SlotsInner
@onready var slot_rows_col  : VBoxContainer  = %SlotRowsCol
@onready var confirm_btn    : Button         = %ConfirmBtn
@onready var cards_row      : HBoxContainer  = %CardsRow
@onready var skill_popup    : PanelContainer = %SkillPopup
@onready var popup_name_lb  : Label          = %PopupName
@onready var popup_cost_lb  : Label          = %PopupCost
@onready var popup_dmg_lb   : Label          = %PopupDmg
@onready var popup_cd_lb    : Label          = %PopupCD
@onready var popup_desc_lb  : Label          = %PopupDesc
@onready var chaos_num_box  : PanelContainer = %ChaosNumberBox
@onready var chaos_num_val  : Label          = %ChaosValue
@onready var energy_warning : Label          = %EnergyWarning

# Preload component scenes
const CardUIScene := preload("res://scenes/battle/CardUI.tscn")
const SlotUIScene := preload("res://scenes/battle/SlotUI.tscn")

# Ink colors (flipped by mode)
var _ink   : Color = Color.BLACK
var _paper : Color = Color.WHITE

# Tween for taunt fade
var _taunt_tween : Tween = null

# ── Lifecycle ───────────────────────────────────────────
func _ready() -> void:
	chaos_hand = CHAOS_CARD_POOL.slice(0, 4)
	confirm_btn.pressed.connect(_on_confirm_pressed)
	render()

# ── Full render ─────────────────────────────────────────
func render() -> void:
	_ink   = Color.WHITE if battle_mode == BattleMode.CHAOS else Color.BLACK
	_paper = Color.BLACK if battle_mode == BattleMode.CHAOS else Color.WHITE

	_apply_bg()
	_render_player_stats()
	_render_enemy_stats()
	_render_slots()
	_render_cards()
	_update_sprite_positions()
	skill_popup.visible  = false
	intent_bar.visible   = false
	taunt_bubble.visible = false
	selected_card        = -1

# ── Background ──────────────────────────────────────────
func _apply_bg() -> void:
	screen_bg.color = _paper

# ── Player stats ────────────────────────────────────────
func _render_player_stats() -> void:
	player_name_lb.text = "Kare" if battle_mode == BattleMode.KARE else "Chaos"
	player_name_lb.add_theme_color_override("font_color", _ink)

	player_hp_bar.value = 72.0  # 144/200
	player_en_bar.value = 60.0  # 12/20
	player_hp_num.text  = "144 / 200"
	player_en_num.text  = "12 / 20"

	turn_badge.text    = "Turn 4 · %s slots" % ("6" if enemy_mode == EnemyMode.MULTI else "4")
	turn_badge.add_theme_color_override("font_color", _ink)

	team_label.visible = enemy_mode == EnemyMode.MULTI
	team_label.text    = "Butter + Ava · team fight"

	# Chips
	for child in chip_row.get_children():
		child.queue_free()
	for chip_text in ["DEF 8", "DMG +5 (2t)"]:
		var chip := Label.new()
		chip.text = chip_text
		var sb   := StyleBoxFlat.new()
		sb.bg_color = Color(_ink, 0.08)
		sb.set_border_width_all(1)
		sb.border_color = Color(_ink, 0.3)
		sb.content_margin_left = 7; sb.content_margin_right = 7
		sb.content_margin_top  = 1; sb.content_margin_bottom = 1
		chip.add_theme_stylebox_override("normal", sb)
		chip.add_theme_color_override("font_color", _ink)
		chip_row.add_child(chip)

# ── Enemy stats ─────────────────────────────────────────
func _render_enemy_stats() -> void:
	for child in enemy_stats.get_children():
		child.queue_free()

	var enemies := [ENEMY_BUTTER, ENEMY_AVA] if enemy_mode == EnemyMode.MULTI else [ENEMY_SINGLE]
	for i in enemies.size():
		if i > 0:
			var sep := HSeparator.new()
			var sep_style := StyleBoxFlat.new()
			sep_style.bg_color = Color(_ink, 0.2)
			sep_style.content_margin_top = 5; sep_style.content_margin_bottom = 5
			enemy_stats.add_child(sep)
		_add_enemy_block(enemies[i])

func _add_enemy_block(e: Dictionary) -> void:
	var nm := Label.new()
	nm.text = e.name
	nm.add_theme_color_override("font_color", _ink)
	nm.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	enemy_stats.add_child(nm)

	var hp_row := HBoxContainer.new()
	hp_row.alignment = BoxContainer.ALIGNMENT_END
	hp_row.add_theme_constant_override("separation", 8)

	var lbl := Label.new()
	lbl.text = "HP"
	lbl.add_theme_color_override("font_color", Color(_ink, 0.5))
	lbl.custom_minimum_size.x = 32

	var bar := ProgressBar.new()
	bar.value = float(e.hp) / float(e.max_hp) * 100.0
	bar.custom_minimum_size = Vector2(135, 12)
	bar.show_percentage = false

	var nums := Label.new()
	nums.text = "%d / %d" % [e.hp, e.max_hp]
	nums.add_theme_color_override("font_color", Color(_ink, 0.5))

	hp_row.add_child(lbl); hp_row.add_child(bar); hp_row.add_child(nums)
	enemy_stats.add_child(hp_row)

	var chip_box := HBoxContainer.new()
	chip_box.alignment = BoxContainer.ALIGNMENT_END
	chip_box.add_theme_constant_override("separation", 5)
	for chip_text in e.get("chips", []):
		var chip := Label.new()
		chip.text = chip_text
		var sb := StyleBoxFlat.new()
		sb.bg_color = Color(_ink, 0.0)
		sb.set_border_width_all(1)
		sb.border_color = Color(_ink, 0.3)
		sb.content_margin_left = 7; sb.content_margin_right = 7
		sb.content_margin_top  = 1; sb.content_margin_bottom = 1
		chip.add_theme_stylebox_override("normal", sb)
		chip.add_theme_color_override("font_color", Color(_ink, 0.6))
		chip_box.add_child(chip)
	enemy_stats.add_child(chip_box)

# ── Slots ───────────────────────────────────────────────
func _render_slots() -> void:
	for child in slot_rows_col.get_children():
		child.queue_free()

	if enemy_mode == EnemyMode.SINGLE:
		slot_rows_col.add_child(_make_slot_row("battle\nrow", SINGLE_SLOTS))
	else:
		slot_rows_col.add_child(_make_slot_row("Butter's\nrow", BUTTER_SLOTS))
		var div := HSeparator.new()
		var div_style := StyleBoxFlat.new()
		div_style.bg_color = Color(_ink, 0.15)
		slot_rows_col.add_child(div)
		slot_rows_col.add_child(_make_slot_row("Ava's\nrow", AVA_SLOTS))

	# Style SlotsInner background
	var inner_style := StyleBoxFlat.new()
	inner_style.bg_color       = Color(_paper, 0.94)
	inner_style.border_color   = Color(_ink, 0.2)
	inner_style.border_width_top    = 2
	inner_style.border_width_bottom = 2
	slots_inner.add_theme_stylebox_override("panel", inner_style)

func _make_slot_row(row_label: String, slots: Array) -> HBoxContainer:
	var row := HBoxContainer.new()
	row.add_theme_constant_override("separation", 0)
	row.custom_minimum_size.y = 68 if enemy_mode == EnemyMode.SINGLE else 66

	var lbl := Label.new()
	lbl.text = row_label
	lbl.custom_minimum_size.x = 54
	lbl.vertical_alignment   = VERTICAL_ALIGNMENT_CENTER
	lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	lbl.add_theme_color_override("font_color", Color(_ink, 0.35))
	row.add_child(lbl)

	var hbox := HBoxContainer.new()
	hbox.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	hbox.add_theme_constant_override("separation", 7)

	for slot_data : Dictionary in slots:
		var slot_inst := SlotUIScene.instantiate()
		slot_inst.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		slot_inst.setup(slot_data, battle_mode == BattleMode.CHAOS)
		slot_inst.clicked.connect(_on_slot_clicked.bind(slot_data))
		hbox.add_child(slot_inst)

	row.add_child(hbox)
	return row

# ── Cards ───────────────────────────────────────────────
func _render_cards() -> void:
	for child in cards_row.get_children():
		child.queue_free()

	var hand : Array = KARE_CARDS if battle_mode == BattleMode.KARE else chaos_hand

	for i in hand.size():
		var card_inst := CardUIScene.instantiate()
		card_inst.setup(hand[i], battle_mode == BattleMode.CHAOS)
		var idx  : int        = i
		var data : Dictionary = hand[i]
		card_inst.clicked.connect(_on_card_clicked.bind(idx, data))
		cards_row.add_child(card_inst)

# ── Sprite positions ────────────────────────────────────
func _update_sprite_positions() -> void:
	# Sprites sit just above the slot strip
	# single: bottom 206px   multi: bottom 278px
	pass  # TODO: position %PlayerSil and %EnemySil1/2 once sprites are in scene

# ── Card interaction ────────────────────────────────────
func _on_card_clicked(index: int, data: Dictionary) -> void:
	if is_shuffling: return

	if selected_card == index:
		# Deselect — close popup
		selected_card = -1
		skill_popup.visible = false
	else:
		selected_card = index
		_show_skill_popup(data)

func _show_skill_popup(data: Dictionary) -> void:
	popup_name_lb.text = data.get("name", "")
	popup_cost_lb.text = "Cost: %d Energy" % data.get("cost", 0)
	var dmg : int = data.get("dmg", 0)
	var nrg : int = data.get("nrg", 0)
	if dmg > 0:
		popup_dmg_lb.text = "Damage: %d" % dmg
	elif nrg > 0:
		popup_dmg_lb.text = "Energy regen: %d" % nrg
	else:
		popup_dmg_lb.text = "Type: %s" % data.get("type", "")
	var cd : int = data.get("cd", 0)
	popup_cd_lb.text   = "Cooldown: %d turns" % cd if cd > 0 else ""
	popup_desc_lb.text = data.get("desc", "")

	# Style popup panel
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(_paper, 0.97)
	sb.set_border_width_all(2)
	sb.border_color = _ink
	skill_popup.add_theme_stylebox_override("panel", sb)

	popup_name_lb.add_theme_color_override("font_color", _ink)
	popup_cost_lb.add_theme_color_override("font_color", Color(_ink, 0.6))
	popup_dmg_lb.add_theme_color_override("font_color",  Color(_ink, 0.6))
	popup_cd_lb.add_theme_color_override("font_color",   Color(_ink, 0.6))
	popup_desc_lb.add_theme_color_override("font_color", Color(_ink, 0.6))

	skill_popup.visible = true

# ── Slot interaction ────────────────────────────────────
func _on_slot_clicked(data: Dictionary) -> void:
	if data.get("owner") == "enemy" and data.get("intent", "") != "":
		# Toggle intent bar
		var same := intent_title.text == data.intent and intent_bar.visible
		intent_bar.visible = not same
		if not same:
			intent_title.text   = data.intent
			intent_desc_lb.text = data.intent_desc
			_style_intent_bar()
	elif data.get("owner") == "empty" and selected_card >= 0:
		# TODO: place card into slot
		pass

func _style_intent_bar() -> void:
	var sb := StyleBoxFlat.new()
	sb.bg_color              = Color(_paper, 0.92)
	sb.border_color          = _ink
	sb.border_width_left     = 4
	sb.border_width_top      = 1
	sb.border_width_right    = 1
	sb.border_width_bottom   = 1
	intent_bar.add_theme_stylebox_override("panel", sb)
	intent_title.add_theme_color_override("font_color", _ink)
	intent_desc_lb.add_theme_color_override("font_color", Color(_ink, 0.55))

# ── Screen click — close popups ─────────────────────────
func _gui_input(event: InputEvent) -> void:
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
		skill_popup.visible  = false
		intent_bar.visible   = false
		selected_card        = -1

# ── Confirm ─────────────────────────────────────────────
func _on_confirm_pressed() -> void:
	if is_shuffling: return
	_fire_taunt()
	if battle_mode == BattleMode.CHAOS:
		_shuffle_chaos_cards()

# ── Taunt bubble ────────────────────────────────────────
func show_taunt(speaker: String, text: String) -> void:
	taunt_speaker.text   = speaker
	taunt_text.text      = text
	taunt_bubble.visible = true
	taunt_bubble.modulate.a = 1.0

	# Style bubble
	taunt_bubble.queue_redraw()

	if _taunt_tween:
		_taunt_tween.kill()
	_taunt_tween = create_tween()
	_taunt_tween.tween_interval(2.5)
	_taunt_tween.tween_property(taunt_bubble, "modulate:a", 0.0, 0.25)
	_taunt_tween.tween_callback(func(): taunt_bubble.visible = false)

func _fire_taunt() -> void:
	var pool := TAUNTS_MULTI if enemy_mode == EnemyMode.MULTI else TAUNTS_SINGLE
	var pick : Array = pool[randi() % pool.size()]
	show_taunt(pick[0], pick[1])

# ── Chaos shuffle ────────────────────────────────────────
func _shuffle_chaos_cards() -> void:
	is_shuffling = true
	skill_popup.visible = false
	selected_card = -1

	var new_hand := _pick_new_chaos_hand()
	var cards    := cards_row.get_children()

	# Animate each card reel
	for i in cards.size():
		if i < new_hand.size():
			_animate_card_reel(cards[i], new_hand[i], i * 0.12)

	var total_time := cards.size() * 0.12 + 1.6
	await get_tree().create_timer(total_time).timeout

	chaos_hand   = new_hand
	is_shuffling = false
	_render_cards()

func _animate_card_reel(card_node : Control, new_data : Dictionary, delay : float) -> void:
	const SYMBOLS := ["#", "$", "%", "^", "&", "*", "@", "!", "?", "~", "∿", "⊘", "◎", "〜"]
	await get_tree().create_timer(delay).timeout

	var tween := create_tween()
	# 22 fast flicker frames at 50ms
	for _j in 22:
		tween.tween_callback(func(): card_node.modulate.a = randf_range(0.15, 0.9))
		tween.tween_interval(0.05)
	# 6 slow-down frames
	for _k in 6:
		tween.tween_callback(func(): card_node.modulate.a = 0.7)
		tween.tween_interval(0.08)
	# Snap to full opacity — the actual card content update happens after in _shuffle_chaos_cards
	tween.tween_property(card_node, "modulate:a", 1.0, 0.06)
	# Bounce: dip down then up
	tween.tween_property(card_node, "position:y", card_node.position.y + 4, 0.06)
	tween.tween_property(card_node, "position:y", card_node.position.y - 3, 0.06)
	tween.tween_property(card_node, "position:y", card_node.position.y,     0.06)

func _pick_new_chaos_hand() -> Array:
	var core  : Array = CHAOS_CARD_POOL.slice(0, 7).duplicate()
	var extra : Array = CHAOS_CARD_POOL.slice(7).duplicate()
	core.shuffle()
	extra.shuffle()
	# Interleave core/extra, mirroring the game's unlock logic
	var interleaved : Array = []
	for i in max(core.size(), extra.size()):
		if i < core.size():  interleaved.append(core[i])
		if i < extra.size(): interleaved.append(extra[i])
	return interleaved.slice(0, chaos_hand.size())

# ── Exec phase toggle ────────────────────────────────────
func toggle_exec() -> void:
	is_exec = not is_exec
	chaos_num_box.visible = is_exec and battle_mode == BattleMode.CHAOS
	if chaos_num_box.visible:
		_animate_chaos_number()

func _animate_chaos_number() -> void:
	const CHARS := "$#%^&*@!?~<>0123456789"
	var final_val : int = randi_range(1, 20)
	var tween := create_tween()
	for i in 22:
		tween.tween_callback(func():
			var c1 := CHARS[randi() % CHARS.length()]
			var c2 := CHARS[randi() % CHARS.length()]
			chaos_num_val.text = c1 + c2
		)
		tween.tween_interval(0.04)
	tween.tween_callback(func(): chaos_num_val.text = "%02d" % final_val)

# ── Public mode switchers ───────────────────────────────
func set_battle_mode(mode: BattleMode) -> void:
	battle_mode  = mode
	chaos_hand   = CHAOS_CARD_POOL.slice(0, 4)
	is_exec      = false
	render()

func set_enemy_mode(mode: EnemyMode) -> void:
	enemy_mode = mode
	render()
