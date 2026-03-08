




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
# Solid bar ─ attack / ultimate
image typebar_attack = Solid("#000000", xsize=130, ysize=6)
image typebar_ultimate = Solid("#000000", xsize=130, ysize=9)

# Horizontal stripe ─ barrier
image typebar_barrier_tile = Composite((8, 6),
    (0, 0), Solid("#000000", xsize=4, ysize=6),
    (4, 0), Solid("#ffffff", xsize=4, ysize=6),
)
image typebar_barrier = Tile("typebar_barrier_tile", xsize=130, ysize=6)

# Fine stripe ─ energy
image typebar_energy_tile = Composite((4, 6),
    (0, 0), Solid("#000000", xsize=2, ysize=6),
    (2, 0), Solid("#ffffff", xsize=2, ysize=6),
)
image typebar_energy = Tile("typebar_energy_tile", xsize=130, ysize=6)

# Diagonal ─ dodge
image typebar_dodge_tile = Composite((6, 6),
    (0, 0), Solid("#000000", xsize=3, ysize=3),
    (3, 3), Solid("#000000", xsize=3, ysize=3),
    (3, 0), Solid("#ffffff", xsize=3, ysize=3),
    (0, 3), Solid("#ffffff", xsize=3, ysize=3),
)
image typebar_dodge = Tile("typebar_dodge_tile", xsize=130, ysize=6)

# Reverse diagonal ─ buff
image typebar_buff_tile = Composite((6, 6),
    (0, 3), Solid("#000000", xsize=3, ysize=3),
    (3, 0), Solid("#000000", xsize=3, ysize=3),
    (0, 0), Solid("#ffffff", xsize=3, ysize=3),
    (3, 3), Solid("#ffffff", xsize=3, ysize=3),
)
image typebar_buff = Tile("typebar_buff_tile", xsize=130, ysize=6)

# ── CHAOS VERSIONS (inverted colours)
image typebar_barrier_chaos_tile = Composite((8, 6),
    (0, 0), Solid("#ffffff", xsize=4, ysize=6),
    (4, 0), Solid("#000000", xsize=4, ysize=6),
)
image typebar_barrier_chaos = Tile("typebar_barrier_chaos_tile", xsize=130, ysize=6)

image typebar_energy_chaos_tile = Composite((4, 6),
    (0, 0), Solid("#ffffff", xsize=2, ysize=6),
    (2, 0), Solid("#000000", xsize=2, ysize=6),
)
image typebar_energy_chaos = Tile("typebar_energy_chaos_tile", xsize=130, ysize=6)

image typebar_dodge_chaos_tile = Composite((6, 6),
    (0, 0), Solid("#ffffff", xsize=3, ysize=3),
    (3, 3), Solid("#ffffff", xsize=3, ysize=3),
    (3, 0), Solid("#000000", xsize=3, ysize=3),
    (0, 3), Solid("#000000", xsize=3, ysize=3),
)
image typebar_dodge_chaos = Tile("typebar_dodge_chaos_tile", xsize=130, ysize=6)

image typebar_buff_chaos_tile = Composite((6, 6),
    (0, 3), Solid("#ffffff", xsize=3, ysize=3),
    (3, 0), Solid("#ffffff", xsize=3, ysize=3),
    (0, 0), Solid("#000000", xsize=3, ysize=3),
    (3, 3), Solid("#000000", xsize=3, ysize=3),
)
image typebar_buff_chaos = Tile("typebar_buff_chaos_tile", xsize=130, ysize=6)

# ── ENEMY SLOT crosshatch background
image slot_enemy_hatch = Tile(
    Composite((5, 5),
        (0, 0), Solid("#00000000", xsize=5, ysize=5),
        (0, 4), Solid("#00000012", xsize=5, ysize=1),
    ),
    xsize=1200, ysize=70
)

image slot_enemy_hatch_chaos = Tile(
    Composite((5, 5),
        (0, 0), Solid("#00000000", xsize=5, ysize=5),
        (0, 4), Solid("#ffffff12", xsize=5, ysize=1),
    ),
    xsize=1200, ysize=70
)
# --- Transforms ---
# ── Single enemy
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

# ── Player └ shift slightly left in multi-enemy fights
transform fight_left_multi:
    xpos 0.28 ypos 0.8 anchor (0.5, 1.0)

# ── Two enemies side by side
# Enemy 0 (Butter) at xpos 0.62
# Enemy 1 (Ava) at xpos 0.80

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

# ── CHAOS slot machine reel animation
transform reel_scroll_transform(duration, num_items, item_height):
    ypos -((num_items - 1) * item_height)
    easeout duration ypos 0

# ── A single card "spinning" └ icons scroll up fast then slow to a stop
transform card_reel_spin(delay=0.0):
    yoffset 0 alpha 1.0
    pause delay
    # fast spin └ blur via quick yoffset cycling
    linear 0.06 yoffset -30
    linear 0.06 yoffset 0
    linear 0.06 yoffset -30
    linear 0.06 yoffset 0
    linear 0.06 yoffset -30
    linear 0.06 yoffset 0
    # slow down
    linear 0.12 yoffset -20
    linear 0.12 yoffset 0
    linear 0.18 yoffset -10
    linear 0.18 yoffset 0
    # final bounce land
    linear 0.08 yoffset -5
    linear 0.12 yoffset 2
    linear 0.08 yoffset 0

# ── The card fades out before spinning
transform card_reel_fadeout(delay=0.0):
    alpha 1.0
    pause delay
    linear 0.1 alpha 0.0

# ── The new card fades in after the reel stops
transform card_reel_fadein(delay=0.0):
    alpha 0.0
    pause delay
    linear 0.15 alpha 1.0

# ── Card landing punctuation
transform card_land_flash(is_chaos=False):
    alpha 0.0
    linear 0.05 alpha (0.7 if is_chaos else 0.5)
    linear 0.2  alpha 0.0

init python:
    import random

    # ── KARE (light mode)
    C_PAPER       = "#ffffff"
    C_PAPER_DARK  = "#f0f0f0"
    C_PAPER_MID   = "#e0e0e0"
    C_INK         = "#000000"
    C_INK_MID     = "#333333"
    C_INK_LIGHT   = "#666666"
    C_INK_FAINT   = "#aaaaaa"

    # ── CHAOS (dark mode)
    C_CHAOS_PAPER      = "#000000"
    C_CHAOS_PAPER_DARK = "#111111"
    C_CHAOS_PAPER_MID  = "#1a1a1a"
    C_CHAOS_INK        = "#ffffff"
    C_CHAOS_INK_MID    = "#cccccc"
    C_CHAOS_INK_LIGHT  = "#888888"
    C_CHAOS_INK_FAINT  = "#333333"

    def ink(is_chaos):
        return C_CHAOS_INK if is_chaos else C_INK

    def paper(is_chaos):
        return C_CHAOS_PAPER if is_chaos else C_PAPER

    def ink_light(is_chaos):
        return C_CHAOS_INK_LIGHT if is_chaos else C_INK_LIGHT

    def ink_faint(is_chaos):
        return C_CHAOS_INK_FAINT if is_chaos else C_INK_FAINT

    def paper_dark(is_chaos):
        return C_CHAOS_PAPER_DARK if is_chaos else C_PAPER_DARK

    def paper_mid(is_chaos):
        return C_CHAOS_PAPER_MID if is_chaos else C_PAPER_MID

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

    def get_typebar(skill_type, is_chaos):
        if skill_type == "attack":
            return "typebar_attack"
        elif skill_type == "barrier":
            return "typebar_barrier_chaos" if is_chaos else "typebar_barrier"
        elif skill_type == "energy":
            return "typebar_energy_chaos" if is_chaos else "typebar_energy"
        elif skill_type == "dodge":
            return "typebar_dodge_chaos" if is_chaos else "typebar_dodge"
        elif skill_type in ["buff", "corrode", "inversion", "unravel", "leech"]:
            return "typebar_buff_chaos" if is_chaos else "typebar_buff"
        else:
            # ultimate / fracture / collapse / overload / unknown
            return "typebar_ultimate"

    def get_chaos_random_value(bm, skill):
        if not getattr(skill, "is_chaos_skill", False):
            if skill.type == "attack":
                return max(0, skill.damage + bm.get_total_buff_value("damage", target="player") - bm.get_total_buff_value("corrosion", target="player"))
            return skill.damage
        if skill.type == "attack":
            base = 0
            if skill.name == "interitus": base = renpy.random.randint(1, 20)
            elif skill.name == "Cataclysm": base = renpy.random.randint(1, 30)
            elif skill.name == "??????": base = renpy.random.randint(1, 60)
            else: base = renpy.random.randint(1, 20)
            return max(0, base + bm.get_total_buff_value("damage", target="player") - bm.get_total_buff_value("corrosion", target="player"))
        if skill.type in ["barrier", "buff"]:
            return renpy.random.randint(1, 50)
        if skill.type == "energy":
            return renpy.random.randint(1, 50)
        if skill.type == "fracture":
            return renpy.random.randint(1, 10) + bm.get_total_buff_value("damage", target="player")
        if skill.type == "corrode":
            return renpy.random.randint(2, 3)
        return skill.damage


    def get_serious_butter():
        intents = get_enemy_intents("law")
        sprites = {'idle': 'seriousbutter_idle', 'attack': 'seriousbutter_attack', 'hit': 'seriousbutter_hit'}
        return Enemy('Butter', 500, sprites, intents)

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
        def __init__(self, name, cost=0, damage=0, energy_regen=0, cooldown=0, type="attack", desc="", animation=None, buff_type=None, buff_duration=0, card_image=None, is_chaos_skill=False, icon=""):
            self.icon = icon
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
            self.is_chaos_skill = is_chaos_skill

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
            self.collapsed = False
            self.still_standing_triggered = False

        @property
        def intents(self):
            # Returns only the currently unlocked intents
            pool = self.full_intent_pool[:self.unlocked_intents_count]
            # Ava's STILL STANDING is handled as a passive triggered by environmental drain
            pool = [i for i in pool if i.type != "still_standing"]
            return pool

    class BattleManager:
        tutorial = False
        dobe_helps = False
        is_chaos = False
        is_shuffling = False
        kare_shuffle_mode = False
        shuffled_slot_idx = -1
        original_skill = None
        chaos_pool = []
        def __init__(self, player_max_hp, enemies=None, starting_slots=2, player_sprites=None, starting_energy=10, max_energy=10, tutorial=False, dobe_helps=False, is_chaos=False, skill_overrides=None, kare_shuffle_mode=False):
            self.player_hp = player_max_hp
            self.player_max_hp = player_max_hp
            self.player_energy = starting_energy
            self.player_max_energy = max_energy
            self.player_barrier = 0
            self.player_buffs = []
            self.tutorial = tutorial
            self.dobe_helps = dobe_helps
            self.is_chaos = is_chaos
            self.kare_shuffle_mode = kare_shuffle_mode
            self.player_name = "Chaos" if is_chaos else "Kare"
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

            # New metrics for specific skills
            self.total_skills_used_this_battle = 0
            self.skills_used_this_turn_types = []
            self.skills_used_last_turn_types = []
            self.rolled_one_last_turn = False
            self.last_drain_amount = 0
            self.skills_unlocked_this_battle = 0
            self.rolled_one_this_turn = False

        def initialize_skills(self, is_chaos):
            char_name = "chaos" if is_chaos else "kare"
            self.full_skill_pool = get_character_skills(char_name)
            icons = {
                "slap": "W", "Defense": "⛊", "Focus": "F", "punch": "P", "yummers": "Y", "evade": "E", "super cool kick": "K",
                "interitus": "~~", "Embrace": "◎", "Entropy": "3", "Cataclysm": "⚡", "dissolutum": "⊘", "playing rough": "R", "??????": "||||",
                "Unravel": "U", "Fracture": "X", "Corrode": "C", "Inversion": "I", "Collapse": "L", "Leech": "H", "Overload": "O"
            }
            for s in self.full_skill_pool:
                s.icon = icons.get(s.name, "S")
            if self.kare_shuffle_mode:
                self.chaos_pool = get_character_skills("chaos")
                for s in self.chaos_pool:
                    s.icon = icons.get(s.name, "S")
            for skill in self.full_skill_pool:
                if skill.name in self.skill_overrides:
                    for attr, value in self.skill_overrides[skill.name].items():
                        setattr(skill, attr, value)
            if is_chaos:
                # First 7 are the core skills in order
                core_pool = self.full_skill_pool[:7]
                new_pool = self.full_skill_pool[7:]
                renpy.random.shuffle(new_pool)

                self.full_skill_pool = []
                for i in range(7):
                    self.full_skill_pool.append(core_pool[i])
                    if i < len(new_pool):
                        self.full_skill_pool.append(new_pool[i])

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
                self.last_targeted_enemy_idx = enemy_idx
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
            self.skills_used_last_turn_types = list(self.skills_used_this_turn_types)
            self.skills_used_this_turn_types = []
            self.rolled_one_last_turn = self.rolled_one_this_turn
            self.rolled_one_this_turn = False

            # Kare Shuffle Logic: Revert last turn's shuffle
            if self.kare_shuffle_mode and self.shuffled_slot_idx != -1:
                self.player_skills[self.shuffled_slot_idx] = self.original_skill
                self.shuffled_slot_idx = -1

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
                enemy.collapsed = False
                if not enemy.is_dead:
                    enemy.slots = [None] * self.current_max_slots
                    num_enemy_slots = self.current_max_slots // 2
                    available_indices = list(range(self.current_max_slots))
                    renpy.random.shuffle(available_indices)

                    # Unique intents, respect cooldowns
                    available_intents = [i for i in enemy.intents if i.current_cooldown <= 0]

                    # Special filtering for RECIDIVISM
                    recidivism_intent = next((i for i in available_intents if i.type == "recidivism"), None)
                    if recidivism_intent and not self.rolled_one_last_turn:
                        available_intents = [i for i in available_intents if i.type != "recidivism"]

                    renpy.random.shuffle(available_intents)

                    # Ensure RECIDIVISM is prioritized if triggered
                    if recidivism_intent and self.rolled_one_last_turn:
                        if recidivism_intent in available_intents:
                            available_intents.remove(recidivism_intent)
                            available_intents.append(recidivism_intent) # Put at end to pop first

                    for _i in range(num_enemy_slots):
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
                self.player_buffs.append([type, value, duration])
            else:
                enemy = self.enemies[enemy_idx]
                # Replace existing buff of the same type
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
                        self.skills_unlocked_this_battle += 1
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
                Skill("interitus", cost=3, damage=0, energy_regen=2, desc="1-20 damage... probably", animation="chaos_normal_anim", card_image="card_chaos_normal", is_chaos_skill=True),
                Skill("Embrace", cost=5, damage=0, type="barrier", desc="1-50 Defense. who knows", cooldown=2, animation="chaos_block_anim", card_image="card_chaos_block", is_chaos_skill=True),
                Skill("Entropy", cost=0, energy_regen=12, type="energy",cooldown=3, desc="everything falls apart eventually. might as well use it", animation="chaos_energy_anim", card_image="card_chaos_energy", is_chaos_skill=True),
                Skill("Cataclysm", cost=7, damage=0,cooldown=3, desc="1-30 damage... maybe", animation="chaos_hard_anim", card_image="card_chaos_hard", is_chaos_skill=True),
                Skill("dissolutum", cost=6, type="dodge",cooldown=2, desc="Shift out of reality.", animation="chaos_dodge_anim", card_image="card_chaos_dodge", is_chaos_skill=True),
                Skill("playing rough", cost=6, damage=0,cooldown=3, type="buff", buff_type="damage", buff_duration=3, desc="1-50 Damage Buff. or 1. who knows.", animation="chaos_buff_anim", is_chaos_skill=True),
                Skill("??????", cost=25, damage=0,cooldown=4, desc="1-60 damage... ??? ?????", animation="chaos_ultimate_anim", card_image="card_chaos_ultimate", is_chaos_skill=True),

                Skill("Unravel", cost=4, type="unravel",cooldown=3, desc="Strips all buffs currently on the enemy.", animation="chaos_buff_anim", is_chaos_skill=True),
                Skill("Fracture", cost=5, type="fracture",cooldown=3, desc="Destroys enemy barrier completely, or deals 1-10 damage.", animation="chaos_normal_anim", is_chaos_skill=True),
                Skill("Corrode", cost=5, type="corrode",cooldown=2, desc="Reduced damage for enemy's next 2-3 attacks.", animation="chaos_normal_anim", is_chaos_skill=True),
                Skill("Inversion", cost=6, type="inversion",cooldown=3, desc="Flips enemy damage buff to a penalty.", animation="chaos_buff_anim", is_chaos_skill=True),
                Skill("Collapse", cost=8, type="collapse",cooldown=3, desc="Nullifies enemy's very next action.", animation="chaos_block_anim", is_chaos_skill=True),
                Skill("Leech", cost=6, type="leech",cooldown=3, desc="Steals a buff from the enemy and applies it to yourself.", animation="chaos_buff_anim", is_chaos_skill=True),
                Skill("Overload", cost=7, type="overload",cooldown=3, desc="Enemy takes damage equal to their current barrier, then removes it.", animation="chaos_hard_anim", is_chaos_skill=True)
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
                EnemyIntent("PRECEDENT", damage=3, desc="if enemy used a barrier or buff last turn, deals 8 damage. If she didn't, deals 3.", animation="serious_butter_normal_anim", type="precedent"),
                EnemyIntent("SENTENCE PASSED", damage=10, desc="deals 10 damage, and all of Chaos's barrier skills are forced on cooldown for 2 turns.", animation="serious_butter_block_anim", type="sentence_passed", cooldown=3),
                EnemyIntent("ENFORCEMENT", damage=4, buff_type="damage", buff_duration=3, desc="Increases damage by 4 for 3 turns.", animation="serious_butter_energy_anim", type="buff", cooldown=4),
                EnemyIntent("THE BILL", damage=0, desc="deals damage equal to the number of skills Chaos has used this battle.", animation="serious_butter_energy_anim", type="the_bill", cooldown=2),
                EnemyIntent("BINDING JUDGMENT", damage=10, desc="a strike that carries the full weight of every law ever written. it shows.", animation="serious_butter_hard_anim", type="attack", cooldown=0),
                EnemyIntent("RECIDIVISM", damage=0, desc="if enemy rolled a 1 last turn, deals 15 flat damage. resets after firing.", animation="serious_butter_hard_anim", type="recidivism"),
                EnemyIntent("DUE PROCESS", desc="Will dodge the next attack", animation="serious_butter_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("ACCUMULATED WEIGHT", damage=0, desc="deals damage equal to the total number of turns that have passed.", animation="serious_butter_ultimate_anim", type="accumulated_weight", cooldown=5),
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
                EnemyIntent("Overdrive", damage=8, buff_type="damage", buff_duration=3, desc="Increases damage by 8 for 3 turns.", animation="lumpi_wheelchair_energy_anim", type="buff", cooldown=4),
                EnemyIntent("Turbo Charge", damage=10, desc="High speed impact.", animation="lumpi_wheelchair_hard_anim", type="attack", cooldown=0),
                EnemyIntent("Drift", desc="Will dodge the next attack.", animation="lumpi_wheelchair_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("crashout", damage=25, desc="thats it im beating the shit out of you", animation="lumpi_wheelchair_ultimate_anim", type="attack", cooldown=6)
            ]
        elif name.lower() == "order":
            return [
                EnemyIntent("correction", damage=8, desc="precise and deliberate", animation="order_normal_anim", type="attack"),
                EnemyIntent("STRUCTURE", damage=10, desc="absolute foundation", animation="order_block_anim", type="barrier", cooldown=3),
                EnemyIntent("EQUILIBRIUM", damage=5, buff_type="damage", buff_duration=3, desc="restoring balance increases damage by 5 for 3 turns", animation="order_energy_anim", type="buff", cooldown=4),
                EnemyIntent("ABSOLUTE RULE", damage=15, desc="the weight of everything held in place. now released.", animation="order_hard_anim", type="attack", cooldown=0),
                EnemyIntent("INEVITABILITY", desc="order always finds a way around chaos", animation="order_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("FINAL ORDER", damage=30, desc="this ends now", animation="order_ultimate_anim", type="attack", cooldown=6)
            ]
        elif name.lower() == "ava":
            return [
                EnemyIntent("poke", damage=6, desc="poke", animation="ava_normal_anim", type="attack"),
                EnemyIntent("ETERNAL RECORD", damage=8, desc="as long as a single soul remembers civilization, I cannot fall. history does not die easily.", animation="ava_block_anim", type="barrier", cooldown=3),
                EnemyIntent("RALLY", damage=15, buff_type="damage", buff_duration=3, desc="Increases damage by 15 for 3 turns.", animation="ava_energy_anim", type="buff", cooldown=4),
                EnemyIntent("CULTURAL IMPACT", damage=15, desc="a strike so significant it will be remembered for generations. probably.", animation="ava_hard_anim", type="attack", cooldown=0),
                EnemyIntent("WRITTEN IN HISTORY", desc="Will dodge the next attack.", animation="ava_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("END OF AN ERA", damage=60, desc="every civilization must fall before a new one rises. unfortunately for you, you are the civilization right now", animation="ava_ultimate_anim", type="attack", cooldown=6)
            ]
        elif name.lower() == "ava2":
            return [
                EnemyIntent("THE ONES WHO BUILT IT", damage=10, desc="if Ava has no barrier, deals 20 damage. If she does have barrier, deals 10 instead.", animation="ava_normal_anim", type="ones_who_built_it"),
                EnemyIntent("MONUMENT", damage=0, desc="gains barrier equal to the number of turns that have passed.", animation="ava_block_anim", type="monument", cooldown=2),
                EnemyIntent("WE REMEMBER", damage=0, desc="heals Ava for damage equal to whatever the drain took from her last turn / 100.", animation="ava_energy_anim", type="we_remember", cooldown=3),
                EnemyIntent("LAST RECORD", damage=15, desc="if Ava's HP is below 50%, this deals double damage.", animation="ava_hard_anim", type="last_record"),
                EnemyIntent("FOUNDATION", damage=0, desc="strips all of Chaos's debuffs on Ava and gains 8 barrier per debuff.", animation="ava_buff_anim", type="foundation", cooldown=4),
                EnemyIntent("THOUSAND YEARS", damage=0, desc="deals 5 damage multiplied by the number of skills Chaos has unlocked this battle.", animation="ava_ultimate_anim", type="thousand_years", cooldown=5),
                EnemyIntent("STILL STANDING", damage=0, desc="if Ava is at 1 HP, survive and gain 15 barrier. Once per battle.", animation="ava_block_anim", type="still_standing", cooldown=0)
            ]
        return []

screen slot_machine(reel_items, label_text="", duration=2.0):
    frame:
        background Solid("#000000cc")
        xalign 0.5 yalign 0.3
        padding (40, 30)
        xsize 180
        ysize 140
        foreground "sketchy_bar_outline"
        vbox:
            spacing 6
            xalign 0.5
            yalign 0.5
            text "[label_text]" size 16 color "#aaa" xalign 0.5
            viewport:
                xsize 140
                ysize 60
                xalign 0.5
                vbox:
                    xalign 0.5
                    spacing 0
                    at reel_scroll_transform(duration, len(reel_items), 60)
                    for item in reel_items:
                        fixed:
                            xsize 140 ysize 60
                            text "[item]" size 40 color "#ffffff" bold True xalign 0.5 yalign 0.5

label chaos_slot_anim(final_value, label_text=""):
    python:
        symbols = "$#%^&*@!?~<>"
        reel_items = [str(final_value)]
        num_spins = 12
        for _i in range(num_spins):
            reel_items.append("".join([renpy.random.choice(symbols + "0123456789") for _idx in range(len(str(final_value)))]))

    show screen slot_machine(reel_items, label_text, duration=1.5)
    $ renpy.pause(1.5, hard=True)
    $ renpy.pause(0.5, hard=True)
    hide screen slot_machine
    return

screen chaos_number_indicator(label_text=""):
    frame:
        background Solid("#000000cc")
        xpos 0.35 xanchor 0.5 ypos 0.15 yanchor 0.5
        padding (20, 15)
        foreground "sketchy_bar_outline"
        vbox:
            spacing 5
            xalign 0.5
            yalign 0.5
            text "[label_text]" size 14 color "#aaa" xalign 0.5
            text "[store.chaos_anim_val]" size 36 color "#ffffff" bold True xalign 0.5

# ── The shuffle screen
screen card_shuffle_screen(bm, shuffling_indices, new_skills):
    # shuffling_indices = list of card positions being replaced (e.g. [2] for kare shuffle, [0,1,2,3,4] for full chaos)
    # new_skills = list of Skill objects landing in those slots
    $ is_chaos = getattr(bm, "is_chaos", False)
    $ _ink     = C_CHAOS_INK   if is_chaos else C_INK
    $ _paper   = C_CHAOS_PAPER if is_chaos else C_PAPER
    $ _ink_faint = C_CHAOS_INK_FAINT if is_chaos else C_INK_FAINT

    frame:
        yalign 1.0
        xfill True
        ysize 220
        background (_paper + "f7")
        xpadding 24
        ypadding 10
        top_padding 10

        vbox:
            spacing 8
            text "your cards":
                font "fonts/Caveat-Regular.ttf"
                size 13
                color _ink_faint

            hbox:
                spacing 12

                for idx, skill in enumerate(bm.player_skills):
                    $ is_spinning = idx in shuffling_indices
                    $ spin_delay  = shuffling_indices.index(idx) * 0.12 if is_spinning else 0.0

                    frame:
                        xsize 130
                        ysize 168
                        # Clip overflow so reel doesn't bleed outside card
                        background _paper
                        foreground Frame(
                            Composite((4,4),
                                (0,0), Solid(_ink, xsize=4, ysize=1),
                                (0,3), Solid(_ink, xsize=4, ysize=1),
                                (0,0), Solid(_ink, xsize=1, ysize=4),
                                (3,0), Solid(_ink, xsize=1, ysize=4),
                            ), 2,2,2,2
                        )

                        if is_spinning:
                            # Show a column of 3 ghost icons scrolling (gives reel illusion)
                            vbox:
                                xfill True
                                yalign 0.5
                                spacing 0
                                at card_reel_spin(delay=spin_delay)

                                # Ghost icons above (previous card icon)
                                frame:
                                    xfill True ysize 56
                                    background _paper
                                    text skill.icon:
                                        xalign 0.5 yalign 0.5
                                        size 30
                                        color (_ink + "44")

                                # Centre slot ─ shows ??? during spin
                                frame:
                                    xfill True ysize 56
                                    background (_paper + "ee")
                                    # border accent on centre slot
                                    foreground Frame(
                                        Composite((2,2),
                                            (0,0), Solid(_ink_faint, xsize=2, ysize=1),
                                            (0,1), Solid(_ink_faint, xsize=2, ysize=1),
                                        ), 1,1,1,1
                                    )
                                    text "?":
                                        xalign 0.5 yalign 0.5
                                        font "fonts/CaveatBrush-Regular.ttf"
                                        size 38
                                        color _ink

                                # Ghost icon below (new card peek)
                                frame:
                                    xfill True ysize 56
                                    background _paper
                                    $ new_skill = new_skills[shuffling_indices.index(idx)]
                                    text new_skill.icon:
                                        xalign 0.5 yalign 0.5
                                        size 30
                                        color (_ink + "44")

                            # ??? text at bottom
                            frame:
                                xfill True
                                background _paper
                                xpadding 6 ypadding 4
                                text "???":
                                    font "fonts/CaveatBrush-Regular.ttf"
                                    size 15
                                    color _ink_faint

                            # Landing flash
                            frame:
                                at card_land_flash(is_chaos)
                                xfill True yfill True
                                background "#ffffff"

                        else:
                            # Non-spinning cards ─ render normally
                            $ _tb = get_typebar(skill.type, is_chaos)
                            vbox:
                                xfill True
                                add _tb xsize 130
                                frame:
                                    xfill True ysize 76
                                    background _paper
                                    text skill.icon:
                                        xalign 0.5 yalign 0.5
                                        size 36
                                        color _ink
                                frame:
                                    xfill True ysize 1
                                    background _ink_faint
                                frame:
                                    xfill True background _paper
                                    xpadding 6 top_padding 4 bottom_padding 5
                                    vbox:
                                        spacing 2
                                        text skill.name:
                                            font "fonts/CaveatBrush-Regular.ttf"
                                            size 15 color _ink
                                        $ _val = (str(skill.damage) + " dmg") if skill.damage > 0 else skill.type
                                        text _val:
                                            font "fonts/Caveat-Regular.ttf"
                                            size 11 color (_ink + "88")

label kare_card_shuffle_anim(bm):
    # One card gets replaced with a random Chaos skill
    $ bm.is_shuffling = True

    # Pick which slot index to replace (not the slap slot at 0)
    $ non_slap = [i for i, s in enumerate(bm.player_skills) if s.name != "slap"]
    if not non_slap:
        $ replace_idx = renpy.random.choice(range(len(bm.player_skills)))
    else:
        $ replace_idx = renpy.random.choice(non_slap)
    $ new_chaos_skill = renpy.random.choice(bm.chaos_pool)

    # Show the shuffle screen
    show screen card_shuffle_screen(bm, [replace_idx], [new_chaos_skill])

    # Wait for the full reel animation to complete
    $ renpy.pause(replace_idx * 0.12 + 1.5, hard=True)

    # Swap the card in
    $ bm.player_skills[replace_idx] = new_chaos_skill

    hide screen card_shuffle_screen
    $ bm.is_shuffling = False
    return

label chaos_card_shuffle_anim(bm):
    # All cards spin ─ full Chaos mode activation
    $ bm.is_shuffling = True
    $ new_skills = [renpy.random.choice(bm.full_skill_pool) for _i in bm.player_skills]
    $ all_indices = list(range(len(bm.player_skills)))

    show screen card_shuffle_screen(bm, all_indices, new_skills)

    # Last card starts at delay = (len-1)*0.12, total = ~1.6s
    $ renpy.pause(len(bm.player_skills) * 0.12 + 1.5, hard=True)

    $ bm.player_skills = new_skills
    hide screen card_shuffle_screen
    $ bm.is_shuffling = False
    return

label chaos_number_anim(final_value, label_text=""):
    $ store.chaos_anim_len = max(2, len(str(final_value)))
    $ store.chaos_anim_val = "?" * store.chaos_anim_len
    show screen chaos_number_indicator(label_text)
    python:
        for i in range(25):
            if i < 22:
                store.chaos_anim_val = "".join([str(renpy.random.randint(0, 9)) for _i in range(store.chaos_anim_len)])
            else:
                store.chaos_anim_val = str(final_value).zfill(store.chaos_anim_len)
            renpy.restart_interaction()
            renpy.pause(0.04, hard=True)
    $ renpy.pause(0.4, hard=True)
    hide screen chaos_number_indicator
    return


# ── CHAOS HP glitch └ apply to HP text in chaos mode
transform chaos_hp_glitch:
    pause 4.5
    linear 0.04 xoffset -4 alpha 0.6
    linear 0.04 xoffset  3 alpha 1.0
    linear 0.03 xoffset -1
    linear 0.03 xoffset  0
    pause 0.1
    linear 0.02 xoffset -6 yoffset -1 alpha 0.4
    linear 0.02 xoffset  0 yoffset  0 alpha 1.0
    repeat

# ── CHAOS slot strip shake └ apply to the slot strip frame in chaos mode
transform chaos_slots_shake:
    pause 8.0
    linear 0.04 xoffset  1 yoffset -1
    linear 0.04 xoffset -1 yoffset  1
    linear 0.04 xoffset  1 yoffset  0
    linear 0.04 xoffset  0 yoffset  0
    repeat

# ── CHAOS general glitch └ apply to character name text in chaos mode
transform chaos_name_glitch:
    pause 7.0
    linear 0.05 xoffset -3
    linear 0.05 xoffset  3
    linear 0.05 xoffset -1
    linear 0.05 xoffset  0
    repeat

screen battle_screen(bm):
    $ is_chaos = getattr(bm, "is_chaos", False)
    $ _ink       = C_CHAOS_INK       if is_chaos else C_INK
    $ _ink_light = C_CHAOS_INK_LIGHT if is_chaos else C_INK_LIGHT
    $ _ink_faint = C_CHAOS_INK_FAINT if is_chaos else C_INK_FAINT
    $ _paper     = C_CHAOS_PAPER     if is_chaos else C_PAPER
    $ _paper_dark= C_CHAOS_PAPER_DARK if is_chaos else C_PAPER_DARK
    $ _paper_mid = C_CHAOS_PAPER_MID  if is_chaos else C_PAPER_MID

    # Chaos forces constant redraw so scramble_hp updates each frame
    if is_chaos:
        timer 0.05 repeat True action [renpy.restart_interaction]

    # ════════════════════
    # TOP BAR
    # ════════════════════
    frame:
        xfill True
        ysize 140
        ypos 0
        background (_paper + "f2")
        bottom_padding 0
        xpadding 24
        ypadding 12

        # Turn badge ─ centred
        frame:
            xalign 0.5 yalign 0.0
            yoffset 14
            background _paper_dark
            padding (14, 3)
            foreground Frame(
                Composite((4,4),
                    (0,0), Solid(_ink_faint, xsize=4, ysize=1),
                    (0,3), Solid(_ink_faint, xsize=4, ysize=1),
                    (0,0), Solid(_ink_faint, xsize=1, ysize=4),
                    (3,0), Solid(_ink_faint, xsize=1, ysize=4),
                ), 2,2,2,2
            )
            text ("Turn " + str(bm.turn_count) + " • " + str(bm.current_max_slots) + " slots"):
                font "fonts/Caveat-Regular.ttf"
                size 14
                color _ink_light

        hbox:
            xfill True

            # ── PLAYER STATS (left column)
            vbox:
                spacing 5
                xsize 460

                # Character name
                if is_chaos:
                    text bm.player_name:
                        font "fonts/CaveatBrush-Regular.ttf"
                        size 28
                        color _ink
                        at chaos_name_glitch
                else:
                    text bm.player_name:
                        font "fonts/CaveatBrush-Regular.ttf"
                        size 28
                        color _ink

                # HP row
                hbox:
                    spacing 10
                    yalign 0.5
                    text "HP":
                        font "fonts/Caveat-Regular.ttf"
                        size 15
                        color _ink_light
                        min_width 52
                        yalign 0.5
                    if is_chaos:
                        text (scramble_hp(bm.player_hp) + " / " + scramble_hp(bm.player_max_hp)):
                            font "fonts/Caveat-Regular.ttf"
                            size 18
                            color _ink
                            at chaos_hp_glitch
                    else:
                        bar value bm.player_hp range bm.player_max_hp:
                            xsize 210 ysize 14 yalign 0.5
                            left_bar  _ink
                            right_bar _paper_mid
                        text (str(bm.player_hp) + " / " + str(bm.player_max_hp)):
                            font "fonts/Caveat-Regular.ttf"
                            size 14
                            color _ink_light
                            yalign 0.5

                # Energy row
                hbox:
                    spacing 10
                    yalign 0.5
                    text "Energy":
                        font "fonts/Caveat-Regular.ttf"
                        size 15
                        color _ink_light
                        min_width 52
                        yalign 0.5
                    bar value bm.player_energy range bm.player_max_energy:
                        xsize 210 ysize 14 yalign 0.5
                        left_bar  _ink
                        right_bar _paper_mid
                    text (str(bm.player_energy) + " / " + str(bm.player_max_energy)):
                        font "fonts/Caveat-Regular.ttf"
                        size 14
                        color _ink_light
                        yalign 0.5

                # Status chips row
                hbox:
                    spacing 6
                    yoffset 2
                    if bm.player_barrier > 0:
                        frame:
                            background _paper_mid
                            padding (7, 2)
                            foreground Frame(
                                Composite((4,4),
                                    (0,0), Solid(_ink_faint, xsize=4, ysize=1),
                                    (0,3), Solid(_ink_faint, xsize=4, ysize=1),
                                    (0,0), Solid(_ink_faint, xsize=1, ysize=4),
                                    (3,0), Solid(_ink_faint, xsize=1, ysize=4),
                                ), 2,2,2,2
                            )
                            text ("DEF " + str(bm.player_barrier)):
                                font "fonts/Caveat-Regular.ttf"
                                size 13
                                color _ink
                    for buff in bm.player_buffs:
                        frame:
                            background _paper_mid
                            padding (7, 2)
                            text (str(buff[0]) + " +" + str(buff[1]) + " (" + str(buff[2]) + "t)"):
                                font "fonts/Caveat-Regular.ttf"
                                size 12
                                color _ink_light

            # ── CENTRE spacer
            null width 0
            xfill True

            # ── ENEMY STATS (right column, one block per enemy)
            vbox:
                spacing 8
                xalign 1.0

                for enemy in bm.enemies:
                    if not enemy.is_dead:
                        vbox:
                            spacing 4
                            xalign 1.0

                            # Enemy name
                            text enemy.name:
                                font "fonts/CaveatBrush-Regular.ttf"
                                size 24
                                color _ink
                                xalign 1.0

                            # HP row (right-aligned, bar flipped)
                            hbox:
                                xalign 1.0
                                spacing 10
                                yalign 0.5
                                text (str(enemy.hp) + " / " + str(enemy.max_hp)):
                                    font "fonts/Caveat-Regular.ttf"
                                    size 14
                                    color _ink_light
                                    yalign 0.5
                                # Low HP shows hatch pattern instead of solid
                                if enemy.hp < enemy.max_hp * 0.3:
                                    frame:
                                        xsize 150 ysize 14 yalign 0.5
                                        background _paper_mid
                                        foreground Frame(
                                            Composite((4,4),
                                                (0,0), Solid(_ink, xsize=4, ysize=1),
                                                (0,3), Solid(_ink, xsize=4, ysize=1),
                                                (0,0), Solid(_ink, xsize=1, ysize=4),
                                                (3,0), Solid(_ink, xsize=1, ysize=4),
                                            ), 2,2,2,2
                                        )
                                        # Hatch fill for low HP
                                        add Tile(
                                            Composite((6,6),
                                                (0,0), Solid(_ink,  xsize=3, ysize=3),
                                                (3,3), Solid(_ink,  xsize=3, ysize=3),
                                                (3,0), Solid(_paper,xsize=3, ysize=3),
                                                (0,3), Solid(_paper,xsize=3, ysize=3),
                                            ),
                                            xsize=int(150 * enemy.hp // enemy.max_hp),
                                            ysize=14
                                        )
                                else:
                                    bar value enemy.hp range enemy.max_hp:
                                        xsize 150 ysize 14 yalign 0.5
                                        left_bar  _ink
                                        right_bar _paper_mid
                                text "HP":
                                    font "fonts/Caveat-Regular.ttf"
                                    size 15
                                    color _ink_light
                                    yalign 0.5

                            # Skill unlock exp bar
                            hbox:
                                xalign 1.0
                                spacing 8
                                text "skill unlock":
                                    font "fonts/Caveat-Regular.ttf"
                                    size 12
                                    color _ink_faint
                                    yalign 0.5
                                bar value enemy.skill_exp range enemy.skill_exp_max:
                                    xsize 120 ysize 7 yalign 0.5
                                    left_bar  _ink
                                    right_bar _paper_mid

                            # Enemy status chips
                            hbox:
                                xalign 1.0
                                spacing 5
                                for buff in enemy.buffs:
                                    frame:
                                        background _paper_mid
                                        padding (5, 2)
                                        text (str(buff[0]) + " +" + str(buff[1])):
                                            font "fonts/Caveat-Regular.ttf"
                                            size 11
                                            color _ink_light
                                if enemy.barrier > 0:
                                    frame:
                                        background _paper_mid
                                        padding (7, 2)
                                        text ("DEF " + str(enemy.barrier)):
                                            font "fonts/Caveat-Regular.ttf"
                                            size 13
                                            color _ink

                            # Divider between multiple enemies
                            if len([e for e in bm.enemies if not e.is_dead]) > 1:
                                frame:
                                    xsize 320 ysize 1
                                    xalign 1.0
                                    background _ink_faint


    # ════════════════════
    # SLOT STRIP  (sits above the card section)
    # Wrapped in a container so CONFIRM spans all enemy rows
    # ════════════════════
    frame:
        yalign 1.0
        yoffset -(220)          # 220 = height of cards section
        xfill True
        $ _num_alive = len([e for e in bm.enemies if not e.is_dead])
        $ _slot_strip_h = _num_alive * 78 + 16
        ysize _slot_strip_h
        background (_paper + "e8")
        top_padding 0

        if is_chaos:
            at chaos_slots_shake

        hbox:
            xfill True yfill True
            xpadding 24

            # Enemy row column
            vbox:
                xfill True yfill True
                spacing 0

                for e_idx, enemy in enumerate(bm.enemies):
                    if not enemy.is_dead:

                        hbox:
                            xfill True
                            ysize 78
                            spacing 10

                            # Row label
                            text (enemy.name.split()[0] + "'s
row"):
                                font "fonts/Caveat-Regular.ttf"
                                size 12
                                color _ink_faint
                                xsize 68
                                yalign 0.5

                            # Slot divider line between rows
                            if e_idx > 0:
                                frame:
                                    xfill True ysize 1
                                    ypos 0
                                    background _ink_faint

                            # Slots
                            for s_idx in range(bm.current_max_slots):
                                $ action = enemy.slots[s_idx]

                                frame:
                                    xsize 0
                                    xmaximum 220
                                    xminimum 80
                                    ysize 62
                                    yalign 0.5

                                    # Empty slot
                                    if action is None:
                                        background _paper
                                        foreground Frame(
                                            Composite((4,4),
                                                (0,0), Solid(_ink_faint, xsize=4, ysize=1),
                                                (0,3), Solid(_ink_faint, xsize=4, ysize=1),
                                                (0,0), Solid(_ink_faint, xsize=1, ysize=4),
                                                (3,0), Solid(_ink_faint, xsize=1, ysize=4),
                                            ), 2,2,2,2
                                        )
                                        if bm.selected_skill is not None:
                                            imagebutton:
                                                xfill True yfill True
                                                idle  Solid("#00000000")
                                                hover Solid(_ink + "18")
                                                action Function(bm.add_to_slot, bm.selected_skill, e_idx, s_idx)
                                        text "— open —":
                                            font "fonts/Caveat-Regular.ttf"
                                            size 12
                                            color _ink_faint
                                            xalign 0.5 yalign 0.5

                                    # Enemy intent slot
                                    elif isinstance(action, EnemyIntent):
                                        background ("slot_enemy_hatch_chaos" if is_chaos else "slot_enemy_hatch")
                                        foreground Frame(
                                            Composite((4,4),
                                                (0,0), Solid(_ink, xsize=4, ysize=1),
                                                (0,3), Solid(_ink, xsize=4, ysize=1),
                                                (0,0), Solid(_ink, xsize=1, ysize=4),
                                                (3,0), Solid(_ink, xsize=1, ysize=4),
                                            ), 2,2,2,2
                                        )
                                        vbox:
                                            xalign 0.5 yalign 0.5
                                            spacing 1
                                            text "ENEMY":
                                                font "fonts/Caveat-Regular.ttf"
                                                size 10
                                                color _ink_light
                                                xalign 0.5
                                            text action.name:
                                                font "fonts/CaveatBrush-Regular.ttf"
                                                size 15
                                                color _ink
                                                xalign 0.5
                                        if action.damage > 0:
                                            text str(action.damage):
                                                font "fonts/Caveat-Regular.ttf"
                                                size 11
                                                color _ink_light
                                                xalign 0.98 yalign 0.92

                                    # Player skill in slot
                                    elif isinstance(action, Skill):
                                        background _paper_dark
                                        foreground Frame(
                                            Composite((4,4),
                                                (0,0), Solid(_ink, xsize=4, ysize=1),
                                                (0,3), Solid(_ink, xsize=4, ysize=1),
                                                (0,0), Solid(_ink, xsize=1, ysize=4),
                                                (3,0), Solid(_ink, xsize=1, ysize=4),
                                            ), 2,2,2,2
                                        )
                                        imagebutton:
                                            xfill True yfill True
                                            idle  Solid("#00000000")
                                            action Function(bm.select_skill, action)
                                        vbox:
                                            xalign 0.5 yalign 0.5
                                            spacing 1
                                            text "YOU":
                                                font "fonts/Caveat-Regular.ttf"
                                                size 10
                                                color _ink
                                                xalign 0.5
                                            text action.name:
                                                font "fonts/CaveatBrush-Regular.ttf"
                                                size 15
                                                color _ink
                                                xalign 0.5

            # CONFIRM button ─ right side, spans all rows
            vbox:
                yalign 0.5
                xpadding 10
                textbutton "CONFIRM":
                    yalign 0.5
                    xsize 140
                    ysize 52
                    background _ink
                    hover_background (_paper_mid if is_chaos else C_INK_MID)
                    action Return("execute")
                    text_font "fonts/CaveatBrush-Regular.ttf"
                    text_size 20
                    text_color _paper
                    text_xalign 0.5


    # ════════════════════
    # INTENT PREVIEW BAR (above slot strip)
    # ════════════════════
    $ _target_idx = getattr(bm, "last_targeted_enemy_idx", -1)
    $ _live = [e for e in bm.enemies if not e.is_dead]
    if _target_idx == -1 or bm.enemies[_target_idx].is_dead:
        if _live:
            $ _preview_enemy = _live[0]
        else:
            $ _preview_enemy = None
    else:
        $ _preview_enemy = bm.enemies[_target_idx]

    if _preview_enemy:
        $ _e_intents = [s for s in _preview_enemy.slots if isinstance(s, EnemyIntent)]
        if _e_intents:
            $ _intent_preview = _e_intents[0]
            frame:
                xpos 24
                xsize 700
                yalign 1.0
                $ _intent_offset = 220 + len(_live) * 78 + 16 + 8
                yoffset (-_intent_offset)
                background (_paper + "df")
                left_padding 4
                right_padding 12
                ypadding 7
                foreground Frame(
                    Composite((4,4),
                        (0,0), Solid(_ink, xsize=4, ysize=4),
                        (0,0), Solid(_ink_faint, xsize=4, ysize=1),
                        (0,3), Solid(_ink_faint, xsize=4, ysize=1),
                    ), 2,2,2,2
                )
                # Thick left border accent
                frame:
                    xsize 4 yfill True
                    xpos 0
                    background _ink
                hbox:
                    spacing 10
                    xpadding 10
                    text (_preview_enemy.name + ": " + _intent_preview.name):
                        style "battle_intent_title"
                        color _ink
                        yalign 0.5
                    text _intent_preview.desc:
                        style "battle_intent_desc"
                        color _ink_light
                        yalign 0.5


    # ════════════════════
    # CARDS SECTION (pinned to bottom)
    # ════════════════════
    frame:
        yalign 1.0
        xfill True
        ysize 220
        background (_paper + "f7")
        xpadding 24
        ypadding 10
        top_padding 10

        vbox:
            spacing 8

            # Header row
            hbox:
                xfill True
                text "your cards":
                    font "fonts/Caveat-Regular.ttf"
                    size 13
                    color _ink_faint
                hbox:
                    xalign 1.0
                    spacing 8
                    text "next skill:":
                        font "fonts/Caveat-Regular.ttf"
                        size 12
                        color _ink_faint
                        yalign 0.5
                    bar value bm.skill_exp range bm.skill_exp_max:
                        xsize 260 ysize 7 yalign 0.5
                        left_bar  _ink
                        right_bar _paper_mid

            # Card row
            hbox:
                spacing 12

                if not getattr(bm, "is_shuffling", False):
                    for skill in bm.player_skills:
                        $ _on_cd  = skill.current_cooldown > 0 or skill in bm.used_skills_this_turn
                        $ _sel    = bm.selected_skill == skill
                        $ _tb     = get_typebar(skill.type, is_chaos)

                        frame:
                            xsize 130
                            ysize 168
                            yoffset (-14 if _sel else 0)
                            background _paper

                            # Card border
                            foreground Frame(
                                Composite((4,4),
                                    (0,0), Solid(_ink, xsize=4, ysize=1),
                                    (0,3), Solid(_ink, xsize=4, ysize=1),
                                    (0,0), Solid(_ink, xsize=1, ysize=4),
                                    (3,0), Solid(_ink, xsize=1, ysize=4),
                                ), 2,2,2,2
                            )

                            vbox:
                                xfill True

                                # Type bar
                                add _tb xsize 130

                                # Icon area
                                frame:
                                    xfill True
                                    ysize 76
                                    background _paper
                                    text skill.icon:
                                        xalign 0.5 yalign 0.5
                                        size 36
                                        color _ink

                                # Divider
                                frame:
                                    xfill True ysize 1
                                    background _ink_faint

                                # Name + stats
                                frame:
                                    xfill True
                                    background _paper
                                    xpadding 6
                                    top_padding 4
                                    bottom_padding 5
                                    vbox:
                                        spacing 2
                                        text skill.name:
                                            font "fonts/CaveatBrush-Regular.ttf"
                                            size 15
                                            color _ink
                                        hbox:
                                            xfill True
                                            $ _val = (str(skill.damage) + " dmg") if skill.damage > 0 else skill.type
                                            text _val:
                                                font "fonts/Caveat-Regular.ttf"
                                                size 11
                                                color _ink_light
                                            if skill.cooldown > 0:
                                                text ("cd:" + str(skill.cooldown)):
                                                    font "fonts/Caveat-Regular.ttf"
                                                    size 11
                                                    color _ink_light
                                                    xalign 1.0

                            # Cost bubble (top-right corner)
                            frame:
                                xalign 1.0 yalign 0.0
                                xoffset -5 yoffset 9
                                xsize 22 ysize 22
                                background _ink
                                text str(skill.cost):
                                    xalign 0.5 yalign 0.5
                                    font "fonts/Caveat-Regular.ttf"
                                    size 12
                                    color _paper

                            # Selected highlight overlay
                            if _sel:
                                frame:
                                    xfill True yfill True
                                    background Solid(_ink + "18")

                            # Cooldown overlay
                            if _on_cd:
                                frame:
                                    xfill True yfill True
                                    background Solid(_paper + "bb")
                                    if skill.current_cooldown > 0:
                                        text str(skill.current_cooldown):
                                            xalign 0.5 yalign 0.5
                                            font "fonts/CaveatBrush-Regular.ttf"
                                            size 46
                                            color _ink_faint
                                    else:
                                        text "USED":
                                            xalign 0.5 yalign 0.5
                                            font "fonts/CaveatBrush-Regular.ttf"
                                            size 24
                                            color _ink_faint

                            # Click area (rendered last so it sits on top)
                            if not _on_cd:
                                imagebutton:
                                    xfill True yfill True
                                    idle  Solid("#00000000")
                                    hover Solid(_ink + "0e")
                                    action Function(bm.select_skill, skill)


    # ════════════════════
    # SKILL POPUP (shows when a card is selected)
    # ════════════════════
    if bm.selected_skill:
        $ s = bm.selected_skill
        frame:
            xpos 24
            yalign 1.0
            yoffset -(220 + (_num_alive if hasattr(bm,'enemies') else 1) * 78 + 60)
            xsize 200
            background _paper_dark
            padding (14, 14)
            foreground Frame(
                Composite((4,4),
                    (0,0), Solid(_ink, xsize=4, ysize=1),
                    (0,3), Solid(_ink, xsize=4, ysize=1),
                    (0,0), Solid(_ink, xsize=1, ysize=4),
                    (3,0), Solid(_ink, xsize=1, ysize=4),
                ), 2,2,2,2
            )
            vbox:
                spacing 4
                text s.name:
                    font "fonts/CaveatBrush-Regular.ttf"
                    size 19
                    color _ink
                text ("Cost: " + str(s.cost) + " Energy"):
                    font "fonts/Caveat-Regular.ttf"
                    size 14
                    color _ink_light
                if s.damage > 0:
                    text ("Damage: " + str(s.damage)):
                        font "fonts/Caveat-Regular.ttf"
                        size 14
                        color _ink_light
                if s.cooldown > 0:
                    text ("Cooldown: " + str(s.cooldown) + " turns"):
                        font "fonts/Caveat-Regular.ttf"
                        size 14
                        color _ink_light
                frame:
                    xfill True ysize 1
                    yoffset 4
                    background _ink_faint
                text s.desc:
                    font "fonts/PatrickHand-Regular.ttf"
                    size 12
                    color _ink_light
                    italic True
                    top_margin 6

                # Remove from slot button
                if s in bm.used_skills_this_turn:
                    $ _ei, _si = bm.get_skill_slot_info(s)
                    if _ei != -1:
                        textbutton "REMOVE FROM SLOT":
                            action Function(bm.remove_from_slot, _ei, _si)
                            xsize 172
                            background _paper_mid
                            hover_background _ink_faint
                            top_margin 8
                            text_font "fonts/CaveatBrush-Regular.ttf"
                            text_size 14
                            text_color _ink
                            text_xalign 0.5


    # ════════════════════
    # CHAOS ??? NUMBER BOX
    # (shows during chaos skill resolution)
    # ════════════════════
    if is_chaos and hasattr(store, "chaos_anim_val"):
        frame:
            xalign 0.35 yalign 0.35
            background C_CHAOS_PAPER
            padding (22, 10)
            foreground Frame(
                Composite((4,4),
                    (0,0), Solid(C_CHAOS_INK, xsize=4, ysize=1),
                    (0,3), Solid(C_CHAOS_INK, xsize=4, ysize=1),
                    (0,0), Solid(C_CHAOS_INK, xsize=1, ysize=4),
                    (3,0), Solid(C_CHAOS_INK, xsize=1, ysize=4),
                ), 2,2,2,2
            )
            at chaos_name_glitch
            vbox:
                spacing 3
                text "DAMAGE":
                    font "fonts/Caveat-Regular.ttf"
                    size 13
                    color C_CHAOS_INK_LIGHT
                    xalign 0.5
                text str(store.chaos_anim_val):
                    font "fonts/CaveatBrush-Regular.ttf"
                    size 50
                    color C_CHAOS_INK
                    xalign 0.5


    # ════════════════════
    # ENERGY WARNING
    # ════════════════════
    if bm.show_energy_warning:
        timer 2.0 action SetField(bm, "show_energy_warning", False)
        frame:
            background Solid("#ff0000cc")
            padding (25, 12)
            xalign 0.5 yalign 0.4
            text "NOT ENOUGH ENERGY":
                color "#ffffff"
                size 36
                bold True

    # Settings button
    textbutton "Settings":
        xpos 10 ypos 10
        action ShowMenu("preferences")
        text_size 12
        text_font "fonts/Caveat-Regular.ttf"
        text_color _ink_faint

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

        $ e_count = sum(1 for e in bm.enemies if not e.is_dead)
        if e_count > 1:
            show expression bm.player_sprites["idle"] as player at fight_left_multi
        else:
            show expression bm.player_sprites["idle"] as player at fight_left

        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    if e_count > 1:
                        if i == 0:
                            pos = Position(xpos=0.62, ypos=0.8, yanchor=1.0)
                        else:
                            pos = Position(xpos=0.80, ypos=0.8, yanchor=1.0)
                    else:
                        pos = fight_right
                    renpy.show(enemy.sprites["idle"], at_list=[pos], tag=tag)
                else:
                    renpy.hide("enemy_" + str(i))

        show screen battle_screen(bm)
        if getattr(bm, "is_chaos", False):
            call chaos_card_shuffle_anim(bm) from _call_chaos_card_shuffle_eng
        elif getattr(bm, "kare_shuffle_mode", False):
            call kare_card_shuffle_anim(bm) from _call_kare_card_shuffle_eng

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
            $ bm.total_skills_used_this_battle += 1
            $ bm.skills_used_this_turn_types.append(skill.type)
            $ skill.current_cooldown = skill.cooldown
            if (not getattr(bm, "is_chaos", False) and not getattr(skill, "is_chaos_skill", False)) or skill.type not in ["energy", "unravel", "fracture", "corrode", "inversion", "collapse", "leech", "overload"]:
                $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)

            # Chaos number animation triggers BEFORE skill animation
            if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                $ skill_value = get_chaos_random_value(bm, skill)
                $ store.locked_skill_value = skill_value
                if skill.type == "attack":
                    call chaos_number_anim(store.locked_skill_value, "DAMAGE") from _call_chaos_slot_attack_eng
                elif skill.type == "barrier":
                    call chaos_number_anim(store.locked_skill_value, "DEFENSE") from _call_chaos_slot_barrier_eng
                elif skill.type == "buff":
                    call chaos_number_anim(store.locked_skill_value, "BUFF POWER") from _call_chaos_slot_buff_eng
                elif skill.type == "energy":
                    call chaos_number_anim(store.locked_skill_value, "ENERGY REGEN") from _call_chaos_slot_energy_eng
                elif skill.type == "fracture":
                    if enemy.barrier > 0:
                        $ store.locked_skill_value = 0
                    call chaos_number_anim(store.locked_skill_value, "DAMAGE") from _call_chaos_slot_fracture_eng
                elif skill.type == "corrode":
                    call chaos_number_anim(store.locked_skill_value, "CORROSION") from _call_chaos_slot_corrode_eng

            if skill.type == "attack":
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    $ actual_damage = store.locked_skill_value
                else:
                    $ actual_damage = get_chaos_random_value(bm, skill)
                if actual_damage == 1:
                    $ bm.rolled_one_this_turn = True

                if enemy.dodge_active:
                    $ bm.is_dodged = True
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_at_dodge_eng
                    $ dodge_anim = get_dodge_anim(enemy.name)
                    call expression dodge_anim pass (bm) from _call_enemy_dodge_anim_reactive_eng
                    $ enemy.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_generic_eng
                    $ bm.take_damage(actual_damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(actual_damage * 5, character_type="player")
                    "[skill.name] deals [actual_damage] damage to [enemy.name]"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_barrier_eng
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    $ actual_barrier = store.locked_skill_value
                else:
                    $ actual_barrier = get_chaos_random_value(bm, skill)
                if actual_barrier == 1:
                    $ bm.rolled_one_this_turn = True
                $ bm.add_barrier(actual_barrier)
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    "You gain [actual_barrier] Defense"
                else:
                    "You gain [skill.damage] Defense"
            elif skill.type == "dodge":
                $ bm.is_dodged = False
                $ bm.dodge_active = True
                $ bm.dodge_expires_at_slot = current_slot_idx + 1
            elif skill.type == "buff":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_buff_eng
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    $ actual_buff = store.locked_skill_value
                else:
                    $ actual_buff = get_chaos_random_value(bm, skill)
                if actual_buff == 1:
                    $ bm.rolled_one_this_turn = True
                $ bm.add_buff(skill.buff_type, actual_buff, skill.buff_duration, target="player")
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    "[skill.name] Damage increased by [actual_buff] for [skill.buff_duration] turns."
                else:
                    "[skill.name] Damage increased by [skill.damage] for [skill.buff_duration] turns."
            elif skill.type == "energy":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_energy_eng
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    if store.locked_skill_value == 1:
                        $ bm.rolled_one_this_turn = True
                    $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + store.locked_skill_value)
                    "You gained [store.locked_skill_value] Energy"
                else:
                    "You gained [skill.energy_regen] Energy"
            elif skill.type == "unravel":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_unravel_anim_eng
                $ enemy.buffs = []
                "You stripped [enemy.name] of all buffs!"
            elif skill.type == "fracture":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_fracture_anim_eng
                if enemy.barrier > 0:
                    $ enemy.barrier = 0
                    "You completely destroyed [enemy.name]'s barrier!"
                else:
                    $ bm.take_damage(store.locked_skill_value, target="enemy", enemy_idx=e_idx)
                    "You dealt [store.locked_skill_value] damage to [enemy.name]!"
            elif skill.type == "corrode":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_corrode_anim_eng
                $ bm.add_buff("corrosion", 5, store.locked_skill_value, target="enemy", enemy_idx=e_idx)
                "You applied corrosion to [enemy.name] for [store.locked_skill_value] turns!"
            elif skill.type == "inversion":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_inversion_anim_eng
                python:
                    for b in enemy.buffs:
                        if b[0] == "damage":
                            b[1] = -b[1]
                            renpy.say(None, "You flipped [enemy.name]'s damage buff into a penalty!")
                            break
                    else:
                        renpy.say(None, "Inversion failed: [enemy.name] has no damage buff.")
            elif skill.type == "collapse":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_collapse_anim_eng
                $ enemy.collapsed = True
                "You collapsed [enemy.name]'s reality! Their next action is nullified."
            elif skill.type == "leech":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_leech_anim_eng
                if enemy.buffs:
                    $ stolen = enemy.buffs.pop(0)
                    $ bm.add_buff(stolen[0], stolen[1], stolen[2], target="player")
                    "You stole [enemy.name]'s [stolen[0]] buff!"
                else:
                    "Leech failed: [enemy.name] has no buffs."
            elif skill.type == "overload":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_overload_anim_eng
                if enemy.barrier > 0:
                    $ dmg = enemy.barrier
                    $ enemy.barrier = 0
                    $ bm.take_damage(dmg, target="enemy", enemy_idx=e_idx)
                    "Overload! [enemy.name] took [dmg] damage from their own barrier!"
                else:
                    "Overload failed: [enemy.name] has no barrier."
        elif isinstance(action, EnemyIntent):
            $ intent = action
            $ intent.current_cooldown = intent.cooldown
            $ bm.enemy_intent = intent

            if enemy.collapsed:
                $ enemy.collapsed = False
                "[enemy.name]'s action was nullified by Collapse!"
                $ e_idx += 1
                jump .engine_resolution_core

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
                    $ damage = max(0, intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
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
            elif intent.type == "precedent":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_generic_precedent
                $ triggered = False
                python:
                    for t in bm.skills_used_last_turn_types:
                        if t in ["barrier", "buff"]:
                            triggered = True
                            break
                $ damage = 8 if triggered else 3
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "[enemy.name] deals [damage] damage with PRECEDENT!"
            elif intent.type == "sentence_passed":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_generic_sentence
                $ damage = max(0, intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                python:
                    for s in bm.player_skills:
                        if s.type == "barrier":
                            s.current_cooldown = max(s.current_cooldown, 2)
                "[enemy.name] deals [damage] damage and forces your barrier skills on cooldown for 2 turns!"
            elif intent.type == "the_bill":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_generic_bill
                $ damage = bm.total_skills_used_this_battle
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "[enemy.name] deals [damage] damage with THE BILL!"
            elif intent.type == "recidivism":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_generic_recidivism
                $ damage = 15
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                $ bm.rolled_one_last_turn = False
                "[enemy.name] deals [damage] flat damage with RECIDIVISM!"
            elif intent.type == "accumulated_weight":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_generic_accumulated
                $ damage = bm.turn_count
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "[enemy.name] deals [damage] damage with ACCUMULATED WEIGHT!"
        if all(e.is_dead for e in bm.enemies):
            window hide
            jump .engine_victory
        if bm.player_hp <= 0:
            window hide
            jump .engine_defeat

        window hide
        $ renpy.pause(0.5, hard=True)
        $ e_count = sum(1 for e in bm.enemies if not e.is_dead)
        if e_count > 1:
            show expression bm.player_sprites["idle"] as player at fight_left_multi
        else:
            show expression bm.player_sprites["idle"] as player at fight_left

        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    if e_count > 1:
                        if i == 0:
                            pos = Position(xpos=0.62, ypos=0.8, yanchor=1.0)
                        else:
                            pos = Position(xpos=0.80, ypos=0.8, yanchor=1.0)
                    else:
                        pos = fight_right
                    renpy.show(enemy.sprites["idle"], at_list=[pos], tag=tag)

        $ e_idx += 1
        jump .engine_resolution_core

    label .engine_turn_end:
        $ bm.reduce_cooldowns()
        $ bm.update_buffs()

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
    $ renpy.pause(0.15, hard=True)
    show chaos_projectile_normal at chaos_projectile_fly
    play sound "audio/magic-spark.mp3"
    $ renpy.pause(0.25, hard=True)
    hide chaos_projectile_normal
    if not bm.is_dodged:
        $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
        play sound "audio/punch-140236.mp3"
    $ renpy.pause(0.4, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    if not bm.enemies[e_idx].is_dead:
        $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label chaos_hard_anim(bm):
    show expression "chaos_hard_sprite" as player at fight_left
    $ renpy.pause(0.5, hard=True)
    show chaos_projectile_hard at chaos_projectile_fly_hard
    play sound "audio/magic-spark.mp3"
    $ renpy.pause(0.2, hard=True)
    hide chaos_projectile_hard
    if not bm.is_dodged:
        $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
        play sound "audio/punch-140236.mp3"
        camera:
            ease 0.1 zoom 1.15
            ease 0.15 zoom 1.0
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    if not bm.enemies[e_idx].is_dead:
        $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label chaos_block_anim(bm):
    show expression "chaos_block_sprite" as player at fight_left
    play sound "audio/Berserk Clang Sound Effect.mp3"
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
    $ renpy.pause(0.3, hard=True)
    show chaos_projectile_ultimate_1 at chaos_projectile_fly
    play sound "audio/magic-spark.mp3"
    $ renpy.pause(0.15, hard=True)
    hide chaos_projectile_ultimate_1
    show chaos_projectile_ultimate_2 at chaos_projectile_fly_2
    play sound "audio/magic-spark.mp3"
    $ renpy.pause(0.15, hard=True)
    hide chaos_projectile_ultimate_2
    show chaos_projectile_ultimate_3 at chaos_projectile_fly_3
    play sound "audio/magic-spark.mp3"
    $ renpy.pause(0.15, hard=True)
    hide chaos_projectile_ultimate_3
    if not bm.is_dodged:
        $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
        play sound "audio/magic-spark.mp3"
        camera:
            ease 0.1 zoom 1.2
            ease 0.1 zoom 1.1
            ease 0.1 zoom 1.0
    $ renpy.pause(0.6, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    if not bm.enemies[e_idx].is_dead:
        $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label chaos_energy_anim(bm):
    show expression "chaos_energy_sprite" as player at fight_left
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return# --- BUTTER ANIMATIONS ---
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
    $ butter.unlocked_intents_count = 11
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 4, "cost": 1},
        "punch":            {"damage": 8, "cost": 3,"cooldown": 3},
        "super cool kick":  {"damage": 20, "cost": 5, "cooldown": 4},
        "Defense":          {"damage": 8, "cost": 2, "cooldown": 2},
        "Focus":            {"damage": 5, "cost": 3, "buff_duration": 3, "cooldown": 3},
        "yummers":          {"energy_regen": 5, "cooldown": 2},
        "evade":            {"cost": 3, "cost": 2, "cooldown": 2},
    }
    $ bm = BattleManager(200, [butter], starting_slots=2, player_sprites=player_sprites, starting_energy=25, max_energy=25, skill_overrides=skill_overrides, kare_shuffle_mode=True)
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
    $ butter.unlocked_intents_count = 11
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
        if getattr(bm, "is_chaos", False):
            call chaos_card_shuffle_anim(bm) from _call_chaos_card_shuffle_boss1
        elif getattr(bm, "kare_shuffle_mode", False):
            call kare_card_shuffle_anim(bm) from _call_kare_card_shuffle_boss1
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
            $ bm.total_skills_used_this_battle += 1
            $ bm.skills_used_this_turn_types.append(skill.type)
            $ skill.current_cooldown = skill.cooldown
            if (not getattr(bm, "is_chaos", False) and not getattr(skill, "is_chaos_skill", False)) or skill.type not in ["energy", "unravel", "fracture", "corrode", "inversion", "collapse", "leech", "overload"]:
                $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)

            # Chaos number animation triggers BEFORE skill animation
            if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                $ skill_value = get_chaos_random_value(bm, skill)
                $ store.locked_skill_value = skill_value
                if skill.type == "attack":
                    call chaos_number_anim(store.locked_skill_value, "DAMAGE") from _call_chaos_slot_attack_boss1
                elif skill.type == "barrier":
                    call chaos_number_anim(store.locked_skill_value, "DEFENSE") from _call_chaos_slot_barrier_boss1
                elif skill.type == "buff":
                    call chaos_number_anim(store.locked_skill_value, "BUFF POWER") from _call_chaos_slot_buff_boss1
                elif skill.type == "energy":
                    call chaos_number_anim(store.locked_skill_value, "ENERGY REGEN") from _call_chaos_slot_energy_boss1
                elif skill.type == "fracture":
                    if enemy.barrier > 0:
                        $ store.locked_skill_value = 0
                    call chaos_number_anim(store.locked_skill_value, "DAMAGE") from _call_chaos_slot_fracture_boss1
                elif skill.type == "corrode":
                    call chaos_number_anim(store.locked_skill_value, "CORROSION") from _call_chaos_slot_corrode_boss1

            if skill.type == "attack":
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    $ actual_damage = store.locked_skill_value
                else:
                    $ actual_damage = get_chaos_random_value(bm, skill)
                if actual_damage == 1:
                    $ bm.rolled_one_this_turn = True

                if enemy.dodge_active:
                    $ bm.is_dodged = True
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_at_dodge_boss1
                    $ dodge_anim = get_dodge_anim(enemy.name)
                    call expression dodge_anim pass (bm) from _call_enemy_dodge_anim_reactive_boss1
                    $ enemy.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_generic_boss1
                    $ bm.take_damage(actual_damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(actual_damage * 5, character_type="player")
                    "[skill.name] deals [actual_damage] damage to [enemy.name]!"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_barrier_boss1
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    $ actual_barrier = store.locked_skill_value
                else:
                    $ actual_barrier = get_chaos_random_value(bm, skill)
                if actual_barrier == 1:
                    $ bm.rolled_one_this_turn = True
                $ bm.add_barrier(actual_barrier)
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    "You gain [actual_barrier] Defense!"
                else:
                    "You gain [skill.damage] Defense"
            elif skill.type == "dodge":
                $ bm.is_dodged = False
                $ bm.dodge_active = True
                $ bm.dodge_expires_at_slot = current_slot_idx + 1
            elif skill.type == "buff":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_buff_boss1
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    $ actual_buff = store.locked_skill_value
                else:
                    $ actual_buff = get_chaos_random_value(bm, skill)
                if actual_buff == 1:
                    $ bm.rolled_one_this_turn = True
                $ bm.add_buff(skill.buff_type, actual_buff, skill.buff_duration, target="player")
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    "[skill.name] activated! Damage increased by [actual_buff] for [skill.buff_duration] turns."
                else:
                    "[skill.name] Damage increased by [skill.damage] for [skill.buff_duration] turns."
            elif skill.type == "energy":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_energy_boss1
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    if store.locked_skill_value == 1:
                        $ bm.rolled_one_this_turn = True
                    $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + store.locked_skill_value)
                    "You gained [store.locked_skill_value] Energy!"
                else:
                    "You gained [skill.energy_regen] Energy"
            elif skill.type == "unravel":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_unravel_anim_boss1
                $ enemy.buffs = []
                "You stripped [enemy.name] of all buffs!"
            elif skill.type == "fracture":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_fracture_anim_boss1
                if enemy.barrier > 0:
                    $ enemy.barrier = 0
                    "You completely destroyed [enemy.name]'s barrier!"
                else:
                    $ bm.take_damage(store.locked_skill_value, target="enemy", enemy_idx=e_idx)
                    "You dealt [store.locked_skill_value] damage to [enemy.name]!"
            elif skill.type == "corrode":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_corrode_anim_boss1
                $ bm.add_buff("corrosion", 5, store.locked_skill_value, target="enemy", enemy_idx=e_idx)
                "You applied corrosion to [enemy.name] for [store.locked_skill_value] turns!"
            elif skill.type == "inversion":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_inversion_anim_boss1
                python:
                    for b in enemy.buffs:
                        if b[0] == "damage":
                            b[1] = -b[1]
                            renpy.say(None, "You flipped [enemy.name]'s damage buff into a penalty!")
                            break
                    else:
                        renpy.say(None, "Inversion failed: [enemy.name] has no damage buff.")
            elif skill.type == "collapse":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_collapse_anim_boss1
                $ enemy.collapsed = True
                "You collapsed [enemy.name]'s reality! Their next action is nullified."
            elif skill.type == "leech":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_leech_anim_boss1
                if enemy.buffs:
                    $ stolen = enemy.buffs.pop(0)
                    $ bm.add_buff(stolen[0], stolen[1], stolen[2], target="player")
                    "You stole [enemy.name]'s [stolen[0]] buff!"
                else:
                    "Leech failed: [enemy.name] has no buffs."
            elif skill.type == "overload":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_overload_anim_boss1
                if enemy.barrier > 0:
                    $ dmg = enemy.barrier
                    $ enemy.barrier = 0
                    $ bm.take_damage(dmg, target="enemy", enemy_idx=e_idx)
                    "Overload! [enemy.name] took [dmg] damage from their own barrier!"
                else:
                    "Overload failed: [enemy.name] has no barrier."
        elif isinstance(action, EnemyIntent):
            $ intent = action
            $ intent.current_cooldown = intent.cooldown
            $ bm.enemy_intent = intent

            if enemy.collapsed:
                $ enemy.collapsed = False
                "[enemy.name]'s action was nullified by Collapse!"
                $ e_idx += 1
                jump .boss1_resolution_core

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
                    $ damage = max(0, intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
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
            elif intent.type == "precedent":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss1_precedent
                $ triggered = False
                python:
                    for t in bm.skills_used_last_turn_types:
                        if t in ["barrier", "buff"]:
                            triggered = True
                            break
                $ damage = 8 if triggered else 3
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "[enemy.name] deals [damage] damage with PRECEDENT!"
            elif intent.type == "sentence_passed":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss1_sentence
                $ damage = max(0, intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                python:
                    for s in bm.player_skills:
                        if s.type == "barrier":
                            s.current_cooldown = max(s.current_cooldown, 2)
                "[enemy.name] deals [damage] damage and forces your barrier skills on cooldown for 2 turns!"
            elif intent.type == "the_bill":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss1_bill
                $ damage = bm.total_skills_used_this_battle
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "[enemy.name] deals [damage] damage with THE BILL!"
            elif intent.type == "recidivism":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss1_recidivism
                $ damage = 15
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                $ bm.rolled_one_last_turn = False
                "[enemy.name] deals [damage] flat damage with RECIDIVISM!"
            elif intent.type == "accumulated_weight":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss1_accumulated
                $ damage = bm.turn_count
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "[enemy.name] deals [damage] damage with ACCUMULATED WEIGHT!"
        if bm.enemies[0].is_dead:
            window hide
            jump .boss1_victory
        if bm.player_hp <= 0:
            window hide
            jump .boss1_defeat

        window hide
        $ renpy.pause(0.5, hard=True)
        $ e_count = sum(1 for e in bm.enemies if not e.is_dead)
        if e_count > 1:
            show expression bm.player_sprites["idle"] as player at fight_left_multi
        else:
            show expression bm.player_sprites["idle"] as player at fight_left

        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    if e_count > 1:
                        if i == 0:
                            pos = Position(xpos=0.62, ypos=0.8, yanchor=1.0)
                        else:
                            pos = Position(xpos=0.80, ypos=0.8, yanchor=1.0)
                    else:
                        pos = fight_right
                    renpy.show(enemy.sprites["idle"], at_list=[pos], tag=tag)
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
                $ renpy.show("ava_attack", tag="enemy_1", at_list=[Position(xpos=0.80, ypos=0.8, yanchor=1.0)])
                play sound 'punch-140236.mp3' volume 2.0
                $ renpy.pause(0.5, hard=True)
                $ damage = max(0, 5 + bm.get_total_buff_value("damage", target="enemy", enemy_idx=1) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=1))
                $ bm.take_damage(damage, target='enemy', enemy_idx=0)
                $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=1)
                'ava attacks butter for [damage] damage! (Butter HP: [bm.enemies[0].hp])'
            'butter' 'HOLD ON why are you attacking me?'
            'ava' 'oh wait i forgot you are my ally'
            'ava' 'my bad gang'
            $ renpy.show("ava_idle", tag="enemy_1", at_list=[Position(xpos=0.80, ypos=0.8, yanchor=1.0)])
        if bm.player_hp <= 0:
            window hide
            jump .boss1_defeat
        $ bm.reduce_cooldowns()
        $ bm.update_buffs()

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
    $ butter.unlocked_intents_count = 11
    $ ava_intents = get_enemy_intents("ava2")
    $ ava = Enemy('Ava', 999999, {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}, ava_intents)
    $ ava.unlocked_intents_count = 7
    $ bm = BattleManager(500, [butter, ava], starting_slots=2, player_sprites=player_sprites, starting_energy=50, max_energy=50, is_chaos=True, skill_overrides=skill_overrides)
    $ bm.initialize_skills(getattr(bm, "is_chaos", False))

    label .boss2_start_logic:
        $ bm.prepare_turn()
        $ e_count = sum(1 for e in bm.enemies if not e.is_dead)
        if e_count > 1:
            show expression bm.player_sprites["idle"] as player at fight_left_multi
        else:
            show expression bm.player_sprites["idle"] as player at fight_left

        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    if e_count > 1:
                        if i == 0:
                            pos = Position(xpos=0.62, ypos=0.8, yanchor=1.0)
                        else:
                            pos = Position(xpos=0.80, ypos=0.8, yanchor=1.0)
                    else:
                        pos = fight_right
                    renpy.show(enemy.sprites["idle"], at_list=[pos], tag=tag)
        show screen battle_screen(bm)
        if getattr(bm, "is_chaos", False):
            call chaos_card_shuffle_anim(bm) from _call_chaos_card_shuffle_boss2
        elif getattr(bm, "kare_shuffle_mode", False):
            call kare_card_shuffle_anim(bm) from _call_kare_card_shuffle_boss2
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
            $ bm.total_skills_used_this_battle += 1
            $ bm.skills_used_this_turn_types.append(skill.type)
            $ skill.current_cooldown = skill.cooldown
            if (not getattr(bm, "is_chaos", False) and not getattr(skill, "is_chaos_skill", False)) or skill.type not in ["energy", "unravel", "fracture", "corrode", "inversion", "collapse", "leech", "overload"]:
                $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)

            # Chaos number animation triggers BEFORE skill animation
            if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                $ skill_value = get_chaos_random_value(bm, skill)
                $ store.locked_skill_value = skill_value
                if skill.type == "attack":
                    call chaos_number_anim(store.locked_skill_value, "DAMAGE") from _call_chaos_slot_attack_boss2
                elif skill.type == "barrier":
                    call chaos_number_anim(store.locked_skill_value, "DEFENSE") from _call_chaos_slot_barrier_boss2
                elif skill.type == "buff":
                    call chaos_number_anim(store.locked_skill_value, "BUFF POWER") from _call_chaos_slot_buff_boss2
                elif skill.type == "energy":
                    call chaos_number_anim(store.locked_skill_value, "ENERGY REGEN") from _call_chaos_slot_energy_boss2
                elif skill.type == "fracture":
                    if enemy.barrier > 0:
                        $ store.locked_skill_value = 0
                    call chaos_number_anim(store.locked_skill_value, "DAMAGE") from _call_chaos_slot_fracture_boss2
                elif skill.type == "corrode":
                    call chaos_number_anim(store.locked_skill_value, "CORROSION") from _call_chaos_slot_corrode_boss2

            if skill.type == "attack":
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    $ actual_damage = store.locked_skill_value
                else:
                    $ actual_damage = get_chaos_random_value(bm, skill)
                if actual_damage == 1:
                    $ bm.rolled_one_this_turn = True

                if enemy.dodge_active:
                    $ bm.is_dodged = True
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_at_dodge_boss2
                    $ dodge_anim = get_dodge_anim(enemy.name)
                    call expression dodge_anim pass (bm) from _call_enemy_dodge_anim_reactive_boss2
                    $ enemy.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_generic_boss2
                    $ bm.take_damage(actual_damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(actual_damage * 5, character_type="player")
                    "[skill.name] deals [actual_damage] damage to [enemy.name]"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_barrier_boss2
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    $ actual_barrier = store.locked_skill_value
                else:
                    $ actual_barrier = get_chaos_random_value(bm, skill)
                if actual_barrier == 1:
                    $ bm.rolled_one_this_turn = True
                $ bm.add_barrier(actual_barrier)
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    "gained [actual_barrier] Defense"
                else:
                    "You gain [skill.damage] Defense"
            elif skill.type == "dodge":
                $ bm.is_dodged = False
                $ bm.dodge_active = True
                $ bm.dodge_expires_at_slot = current_slot_idx + 1
            elif skill.type == "buff":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_buff_boss2
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    $ actual_buff = store.locked_skill_value
                else:
                    $ actual_buff = get_chaos_random_value(bm, skill)
                if actual_buff == 1:
                    $ bm.rolled_one_this_turn = True
                $ bm.add_buff(skill.buff_type, actual_buff, skill.buff_duration, target="player")
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    "[skill.name] Damage increased by [actual_buff] for [skill.buff_duration] turns."
                else:
                    "[skill.name] Damage increased by [skill.damage] for [skill.buff_duration] turns."
            elif skill.type == "energy":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_energy_boss2
                if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                    if store.locked_skill_value == 1:
                        $ bm.rolled_one_this_turn = True
                    $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + store.locked_skill_value)
                    "gained [store.locked_skill_value] Energy"
                else:
                    "You gained [skill.energy_regen] Energy"
            elif skill.type == "unravel":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_unravel_anim_boss2
                $ enemy.buffs = []
                "You stripped [enemy.name] of all buffs!"
            elif skill.type == "fracture":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_fracture_anim_boss2
                if enemy.barrier > 0:
                    $ enemy.barrier = 0
                    "You completely destroyed [enemy.name]'s barrier!"
                else:
                    $ bm.take_damage(store.locked_skill_value, target="enemy", enemy_idx=e_idx)
                    "You dealt [store.locked_skill_value] damage to [enemy.name]"
            elif skill.type == "corrode":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_corrode_anim_boss2
                $ bm.add_buff("corrosion", 5, store.locked_skill_value, target="enemy", enemy_idx=e_idx)
                "applied corrosion to [enemy.name] for [store.locked_skill_value] turns"
            elif skill.type == "inversion":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_inversion_anim_boss2
                python:
                    for b in enemy.buffs:
                        if b[0] == "damage":
                            b[1] = -b[1]
                            renpy.say(None, "You flipped [enemy.name]'s damage buff into a penalty!")
                            break
                    else:
                        renpy.say(None, "Inversion failed: [enemy.name] has no damage buff.")
            elif skill.type == "collapse":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_collapse_anim_boss2
                $ enemy.collapsed = True
                "You collapsed [enemy.name]'s reality! Their next action is nullified."
            elif skill.type == "leech":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_leech_anim_boss2
                if enemy.buffs:
                    $ stolen = enemy.buffs.pop(0)
                    $ bm.add_buff(stolen[0], stolen[1], stolen[2], target="player")
                    "You stole [enemy.name]'s [stolen[0]] buff!"
                else:
                    "Leech failed: [enemy.name] has no buffs."
            elif skill.type == "overload":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_chaos_overload_anim_boss2
                if enemy.barrier > 0:
                    $ dmg = enemy.barrier
                    $ enemy.barrier = 0
                    $ bm.take_damage(dmg, target="enemy", enemy_idx=e_idx)
                    "[enemy.name] took [dmg] damage from their own barrier"
                else:
                    "Overload failed: [enemy.name] has no barrier."
        elif isinstance(action, EnemyIntent):
            $ intent = action
            $ intent.current_cooldown = intent.cooldown
            $ bm.enemy_intent = intent

            if enemy.collapsed:
                $ enemy.collapsed = False
                "[enemy.name]'s action was nullified by Collapse!"
                $ e_idx += 1
                jump .boss2_resolution_core

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
                    $ damage = max(0, intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                    $ bm.take_damage(damage, target="player")
                    $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)
                    "[enemy.name] deals [damage] damage with [intent.name]!"
            elif intent.type == "barrier":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_barrier_boss2
                $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)
                "[enemy.name] gains [intent.damage] Defense"
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
                "[enemy.name]'s damage increased by [intent.damage]"
            elif intent.type == "energy":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_energy_boss2
                "[enemy.name] is recovering."
            elif intent.type == "precedent":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss2_precedent
                $ triggered = False
                python:
                    for t in bm.skills_used_last_turn_types:
                        if t in ["barrier", "buff"]:
                            triggered = True
                            break
                $ damage = 8 if triggered else 3
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "[enemy.name] deals [damage] damage with PRECEDENT!"
            elif intent.type == "sentence_passed":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss2_sentence
                $ damage = max(0, intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                python:
                    for s in bm.player_skills:
                        if s.type == "barrier":
                            s.current_cooldown = max(s.current_cooldown, 2)
                "[enemy.name] deals [damage] damage and forces your barrier skills on cooldown for 2 turns!"
            elif intent.type == "the_bill":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss2_bill
                $ damage = bm.total_skills_used_this_battle
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "dealt [damage] damage"
            elif intent.type == "recidivism":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss2_recidivism
                $ damage = 15
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                $ bm.rolled_one_last_turn = False
                "dealt [damage] damage"
            elif intent.type == "accumulated_weight":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss2_accumulated
                $ damage = bm.turn_count
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "dealt [damage] damage"
            elif intent.type == "ones_who_built_it":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss2_onesbuilt
                $ damage = 20 if enemy.barrier == 0 else 10
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "dealt [damage] damage"
            elif intent.type == "monument":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_barrier_boss2_monument
                $ bm.add_barrier(bm.turn_count, target="enemy", enemy_idx=e_idx)
                "gained [bm.turn_count] Defense"
            elif intent.type == "we_remember":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_energy_boss2_remember
                $ heal = bm.last_drain_amount // 100
                $ old_hp = enemy.hp
                $ enemy.hp = min(enemy.max_hp, enemy.hp + heal)
                $ actual_healed = enemy.hp - old_hp
                "[enemy.name] healed [actual_healed] with WE REMEMBER"
            elif intent.type == "last_record":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss2_lastrecord
                $ damage = intent.damage
                if enemy.hp < (enemy.max_hp / 2):
                    $ damage *= 2
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "dealt [damage] damage"
            elif intent.type == "foundation":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_buff_boss2_foundation
                $ count = 0
                python:
                    new_buffs = []
                    for b in enemy.buffs:
                        if b[0] == "corrosion" or b[1] < 0:
                            count += 1
                        else:
                            new_buffs.append(b)
                    enemy.buffs = new_buffs
                $ barrier = count * 8
                $ bm.add_barrier(barrier, target="enemy", enemy_idx=e_idx)
                "[enemy.name] stripped [count] debuffs and gained [barrier] Defense"
            elif intent.type == "thousand_years":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_generic_boss2_thousand
                $ damage = bm.skills_unlocked_this_battle * 5
                $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                "dealt [damage] damage"
            elif intent.type == "still_standing":
                $ bm.is_dodged = False
                if intent.animation:
                    call expression intent.animation pass (bm) from _call_intent_anim_barrier_boss2_still
                $ bm.add_barrier(15, target="enemy", enemy_idx=e_idx)
                $ enemy.still_standing_triggered = True
                "[enemy.name] gained 15 Defense"
        if all(e.is_dead for e in bm.enemies):
            window hide
            jump .boss2_victory
        if bm.player_hp <= 0:
            window hide
            jump .boss2_defeat

        window hide
        $ renpy.pause(0.5, hard=True)
        $ e_count = sum(1 for e in bm.enemies if not e.is_dead)
        if e_count > 1:
            show expression bm.player_sprites["idle"] as player at fight_left_multi
        else:
            show expression bm.player_sprites["idle"] as player at fight_left

        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    if e_count > 1:
                        if i == 0:
                            pos = Position(xpos=0.62, ypos=0.8, yanchor=1.0)
                        else:
                            pos = Position(xpos=0.80, ypos=0.8, yanchor=1.0)
                    else:
                        pos = fight_right
                    renpy.show(enemy.sprites["idle"], at_list=[pos], tag=tag)
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
                show ava_attack as enemy_1 at Position(xpos=0.80, ypos=0.8, yanchor=1.0):
                    ease 0.2 xpos 0.35
                    ease 0.2 xpos 0.80
                play sound 'audio/sword-slash-and-swing-185432.mp3' volume 2.0
                $ renpy.pause(1.0, hard=True)
                show ava_idle as enemy_1 at Position(xpos=0.80, ypos=0.8, yanchor=1.0)
                $ damage = max(0, 50 + bm.get_total_buff_value("damage", target="enemy", enemy_idx=1) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=1))
                $ bm.take_damage(damage, target='player')
                $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=1)
                'ava attacks for [damage] damage'
        if bm.player_hp <= 0:
            window hide
            jump .boss2_defeat
        $ bm.reduce_cooldowns()
        $ bm.update_buffs()

        # buildings collapsing drains Ava every turn
        if not bm.enemies[1].is_dead:
            python:
                store.drain_amount = 33333
                # STILL STANDING Trigger logic
                if bm.enemies[1].hp <= store.drain_amount and not bm.enemies[1].still_standing_triggered:
                    bm.enemies[1].hp = 1
                    bm.enemies[1].still_standing_triggered = True
                    bm.enemies[1].barrier += 15
                    renpy.say(None, "Ava survived the collapse with 1 HP and gained 15 Defense")
                else:
                    bm.take_damage(store.drain_amount, target="enemy", enemy_idx=1)

                bm.last_drain_amount = store.drain_amount

            if getattr(renpy.store, "drain_amount", 0) > 0 and not bm.enemies[1].still_standing_triggered:
                "the city crumbles... Ava takes [store.drain_amount] damage from destruction"
                if bm.enemies[1].is_dead:
                    show ava_hit as enemy_1
                    "Ava" "my buildings..."
                    $ renpy.hide("enemy_1")
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
    if getattr(bm, "is_chaos", False):
        call chaos_card_shuffle_anim(bm) from _call_chaos_card_shuffle_order
    elif getattr(bm, "kare_shuffle_mode", False):
        call kare_card_shuffle_anim(bm) from _call_kare_card_shuffle_order

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
        $ bm.total_skills_used_this_battle += 1
        $ bm.skills_used_this_turn_types.append(skill.type)
        $ skill.current_cooldown = skill.cooldown
        if (not getattr(bm, "is_chaos", False) and not getattr(skill, "is_chaos_skill", False)) or skill.type not in ["energy", "unravel", "fracture", "corrode", "inversion", "collapse", "leech", "overload"]:
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)

        # Chaos number animation triggers BEFORE skill animation
        if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
            $ skill_value = get_chaos_random_value(bm, skill)
            $ store.locked_skill_value = skill_value
            if skill.type == "attack":
                call chaos_number_anim(store.locked_skill_value, "DAMAGE") from _call_chaos_slot_attack_order
            elif skill.type == "barrier":
                call chaos_number_anim(store.locked_skill_value, "DEFENSE") from _call_chaos_slot_barrier_order
            elif skill.type == "buff":
                call chaos_number_anim(store.locked_skill_value, "BUFF POWER") from _call_chaos_slot_buff_order
            elif skill.type == "energy":
                call chaos_number_anim(store.locked_skill_value, "ENERGY REGEN") from _call_chaos_slot_energy_order
            elif skill.type == "fracture":
                if enemy.barrier > 0:
                    $ store.locked_skill_value = 0
                call chaos_number_anim(store.locked_skill_value, "DAMAGE") from _call_chaos_slot_fracture_order
            elif skill.type == "corrode":
                call chaos_number_anim(store.locked_skill_value, "CORROSION") from _call_chaos_slot_corrode_order

        if skill.type == "attack":
            if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                $ actual_damage = store.locked_skill_value
            else:
                $ actual_damage = get_chaos_random_value(bm, skill)
            if actual_damage == 1:
                $ bm.rolled_one_this_turn = True

            if enemy.dodge_active:
                $ bm.is_dodged = True
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_at_dodge_order
                $ dodge_anim = get_dodge_anim(enemy.name)
                call expression dodge_anim pass (bm) from _call_enemy_dodge_anim_reactive_order
                $ enemy.dodge_active = False
                $ bm.is_dodged = False
            else:
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_generic_order
                $ bm.take_damage(actual_damage, target="enemy", enemy_idx=e_idx)
                $ bm.gain_exp(actual_damage * 5, character_type="player")
                "[skill.name] deals [actual_damage] damage to Order!"
                if enemy.is_dead:
                    "Order has been defeated"
                    $ renpy.hide("enemy_" + str(e_idx))
        elif skill.type == "barrier":
            $ bm.is_dodged = False
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_barrier_order
            if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                $ actual_barrier = store.locked_skill_value
            else:
                $ actual_barrier = get_chaos_random_value(bm, skill)
            if actual_barrier == 1:
                $ bm.rolled_one_this_turn = True
            $ bm.add_barrier(actual_barrier)
            if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                "You gain [actual_barrier] Defense"
            else:
                "You gain [skill.damage] Defense"
        elif skill.type == "dodge":
            $ bm.is_dodged = False
            $ bm.dodge_active = True
            $ bm.dodge_expires_at_slot = current_slot_idx + 1
        elif skill.type == "buff":
            $ bm.is_dodged = False
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_buff_order
            if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                $ actual_buff = store.locked_skill_value
            else:
                $ actual_buff = get_chaos_random_value(bm, skill)
            if actual_buff == 1:
                $ bm.rolled_one_this_turn = True
            $ bm.add_buff(skill.buff_type, actual_buff, skill.buff_duration, target="player")
            if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                "[skill.name] Damage increased by [actual_buff] for [skill.buff_duration] turns."
            else:
                "[skill.name] Damage increased by [skill.damage] for [skill.buff_duration] turns."
        elif skill.type == "energy":
            $ bm.is_dodged = False
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_energy_order
            if getattr(bm, "is_chaos", False) or getattr(skill, "is_chaos_skill", False):
                if store.locked_skill_value == 1:
                    $ bm.rolled_one_this_turn = True
                $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + store.locked_skill_value)
                "You gained [store.locked_skill_value] Energy"
            else:
                "You gained [skill.energy_regen] Energy"
        elif skill.type == "unravel":
            $ bm.is_dodged = False
            if skill.animation:
                call expression skill.animation pass (bm) from _call_chaos_unravel_anim_order
            $ enemy.buffs = []
        elif skill.type == "fracture":
            $ bm.is_dodged = False
            if skill.animation:
                call expression skill.animation pass (bm) from _call_chaos_fracture_anim_order
            if enemy.barrier > 0:
                $ enemy.barrier = 0
                "You completely destroyed Order's barrier!"
            else:
                $ bm.take_damage(store.locked_skill_value, target="enemy", enemy_idx=e_idx)
                "You dealt [store.locked_skill_value] damage to Order!"
        elif skill.type == "corrode":
            $ bm.is_dodged = False
            if skill.animation:
                call expression skill.animation pass (bm) from _call_chaos_corrode_anim_order
            $ bm.add_buff("corrosion", 5, store.locked_skill_value, target="enemy", enemy_idx=e_idx)
            "You applied corrosion to Order for [store.locked_skill_value] turns!"
        elif skill.type == "inversion":
            $ bm.is_dodged = False
            if skill.animation:
                call expression skill.animation pass (bm) from _call_chaos_inversion_anim_order
            python:
                for b in enemy.buffs:
                    if b[0] == "damage":
                        b[1] = -b[1]
                        renpy.say(None, "You flipped Order's damage buff into a penalty!")
                        break
                else:
                    renpy.say(None, "Inversion failed: Order has no damage buff.")
        elif skill.type == "collapse":
            $ bm.is_dodged = False
            if skill.animation:
                call expression skill.animation pass (bm) from _call_chaos_collapse_anim_order
            $ enemy.collapsed = True
            "You collapsed Order's reality! Their next action is nullified."
        elif skill.type == "leech":
            $ bm.is_dodged = False
            if skill.animation:
                call expression skill.animation pass (bm) from _call_chaos_leech_anim_order
            if enemy.buffs:
                $ stolen = enemy.buffs.pop(0)
                $ bm.add_buff(stolen[0], stolen[1], stolen[2], target="player")
                "You stole Order's [stolen[0]] buff!"
            else:
                "Leech failed: Order has no buffs."
        elif skill.type == "overload":
            $ bm.is_dodged = False
            if skill.animation:
                call expression skill.animation pass (bm) from _call_chaos_overload_anim_order
            if enemy.barrier > 0:
                $ dmg = enemy.barrier
                $ enemy.barrier = 0
                $ bm.take_damage(dmg, target="enemy", enemy_idx=e_idx)
                "Overload! Order took [dmg] damage from their own barrier!"
            else:
                "Overload failed: Order has no barrier."
    elif isinstance(action, EnemyIntent):
        $ intent = action
        $ intent.current_cooldown = intent.cooldown

        if enemy.collapsed:
            $ enemy.collapsed = False
            "Order's action was nullified by Collapse!"
            $ e_idx += 1
            jump order_battle_resolution_core

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
                $ damage = max(0, intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
                $ bm.take_damage(damage, target="player")
                $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)
                "Order deals [damage] damage with [intent.name]!"
        elif intent.type == "barrier":
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_order_barrier
            $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)
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
        elif intent.type == "precedent":
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_order_default_precedent
            $ triggered = False
            python:
                for t in bm.skills_used_last_turn_types:
                    if t in ["barrier", "buff"]:
                        triggered = True
                        break
            $ damage = 8 if triggered else 3
            $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
            $ bm.take_damage(damage, target="player")
        elif intent.type == "sentence_passed":
            $ bm.is_dodged = False
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_order_default_sentence
            $ damage = max(0, intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
            $ bm.take_damage(damage, target="player")
            python:
                for s in bm.player_skills:
                    if s.type == "barrier":
                        s.current_cooldown = max(s.current_cooldown, 2)
        elif intent.type == "the_bill":
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_order_default_bill
            $ damage = bm.total_skills_used_this_battle
            $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
            $ bm.take_damage(damage, target="player")
        elif intent.type == "recidivism":
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_order_default_recidivism
            $ damage = 15
            $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
            $ bm.take_damage(damage, target="player")
            $ bm.rolled_one_last_turn = False
        elif intent.type == "accumulated_weight":
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_order_default_accumulated
            $ damage = bm.turn_count
            $ damage = max(0, damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx) - bm.get_total_buff_value("corrosion", target="enemy", enemy_idx=e_idx))
            $ bm.take_damage(damage, target="player")
            "[enemy.name] deals [damage] damage with ACCUMULATED WEIGHT!"

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
style battle_charname:
    font "fonts/CaveatBrush-Regular.ttf"
    size 28

style battle_label:
    font "fonts/Caveat-Regular.ttf"
    size 15
    color "#666666"
    min_width 52

style battle_cardname:
    font "fonts/CaveatBrush-Regular.ttf"
    size 14

style battle_cardstat:
    font "fonts/Caveat-Regular.ttf"
    size 11
    color "#666666"

style battle_faint:
    font "fonts/Caveat-Regular.ttf"
    size 13
    color "#aaaaaa"

style battle_slottag:
    font "fonts/Caveat-Regular.ttf"
    size 10
    letter_spacing 1
    color "#000000"

style battle_slotname:
    font "fonts/CaveatBrush-Regular.ttf"
    size 15
    color "#000000"

style battle_cooldown_num:
    font "fonts/CaveatBrush-Regular.ttf"
    size 46
    color "#aaaaaa"

style battle_intent_title:
    font "fonts/CaveatBrush-Regular.ttf"
    size 17

style battle_intent_desc:
    font "fonts/PatrickHand-Regular.ttf"
    size 13
    italic True

image frame_plain = Frame(
    Composite(
        (12, 12),
        (0,   0),  Solid("#000000"),
        (11,  0),  Solid("#000000"),
        (0,  11),  Solid("#000000"),
        (11, 11),  Solid("#000000"),
        (1,   0),  Solid("#000000", xsize=10, ysize=1),
        (0,   1),  Solid("#000000", xsize=1, ysize=10),
        (11,  1),  Solid("#000000", xsize=1, ysize=10),
        (1,  11),  Solid("#000000", xsize=10, ysize=1),
    ),
    3, 3, 3, 3
)

image slot_border_composite = Composite(
    (100, 100),
    (0, 0), Solid("#000000", xsize=100, ysize=2),
    (0, 98), Solid("#000000", xsize=100, ysize=2),
    (0, 2), Solid("#000000", xsize=2, ysize=96),
    (98, 2), Solid("#000000", xsize=2, ysize=96),
)
image battle_slot_frame = Frame("slot_border_composite", 4, 4, 4, 4)