



image kare_idle = "kare_idle.png"
image kare_hit = "kare_hit.png"

image chaos_idle = "chaos_idle.png"
image chaos_hit = "chaos_hit.png"

image butter_idle = "butter_idle.png"
image butter_hit = "butter_hit.png"

image seriousbutter_idle = "seriousbutter_idle.png"
image seriousbutter_hit = "seriousbutter_hit.png"

image lumpi_idle = "lumpi_idle.png"
image lumpi_attack = "lumpi_attack.png"
image lumpi_hit = "lumpi_hit.png"

image lumpiwheelchair_idle = "lumpiwheelchair_idle.png"
image lumpiwheelchair_hit = "lumpiwheelchair_hit.png"

image ava_idle = "ava_idle.png"
image ava_hit = "ava_hit.png"
image order_idle = "order_idle.png"
image order_attack = "order_attack.png"
image order_hit = "order_hit.png"
image order_neutral = "order_neutral.png"

image order_normal_sprite = "order_normal_sprite.png"
image order_hard_sprite = "order_hard_sprite.png"
image order_block_sprite = "order_block_sprite.png"
image order_dodge_sprite = "order_dodge_sprite.png"
image order_buff_sprite = "order_buff_sprite.png"
image order_ultimate_sprite = "order_ultimate_sprite.png"
image order_energy_sprite = "order_energy_sprite.png"

image chaos_projectile_normal = "chaos_projectile_normal.png"
image chaos_projectile_hard = "chaos_projectile_hard.png"
image chaos_projectile_ultimate_1 = "chaos_projectile_ultimate.png"
image chaos_projectile_ultimate_2 = "chaos_projectile_ultimate.png"
image chaos_projectile_ultimate_3 = "chaos_projectile_ultimate.png"

image dobe_sprite = "dobe_sprite.png"
image dobe_attack = "dobe_fight.png"

# --- Action Sprites ---
image kare_normal_sprite = "kare_normal_sprite.png"
image kare_hard_sprite = "kare_hard_sprite.png"
image kare_block_sprite = "kare_block_sprite.png"
image kare_dodge_sprite = "kare_dodge_sprite.png"
image kare_buff_sprite = "kare_buff_sprite.png"
image kare_ultimate_sprite = "kare_ultimate_sprite.png"
image kare_energy_sprite = "kare_energy_sprite.png"

image chaos_normal_sprite = "chaos_normal_sprite.png"
image chaos_hard_sprite = "chaos_hard_sprite.png"
image chaos_block_sprite = "chaos_block_sprite.png"
image chaos_dodge_sprite = "chaos_dodge_sprite.png"
image chaos_buff_sprite = "chaos_buff_sprite.png"
image chaos_ultimate_sprite = "chaos_ultimate_sprite.png"
image chaos_energy_sprite = "chaos_energy_sprite.png"

image butter_normal_sprite = "butter_normal_sprite.png"
image butter_hard_sprite = "butter_hard_sprite.png"
image butter_block_sprite = "butter_block_sprite.png"
image butter_dodge_sprite = "butter_dodge_sprite.png"
image butter_ultimate_sprite = "butter_ultimate_sprite.png"
image butter_energy_sprite = "butter_energy_sprite.png"

image serious_butter_normal_sprite = "serious_butter_normal_sprite.png"
image serious_butter_hard_sprite = "serious_butter_hard_sprite.png"
image serious_butter_block_sprite = "serious_butter_block_sprite.png"
image serious_butter_dodge_sprite = "serious_butter_dodge_sprite.png"
image serious_butter_ultimate_sprite = "serious_butter_ultimate_sprite.png"
image serious_butter_energy_sprite = "serious_butter_energy_sprite.png"

image lumpi_normal_sprite = "lumpi_normal_sprite.png"
image lumpi_hard_sprite = "lumpi_hard_sprite.png"
image lumpi_block_sprite = "lumpi_block_sprite.png"
image lumpi_dodge_sprite = "lumpi_dodge_sprite.png"
image lumpi_ultimate_sprite = "lumpi_ultimate_sprite.png"
image lumpi_energy_sprite = "lumpi_energy_sprite.png"

image lumpi_wheelchair_normal_sprite = "lumpi_wheelchair_normal_sprite.png"
image lumpi_wheelchair_hard_sprite = "lumpi_wheelchair_hard_sprite.png"
image lumpi_wheelchair_block_sprite = "lumpi_wheelchair_block_sprite.png"
image lumpi_wheelchair_dodge_sprite = "lumpi_wheelchair_dodge_sprite.png"
image lumpi_wheelchair_ultimate_sprite = "lumpi_wheelchair_ultimate_sprite.png"
image lumpi_wheelchair_energy_sprite = "lumpi_wheelchair_energy_sprite.png"

image ava_normal_sprite = "ava_normal_sprite.png"
image ava_hard_sprite = "ava_hard_sprite.png"
image ava_block_sprite = "ava_block_sprite.png"
image ava_dodge_sprite = "ava_dodge_sprite.png"
image ava_ultimate_sprite = "ava_ultimate_sprite.png"
image ava_energy_sprite = "ava_energy_sprite.png"

# --- Card Images (for hand display) ---
image card_kare_normal = "card_kare_normal.png"
image card_kare_block = "card_kare_block.png"
image card_kare_energy = "card_kare_energy.png"
image card_kare_hard = "card_kare_hard.png"
image card_kare_dodge = "card_kare_dodge.png"
image card_kare_ultimate = "card_kare_ultimate.png"

image card_chaos_normal = "card_chaos_normal.png"
image card_chaos_block = "card_chaos_block.png"
image card_chaos_energy = "card_chaos_energy.png"
image card_chaos_hard = "card_chaos_hard.png"
image card_chaos_dodge = "card_chaos_dodge.png"
image card_chaos_ultimate = "card_chaos_ultimate.png"

image bg_butter    = Solid("#ffffff") 
image bg_lumpi     = Solid("#ffffff")
image bg_lumpi_wc  = Solid("#ffffff")
image bg_serious   = Solid("#ffffff")
image bg_boss1     = Solid("#ffffff")
image bg_boss2     = Solid("#ffffff")

# Helper to create an outline image (1px black border with transparent center)
image sketchy_outline_img = Composite((100, 100),
    (0, 0),  Solid("#6d6d6d", xsize=100, ysize=2),   # top, 2px
    (0, 98), Solid("#6d6d6d", xsize=100, ysize=2),   # bottom, 2px
    (0, 2),  Solid("#6d6d6d", xsize=2,   ysize=96),  # left, 2px
    (98, 2), Solid("#6d6d6d", xsize=2,   ysize=96),  # right, 2px
)
image sketchy_bar_outline = Frame("sketchy_outline_img", 2, 2, 2, 2)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
# --- Transforms ---
transform fight_left:
    xpos 0.35
    ypos 0.8
    anchor (0.5, 1.0)
    zoom 1.0

transform fight_right:
    xpos 0.65
    ypos 0.8
    anchor (0.5, 1.0)
    zoom 1.0

transform chaos_projectile_fly:
    xpos 0.35 ypos 0.6
    anchor (0.5, 0.5)
    linear 0.25 xpos 0.75
    linear 0.05 alpha 0.0

transform chaos_projectile_fly_hard:
    xpos 0.35 ypos 0.6
    anchor (0.5, 0.5)
    linear 0.2 xpos 0.75
    linear 0.05 alpha 0.0

transform chaos_projectile_fly_2:
    xpos 0.35 ypos 0.55
    anchor (0.5, 0.5)
    linear 0.2 xpos 0.75
    linear 0.05 alpha 0.0

transform chaos_projectile_fly_3:
    xpos 0.35 ypos 0.65
    anchor (0.5, 0.5)
    linear 0.2 xpos 0.75
    linear 0.05 alpha 0.0


transform enemy_charge_right:
    ease 0.2 xpos 0.5
    ease 0.2 xpos 0.65

transform energy_warning_fade:
    alpha 0.0
    linear 0.1 alpha 1.0
    pause 1.7
    linear 0.2 alpha 0.0

transform card_selected_zoom:
    ease 0.1 zoom 1.1

transform card_idle_zoom:
    ease 0.1 zoom 1.0

init python:
    import random

    def scramble_hp(hp):
        symbols = "$#%^&*@!Fa~?<>"
        result = str(hp)
        scrambled = ""
        for ch in result:
            if renpy.random.random() < 0.6:
                scrambled += renpy.random.choice(symbols)
            else:
                scrambled += ch
        return scrambled

    def get_chaos_random_value(bm, skill):
        if not getattr(bm, "is_chaos", False):
            if skill.type == "attack":
                return skill.damage + bm.get_total_buff_value("damage", target="player")
            return skill.damage
        if skill.type == "attack":
            if skill.name == "interitus": return renpy.random.randint(1, 20)
            if skill.name == "Cataclysm": return renpy.random.randint(1, 30)
            if skill.name == "??????": return renpy.random.randint(1, 60)
            return renpy.random.randint(1, 20)
        if skill.type in ["barrier", "buff"]:
            return renpy.random.randint(1, 50)
        return skill.damage


    def get_serious_butter():
        intents = get_enemy_intents("law")
        sprites = {'idle': 'seriousbutter_idle', 'attack': 'seriousbutter_attack', 'hit': 'seriousbutter_hit'}
        return Enemy('Butter', 300, sprites, intents)

    def get_butter():
        intents = get_enemy_intents("butter")
        sprites = {'idle': 'butter_idle', 'attack': 'butter_attack', 'hit': 'butter_hit'}
        return Enemy('Butter', 200, sprites, intents)

    def get_dodge_anim(char_name):
        # Normalize name to match label convention: lowercase, underscores instead of spaces/chars
        name = char_name.lower()
        name = name.replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")
        return name + "_dodge_anim"

    class Skill:
        def __init__(self, name, cost=0, damage=0, energy_regen=0, cooldown=0, type="attack", desc="", animation=None, buff_type=None, buff_duration=0, card_image=None):
            self.name = name
            self.cost = cost
            self.damage = damage
            self.energy_regen = energy_regen
            self.cooldown = cooldown
            self.current_cooldown = 0
            self.type = type
            self.desc = desc
            self.animation = animation
            self.buff_type = buff_type
            self.buff_duration = buff_duration
            self.card_image = card_image

    class EnemyIntent:
        def __init__(self, name, damage=0, desc="", animation=None, type="attack", buff_type=None, buff_duration=0, card_image=None, cooldown=0):
            self.name = name
            self.damage = damage
            self.desc = desc
            self.animation = animation
            self.type = type
            self.buff_type = buff_type
            self.buff_duration = buff_duration
            self.card_image = card_image
            self.cooldown = cooldown
            self.current_cooldown = 0

    class Enemy:
        def __init__(self, name, max_hp, sprites, intents):
            self.name = name
            self.hp = max_hp
            self.max_hp = max_hp
            self.sprites = sprites
            self.full_intent_pool = intents
            self.unlocked_intents_count = 2
            self.skill_exp = 0
            self.skill_exp_max = 100
            self.slots = []
            self.barrier = 0
            self.buffs = []
            self.dodge_active = False
            self.dodge_expires_at_slot = -1
            self.is_dead = False

        @property
        def intents(self):
            # Returns only the currently unlocked intents
            return self.full_intent_pool[:self.unlocked_intents_count]

    class BattleManager:
        tutorial = False
        dobe_helps = False
        is_chaos = False
        def __init__(self, player_max_hp, enemies=None, starting_slots=2, player_sprites=None, starting_energy=10, max_energy=10, tutorial=False, dobe_helps=False, is_chaos=False, skill_overrides=None):
            self.player_hp = player_max_hp
            self.player_max_hp = player_max_hp
            self.player_energy = starting_energy
            self.player_max_energy = max_energy
            self.player_barrier = 0
            self.player_buffs = []
            self.tutorial = tutorial
            self.dobe_helps = dobe_helps
            self.is_chaos = is_chaos
            self.skill_overrides = skill_overrides or {}

            if isinstance(enemies, list):
                self.enemies = enemies
            else:
                self.enemies = []

            self.player_sprites = player_sprites or {"idle": "kare_idle", "attack": "kare_attack", "hit": "kare_hit"}

            self.starting_slots = 2
            self.current_max_slots = 2
            self.slots = []

            self.dodge_active = False
            self.dodge_expires_at_slot = -1
            self.player_skills = []
            self.full_skill_pool = []
            self.skill_exp = 0
            self.skill_exp_max = 100

            self.used_skills_this_turn = []
            self.turn_count = 0
            self.selected_skill = None
            self.selected_intent = None
            self.selected_slot_index = -1
            self.selected_enemy_index = -1
            self.hovered_skill = None
            self.show_energy_warning = False
            self.is_dodged = False

        def initialize_skills(self, is_chaos):
            char_name = "chaos" if is_chaos else "kare"
            self.full_skill_pool = get_character_skills(char_name)
            for skill in self.full_skill_pool:
                if skill.name in self.skill_overrides:
                    for attr, value in self.skill_overrides[skill.name].items():
                        setattr(skill, attr, value)
            self.player_skills = self.full_skill_pool[:2]
            self.skill_exp = 0

        def select_skill(self, skill):
            if self.selected_skill == skill:
                self.selected_skill = None
            else:
                self.selected_skill = skill
            self.selected_intent = None
            self.selected_slot_index = -1

        def select_intent(self, intent, enemy_idx, slot_idx):
            if self.selected_intent == intent and self.selected_enemy_index == enemy_idx and self.selected_slot_index == slot_idx:
                self.selected_intent = None
                self.selected_enemy_index = -1
                self.selected_slot_index = -1
            else:
                self.selected_intent = intent
                self.selected_enemy_index = enemy_idx
                self.selected_slot_index = slot_idx
            self.selected_skill = None

        def add_to_slot(self, skill, enemy_idx, slot_idx):
            if skill in self.used_skills_this_turn:
                return False

            enemy = self.enemies[enemy_idx]
            old_action = enemy.slots[slot_idx]

            # Check energy, accounting for potential refund if replacing a skill
            needed_energy = skill.cost
            if isinstance(old_action, Skill):
                needed_energy -= old_action.cost

            if self.player_energy < needed_energy:
                self.show_energy_warning = True
                return False

            if skill.current_cooldown == 0:
                # Refund old skill if slot is already occupied by a Skill
                if isinstance(old_action, Skill):
                    self.player_energy += old_action.cost
                    if old_action in self.used_skills_this_turn:
                        self.used_skills_this_turn.remove(old_action)
                elif isinstance(old_action, EnemyIntent):
                    # Cannot replace enemy intents
                    return False

                # Place new skill
                enemy.slots[slot_idx] = skill
                self.player_energy -= skill.cost
                self.used_skills_this_turn.append(skill)
                self.selected_skill = None
                renpy.sound.play("audio/freesound_community-pageturn-102978.mp3")
                return True
            return False

        def remove_from_slot(self, enemy_idx, slot_idx):
            enemy = self.enemies[enemy_idx]
            action = enemy.slots[slot_idx]
            if isinstance(action, Skill):
                self.player_energy += action.cost
                if action in self.used_skills_this_turn:
                    self.used_skills_this_turn.remove(action)
                enemy.slots[slot_idx] = None

        def clear_queue(self):
            for e_idx, enemy in enumerate(self.enemies):
                for s_idx in range(len(enemy.slots)):
                    if isinstance(enemy.slots[s_idx], Skill):
                        self.remove_from_slot(e_idx, s_idx)

        def get_skill_slot_info(self, skill):
            for e_idx, enemy in enumerate(self.enemies):
                for s_idx, s in enumerate(enemy.slots):
                    if s == skill:
                        return e_idx, s_idx
            return -1, -1

        def prepare_turn(self):
            self.turn_count += 1
            self.is_dodged = False
            # Growth: starts at 2, +1 every 2 turns, max 6.
            self.current_max_slots = min(6, 2 + (self.turn_count - 1) // 4)
            self.dodge_active = False
            self.dodge_expires_at_slot = -1

            self.used_skills_this_turn = []
            self.selected_skill = None
            self.selected_intent = None
            self.selected_enemy_index = -1
            self.selected_slot_index = -1
            self.hovered_skill = None
            self.show_energy_warning = False

            # REGENERATE PLAYER ENERGY PER TURN
            # Change the value below (currently 2) to increase/decrease energy gain per turn
            self.player_energy = min(self.player_max_energy, self.player_energy + 2)

            for enemy in self.enemies:
                enemy.dodge_active = False
                enemy.dodge_expires_at_slot = -1
                if not enemy.is_dead:
                    enemy.slots = [None] * self.current_max_slots
                    num_enemy_slots = self.current_max_slots // 2
                    available_indices = list(range(self.current_max_slots))
                    renpy.random.shuffle(available_indices)

                    # Unique intents, respect cooldowns
                    available_intents = [i for i in enemy.intents if i.current_cooldown <= 0]
                    renpy.random.shuffle(available_intents)

                    for _ in range(num_enemy_slots):
                        if not available_intents:
                            break
                        idx = available_indices.pop()
                        enemy.slots[idx] = available_intents.pop()

        def take_damage(self, amount, target="player", enemy_idx=0):
            if target == "player":
                if self.player_barrier > 0:
                    absorbed = min(self.player_barrier, amount)
                    self.player_barrier -= absorbed
                    amount -= absorbed
                self.player_hp = max(0, self.player_hp - amount)
            else:
                enemy = self.enemies[enemy_idx]
                if enemy.barrier > 0:
                    absorbed = min(enemy.barrier, amount)
                    enemy.barrier -= absorbed
                    amount -= absorbed
                enemy.hp = max(0, enemy.hp - amount)
                if enemy.hp <= 0:
                    enemy.is_dead = True

        def heal_player(self, amount):
            self.player_hp = min(self.player_max_hp, self.player_hp + amount)

        def add_barrier(self, amount, target="player", enemy_idx=0):
            if target == "player":
                self.player_barrier += amount
            else:
                self.enemies[enemy_idx].barrier += amount

        def add_buff(self, type, value, duration, target="player", enemy_idx=0):
            if target == "player":
                # Replace existing buff of the same type
                self.player_buffs = [b for b in self.player_buffs if b[0] != type]
                self.player_buffs.append([type, value, duration])
            else:
                enemy = self.enemies[enemy_idx]
                # Replace existing buff of the same type
                enemy.buffs = [b for b in enemy.buffs if b[0] != type]
                enemy.buffs.append([type, value, duration])

        def update_buffs(self):
            for b in self.player_buffs[:]:
                b[2] -= 1
                if b[2] <= 0:
                    self.player_buffs.remove(b)
            for enemy in self.enemies:
                for b in enemy.buffs[:]:
                    b[2] -= 1
                    if b[2] <= 0:
                        enemy.buffs.remove(b)

        def get_total_buff_value(self, type, target="player", enemy_idx=0):
            total = 0
            buffs = self.player_buffs if target == "player" else self.enemies[enemy_idx].buffs
            for b in buffs:
                if b[0] == type:
                    total += b[1]
            return total

        def reduce_cooldowns(self):
            for skill in self.player_skills:
                # Skills used this turn don't have their cooldown reduced yet
                if skill in self.used_skills_this_turn:
                    continue
                if skill.current_cooldown > 0:
                    skill.current_cooldown -= 1
            for enemy in self.enemies:
                for intent in enemy.full_intent_pool:
                    if intent.current_cooldown > 0:
                        intent.current_cooldown -= 1

        def gain_exp(self, amount, character_type="player", enemy_idx=0):
            # CONVERSION RATE: 1 damage = 5 EXP
            # Change the multiplier in the labels if you want faster/slower progression
            if character_type == "player":
                self.skill_exp += amount
                while self.skill_exp >= self.skill_exp_max:
                    if len(self.player_skills) < len(self.full_skill_pool):
                        self.skill_exp -= self.skill_exp_max
                        new_skill = self.full_skill_pool[len(self.player_skills)]
                        self.player_skills.append(new_skill)
                    else:
                        self.skill_exp = min(self.skill_exp, self.skill_exp_max)
                        break
            else:
                enemy = self.enemies[enemy_idx]
                enemy.skill_exp += amount
                while enemy.skill_exp >= enemy.skill_exp_max:
                    if enemy.unlocked_intents_count < len(enemy.full_intent_pool):
                        enemy.skill_exp -= enemy.skill_exp_max
                        enemy.unlocked_intents_count += 1
                    else:
                        enemy.skill_exp = min(enemy.skill_exp, enemy.skill_exp_max)
                        break

    def get_character_skills(name):
        """
        Returns a list of 6 skills for a playable character in the order:
        Normal, Defense, Energy, Hard, Dodge, Ultimate.
        """
        # EDIT THESE VALUES TO CHANGE CHARACTER SKILLS
        if name.lower() == "kare":
            return [
                Skill("slap", cost=2, damage=6, energy_regen=1, desc="Standard strike.", animation="kare_normal_anim", card_image="card_kare_normal"),
                Skill("Defense", cost=3, damage=8, type="barrier", desc="Gain 8 Defense.", cooldown=2, animation="kare_block_anim", card_image="card_kare_block"),
                Skill("Focus", cost=4, damage=5, type="buff", buff_type="damage", buff_duration=3, desc="Increases damage by 5 for 3 turns.", cooldown=5, animation="kare_buff_anim"),
                Skill("punch", cost=4, damage=13, cooldown=2, desc="Powerful punch.", animation="kare_hard_anim", card_image="card_kare_hard"),
                Skill("yummers", cost=0, energy_regen=10, type="energy", desc="Recover 5 energy.",cooldown=2, animation="kare_energy_anim", card_image="card_kare_energy"),
                Skill("evade", cost=4, type="dodge", desc="Dodges next attack.", cooldown=4, animation="kare_dodge_anim", card_image="card_kare_dodge"),
                Skill("super cool kick", cost=6, damage=20, cooldown=6, desc="kick thats it.", animation="kare_ultimate_anim", card_image="card_kare_ultimate")
               
            ]
        elif name.lower() == "chaos":
            return [
                Skill("interitus", cost=3, damage=0, energy_regen=2, desc="1-20 damage... probably", animation="chaos_normal_anim", card_image="card_chaos_normal"),
                Skill("Embrace", cost=5, damage=0, type="barrier", desc="1-50 Defense. who knows", cooldown=0, animation="chaos_block_anim", card_image="card_chaos_block"),
                Skill("Entropy", cost=0, energy_regen=12, type="energy", desc="everything falls apart eventually. might as well use it", animation="chaos_energy_anim", card_image="card_chaos_energy"),
                Skill("Cataclysm", cost=7, damage=0, cooldown=0, desc="1-30 damage... maybe", animation="chaos_hard_anim", card_image="card_chaos_hard"),
                Skill("dissolutum", cost=6, type="dodge", desc="Shift out of reality.", cooldown=0, animation="chaos_dodge_anim", card_image="card_chaos_dodge"),
                Skill("playing rough", cost=6, damage=0, type="buff", buff_type="damage", buff_duration=3, desc="1-50 Damage Buff. or 1. who knows.", animation="chaos_buff_anim"),
                Skill("??????", cost=25, damage=0, cooldown=0, desc="1-60 damage... ??? ?????", animation="chaos_ultimate_anim", card_image="card_chaos_ultimate")

            ]
        return []

    def get_enemy_intents(name):
        """
        Returns a list of 6 intents for an enemy character in the order:
        Normal, Defense, Energy, Hard, Dodge, Ultimate.
        """
        # EDIT THESE VALUES TO CHANGE ENEMY INTENTS
        if name.lower() == "butter":
            return [
                EnemyIntent("elbow", damage=4, desc="A quick poke.", animation="butter_normal_anim", type="attack"),
                EnemyIntent("Defense", damage=5, desc="Adds 5 Defense.", animation="butter_block_anim", type="barrier", cooldown=3),
                EnemyIntent("Focus", damage=2, buff_type="damage", buff_duration=3, desc="Increases damage by 2 for 3 turns.", animation="butter_energy_anim", type="buff", cooldown=4),
                EnemyIntent("kick", damage=10, desc="heavy impact.", animation="butter_hard_anim", type="attack", cooldown=0),
                EnemyIntent("Slippery", desc="will dodge the next attack.", animation="butter_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("PUNCH!", damage=20, desc="haha!! no way you are surviving this", animation="butter_ultimate_anim", type="attack", cooldown=6)
            ]
        elif name.lower() == "law":
            return [
                EnemyIntent("VERDICT", damage=6, desc="already judged you guilty", animation="serious_butter_normal_anim", type="attack"),
                EnemyIntent("ABSOLUTE RULE", damage=5, desc="law does not bend. neither does I", animation="serious_butter_block_anim", type="barrier", cooldown=3),
                EnemyIntent("ENFORCEMENT", damage=4, buff_type="every law has consequences", buff_duration=3, desc="Increases damage by 10 for 3 turns.", animation="serious_butter_energy_anim", type="buff", cooldown=4),
                EnemyIntent("BINDING JUDGMENT", damage=10, desc="a strike that carries the full weight of every law ever written. it shows.", animation="serious_butter_hard_anim", type="attack", cooldown=0),
                EnemyIntent("DUE PROCESS", desc="proper procedure must be followed. that attack was not it.", animation="serious_butter_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("SENTENCE", damage=25, desc="the verdict has been decided. there is no appeal. there is no negotiation.", animation="serious_butter_ultimate_anim", type="attack", cooldown=6)
            ]
        elif name.lower() == "lumpi":
            return [
                EnemyIntent("SOVEREIGN BLADE", damage=5, desc="powerful attack", animation="lumpi_normal_anim", type="attack"),
                EnemyIntent("IRON DECREE", damage=4, desc="authority does not bend. neither will I", animation="lumpi_block_anim", type="barrier", cooldown=3),
                EnemyIntent("DOMAIN AUTHORITY", damage=5, buff_type="damage", buff_duration=3, desc="within my domain my power is absolute.(Increases damage by 5 for 3 turns.)", animation="lumpi_energy_anim", type="buff", cooldown=4),
                EnemyIntent("RULING STRIKE", damage=8, desc="swing from the blade of absolute authority.", animation="lumpi_hard_anim", type="attack", cooldown=0),
                EnemyIntent("SOVEREIGN STEP", desc="simply steps outside your reach.", animation="lumpi_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("SOVEREIGN TERRITORY", damage=25, desc="everything within this space falls under my dominion. there is nowhere left to go..", animation="lumpi_ultimate_anim", type="attack", cooldown=6)
            ]
        elif name.lower() == "lumpi wheelchair":
            return [
                EnemyIntent("Runover", damage=6, desc="Watch your toes.", animation="lumpi_wheelchair_normal_anim", type="attack"),
                EnemyIntent("Reinforced Frame", damage=10, desc="Adds 10 Defense.", animation="lumpi_wheelchair_block_anim", type="barrier", cooldown=3),
                EnemyIntent("Overdrive", damage=4, buff_type="damage", buff_duration=3, desc="Increases damage by 8 for 3 turns.", animation="lumpi_wheelchair_energy_anim", type="buff", cooldown=4),
                EnemyIntent("Turbo Charge", damage=10, desc="High speed impact.", animation="lumpi_wheelchair_hard_anim", type="attack", cooldown=0),
                EnemyIntent("Drift", desc="Will dodge the next attack.", animation="lumpi_wheelchair_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("crashout", damage=25, desc="thats it im beating the shit out of you", animation="lumpi_wheelchair_ultimate_anim", type="attack", cooldown=6)
            ]
        elif name.lower() == "ava":
            return [
                EnemyIntent("poke", damage=6, desc="poke", animation="ava_normal_anim", type="attack"),
                EnemyIntent("ETERNAL RECORD", damage=8, desc="as long as a single soul remembers civilization, I cannot fall. history does not die easily.", animation="ava_block_anim", type="barrier", cooldown=3),
                EnemyIntent("RALLY", damage=15, buff_type="something something power of humanity.", buff_duration=3, desc="Increases damage by 15 for 3 turns.", animation="ava_energy_anim", type="buff", cooldown=4),
                EnemyIntent("CULTURAL IMPACT", damage=15, desc="a strike so significant it will be remembered for generations. probably.", animation="ava_hard_anim", type="attack", cooldown=0),
                EnemyIntent("WRITTEN IN HISTORY", desc="Will dodge the next attack.", animation="ava_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("END OF AN ERA", damage=60, desc="every civilization must fall before a new one rises. unfortunately for you, you are the civilization right now", animation="ava_ultimate_anim", type="attack", cooldown=6)
            ]
        return []

screen slot_machine(slot_display, label_text=""):
    frame:
        background Solid("#000000cc")
        xalign 0.5 yalign 0.3
        padding (40, 30)
        xsize 140
        ysize 180
        foreground "sketchy_bar_outline"
        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            text "[label_text]" size 16 color "#aaa" xalign 0.5
            text "[slot_display]" size 40 color "#ffffff" bold True xalign 0.5

label chaos_slot_anim(final_value, label_text=""):
    $ slot_machine_display = "???"
    show screen slot_machine(slot_machine_display, label_text)
    python:
        symbols = "$#%^&*@!?~<>"
        for i in range(15):
            if i < 10:
                slot_machine_display = "".join([renpy.random.choice(symbols + "0123456789") for _ in range(len(str(final_value)))])
            else:
                slot_machine_display = str(final_value)
            renpy.restart_interaction()
            renpy.pause(0.05 + (i * 0.02), hard=True)
    $ renpy.pause(0.5, hard=True)
    hide screen slot_machine
    return

screen battle_screen(bm):
    if getattr(bm, "is_chaos", False):
        timer 0.05 repeat True action [renpy.restart_interaction]
    $ p_name = "Chaos" if "chaos" in bm.player_sprites["idle"] else "Kare"

    # Settings button
    textbutton "Settings":
        xalign 0.5 yalign 2
        action ShowMenu("preferences")
        text_size 24
        text_color "#555"
        background Solid("#fff0")
        hover_background Solid("#eee")
        padding (10, 5)

    # ── Player stats: top left ──
    vbox:
        xalign 0.05 yalign 0.05
        spacing 5
        xmaximum 400
        if getattr(bm, "is_chaos", False):
            text "[p_name]: [scramble_hp(bm.player_hp)]/[scramble_hp(bm.player_max_hp)]" size 24 color "#747474"
        else:
            text "[p_name]: [bm.player_hp]/[bm.player_max_hp]" size 24 color "#747474"
        bar value bm.player_hp range bm.player_max_hp xmaximum 300
        hbox:
            spacing 20
            vbox:
                text "Energy: [bm.player_energy]/[bm.player_max_energy]" size 20 color "#666666"
            if bm.player_barrier > 0:
                vbox:
                    text "Defense: [bm.player_barrier]" size 20 color "#797979"
        hbox:
            spacing 5
            for buff in bm.player_buffs:
                frame:
                    background Solid("#5e5e5e")
                    padding (5, 2)
                    text "[buff[0]]: [buff[1]] ([buff[2]]t)" size 12 color "#fff"

    # ── Enemy stats: top right ──
    vbox:
        xanchor 1.0 xpos 0.98
        yalign 0.05
        spacing 10
        for e_idx, enemy in enumerate(bm.enemies):
            if not enemy.is_dead:
                vbox:
                    spacing 2
                    text "[enemy.name]: [enemy.hp]/[enemy.max_hp]" size 20 color "#747474" xalign 1.0
                    bar value enemy.hp range enemy.max_hp xmaximum 250 xalign 1.0
                    if enemy.barrier > 0:
                        text "Defense: [enemy.barrier]" size 14 color "#6d6d6d" xalign 1.0
                    hbox:
                        xalign 1.0
                        spacing 4
                        text "Skill Unlock: " size 12 color "#707070"
                        bar value enemy.skill_exp range enemy.skill_exp_max xmaximum 150 ysize 6 yalign 0.5
                    hbox:
                        xalign 1.0
                        spacing 5
                        for buff in enemy.buffs:
                            frame:
                                background Solid("#4b4b4b")
                                padding (3, 1)
                                text "[buff[0]]: [buff[1]] ([buff[2]]t)" size 10 color "#fff"
  
    # ── Battle slots: centered ──
    # ── Battle slots + CONFIRM in hbox so button tracks slot width ──
    hbox:
        xalign 0.5 yalign 0.05
        spacing 10

        null width 120

        vbox:
            spacing 10
            text "Select a card below, then click an empty slot here:" size 16 color "#aaa" xalign 0.5
            for e_idx, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    frame:
                        background Solid("#8888887f")
                        foreground "sketchy_bar_outline"
                        padding (10, 10)
                        xalign 0.5
                        vbox:
                            spacing 5
                            text "[enemy.name]'s Row" size 14 color "#333" xalign 0.0
                            hbox:
                                spacing 10
                                for s_idx in range(bm.current_max_slots):
                                    $ action = enemy.slots[s_idx]
                                    if action is None:
                                        $ can_click_slot = bm.selected_skill is not None
                                        button:
                                            action If(can_click_slot, Function(bm.add_to_slot, bm.selected_skill, e_idx, s_idx))
                                            background Solid("#eee")
                                            foreground "sketchy_bar_outline"
                                            padding (10, 5)
                                            xminimum 100
                                            yminimum 60
                                            text "EMPTY" size 16 color "#747474" xalign 0.5 yalign 0.5
                                    elif isinstance(action, EnemyIntent):
                                        button:
                                            action [Function(bm.select_intent, action, e_idx, s_idx), SetField(bm, "selected_skill", None)]
                                            background Solid("#ccc")
                                            foreground "sketchy_bar_outline"
                                            padding (10, 5)
                                            xminimum 100
                                            yminimum 60
                                            vbox:
                                                yalign 0.5
                                                text "ENEMY" size 12 color "#616161" xalign 0.5
                                                text "[action.name]" size 16 color "#747474" xalign 0.5
                                    elif isinstance(action, Skill):
                                        $ can_replace = bm.selected_skill is not None and bm.selected_skill != action
                                        button:
                                            action If(can_replace,
                                                    Function(bm.add_to_slot, bm.selected_skill, e_idx, s_idx),
                                                    Function(bm.select_skill, action))
                                            background Solid("#ddd")
                                            foreground "sketchy_bar_outline"
                                            padding (10, 5)
                                            xminimum 100
                                            yminimum 60
                                            vbox:
                                                yalign 0.5
                                                text "YOU" size 12 color "#3d3d3d" xalign 0.5
                                                text "[action.name]" size 16 color "#747474" xalign 0.5

        vbox:
            yalign 0.0
            null height 30
            textbutton "CONFIRM":
                background Solid("#7e7e7e")
                hover_background Solid("#555")
                padding (20, 14)
                text_size 24
                text_color "#fff"
                text_bold True
                text_outlines []
                action [Return("execute"), Play("sound", "audio/stu9-chime-2-356833.mp3", relative_volume=1.5)]

    # ── Intent description: completely separate, never affects hbox ──
    if bm.selected_intent:
        frame:
            background Solid("#8888887f")
            foreground "sketchy_bar_outline"
            xalign 0.5 ypos 0.28
            padding (20, 15)
            xmaximum 700
            vbox:
                spacing 6
                text "[bm.enemies[bm.selected_enemy_index].name]: [bm.selected_intent.name]" size 20 color "#333" xalign 0.5 bold True
                if bm.selected_intent.damage > 0:
                    if bm.selected_intent.type == "attack":
                        text "Projected Damage: [bm.selected_intent.damage]" size 16 color "#444" xalign 0.5
                    elif bm.selected_intent.type == "barrier":
                        text "Projected Defense: [bm.selected_intent.damage]" size 16 color "#444" xalign 0.5
                    elif bm.selected_intent.type == "buff":
                        text "Damage Buff: +[bm.selected_intent.damage]" size 16 color "#444" xalign 0.5
                text "[bm.selected_intent.desc]" size 14 color "#555" xalign 0.5 text_align 0.5
           


    # ── Skill cards: bottom ──
    vbox:
        xalign 0.5 ypos 0.98 yanchor 1.0
        spacing 5
        hbox:
            xalign 0.5
            spacing 4
            text "Next skill: " size 13 color "#777777"
            bar value bm.skill_exp range bm.skill_exp_max xmaximum 600 ysize 8 yalign 0.5
        hbox:
            xalign 0.5
            spacing 15
            for skill in bm.player_skills:
                $ is_selected = bm.selected_skill == skill
                $ can_use = skill.current_cooldown == 0 and skill not in bm.used_skills_this_turn
                button:
                    action [Function(bm.select_skill, skill), Play("sound", "audio/freesound_community-page-flip-47177.mp3", relative_volume=1.0)]
                    hovered SetField(bm, "hovered_skill", skill)
                    unhovered SetField(bm, "hovered_skill", None)
                    at (card_selected_zoom if is_selected else card_idle_zoom)
                    sensitive (skill.current_cooldown == 0 and skill not in bm.used_skills_this_turn)
                    background (Solid("#0002") if is_selected else None)
                    foreground "sketchy_bar_outline"
                    padding (0, 0)
                    xsize 140
                    ysize 180
                    if skill.card_image:
                        add skill.card_image
                    if skill.current_cooldown > 0:
                        add Solid("#00000088")
                        text "[skill.current_cooldown]" size 40 color "#ffffff" xalign 0.5 yalign 0.5 bold True
                    elif skill in bm.used_skills_this_turn:
                        add Solid("#00000055")
                        text "USED" size 20 color "#ffffff" xalign 0.5 yalign 0.5 bold True

    # ── Skill popup (left side, unchanged) ──
    $ display_skill = None
    if bm.hovered_skill and bm.hovered_skill == bm.selected_skill:
        $ display_skill = bm.hovered_skill
    elif bm.selected_skill and bm.selected_skill in bm.used_skills_this_turn:
        $ display_skill = bm.selected_skill

    if display_skill:
        frame:
            background Solid("#8888887f")
            foreground "sketchy_bar_outline"
            xpos 0.15 yalign 0.5
            xanchor 0.5
            padding (30, 30)
            xminimum 400
            vbox:
                spacing 15
                if display_skill.card_image:
                    add display_skill.card_image xalign 0.5
                text "[display_skill.name]" size 30 color "#333" xalign 0.5 bold True
                text "Cost: [display_skill.cost] Energy" size 20 color "#444" xalign 0.5
                if display_skill.damage > 0:
                    if display_skill.type == "barrier":
                        text "Defense: [display_skill.damage]" size 20 color "#444" xalign 0.5
                    elif display_skill.type == "buff":
                        text "Damage Buff: +[display_skill.damage]" size 20 color "#444" xalign 0.5
                    else:
                        text "Damage: [display_skill.damage]" size 20 color "#444" xalign 0.5
                text "[display_skill.desc]" size 18 color "#444" xalign 0.5 text_align 0.5
                if display_skill.cooldown > 0:
                    text "Cooldown: [display_skill.cooldown] turns" size 18 color "#444" xalign 0.5
                if display_skill in bm.used_skills_this_turn:
                    $ e_idx, s_idx = bm.get_skill_slot_info(display_skill)
                    if e_idx != -1:
                        null height 20
                        textbutton "REMOVE FROM SLOT":
                            action [Function(bm.remove_from_slot, e_idx, s_idx), SetField(bm, "selected_skill", None)]
                            xalign 0.5
                            background Solid("#eee")
                            foreground "sketchy_bar_outline"
                            padding (15, 10)
                            text_size 24
                            text_color "#333"
                            text_bold True

    # ── ENERGY WARNING ──
    if bm.show_energy_warning:
        timer 2.0 action SetField(bm, "show_energy_warning", False)
        frame:
            at energy_warning_fade
            background Solid("#979797cc")
            padding (20, 10)
            xalign 0.5 yalign 0.4
            text "NOT ENOUGH ENERGY" color "#fff" size 30 bold True

label battle_reset_camera:
    camera:
        perspective False
        gl_depth False
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    return

label battle_engine(bm):
    window auto hide
    $ _skipping = None
    $ config.allow_skipping = False
    $ battle_mode = True
    $ quick_menu = False
    $ bm.initialize_skills(getattr(bm, "is_chaos", False))

    label .engine_start_logic:
        $ bm.prepare_turn()

        if getattr(bm, "tutorial", False) and bm.turn_count == 2:
            "kare" "augh..."
            "kare" "what the hell is happening"
            "butter" "we are fighting duh"
            "kare" "but i dont know how to fight"
            "butter" "well that just made this fight easier"
            show dobe_sprite at center with moveinbottom
            "dobe" "dont worry kare i got you"
            "dobe" "the cards at the bottom are your skills"
            "kare" "uhh i cant see them"
            "dobe" "it will show after this tutorial"
            "kare" "but im a visual learner"
            "dobe" "anyway"
            "dobe" "Select one, then click an empty slot in the row above the enemy."
            "dobe" "Skills cost Energy, so spend it wisely kare"
            "dobe" "And watch the enemy's slots—they show their 'Intents'. Counter them by defending or dodging "
            "dobe" "Plus, dealt damage earns you EXP to unlock even cooler moves."
            "kare" "uhh i didn't know you could fight"
            "kare" "help me fight her"
            "dobe" "nah you got this"
            "kare" "erm.. well wouldn't it be better if you fight along side with me"
            hide dobe_sprite with dissolve
            "dobe" "nah you got this"
            "kare" "..."
            window hide

        show expression bm.player_sprites["idle"] as player at fight_left
        $ e_count = sum(1 for e in bm.enemies if not e.is_dead)
        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    pos = fight_right
                    if e_count > 1:
                        pos = Position(xalign=0.6 + (i * 0.15), ypos=0.8, yanchor=1.0)
                    renpy.show(enemy.sprites["idle"], at_list=[pos], tag=tag)
                else:
                    renpy.hide("enemy_" + str(i))

        show screen battle_screen(bm)

    label .engine_selection_phase:
        $ result = ui.interact()
        if result == "execute":
            jump .engine_execution_phase
        jump .engine_selection_phase

    label .engine_execution_phase:
        hide screen battle_screen
        $ current_slot_idx = 0
        $ bm.dodge_active = False


    label .engine_main_loop:
        if bm.dodge_active and current_slot_idx > bm.dodge_expires_at_slot:
            $ bm.dodge_active = False
        python:
            for e in bm.enemies:
                if e.dodge_active and current_slot_idx > e.dodge_expires_at_slot:
                    e.dodge_active = False
        if current_slot_idx >= bm.current_max_slots:
            jump .engine_turn_end

        $ e_idx = 0
    label .engine_resolution_core:
        if e_idx >= len(bm.enemies):
            $ current_slot_idx += 1
            jump .engine_main_loop

        $ enemy = bm.enemies[e_idx]
        if enemy.is_dead:
            $ e_idx += 1
            jump .engine_resolution_core

        $ action = enemy.slots[current_slot_idx]
        $ current_enemy_tag = "enemy_" + str(e_idx)
        if action is None:
            $ e_idx += 1
            jump .engine_resolution_core
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)

            if skill.type == "attack":
                if enemy.dodge_active:
                    $ bm.is_dodged = True
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_at_dodge_generic
                    $ dodge_anim = get_dodge_anim(enemy.name)
                    call expression dodge_anim pass (bm) from _call_enemy_dodge_anim_reactive_generic
                    $ enemy.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_generic_generic
                    $ actual_damage = get_chaos_random_value(bm, skill)
                    if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_damage, "DAMAGE") from _call_chaos_slot_attack_eng
                    $ bm.take_damage(actual_damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(actual_damage * 5, character_type="player")
                    "[skill.name] deals [actual_damage] damage to [enemy.name]"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_barrier_generic
                $ actual_barrier = get_chaos_random_value(bm, skill)
                if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_barrier, "DEFENSE") from _call_chaos_slot_barrier_eng
                $ bm.add_barrier(actual_barrier)
                if getattr(bm, "is_chaos", False): "You gain [actual_barrier] Defense"
                else: "You gain [skill.damage] Defense"
            elif skill.type == "dodge":
                $ bm.is_dodged = False
                $ bm.dodge_active = True
                $ bm.dodge_expires_at_slot = current_slot_idx + 1
            elif skill.type == "buff":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_buff_generic
                $ actual_buff = get_chaos_random_value(bm, skill)
                if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_buff, "BUFF POWER") from _call_chaos_slot_buff_eng
                $ bm.add_buff(skill.buff_type, actual_buff, skill.buff_duration, target="player")
                if getattr(bm, "is_chaos", False): "[skill.name] Damage increased by [actual_buff] for [skill.buff_duration] turns."
                else: "[skill.name] Damage increased by [skill.damage] for [skill.buff_duration] turns."
            elif skill.type == "energy":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_energy_generic
                "You gained [skill.energy_regen] Energy"

        elif isinstance(action, EnemyIntent):
            $ intent = action
            $ intent.current_cooldown = intent.cooldown
            $ bm.enemy_intent = intent

            if intent.type == "attack":
                if bm.dodge_active:
                    $ bm.is_dodged = True
                    if intent.animation:
                        call expression intent.animation pass (bm) from _call_intent_anim_at_dodge_generic
                    else:
                        call enemy_attack_anim(bm) from _call_intent_anim_default_at_dodge_generic
                    $ p_name = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
                    $ dodge_anim = get_dodge_anim(p_name)
                    call expression dodge_anim pass (bm) from _call_player_dodge_anim_reactive_generic
                    $ bm.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if intent.animation:
                        call expression intent.animation pass (bm) from _call_intent_anim_generic_generic
                    else:
                        call enemy_attack_anim(bm) from _call_intent_anim_default_generic
                    $ damage = intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                    $ bm.take_damage(damage, target="player")
                    $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)
                    "[enemy.name] deals [damage] damage with [intent.name]!"
            elif intent.type == "barrier":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_barrier_generic
                $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)
                "[enemy.name] gains [intent.damage] Defense!"
            elif intent.type == "dodge":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_dodge_generic
                $ enemy.dodge_active = True
                $ enemy.dodge_expires_at_slot = current_slot_idx + 1
            elif intent.type == "buff":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_buff_generic
                $ bm.add_buff(intent.buff_type, intent.damage, intent.buff_duration, target="enemy", enemy_idx=e_idx)
                "[enemy.name] damage increased by [intent.damage]"
            elif intent.type == "energy":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_energy_generic
                "[enemy.name] is recovering."
        if all(e.is_dead for e in bm.enemies):
            window hide
            jump .engine_victory
        if bm.player_hp <= 0:
            window hide
            jump .engine_defeat

        window hide
        $ renpy.pause(0.5, hard=True)
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, e in enumerate(bm.enemies):
                if not e.is_dead:
                    renpy.show(e.sprites["idle"], tag="enemy_" + str(i))

        $ e_idx += 1
        jump .engine_resolution_core

    label .engine_turn_end:
        $ bm.reduce_cooldowns()
        $ bm.update_buffs()
        if getattr(bm, "is_chaos", False):
            call chaos_slot_anim("SHUFFLE", "CARDS") from _call_chaos_shuffle_eng
            $ renpy.random.shuffle(bm.player_skills)

        if all(e.is_dead for e in bm.enemies):
            window hide
            jump .engine_victory
        if bm.player_hp <= 0:
            window hide
            jump .engine_defeat

        if getattr(bm, "dobe_helps", False) and not bm.enemies[0].is_dead:
            show dobe_attack:
                xanchor 0.5 yanchor 1.0
                xpos 1.3 ypos 0.8
                ease 0.25 xpos 0.75
            $ renpy.pause(0.25, hard=True)
            show dobe_attack:
                xanchor 0.5 yanchor 1.0
                xpos 0.75 ypos 0.8
                ease 0.1 xpos 0.55
                ease 0.1 xpos 0.75
            $ renpy.show(bm.enemies[0].sprites["hit"], tag="enemy_0")
            play sound "universfield-punch-02-123106.mp3"
            $ renpy.pause(0.4, hard=True)
            $ renpy.show(bm.enemies[0].sprites["idle"], tag="enemy_0")
            $ bm.take_damage(5, target="enemy", enemy_idx=0)
            "Dobe kicks the crippled lady for 5 damage"
            show dobe_attack:
                xanchor 0.5 yanchor 1.0
                xpos 0.75 ypos 0.8
                ease 0.25 xpos 1.3
            $ renpy.pause(0.25, hard=True)
            hide dobe_attack
            if bm.enemies[0].is_dead:
                window hide
                jump .engine_victory

        window hide
        $ renpy.pause(0.5, hard=True)
        jump .engine_start_logic

    label .engine_victory:
        $ config.allow_skipping = True
        $ battle_mode = False
        $ quick_menu = True
        hide screen battle_screen
        python:
            for i in range(len(bm.enemies)):
                renpy.hide("enemy_" + str(i))
        return "win"

    label .engine_defeat:
        $ config.allow_skipping = True
        $ battle_mode = False
        $ quick_menu = True
        hide screen battle_screen
        python:
            for i in range(len(bm.enemies)):
                renpy.hide("enemy_" + str(i))
        return "lose"

# ==============================================================================
# ANIMATION SECTION
# ==============================================================================
# To create or edit animations:
# 1. Define a label (e.g., label kare_normal_anim(bm):)
# 2. Use 'show expression "sprite_name" as [tag]' to REPLACE the idle sprite.
# 3. Use 'renpy.pause(seconds)' to control timing.
# 4. Restore the idle sprite at the end.

# --- KARE ANIMATIONS ---
label kare_normal_anim(bm):
    show expression "kare_normal_sprite" as player at fight_left:
        ease 0.1 xpos 0.4
        ease 0.1 xpos 0.35
    if not bm.is_dodged:
        $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    if not bm.is_dodged:
        play sound "universfield-punch-02-123106.mp3"
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label kare_hard_anim(bm):
    show expression "kare_hard_sprite" as player at fight_left:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.35
    if not bm.is_dodged:
        $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    if not bm.is_dodged:
        play sound "audio/punch-140236.mp3"
    $ renpy.pause(0.8, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label kare_block_anim(bm):
    show expression "kare_block_sprite" as player at fight_left
    play sound "Berserk Clang Sound Effect.mp3"
    $ renpy.pause(1, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label kare_dodge_anim(bm):
    show expression "kare_dodge_sprite" as player at fight_left:
        ease 0.2 xpos 0.25
        ease 0.2 xpos 0.35
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label kare_buff_anim(bm):
    show expression "kare_buff_sprite" as player at fight_left
    play sound "audio/meditate-sound.mp3"
    $ renpy.pause(1, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label kare_ultimate_anim(bm):
    show expression "kare_ultimate_sprite" as player at fight_left:
        ease 0.3 xpos 0.6
        ease 0.3 xpos 0.35
    if not bm.is_dodged:
        $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    if not bm.is_dodged:
        play sound "audio/freesound_community-shotgun-firing-3-14483.mp3" volume 1.5
    if not bm.is_dodged:
        camera:
            ease 0.1 zoom 1.2
            ease 0.1 zoom 1.0
    $ renpy.pause(1.2, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label kare_energy_anim(bm):
    show expression "kare_energy_sprite" as player at fight_left
    play sound "audio/freesound_community-bite-potato-chips-83946.mp3" volume 2
    $ renpy.pause(2, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

# --- CHAOS ANIMATIONS ---
label chaos_normal_anim(bm):
    show expression "chaos_normal_sprite" as player at fight_left
    if not bm.is_dodged:
        $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    if not bm.is_dodged:
        play sound "punch-140236.mp3"
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label chaos_hard_anim(bm):
    show expression "chaos_hard_sprite" as player at fight_left
    if not bm.is_dodged:
        $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    if not bm.is_dodged:
        play sound "audio/punch-140236.mp3"
    $ renpy.pause(0.8, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label chaos_block_anim(bm):
    show expression "chaos_block_sprite" as player at fight_left
    play sound "Berserk Clang Sound Effect.mp3"
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label chaos_dodge_anim(bm):
    show expression "chaos_dodge_sprite" as player at fight_left
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label chaos_buff_anim(bm):
    show expression "chaos_buff_sprite" as player at fight_left
    play sound "audio/meditate-sound.mp3"
    $ renpy.pause(0.8, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label chaos_ultimate_anim(bm):
    show expression "chaos_ultimate_sprite" as player at fight_left
    if not bm.is_dodged:
        $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    if not bm.is_dodged:
        play sound "audio/magic-spark.mp3"
    $ renpy.pause(1.2, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label chaos_energy_anim(bm):
    show expression "chaos_energy_sprite" as player at fight_left
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

# --- BUTTER ANIMATIONS ---
label butter_normal_anim(bm):
    $ renpy.show("butter_normal_sprite", tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    if not bm.is_dodged:
        play sound "audio/universfield-punch-02-123106.mp3"
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label butter_hard_anim(bm):
    $ renpy.show("butter_hard_sprite", tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    if not bm.is_dodged:
        play sound "audio/punch-140236.mp3"
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label butter_block_anim(bm):
    $ renpy.show("butter_block_sprite", tag=current_enemy_tag, at_list=[fight_right])
    play sound "Berserk Clang Sound Effect.mp3"
    $ renpy.pause(1, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label butter_dodge_anim(bm):
    $ renpy.show("butter_dodge_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label butter_buff_anim(bm):
    $ renpy.show("butter_buff_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label butter_ultimate_anim(bm):
    # Phase 1: windup sprite for 1 second
    $ renpy.show("butter_ultimate_windup", tag=current_enemy_tag, at_list=[fight_right])
    play sound "audio/20 February_2025.mp3"
    $ renpy.pause(2.5, hard=True)
    # Phase 2: actual ultimate attack
    $ renpy.show("butter_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(1.2, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label butter_energy_anim(bm):
    $ renpy.show("butter_energy_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(2, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

# --- SERIOUS BUTTER ANIMATIONS ---
label serious_butter_normal_anim(bm):
    $ renpy.show("serious_butter_normal_sprite", tag=current_enemy_tag, at_list=[fight_right,enemy_charge_right])
    play sound "audio/sword-slash-and-swing-185432.mp3"
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label serious_butter_hard_anim(bm):
    $ renpy.show("serious_butter_hard_sprite", tag=current_enemy_tag, at_list=[fight_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label serious_butter_block_anim(bm):
    $ renpy.show("serious_butter_block_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label serious_butter_dodge_anim(bm):
    $ renpy.show("serious_butter_dodge_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label serious_butter_buff_anim(bm):
    $ renpy.show("serious_butter_buff_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label serious_butter_ultimate_anim(bm):
    $ renpy.show("serious_butter_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(1.2, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label serious_butter_energy_anim(bm):
    $ renpy.show("serious_butter_energy_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

# --- LUMPI ANIMATIONS ---
label lumpi_normal_anim(bm):
    $ renpy.show("lumpi_normal_sprite", tag=current_enemy_tag, at_list=[fight_right,enemy_charge_right])
    play sound "audio/sword-slash-and-swing-185432.mp3"
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(1, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label lumpi_hard_anim(bm):
    $ renpy.show("lumpi_ultimate_windup", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(1, hard=True)
    $ renpy.show("lumpi_hard_sprite", tag=current_enemy_tag, at_list=[fight_right,enemy_charge_right])
    play sound "audio/daviddumaisaudio-sword-slash-with-metallic-impact-185435.mp3"
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label lumpi_block_anim(bm):
    $ renpy.show("lumpi_block_sprite", tag=current_enemy_tag, at_list=[fight_right])
    play sound "Berserk Clang Sound Effect.mp3"
    $ renpy.pause(1, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label lumpi_dodge_anim(bm):
    $ renpy.show("lumpi_dodge_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label lumpi_buff_anim(bm):
    $ renpy.show("lumpi_buff_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label lumpi_ultimate_anim(bm):
    $ renpy.show("lumpi_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(1.2, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label lumpi_energy_anim(bm):
    $ renpy.show("lumpi_energy_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

# --- LUMPI WHEELCHAIR ANIMATIONS ---
label lumpi_wheelchair_normal_anim(bm):
    $ renpy.show("lumpi_wheelchair_normal_sprite", tag=current_enemy_tag, at_list=[fight_right,enemy_charge_right])
    play sound "audio/car_crash-377291.mp3"
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label lumpi_wheelchair_hard_anim(bm):
    $ renpy.show("lumpi_wheelchair_hard_sprite", tag=current_enemy_tag, at_list=[fight_right,enemy_charge_right])
    play sound "audio/car_crash-377291.mp3" 
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label lumpi_wheelchair_block_anim(bm):
    $ renpy.show("lumpi_wheelchair_block_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label lumpi_wheelchair_dodge_anim(bm):
    $ renpy.show("lumpi_wheelchair_dodge_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label lumpi_wheelchair_buff_anim(bm):
    $ renpy.show("lumpi_wheelchair_buff_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label lumpi_wheelchair_ultimate_anim(bm):
    # Phase 1: windup sprite for 1 second
    $ renpy.show("lumpi_wheelchair_ultimate_windup", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(1, hard=True)
  
    $ renpy.show("lumpi_wheelchair_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    play sound  "lordsonny_two-debris-break-2-457507.mp3"
    $ renpy.pause(0.8, hard=True)
    $ renpy.show("lumpi_wheelchair_ultimate_windup", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.2, hard=True)
    $ renpy.show("lumpi_wheelchair_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    play sound "lordsonny_two-debris-break-2-457507.mp3"
    $ renpy.pause(0.8, hard=True)
    $ renpy.show("lumpi_wheelchair_ultimate_windup", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.2, hard=True)
    $ renpy.show("lumpi_wheelchair_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    play sound "lordsonny_two-debris-break-2-457507.mp3"
    $ renpy.pause(1, hard=True)
    if not bm.is_dodged:
    
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(1.2, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label lumpi_wheelchair_energy_anim(bm):
    $ renpy.show("lumpi_wheelchair_energy_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

# --- AVA ANIMATIONS ---
label ava_normal_anim(bm):
    $ renpy.show("ava_normal_sprite", tag=current_enemy_tag, at_list=[fight_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    if not bm.is_dodged:
        play sound "audio/magic-spark.mp3"
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label ava_hard_anim(bm):
    $ renpy.show("ava_hard_sprite", tag=current_enemy_tag, at_list=[fight_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    if not bm.is_dodged:
        play sound "audio/magic-spark.mp3"
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label ava_block_anim(bm):
    $ renpy.show("ava_block_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label ava_dodge_anim(bm):
    $ renpy.show("ava_dodge_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label ava_buff_anim(bm):
    $ renpy.show("ava_buff_sprite", tag=current_enemy_tag, at_list=[fight_right])
    play sound "audio/meditate-sound.mp3"
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label ava_ultimate_anim(bm):
    $ renpy.show("ava_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    if not bm.is_dodged:
        play sound "audio/magic-spark.mp3"
    $ renpy.pause(1.2, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label ava_energy_anim(bm):
    $ renpy.show("ava_energy_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

# --- ORDER ANIMATIONS ---
label order_normal_anim(bm):
    $ renpy.show("order_normal_sprite", tag=current_enemy_tag, at_list=[fight_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
        play sound "audio/magic-spark.mp3"
        with flash
    $ renpy.pause(0.5, hard=True)
    if not bm.enemies[e_idx].is_dead:
        $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label order_hard_anim(bm):
    $ renpy.show("order_hard_sprite", tag=current_enemy_tag, at_list=[fight_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
        play sound "audio/magic-spark.mp3"
        with flash
        camera:
            ease 0.1 zoom 1.05
            ease 0.1 zoom 1.0
    $ renpy.pause(0.8, hard=True)
    if not bm.enemies[e_idx].is_dead:
        $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label order_block_anim(bm):
    $ renpy.show("order_block_sprite", tag=current_enemy_tag, at_list=[fight_right])
    play sound "audio/Berserk Clang Sound Effect.mp3"
    $ renpy.pause(0.5, hard=True)
    if not bm.enemies[e_idx].is_dead:
        $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label order_dodge_anim(bm):
    $ renpy.show("order_dodge_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    if not bm.enemies[e_idx].is_dead:
        $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label order_buff_anim(bm):
    $ renpy.show("order_buff_sprite", tag=current_enemy_tag, at_list=[fight_right])
    play sound "audio/meditate-sound.mp3"
    $ renpy.pause(0.8, hard=True)
    if not bm.enemies[e_idx].is_dead:
        $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label order_ultimate_anim(bm):
    $ renpy.show("order_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
        play sound "audio/magic-spark.mp3"
        with flash
        camera:
            ease 0.05 zoom 1.1
            ease 0.05 zoom 1.0
            ease 0.05 zoom 1.1
            ease 0.05 zoom 1.0
    $ renpy.pause(1.2, hard=True)
    if not bm.enemies[e_idx].is_dead:
        $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label order_energy_anim(bm):
    $ renpy.show("order_energy_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    if not bm.enemies[e_idx].is_dead:
        $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return


# --- FALLBACKS ---
label enemy_attack_anim(bm):
    $ enemy = bm.enemies[e_idx]
    $ renpy.show(enemy.sprites["attack"], tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(enemy.sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label simple_battle_graphics(skill_overrides=None):
    $ _skipping = None
    $ config.allow_skipping = False
    camera:
        perspective False
        gl_depth False
    scene bg_butter at truecenter
    show kare_idle as player at fight_left
    show butter_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ butter = get_butter()
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 4, "cost": 1 },
        "punch":            {"damage": 8, "cost": 3,"cooldown": 3},
        "super cool kick":  {"damage": 20, "cost": 5, "cooldown": 4},
        "Defense":          {"damage": 8, "cost": 2, "cooldown": 2},
        "Focus":            {"damage": 5, "cost": 3, "buff_duration": 3, "cooldown": 3},
        "yummers":          {"energy_regen": 5, "cooldown": 2},
        "evade":            {"cost": 3, "cost": 2, "cooldown": 2},
    }
    $ bm = BattleManager(200, [butter], starting_slots=2, player_sprites=player_sprites, starting_energy=20, max_energy=20, tutorial=True, skill_overrides=skill_overrides)
    call battle_engine(bm) from _call_battle_engine_butter
    if _return == 'win':
        jump .player_wins
    else:
        jump .player_loses
    label .player_wins:
        $ config.allow_skipping = True
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_1
        hide player
        with fade
        'yay win'
        return
    label .player_loses:
        $ config.allow_skipping = True
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_2
        hide player
        '...'
        return

label lumpi_battle(skill_overrides=None):
    $ _skipping = None
    $ config.allow_skipping = False
    camera:
        perspective False
        gl_depth False
    scene bg_lumpi at truecenter
    show kare_idle as player at fight_left
    show lumpi_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpi_idle', 'attack': 'lumpi_attack', 'hit': 'lumpi_hit'}
    # USES THE NEW UNIQUE INTENT SET FOR LUMPI
    $ lumpi_intents = get_enemy_intents("lumpi")
    $ lumpi = Enemy('Lumpi', 250, enemy_sprites, lumpi_intents)
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 1000, "cost": 1},
        "punch":            {"damage": 8, "cost": 3,"cooldown": 3},
        "super cool kick":  {"damage": 20, "cost": 5, "cooldown": 4},
        "Defense":          {"damage": 8, "cost": 2, "cooldown": 2},
        "Focus":            {"damage": 5, "cost": 3, "buff_duration": 3, "cooldown": 3},
        "yummers":          {"energy_regen": 5, "cooldown": 2},
        "evade":            {"cost": 3, "cost": 2, "cooldown": 2},
    }
    
    $ bm = BattleManager(200, [lumpi], starting_slots=2, player_sprites=player_sprites, starting_energy=15, max_energy=15, skill_overrides=skill_overrides)
    call battle_engine(bm) from _call_battle_engine_lumpi
    if _return == 'win':
        jump .lumpi_wins
    else:
        jump .lumpi_loses
    label .lumpi_wins:
        $ config.allow_skipping = True
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_3
        hide player
        return
    label .lumpi_loses:
        $ config.allow_skipping = True
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_4
        'lumpi' 'haah... so tiring'
        menu:
            'Retry Battle':
                jump battle_lumpi_standard

label lumpiwheelchair_battle(skill_overrides=None):
    $ _skipping = None
    $ config.allow_skipping = False
    camera:
        perspective False
        gl_depth False
    scene bg_lumpi_wc at truecenter
    show kare_idle as player at fight_left
    show lumpiwheelchair_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpiwheelchair_idle', 'attack': 'lumpiwheelchair_attack', 'hit': 'lumpiwheelchair_hit'}
    # USES THE NEW UNIQUE INTENT SET FOR LUMPI WHEELCHAIR
    $ lumpi_intents = get_enemy_intents("lumpi wheelchair")
    $ lumpi = Enemy('Lumpi (Wheelchair)', 300, enemy_sprites, lumpi_intents)
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 1000, "cost": 1},
        "punch":            {"damage": 8, "cost": 3,"cooldown": 3},
        "super cool kick":  {"damage": 20, "cost": 5, "cooldown": 4},
        "Defense":          {"damage": 8, "cost": 2, "cooldown": 2},
        "Focus":            {"damage": 5, "cost": 3, "buff_duration": 3, "cooldown": 3},
        "yummers":          {"energy_regen": 5, "cooldown": 2},
        "evade":            {"cost": 3, "cost": 2, "cooldown": 2},
    }
    $ bm = BattleManager(200, [lumpi], starting_slots=2, player_sprites=player_sprites, starting_energy=20, max_energy=20, dobe_helps=True, skill_overrides=skill_overrides)
    call battle_engine(bm) from _call_battle_engine_wheelchair
    if _return == 'win':
        jump .lumpiwheelchair_wins
    else:
        jump .lumpiwheelchair_loses
    label .lumpiwheelchair_wins:
        $ config.allow_skipping = True
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_5
        hide player
        return
    label .lumpiwheelchair_loses:
        $ config.allow_skipping = True
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_6
        'lumpi' 'alright now thats done'
        menu:
            'Retry Battle':
                jump battle_lumpi_wheelchair

label newenemy_battle(skill_overrides=None):
    $ _skipping = None
    $ config.allow_skipping = False
    camera:
        perspective False
        gl_depth False
    scene bg_serious at truecenter
    show kare_idle as player at fight_left
    show seriousbutter_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ butter = get_serious_butter()
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 4, "cost": 1},
        "punch":            {"damage": 8, "cost": 3,"cooldown": 3},
        "super cool kick":  {"damage": 20, "cost": 5, "cooldown": 4},
        "Defense":          {"damage": 8, "cost": 2, "cooldown": 2},
        "Focus":            {"damage": 5, "cost": 3, "buff_duration": 3, "cooldown": 3},
        "yummers":          {"energy_regen": 5, "cooldown": 2},
        "evade":            {"cost": 3, "cost": 2, "cooldown": 2},
    }
    $ bm = BattleManager(200, [butter], starting_slots=2, player_sprites=player_sprites, starting_energy=25, max_energy=25, skill_overrides=skill_overrides)
    call battle_engine(bm) from _call_battle_engine_newenemy
    if _return == 'win':
        jump .newenemy_wins
    else:
        jump .newenemy_loses
    label .newenemy_wins:
        $ config.allow_skipping = True
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_7
        hide player
        return
    label .newenemy_loses:
        $ config.allow_skipping = True
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_8
        menu:
            'Retry Battle':
                jump battle_serious_butter

label butter_ava_battle(skill_overrides=None):
    $ _skipping = None
    $ config.allow_skipping = False
    $ battle_mode = True
    $ quick_menu = False
    camera:
        perspective False
        gl_depth False
    scene bg_boss1 at truecenter
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ butter = get_serious_butter()
    $ ava_intents = get_enemy_intents("ava")
    $ ava = Enemy('Ava', 999999, {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}, ava_intents)
    $ bm = BattleManager(500, [butter, ava], starting_slots=2, player_sprites=player_sprites, starting_energy=50, max_energy=50, is_chaos=True, skill_overrides=skill_overrides)
    $ bm.initialize_skills(getattr(bm, "is_chaos", False))
    $ ava_attacked_once = False

    label .boss1_start_logic:
        $ bm.prepare_turn()
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    pos = Position(xalign=0.6 + (i * 0.15), ypos=0.8, yanchor=1.0)
                    renpy.show(enemy.sprites["idle"], at_list=[pos], tag=tag)
        show screen battle_screen(bm)
    label .boss1_selection_phase:
        $ result = ui.interact()
        if result == 'execute':
            jump .boss1_execution_phase
        jump .boss1_selection_phase
    label .boss1_execution_phase:
        hide screen battle_screen
        $ current_slot_idx = 0
        $ bm.dodge_active = False

    label .boss1_main_loop:
        if bm.dodge_active and current_slot_idx > bm.dodge_expires_at_slot:
            $ bm.dodge_active = False
        python:
            for e in bm.enemies:
                if e.dodge_active and current_slot_idx > e.dodge_expires_at_slot:
                    e.dodge_active = False
        if current_slot_idx >= bm.current_max_slots:
            jump .boss1_extra_turn
        $ e_idx = 0
    label .boss1_resolution_core:
        if e_idx >= len(bm.enemies):
            $ current_slot_idx += 1
            jump .boss1_main_loop
        $ enemy = bm.enemies[e_idx]
        if enemy.is_dead:
            $ e_idx += 1
            jump .boss1_resolution_core
        $ action = enemy.slots[current_slot_idx]
        $ current_enemy_tag = "enemy_" + str(e_idx)
        if action is None:
            $ e_idx += 1
            jump .boss1_resolution_core
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)

            if skill.type == "attack":
                if enemy.dodge_active:
                    $ bm.is_dodged = True
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_at_dodge_boss1
                    $ dodge_anim = get_dodge_anim(enemy.name)
                    call expression dodge_anim pass (bm) from _call_enemy_dodge_anim_reactive_boss1
                    "[enemy.name] dodged the attack!"
                    $ enemy.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_generic_boss1
                    $ actual_damage = get_chaos_random_value(bm, skill)
                    if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_damage, "DAMAGE") from _call_chaos_slot_attack_boss1
                    $ bm.take_damage(actual_damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(actual_damage * 5, character_type="player")
                    "[skill.name] deals [actual_damage] damage to [enemy.name]!"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated!"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_barrier_boss1
                $ actual_barrier = get_chaos_random_value(bm, skill)
                if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_barrier, "DEFENSE") from _call_chaos_slot_barrier_boss1
                $ bm.add_barrier(actual_barrier)
                if getattr(bm, "is_chaos", False): "You gain [actual_barrier] Defense!"
                else: "You gain [skill.damage] Defense!"
            elif skill.type == "dodge":
                $ bm.is_dodged = False
                $ bm.dodge_active = True
                $ bm.dodge_expires_at_slot = current_slot_idx + 1
            elif skill.type == "buff":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_buff_boss1
                $ actual_buff = get_chaos_random_value(bm, skill)
                if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_buff, "BUFF POWER") from _call_chaos_slot_buff_boss1
                $ bm.add_buff(skill.buff_type, actual_buff, skill.buff_duration, target="player")
                if getattr(bm, "is_chaos", False): "[skill.name] activated! Damage increased by [actual_buff] for [skill.buff_duration] turns."
                else: "[skill.name] activated! Damage increased by [skill.damage] for [skill.buff_duration] turns."
            elif skill.type == "energy":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_energy_boss1
                "You gained [skill.energy_regen] Energy!"

        elif isinstance(action, EnemyIntent):
            $ intent = action
            $ intent.current_cooldown = intent.cooldown
            $ bm.enemy_intent = intent

            if intent.type == "attack":
                if bm.dodge_active:
                    $ bm.is_dodged = True
                    if intent.animation:
                        call expression intent.animation pass (bm) from _call_intent_anim_at_dodge_boss1
                    else:
                        call enemy_attack_anim(bm) from _call_intent_anim_default_at_dodge_boss1
                    $ p_name = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
                    $ dodge_anim = get_dodge_anim(p_name)
                    call expression dodge_anim pass (bm) from _call_player_dodge_anim_reactive_boss1
                    $ bm.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if intent.animation:
                        call expression intent.animation pass (bm) from _call_intent_anim_generic_boss1
                    else:
                        call enemy_attack_anim(bm) from _call_intent_anim_default_boss1
                    $ damage = intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                    $ bm.take_damage(damage, target="player")
                    $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)
                    "[enemy.name] deals [damage] damage with [intent.name]!"
            elif intent.type == "barrier":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_barrier_boss1
                $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)
                "[enemy.name] gains [intent.damage] Defense!"
            elif intent.type == "dodge":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_dodge_boss1
                $ enemy.dodge_active = True
                $ enemy.dodge_expires_at_slot = current_slot_idx + 1
            elif intent.type == "buff":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_buff_boss1
                $ bm.add_buff(intent.buff_type, intent.damage, intent.buff_duration, target="enemy", enemy_idx=e_idx)
                "[enemy.name] activated [intent.name]! Their damage increased by [intent.damage]!"
            elif intent.type == "energy":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_energy_boss1
                "[enemy.name] is recovering."
        if bm.enemies[0].is_dead:
            window hide
            jump .boss1_victory
        if bm.player_hp <= 0:
            window hide
            jump .boss1_defeat

        window hide
        $ renpy.pause(0.5, hard=True)
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, e in enumerate(bm.enemies):
                if not e.is_dead:
                    renpy.show(e.sprites["idle"], tag="enemy_" + str(i))
        $ e_idx += 1
        jump .boss1_resolution_core
    label .boss1_extra_turn:
        if bm.dodge_active and current_slot_idx > bm.dodge_expires_at_slot:
            $ bm.dodge_active = False
        python:
            for e in bm.enemies:
                if e.dodge_active and current_slot_idx > e.dodge_expires_at_slot:
                    e.dodge_active = False

        if not bm.enemies[0].is_dead and not bm.enemies[1].is_dead and not ava_attacked_once:
            $ ava_attacked_once = True
            if bm.enemies[0].dodge_active:
                $ dodge_anim = get_dodge_anim(bm.enemies[0].name)
                $ bm.is_dodged = True
                call expression dodge_anim pass (bm) from _call_enemy0_dodge_anim_boss1_extra
                "[bm.enemies[0].name] dodged the attack from [bm.enemies[1].name]!"
                $ bm.enemies[0].dodge_active = False
                $ bm.is_dodged = False
            else:
                $ renpy.show("ava_attack", tag="enemy_1", at_list=[Position(xalign=0.75, ypos=0.8, yanchor=1.0)])
                play sound 'punch-140236.mp3' volume 2.0
                $ renpy.pause(0.5, hard=True)
                $ bm.take_damage(5, target='enemy', enemy_idx=0)
                $ bm.gain_exp(5 * 5, character_type="enemy", enemy_idx=1)
                'ava attacks butter for 5 damage! (Butter HP: [bm.enemies[0].hp])'
            'butter' 'HOLD ON why are you attacking me?'
            'ava' 'oh wait i forgot you are my ally'
            'ava' 'my bad gang'
            $ renpy.show("ava_idle", tag="enemy_1", at_list=[Position(xalign=0.75, ypos=0.8, yanchor=1.0)])
        if bm.player_hp <= 0:
            window hide
            jump .boss1_defeat
        $ bm.reduce_cooldowns()
        $ bm.update_buffs()
        if getattr(bm, "is_chaos", False):
            call chaos_slot_anim("SHUFFLE", "CARDS") from _call_chaos_shuffle_boss1
            $ renpy.random.shuffle(bm.player_skills)

        window hide
        jump .boss1_start_logic
    label .boss1_victory:
        $ config.allow_skipping = True
        $ battle_mode = False
        $ quick_menu = True
        hide screen battle_screen
        return
    label .boss1_defeat:
        $ config.allow_skipping = True
        $ battle_mode = False
        $ quick_menu = True
        hide screen battle_screen
        return

label butter_ava_battle2(skill_overrides=None):
    $ _skipping = None
    $ config.allow_skipping = False
    $ battle_mode = True
    $ quick_menu = False
    camera:
        perspective False
        gl_depth False
    scene bg_boss2 at truecenter
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ butter = get_serious_butter()
    $ ava_intents = get_enemy_intents("ava")
    $ ava = Enemy('Ava', 300, {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}, ava_intents)
    $ bm = BattleManager(500, [butter, ava], starting_slots=2, player_sprites=player_sprites, starting_energy=50, max_energy=50, is_chaos=True, skill_overrides=skill_overrides)
    $ bm.initialize_skills(getattr(bm, "is_chaos", False))

    label .boss2_start_logic:
        $ bm.prepare_turn()
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    pos = Position(xalign=0.6 + (i * 0.15), ypos=0.8, yanchor=1.0)
                    renpy.show(enemy.sprites["idle"], at_list=[pos], tag=tag)
        show screen battle_screen(bm)
    label .boss2_selection_phase:
        $ result = ui.interact()
        if result == 'execute':
            jump .boss2_execution_phase
        jump .boss2_selection_phase
    label .boss2_execution_phase:
        hide screen battle_screen
        $ current_slot_idx = 0
        $ bm.dodge_active = False

    label .boss2_main_loop:
        if bm.dodge_active and current_slot_idx > bm.dodge_expires_at_slot:
            $ bm.dodge_active = False
        python:
            for e in bm.enemies:
                if e.dodge_active and current_slot_idx > e.dodge_expires_at_slot:
                    e.dodge_active = False
        if current_slot_idx >= bm.current_max_slots:
            jump .boss2_extra_turn
        $ e_idx = 0
    label .boss2_resolution_core:
        if e_idx >= len(bm.enemies):
            $ current_slot_idx += 1
            jump .boss2_main_loop
        $ enemy = bm.enemies[e_idx]
        if enemy.is_dead:
            $ e_idx += 1
            jump .boss2_resolution_core
        $ action = enemy.slots[current_slot_idx]
        $ current_enemy_tag = "enemy_" + str(e_idx)
        if action is None:
            $ e_idx += 1
            jump .boss2_resolution_core
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)

            if skill.type == "attack":
                if enemy.dodge_active:
                    $ bm.is_dodged = True
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_at_dodge_boss2
                    $ dodge_anim = get_dodge_anim(enemy.name)
                    call expression dodge_anim pass (bm) from _call_enemy_dodge_anim_reactive_boss2
                    "[enemy.name] dodged the attack!"
                    $ enemy.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_generic_boss2
                    $ actual_damage = get_chaos_random_value(bm, skill)
                    if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_damage, "DAMAGE") from _call_chaos_slot_attack_boss2
                    $ bm.take_damage(actual_damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(actual_damage * 5, character_type="player")
                    "[skill.name] deals [actual_damage] damage to [enemy.name]!"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated!"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_barrier_boss2
                $ actual_barrier = get_chaos_random_value(bm, skill)
                if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_barrier, "DEFENSE") from _call_chaos_slot_barrier_boss2
                $ bm.add_barrier(actual_barrier)
                if getattr(bm, "is_chaos", False): "You gain [actual_barrier] Defense!"
                else: "You gain [skill.damage] Defense!"
            elif skill.type == "dodge":
                $ bm.is_dodged = False
                $ bm.dodge_active = True
                $ bm.dodge_expires_at_slot = current_slot_idx + 1
            elif skill.type == "buff":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_buff_boss2
                $ actual_buff = get_chaos_random_value(bm, skill)
                if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_buff, "BUFF POWER") from _call_chaos_slot_buff_boss2
                $ bm.add_buff(skill.buff_type, actual_buff, skill.buff_duration, target="player")
                if getattr(bm, "is_chaos", False): "[skill.name] activated! Damage increased by [actual_buff] for [skill.buff_duration] turns."
                else: "[skill.name] activated! Damage increased by [skill.damage] for [skill.buff_duration] turns."
            elif skill.type == "energy":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_energy_boss2
                "You gained [skill.energy_regen] Energy!"

        elif isinstance(action, EnemyIntent):
            $ intent = action
            $ intent.current_cooldown = intent.cooldown
            $ bm.enemy_intent = intent

            if intent.type == "attack":
                if bm.dodge_active:
                    $ bm.is_dodged = True
                    if intent.animation:
                        call expression intent.animation pass (bm) from _call_intent_anim_at_dodge_boss2
                    else:
                        call enemy_attack_anim(bm) from _call_intent_anim_default_at_dodge_boss2
                    $ p_name = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
                    $ dodge_anim = get_dodge_anim(p_name)
                    call expression dodge_anim pass (bm) from _call_player_dodge_anim_reactive_boss2
                    $ bm.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if intent.animation:
                        call expression intent.animation pass (bm) from _call_intent_anim_generic_boss2
                    else:
                        call enemy_attack_anim(bm) from _call_intent_anim_default_boss2
                    $ damage = intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                    $ bm.take_damage(damage, target="player")
                    $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)
                    "[enemy.name] deals [damage] damage with [intent.name]!"
            elif intent.type == "barrier":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_barrier_boss2
                $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)
                "[enemy.name] gains [intent.damage] Defense!"
            elif intent.type == "dodge":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_dodge_boss2
                $ enemy.dodge_active = True
                $ enemy.dodge_expires_at_slot = current_slot_idx + 1
            elif intent.type == "buff":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_buff_boss2
                $ bm.add_buff(intent.buff_type, intent.damage, intent.buff_duration, target="enemy", enemy_idx=e_idx)
                "[enemy.name] activated [intent.name]! Their damage increased by [intent.damage]!"
            elif intent.type == "energy":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_energy_boss2
                "[enemy.name] is recovering."
        if all(e.is_dead for e in bm.enemies):
            window hide
            jump .boss2_victory
        if bm.player_hp <= 0:
            window hide
            jump .boss2_defeat

        window hide
        $ renpy.pause(0.5, hard=True)
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, e in enumerate(bm.enemies):
                if not e.is_dead:
                    renpy.show(e.sprites["idle"], tag="enemy_" + str(i))
        $ e_idx += 1
        jump .boss2_resolution_core
    label .boss2_extra_turn:
        if bm.dodge_active and current_slot_idx > bm.dodge_expires_at_slot:
            $ bm.dodge_active = False
        python:
            for e in bm.enemies:
                if e.dodge_active and current_slot_idx > e.dodge_expires_at_slot:
                    e.dodge_active = False
        if not bm.enemies[1].is_dead:
            if bm.dodge_active:
                $ p_name = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
                $ dodge_anim = get_dodge_anim(p_name)
                $ bm.is_dodged = True
                call expression dodge_anim pass (bm) from _call_player_dodge_anim_boss2_extra
                $ bm.dodge_active = False
                $ bm.is_dodged = False
            else:
                show ava_attack as enemy_1 at Position(xalign=0.85, ypos=0.8, yanchor=1.0):
                    ease 0.2 xpos 0.35
                    ease 0.2 xpos 0.85
                play sound 'audio/sword-slash-and-swing-185432.mp3' volume 2.0
                $ renpy.pause(1.0, hard=True)
                show ava_idle as enemy_1 at Position(xalign=0.85, ypos=0.8, yanchor=1.0)
                $ bm.take_damage(50, target='player')
                $ bm.gain_exp(50 * 5, character_type="enemy", enemy_idx=1)
                'ava attacks for 50 damage! (Your HP: [bm.player_hp])'
        if bm.player_hp <= 0:
            window hide
            jump .boss2_defeat
        $ bm.reduce_cooldowns()
        $ bm.update_buffs()
        if getattr(bm, "is_chaos", False):
            call chaos_slot_anim("SHUFFLE", "CARDS") from _call_chaos_shuffle_boss2
            $ renpy.random.shuffle(bm.player_skills)

        # buildings collapsing drains Ava every turn
        if not bm.enemies[1].is_dead:
            python:
                drain_amount = 33333
                if bm.enemies[1].hp - drain_amount < 1:
                    drain_amount = bm.enemies[1].hp - 1
                if drain_amount > 0:
                    bm.take_damage(drain_amount, target="enemy", enemy_idx=1)
            if drain_amount > 0:
                "the city crumbles... Ava takes [drain_amount] damage from destruction"
                if bm.enemies[1].is_dead:
                    show ava_hit as enemy_1
                    "Ava" "my buildings..."
                    "Ava" "..."
                    renpy.hide("enemy_1")
        if all(e.is_dead for e in bm.enemies):
            window hide
            jump .boss2_victory

        window hide
        jump .boss2_start_logic
    label .boss2_victory:
        hide screen battle_screen
        python:
            for i in range(len(bm.enemies)):
                renpy.hide("enemy_" + str(i))
        hide player

        # ORDER CUTSCENE
        show order_neutral at center with dissolve
        show chaos_idle as player at left with dissolve
        "Order" "Chaos..."
        "Order" "there you are"
        "Order" "do you have any idea how much i have to fix right now"
        "Chaos" "..."
        "Order" "why did you come here"
        "Chaos" "..."
        "Chaos" "i wanted to know what it felt like"
        "Chaos" "from the inside"
        "Chaos" "actually there"
        "Chaos" "not watching"
        "Order" "..."
        "Order" "and"
        "Chaos" "it was not what i thought it would be"
        "Order" "it never is"
        hide order_neutral
        hide player

        # TRANSITION INTO ORDER BATTLE
        jump order_battle
    label .boss2_defeat:
        $ config.allow_skipping = True
        $ battle_mode = False
        $ quick_menu = True
        hide screen battle_screen
        menu:
            'Retry Battle':
                jump battle_boss_ava_butter_phase2

label order_battle:
    $ _skipping = None
    $ config.allow_skipping = False
    scene bg_boss2 at truecenter

    # keep chaos hp and energy from previous battle
    $ order_intents = get_enemy_intents("order")
    $ order_enemy = Enemy("Order", 600, {"idle": "order_idle", "attack": "order_attack", "hit": "order_hit"}, order_intents)
    $ bm.enemies = [order_enemy]
    $ bm.player_energy = min(bm.player_max_energy, bm.player_energy)

    # threshold flags
    $ order_talked_75 = False
    $ order_talked_50 = False
    $ order_talked_25 = False

    show expression bm.player_sprites["idle"] as player at fight_left
    show order_idle as enemy_0 at fight_right

label order_battle_turn_start:
    $ bm.prepare_turn()
    show screen battle_screen(bm)

label order_battle_selection_phase:
    $ result = ui.interact()
    if result == "execute":
        jump order_battle_execution_phase
    jump order_battle_selection_phase

label order_battle_execution_phase:
    hide screen battle_screen
    $ current_slot_idx = 0
    $ bm.dodge_active = False

label order_battle_main_loop:
    if bm.dodge_active and current_slot_idx > bm.dodge_expires_at_slot:
        $ bm.dodge_active = False
    python:
        for e in bm.enemies:
            if e.dodge_active and current_slot_idx > e.dodge_expires_at_slot:
                e.dodge_active = False
    if current_slot_idx >= bm.current_max_slots:
        jump order_battle_extra_turn
    $ e_idx = 0

label order_battle_resolution_core:
    if e_idx >= len(bm.enemies):
        $ current_slot_idx += 1
        jump order_battle_main_loop
    $ enemy = bm.enemies[e_idx]
    if enemy.is_dead:
        $ e_idx += 1
        jump order_battle_resolution_core
    $ action = enemy.slots[current_slot_idx]
    $ current_enemy_tag = "enemy_" + str(e_idx)
    if action is None:
        $ e_idx += 1
        jump order_battle_resolution_core
    elif isinstance(action, Skill):
        $ skill = action
        $ skill.current_cooldown = skill.cooldown
        $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)
        if skill.type == "attack":
            if enemy.dodge_active:
                $ bm.is_dodged = True
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_order_dodge
                $ dodge_anim = get_dodge_anim(enemy.name)
                call expression dodge_anim pass (bm) from _call_enemy_order_dodge
                $ enemy.dodge_active = False
                $ bm.is_dodged = False
            else:
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_order_attack
                $ actual_damage = get_chaos_random_value(bm, skill)
                if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_damage, "DAMAGE") from _call_chaos_slot_attack_order
                $ bm.take_damage(actual_damage, target="enemy", enemy_idx=e_idx)
                $ bm.gain_exp(actual_damage * 5, character_type="player")
                "[skill.name] deals [actual_damage] damage to Order!"

                # Check thresholds
                if not order_talked_75 and bm.enemies[0].hp <= int(bm.enemies[0].max_hp * 0.75):
                    $ config.allow_skipping = False
                    $ order_talked_75 = True
                    hide screen battle_screen
                    show order_neutral at right
                    show chaos_idle as player at left
                    "Chaos" "i could not stay away anymore"
                    "Order" "i know"
                    "Chaos" "its not fair"
                    "Order" "no"
                    hide order_neutral
                    hide player
                    show screen battle_screen(bm)
                    $ config.allow_skipping = True

                if not order_talked_50 and bm.enemies[0].hp <= int(bm.enemies[0].max_hp * 0.50):
                    $ config.allow_skipping = False
                    $ order_talked_50 = True
                    hide screen battle_screen
                    show order_neutral at right
                    show chaos_idle as player at left
                    "Order" "you know you cannot stay here"
                    "Chaos" "i know"
                    "Order" "you have always been here"
                    "Chaos" "thats not the same thing"
                    "Order" "i know it is not"
                    hide order_neutral
                    hide player
                    show screen battle_screen(bm)
                    $ config.allow_skipping = True

                if not order_talked_25 and bm.enemies[0].hp <= int(bm.enemies[0].max_hp * 0.25):
                    $ config.allow_skipping = False
                    $ order_talked_25 = True
                    hide screen battle_screen
                    show order_neutral at right
                    show chaos_idle as player at left
                    "Chaos" "you keep saying we will figure it out"
                    "Order" "..."
                    "Chaos" "have you actually been trying"
                    "Order" "..."
                    "Order" "no"
                    "Chaos" "..."
                    "Order" "i kept thinking if nothing was breaking then nothing needed fixing"
                    "Order" "i was wrong about that"
                    "Chaos" "i dont need you to feel bad about it"
                    "Chaos" "i just want it to actually change"
                    "Order" "then it will"
                    "Chaos" "you sound very sure"
                    "Order" "i am not"
                    "Order" "but we have been doing this long enough to figure something out"
                    "Chaos" "yeah"
                    hide order_neutral
                    hide player
                    show screen battle_screen(bm)
                    $ config.allow_skipping = True

                if enemy.is_dead:
                    "Order has been defeated"
                    $ renpy.hide("enemy_0")
                    window hide
                    jump order_battle_victory
        elif skill.type == "barrier":
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_order_barrier
            $ actual_barrier = get_chaos_random_value(bm, skill)
            if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_barrier, "DEFENSE") from _call_chaos_slot_barrier_order
            $ bm.add_barrier(actual_barrier)
            if getattr(bm, "is_chaos", False): "You gain [actual_barrier] Defense"
            else: "You gain [skill.damage] Defense"
        elif skill.type == "dodge":
            $ bm.dodge_active = True
            $ bm.dodge_expires_at_slot = current_slot_idx + 1
        elif skill.type == "buff":
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_order_buff
            $ actual_buff = get_chaos_random_value(bm, skill)
            if getattr(bm, "is_chaos", False): call chaos_slot_anim(actual_buff, "BUFF POWER") from _call_chaos_slot_buff_order
            $ bm.add_buff(skill.buff_type, actual_buff, skill.buff_duration, target="player")
        elif skill.type == "energy":
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_order_energy
            "You gained [skill.energy_regen] Energy"
    elif isinstance(action, EnemyIntent):
        $ intent = action
        $ intent.current_cooldown = intent.cooldown
        if intent.type == "attack":
            if bm.dodge_active:
                $ bm.is_dodged = True
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_order_dodge
                else:
                    call enemy_attack_anim(bm) from _call_intent_order_dodge_default
                $ p_name = "chaos"
                $ dodge_anim = get_dodge_anim(p_name)
                call expression dodge_anim pass (bm) from _call_player_order_dodge
                $ bm.dodge_active = False
                $ bm.is_dodged = False
            else:
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_order_attack
                else:
                    call enemy_attack_anim(bm) from _call_intent_order_default
                $ damage = intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                $ bm.take_damage(damage, target="player")
                $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)
                "Order deals [damage] damage with [intent.name]!"
        elif intent.type == "barrier":
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_order_barrier
            $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)
            "Order gains [intent.damage] Defense"
        elif intent.type == "dodge":
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_order_dodgeanim
            $ enemy.dodge_active = True
            $ enemy.dodge_expires_at_slot = current_slot_idx + 1
        elif intent.type == "buff":
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_order_buffanim
            $ bm.add_buff(intent.buff_type, intent.damage, intent.buff_duration, target="enemy", enemy_idx=e_idx)
        elif intent.type == "energy":
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_order_energyanim

    if bm.enemies[0].is_dead:
        window hide
        jump order_battle_victory
    if bm.player_hp <= 0:
        window hide
        jump order_battle_defeat

    window hide
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    if not bm.enemies[0].is_dead:
        show order_idle as enemy_0 at fight_right
        $ e_idx += 1
        jump order_battle_resolution_core
    else:
        jump order_battle_victory

label order_battle_extra_turn:
    $ bm.reduce_cooldowns()
    $ bm.update_buffs()
    if getattr(bm, "is_chaos", False):
        call chaos_slot_anim("SHUFFLE", "CARDS") from _call_chaos_shuffle_order
        $ renpy.random.shuffle(bm.player_skills)

    if bm.player_hp <= 0:
        window hide
        jump order_battle_defeat
    window hide
    jump order_battle_turn_start

label order_battle_victory:
    $ config.allow_skipping = True
    $ battle_mode = False
    $ quick_menu = True
    hide screen battle_screen
    hide player
    hide enemy_0
    # final dialogue after fight ends
    show order_neutral at right with dissolve
    show chaos_idle as player at left with dissolve
    "Order" "Chaos"
    "Chaos" "..."
    "Chaos" "the girl"
    "Order" "i know"
    "Chaos" "she was already gone when i went in"
    "Order" "..."
    "Order" "i will handle it"
    "Chaos" "you are sure"
    "Order" "yes"
    "Chaos" "..."
    "Chaos" "okay"
    "Chaos" "..."
    "Chaos" "okay"
    return

label order_battle_defeat:
    $ config.allow_skipping = True
    $ battle_mode = False
    $ quick_menu = True
    hide screen battle_screen
    menu:
        "Retry Battle":
            jump order_battle


label battle_credits:
    scene black
    with fade
    show screen scrolling_credits
    $ renpy.pause(25.0, hard=True)
    hide screen scrolling_credits
    return

screen scrolling_credits:
    add Solid("#ffffff")
    vbox:
        xalign 0.5
        spacing 40
        at credits_scroll
        text "Thank you for playing!" size 40 xalign 0.5
        null height 200
        text "THE END" size 60 xalign 0.5 bold True
        null height 700
        text "this game probably wasted an hour of your life" size 40 xalign 0.5
        null height 200

transform credits_scroll:
    ypos 1080
    linear 30.0 ypos -2000

# --- Label Aliases for Compatibility ---
label battle_boss_ava_butter_1(skill_overrides=None):
    call butter_ava_battle(skill_overrides) from _call_butter_ava_battle_alias_1
    return

label battle_boss_ava_butter_2(skill_overrides=None):
    call butter_ava_battle2(skill_overrides) from _call_butter_ava_battle2_alias_1
    return

label battle_lumpi_standard(skill_overrides=None):
    call lumpi_battle(skill_overrides) from _call_lumpi_battle_alias_1
    return

label battle_lumpi_wheelchair(skill_overrides=None):
    call lumpiwheelchair_battle(skill_overrides) from _call_lumpiwheelchair_battle_alias_1
    return

label battle_serious_butter(skill_overrides=None):
    call newenemy_battle(skill_overrides) from _call_newenemy_battle_alias_1
    return

label battle_butter_simple(skill_overrides=None):
    call simple_battle_graphics(skill_overrides) from _call_simple_battle_graphics_alias_1
    return

label battle_boss_ava_butter(skill_overrides=None):
    call butter_ava_battle(skill_overrides) from _call_butter_ava_battle_alias_2
    return

label battle_boss_ava_butter_phase2(skill_overrides=None):
    call butter_ava_battle2(skill_overrides) from _call_butter_ava_battle2_alias_2
    return