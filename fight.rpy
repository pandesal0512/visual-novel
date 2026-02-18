
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

# --- Transforms ---
transform fight_left:
    xpos 0.35
    ypos 0.5
    anchor (0.5, 0.5)
    zoom 1.0

transform fight_right:
    xpos 0.65
    ypos 0.5
    anchor (0.5, 0.5)
    zoom 1.0

transform enemy_charge_right:
    ease 0.2 xpos 0.5
    ease 0.2 xpos 0.65

init python:
    import random

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
            self.is_dead = False

        @property
        def intents(self):
            # Returns only the currently unlocked intents
            return self.full_intent_pool[:self.unlocked_intents_count]

    class BattleManager:
        def __init__(self, player_max_hp, enemies=None, starting_slots=2, player_sprites=None):
            self.player_hp = player_max_hp
            self.player_max_hp = player_max_hp
            self.player_energy = 10
            self.player_max_energy = 10
            self.player_barrier = 0
            self.player_buffs = []

            if isinstance(enemies, list):
                self.enemies = enemies
            else:
                self.enemies = []

            self.player_sprites = player_sprites or {"idle": "kare_idle", "attack": "kare_attack", "hit": "kare_hit"}

            self.starting_slots = 2
            self.current_max_slots = 2
            self.slots = []

            self.dodge_active = False
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

        def initialize_skills(self, is_chaos):
            # INITIAL PLAYER ENERGY
            # Change these values to set starting/max energy for Kare and Chaos
            self.player_max_energy = 50 if is_chaos else 10
            self.player_energy = self.player_max_energy
            char_name = "chaos" if is_chaos else "kare"
            self.full_skill_pool = get_character_skills(char_name)
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
            if self.player_energy >= skill.cost and skill.current_cooldown == 0:
                enemy = self.enemies[enemy_idx]
                if enemy.slots[slot_idx] is None:
                    enemy.slots[slot_idx] = skill
                    self.player_energy -= skill.cost
                    self.used_skills_this_turn.append(skill)
                    self.selected_skill = None
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
            # Growth: starts at 2, +1 every 2 turns, max 6.
            self.current_max_slots = min(6, 2 + (self.turn_count - 1) // 2)

            self.used_skills_this_turn = []
            self.selected_skill = None
            self.selected_intent = None
            self.selected_enemy_index = -1
            self.selected_slot_index = -1

            # REGENERATE PLAYER ENERGY PER TURN
            # Change the value below (currently 2) to increase/decrease energy gain per turn
            self.player_energy = min(self.player_max_energy, self.player_energy + 2)

            for enemy in self.enemies:
                if not enemy.is_dead:
                    enemy.slots = [None] * self.current_max_slots
                    num_enemy_slots = self.current_max_slots // 2
                    available_indices = list(range(self.current_max_slots))
                    renpy.random.shuffle(available_indices)

                    # Unique intents, ignore cooldowns for enemies
                    available_intents = list(enemy.intents)
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
                self.player_buffs.append([type, value, duration])
            else:
                self.enemies[enemy_idx].buffs.append([type, value, duration])

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
        Normal, Shields, Energy, Hard, Dodge, Ultimate.
        """
        # EDIT THESE VALUES TO CHANGE CHARACTER SKILLS
        if name.lower() == "kare":
            return [
                Skill("slap", cost=2, damage=5, energy_regen=1, desc="Standard strike.", animation="kare_normal_anim", card_image="card_kare_normal"),
                Skill("block", cost=3, damage=8, type="barrier", desc="Gain 8 Shields.", cooldown=0, animation="kare_block_anim", card_image="card_kare_block"),
                Skill("yummers", cost=0, energy_regen=5, type="energy", desc="Recover 5 energy.", animation="kare_energy_anim", card_image="card_kare_energy"),
                Skill("punch", cost=5, damage=12, cooldown=0, desc="Powerful punch.", animation="kare_hard_anim", card_image="card_kare_hard"),
                Skill("evade", cost=4, type="dodge", desc="Dodges next attack.", cooldown=0, animation="kare_dodge_anim", card_image="card_kare_dodge"),
                Skill("super cool kick", cost=15, damage=40, cooldown=0, desc="kick thats it.", animation="kare_ultimate_anim", card_image="card_kare_ultimate"),
                Skill("Focus", cost=4, damage=5, type="buff", buff_type="damage", buff_duration=3, desc="Increases damage by 5 for 3 turns.", animation="kare_buff_anim")
            ]
        elif name.lower() == "chaos":
            return [
                Skill("interitus", cost=3, damage=8, energy_regen=2, desc="huahuahuaha!!", animation="chaos_normal_anim", card_image="card_chaos_normal"),
                Skill("Embrace", cost=5, damage=15, type="barrier", desc="Embrace the heat death of all things", cooldown=0, animation="chaos_block_anim", card_image="card_chaos_block"),
                Skill("Entropy", cost=0, energy_regen=12, type="energy", desc="gain 12 energy", animation="chaos_energy_anim", card_image="card_chaos_energy"),
                Skill("Cataclysm", cost=7, damage=18, cooldown=0, desc="Reality fractures under my touch.", animation="chaos_hard_anim", card_image="card_chaos_hard"),
                Skill("dissolutum", cost=6, type="dodge", desc="Shift out of reality.", cooldown=0, animation="chaos_dodge_anim", card_image="card_chaos_dodge"),
                Skill("████████", cost=25, damage=100, cooldown=0, desc="█████ ████████████", animation="chaos_ultimate_anim", card_image="card_chaos_ultimate"),
                Skill("Aura of Dread", cost=6, damage=10, type="buff", buff_type="damage", buff_duration=3, desc="Increases damage by 10 for 3 turns.", animation="chaos_buff_anim")
            ]
        return []

    def get_enemy_intents(name):
        """
        Returns a list of 6 intents for an enemy character in the order:
        Normal, Shields, Energy, Hard, Dodge, Ultimate.
        """
        # EDIT THESE VALUES TO CHANGE ENEMY INTENTS
        if name.lower() == "butter":
            return [
                EnemyIntent("Butter Knife", damage=4, desc="A quick poke.", animation="butter_normal_anim", type="attack"),
                EnemyIntent("Hard Shell", damage=6, desc="Adds 6 Shields.", animation="butter_block_anim", type="barrier", cooldown=0),
                EnemyIntent("Churn Up", damage=5, buff_type="damage", buff_duration=3, desc="Increases damage by 5 for 3 turns.", animation="butter_energy_anim", type="buff"),
                EnemyIntent("Melting Slam", damage=10, desc="A heavy impact.", animation="butter_hard_anim", type="attack", cooldown=0),
                EnemyIntent("Slippery", desc="Will dodge the next attack.", animation="butter_dodge_anim", type="dodge", cooldown=0),
                EnemyIntent("Golden Spread", damage=30, desc="ULTIMATE: Covered in gold.", animation="butter_ultimate_anim", type="attack", cooldown=0)
            ]
        elif name.lower() == "serious butter":
            return [
                EnemyIntent("Serious Slash", damage=10, desc="No jokes here.", animation="serious_butter_normal_anim", type="attack"),
                EnemyIntent("Armor of the Serious", damage=20, desc="Adds 20 Shields.", animation="serious_butter_block_anim", type="barrier", cooldown=0),
                EnemyIntent("Market Analysis", damage=10, buff_type="damage", buff_duration=3, desc="Increases damage by 10 for 3 turns.", animation="serious_butter_energy_anim", type="buff"),
                EnemyIntent("Executive Decision", damage=25, desc="Finalized.", animation="serious_butter_hard_anim", type="attack", cooldown=0),
                EnemyIntent("Calculated Move", desc="Will dodge the next attack.", animation="serious_butter_dodge_anim", type="dodge", cooldown=0),
                EnemyIntent("MARKET CRASH", damage=80, desc="ULTIMATE: Absolute devastation.", animation="serious_butter_ultimate_anim", type="attack", cooldown=0)
            ]
        elif name.lower() == "lumpi":
            return [
                EnemyIntent("slash", damage=3, desc="very powerful sword", animation="lumpi_normal_anim", type="attack"),
                EnemyIntent("Nebula Veil", damage=5, desc="Adds 5 Shields.", animation="lumpi_block_anim", type="barrier", cooldown=0),
                EnemyIntent("Moonlight Blessing", damage=5, buff_type="damage", buff_duration=3, desc="Increases damage by 5 for 3 turns.", animation="lumpi_energy_anim", type="buff"),
                EnemyIntent("Meteor Cleave", damage=8, desc="poweful attack", animation="lumpi_hard_anim", type="attack", cooldown=0),
                EnemyIntent("evade", desc="Will dodge the next attack.", animation="lumpi_dodge_anim", type="dodge", cooldown=0),
                EnemyIntent("Execution", damage=25, desc="very powerful attack.", animation="lumpi_ultimate_anim", type="attack", cooldown=0)
            ]
        elif name.lower() == "lumpi wheelchair":
            return [
                EnemyIntent("Tire Runover", damage=7, desc="Watch your toes.", animation="lumpi_wheelchair_normal_anim", type="attack"),
                EnemyIntent("Reinforced Frame", damage=12, desc="Adds 12 Shields.", animation="lumpi_wheelchair_block_anim", type="barrier", cooldown=0),
                EnemyIntent("Overdrive", damage=8, buff_type="damage", buff_duration=3, desc="Increases damage by 8 for 3 turns.", animation="lumpi_wheelchair_energy_anim", type="buff"),
                EnemyIntent("Turbo Charge", damage=15, desc="High speed impact.", animation="lumpi_wheelchair_hard_anim", type="attack", cooldown=0),
                EnemyIntent("Drift", desc="Will dodge the next attack.", animation="lumpi_wheelchair_dodge_anim", type="dodge", cooldown=0),
                EnemyIntent("SUPERSONIC CRASH", damage=50, desc="ULTIMATE: Breaking sound barrier.", animation="lumpi_wheelchair_ultimate_anim", type="attack", cooldown=0)
            ]
        elif name.lower() == "ava":
            return [
                EnemyIntent("Magic Spark", damage=6, desc="A tiny burst.", animation="ava_normal_anim", type="attack"),
                EnemyIntent("Mana Veil", damage=10, desc="Adds 10 Shields.", animation="ava_block_anim", type="barrier", cooldown=0),
                EnemyIntent("Arcane Focus", damage=15, buff_type="damage", buff_duration=3, desc="Increases damage by 15 for 3 turns.", animation="ava_energy_anim", type="buff"),
                EnemyIntent("Arcane Blast", damage=15, desc="Powerful magic.", animation="ava_hard_anim", type="attack", cooldown=0),
                EnemyIntent("Blink", desc="Will dodge the next attack.", animation="ava_dodge_anim", type="dodge", cooldown=0),
                EnemyIntent("COSMIC BURST", damage=60, desc="ULTIMATE: Nebula explosion.", animation="ava_ultimate_anim", type="attack", cooldown=0)
            ]
        return []

screen battle_screen(bm):
    $ p_name = "Chaos" if "chaos" in bm.player_sprites["idle"] else "Kare"
    # ── Player stats: top left ──
    vbox:
        xalign 0.05 yalign 0.05
        spacing 5
        xmaximum 400
        text "[p_name]: [bm.player_hp]/[bm.player_max_hp]" size 24 color "#747474" outlines [(2, "#000")]
        bar value bm.player_hp range bm.player_max_hp xmaximum 300

        hbox:
            spacing 20
            vbox:
                text "Energy: [bm.player_energy]/[bm.player_max_energy]" size 20 color "#666666" outlines [(1, "#000")]
            if bm.player_barrier > 0:
                vbox:
                    text "Shields: [bm.player_barrier]" size 20 color "#797979" outlines [(1, "#000")]

        hbox:
            spacing 5
            for buff in bm.player_buffs:
                frame:
                    background Solid("#5e5e5e")
                    padding (5, 2)
                    text "[buff[0]]: [buff[1]] ([buff[2]]t)" size 12 color "#fff"

    # ── Enemy stats: top right ──
    vbox:
        xalign 0.95 yalign 0.05
        spacing 10
        for e_idx, enemy in enumerate(bm.enemies):
            if not enemy.is_dead:
                vbox:
                    spacing 2
                    text "[enemy.name]: [enemy.hp]/[enemy.max_hp]" size 20 color "#747474" xalign 1.0 outlines [(2, "#000")]
                    bar value enemy.hp range enemy.max_hp xmaximum 250 xalign 1.0
                    if enemy.barrier > 0:
                        text "Shields: [enemy.barrier]" size 14 color "#6d6d6d" xalign 1.0

                    # ENEMY SKILL PROGRESS BAR
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

    # ── Battle slots: top center, same height as health bars ──
    vbox:
        xalign 0.5 yalign 0.05
        spacing 10
        text "Select a card below, then click an empty slot here:" size 16 color "#aaa" xalign 0.5

        for e_idx, enemy in enumerate(bm.enemies):
            if not enemy.is_dead:
                frame:
                    background Solid("#0006")
                    padding (10, 10)
                    xalign 0.5
                    vbox:
                        spacing 5
                        text "[enemy.name]'s Row" size 14 color "#ccc" xalign 0.0
                        hbox:
                            spacing 10
                            for s_idx in range(bm.current_max_slots):
                                $ action = enemy.slots[s_idx]
                                if action is None:
                                    $ can_add = bm.selected_skill is not None and bm.player_energy >= bm.selected_skill.cost
                                    button:
                                        action If(can_add, Function(bm.add_to_slot, bm.selected_skill, e_idx, s_idx))
                                        background Solid("#333")
                                        padding (10, 5)
                                        xminimum 80
                                        yminimum 40
                                        text "EMPTY" size 16 color "#555" xalign 0.5
                                elif isinstance(action, EnemyIntent):
                                    button:
                                        action [Function(bm.select_intent, action, e_idx, s_idx), SetField(bm, "selected_skill", None)]
                                        background Solid("#5e5e5e")
                                        padding (10, 5)
                                        xminimum 80
                                        yminimum 40
                                        vbox:
                                            text "ENEMY" size 12 color "#616161" xalign 0.5
                                            text "[action.name]" size 16 color "#fff" xalign 0.5
                                elif isinstance(action, Skill):
                                    button:
                                        action Function(bm.select_skill, action)
                                        background Solid("#686868")
                                        padding (10, 5)
                                        xminimum 80
                                        yminimum 40
                                        vbox:
                                            text "YOU" size 12 color "#aaaaff" xalign 0.5
                                            text "[action.name]" size 16 color "#fff" xalign 0.5



    # ── Skill cards: bottom ──
    vbox:
        xalign 0.5 ypos 0.98 yanchor 1.0
        spacing 5

        hbox:
            xalign 0.5
            spacing 4
            text "Next skill: " size 13 color "#777777" outlines [(1,"#000")]
            bar value bm.skill_exp range bm.skill_exp_max xmaximum 600 ysize 8 yalign 0.5

        hbox:
            xalign 0.5
            spacing 15
            for skill in bm.player_skills:
                $ is_selected = bm.selected_skill == skill
                $ can_use = skill.current_cooldown == 0 and skill not in bm.used_skills_this_turn
                $ card_bg = Solid("#555") if is_selected else (Solid("#333e") if can_use else Solid("#111e"))
                $ name_col = "#fff" if can_use else "#666"

                button:
                    action Function(bm.select_skill, skill)
                    sensitive (skill.current_cooldown == 0 and skill not in bm.used_skills_this_turn)
                    background card_bg
                    padding (0, 0)
                    xsize 140
                    ysize 180

                    if skill.card_image:
                        add skill.card_image

                    if skill.current_cooldown > 0:
                        text "[skill.current_cooldown]" size 40 color "#838383" xalign 0.5 yalign 0.5 bold True outlines [(2, "#000")]
                    elif skill in bm.used_skills_this_turn:
                        text "USED" size 20 color "#888" xalign 0.5 yalign 0.5 bold True outlines [(1, "#000")]

    # ── Confirm / Clear buttons ──
    $ has_player_action = any(isinstance(s, Skill) for enemy in bm.enemies for s in enemy.slots)
    textbutton "CONFIRM":
        xalign 0.95 yalign 0.8
        background Solid("#7e7e7e")
        padding (20, 10)
        text_size 30
        text_color "#fff"
        text_bold True
        action Return("execute")

    if has_player_action:
        textbutton "CLEAR":
            xalign 0.05 yalign 0.8
            background Solid("#444")
            padding (10, 5)
            text_size 20
            text_color "#fff"
            action Function(bm.clear_queue)


    # ── POPUPS ──
    if bm.selected_skill or bm.selected_intent:
        if bm.selected_skill:
            frame:
                background Solid("#222d")
                xalign 0.5 yalign 0.5
                padding (30, 30)
                xminimum 400
                vbox:
                    spacing 15
                    if bm.selected_skill.card_image:
                        add bm.selected_skill.card_image xalign 0.5
                    text "[bm.selected_skill.name]" size 30 color "#fff" xalign 0.5 bold True
                    text "Cost: [bm.selected_skill.cost] Energy" size 20 color "#808080" xalign 0.5
                    if bm.selected_skill.damage > 0:
                        text "Damage: [bm.selected_skill.damage]" size 20 color "#797979" xalign 0.5
                    text "[bm.selected_skill.desc]" size 18 color "#ccc" xalign 0.5 text_align 0.5
                    if bm.selected_skill.cooldown > 0:
                        text "Cooldown: [bm.selected_skill.cooldown] turns" size 18 color "#7a7a7a" xalign 0.5

                    if bm.selected_skill in bm.used_skills_this_turn:
                        $ e_idx, s_idx = bm.get_skill_slot_info(bm.selected_skill)
                        if e_idx != -1:
                            null height 20
                            textbutton "REMOVE FROM SLOT":
                                action [Function(bm.remove_from_slot, e_idx, s_idx), SetField(bm, "selected_skill", None)]
                                xalign 0.5
                                background Solid("#8a8a8a")
                                padding (15, 10)
                                text_size 24
                                text_bold True

        if bm.selected_intent:
            frame:
                background Solid("#222d")
                xalign 0.5 yalign 0.5
                padding (30, 30)
                xminimum 400
                vbox:
                    spacing 15
                    text "[bm.enemies[bm.selected_enemy_index].name]'s Intent: [bm.selected_intent.name]" size 30 color "#ffffff" xalign 0.5 bold True
                    if bm.selected_intent.damage > 0:
                        if bm.selected_intent.type == "attack":
                            text "Projected Damage: [bm.selected_intent.damage]" size 20 color "#818181" xalign 0.5
                        elif bm.selected_intent.type == "barrier":
                            text "Projected Shields: [bm.selected_intent.damage]" size 20 color "#5c5c5c" xalign 0.5
                    text "[bm.selected_intent.desc]" size 18 color "#ccc" xalign 0.5 text_align 0.5

label battle_reset_camera:
    camera:
        perspective False
        gl_depth False
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    return

label battle_engine(bm, is_chaos=False):
    $ bm.initialize_skills(is_chaos)

    label .engine_start_logic:
        $ bm.prepare_turn()

        show expression bm.player_sprites["idle"] as player at fight_left
        $ e_count = sum(1 for e in bm.enemies if not e.is_dead)
        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    pos = fight_right
                    if e_count > 1:
                        pos = Position(xalign=0.6 + (i * 0.15), yalign=0.5)
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
        if action is None:
            $ pass
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)
            $ current_enemy_tag = "enemy_" + str(e_idx)

            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_generic_new

            if skill.type == "attack":
                if enemy.dodge_active:
                    "[enemy.name] dodged the attack!"
                    $ enemy.dodge_active = False
                else:
                    $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")
                    $ bm.take_damage(damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(damage * 5, character_type="player")
                    "[skill.name] deals [damage] damage to [enemy.name]!"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated!"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.add_barrier(skill.damage)
                "You gain [skill.damage] Shields!"
            elif skill.type == "dodge":
                $ bm.dodge_active = True
                "You prepare to dodge!"
            elif skill.type == "buff":
                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")
                "[skill.name] activated! Damage increased by [skill.damage] for [skill.buff_duration] turns."
            elif skill.type == "energy":
                "You gained [skill.energy_regen] Energy!"

        elif isinstance(action, EnemyIntent):
            $ intent = action
            # Enemies no longer use cooldowns
            $ bm.enemy_intent = intent
            $ current_enemy_tag = "enemy_" + str(e_idx)

            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_anim_generic_new
            else:
                call enemy_attack_anim(bm) from _call_intent_anim_default_new

            if intent.type == "attack":
                if bm.dodge_active:
                    "DODGED!"
                    $ bm.dodge_active = False
                else:
                    $ damage = intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                    $ bm.take_damage(damage, target="player")
                    $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)
                    "[enemy.name] deals [damage] damage with [intent.name]!"
            elif intent.type == "barrier":
                $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)
                "[enemy.name] gains [intent.damage] Shields!"
            elif intent.type == "dodge":
                $ enemy.dodge_active = True
                "[enemy.name] will dodge the next attack!"
            elif intent.type == "buff":
                $ bm.add_buff(intent.buff_type, intent.damage, intent.buff_duration, target="enemy", enemy_idx=e_idx)
                "[enemy.name] activated [intent.name]! Their damage increased by [intent.damage]!"
            elif intent.type == "energy":
                "[enemy.name] is recovering."

        if all(e.is_dead for e in bm.enemies):
            jump .engine_victory
        if bm.player_hp <= 0:
            jump .engine_defeat

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
        jump .engine_start_logic

    label .engine_victory:
        hide screen battle_screen
        python:
            for i in range(len(bm.enemies)):
                renpy.hide("enemy_" + str(i))
        return "win"

    label .engine_defeat:
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
    $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    play sound "punch-140236.mp3"
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label kare_hard_anim(bm):
    show expression "kare_hard_sprite" as player at fight_left:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.35
    $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    play sound "audio/sword-slash-and-swing-185432.mp3"
    $ renpy.pause(0.8, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label kare_block_anim(bm):
    show expression "kare_block_sprite" as player at fight_left
    play sound "Berserk Clang Sound Effect.mp3"
    $ renpy.pause(0.5, hard=True)
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
    $ renpy.pause(0.8, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label kare_ultimate_anim(bm):
    show expression "kare_ultimate_sprite" as player at fight_left:
        ease 0.3 xpos 0.6
        ease 0.3 xpos 0.35
    $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    play sound "audio/sword-slash-and-swing-185432.mp3"
    camera:
        ease 0.1 zoom 1.2
        ease 0.1 zoom 1.0
    $ renpy.pause(1.2, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label kare_energy_anim(bm):
    show expression "kare_energy_sprite" as player at fight_left
    play sound "audio/item-pickup-37089.mp3"
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

# --- CHAOS ANIMATIONS ---
label chaos_normal_anim(bm):
    show expression "chaos_normal_sprite" as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    play sound "punch-140236.mp3"
    $ renpy.pause(0.5, hard=True)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label chaos_hard_anim(bm):
    show expression "chaos_hard_sprite" as player at fight_left
    $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
    play sound "audio/sword-slash-and-swing-185432.mp3"
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
    $ renpy.show(bm.enemies[e_idx].sprites["hit"], tag=current_enemy_tag)
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
    show expression bm.player_sprites["hit"] as player at fight_left
    play sound "audio/sword-slash-and-swing-185432.mp3"
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label butter_hard_anim(bm):
    $ renpy.show("butter_hard_sprite", tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    show expression bm.player_sprites["hit"] as player at fight_left
    play sound "audio/sword-slash-and-swing-185432.mp3"
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label butter_block_anim(bm):
    $ renpy.show("butter_block_sprite", tag=current_enemy_tag, at_list=[fight_right])
    play sound "Berserk Clang Sound Effect.mp3"
    $ renpy.pause(0.5, hard=True)
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
    $ renpy.show("butter_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right])
    show expression bm.player_sprites["hit"] as player at fight_left
    play sound "audio/single-gunshot-62-hp-37188.mp3"
    $ renpy.pause(1.2, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label butter_energy_anim(bm):
    $ renpy.show("butter_energy_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

# --- SERIOUS BUTTER ANIMATIONS ---
label serious_butter_normal_anim(bm):
    $ renpy.show("serious_butter_normal_sprite", tag=current_enemy_tag, at_list=[fight_right])
    show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label serious_butter_hard_anim(bm):
    $ renpy.show("serious_butter_hard_sprite", tag=current_enemy_tag, at_list=[fight_right])
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
    $ renpy.show("lumpi_normal_sprite", tag=current_enemy_tag, at_list=[fight_right])
    show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label lumpi_hard_anim(bm):
    $ renpy.show("lumpi_hard_sprite", tag=current_enemy_tag, at_list=[fight_right])
    show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.8, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label lumpi_block_anim(bm):
    $ renpy.show("lumpi_block_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5, hard=True)
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
    $ renpy.show("lumpi_wheelchair_normal_sprite", tag=current_enemy_tag, at_list=[fight_right])
    show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label lumpi_wheelchair_hard_anim(bm):
    $ renpy.show("lumpi_wheelchair_hard_sprite", tag=current_enemy_tag, at_list=[fight_right])
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
    $ renpy.show("lumpi_wheelchair_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right])
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
    show expression bm.player_sprites["hit"] as player at fight_left
    play sound "audio/magic-spark.mp3"
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label ava_hard_anim(bm):
    $ renpy.show("ava_hard_sprite", tag=current_enemy_tag, at_list=[fight_right])
    show expression bm.player_sprites["hit"] as player at fight_left
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
    show expression bm.player_sprites["hit"] as player at fight_left
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

# --- FALLBACKS ---
label enemy_attack_anim(bm):
    $ enemy = bm.enemies[e_idx]
    $ renpy.show(enemy.sprites["attack"], tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(0.5, hard=True)
    $ renpy.show(enemy.sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label battle_butter_simple:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show butter_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'butter_idle', 'attack': 'butter_attack', 'hit': 'butter_hit'}
    # USES THE NEW UNIQUE INTENT SET FOR BUTTER
    $ butter_intents = get_enemy_intents("butter")
    $ butter = Enemy('Butter', 15, enemy_sprites, butter_intents)
    $ bm = BattleManager(10, [butter], starting_slots=2, player_sprites=player_sprites)
    call battle_engine(bm) from _call_battle_engine_butter
    if _return == 'win':
        jump .player_wins
    else:
        jump .player_loses
    label .player_wins:
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_1
        hide player
        with fade
        'yay win'
        return
    label .player_loses:
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_2
        hide player
        'You were defeated by butter...'
        return

label battle_lumpi_standard:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show lumpi_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpi_idle', 'attack': 'lumpi_attack', 'hit': 'lumpi_hit'}
    # USES THE NEW UNIQUE INTENT SET FOR LUMPI
    $ lumpi_intents = get_enemy_intents("lumpi")
    $ lumpi = Enemy('Lumpi', 25, enemy_sprites, lumpi_intents)
    $ bm = BattleManager(15, [lumpi], starting_slots=2, player_sprites=player_sprites)
    call battle_engine(bm) from _call_battle_engine_lumpi
    if _return == 'win':
        jump .lumpi_wins
    else:
        jump .lumpi_loses
    label .lumpi_wins:
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_3
        hide player
        return
    label .lumpi_loses:
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_4
        'You were defeated by Lumpi...'
        menu:
            'Retry Battle':
                jump battle_lumpi_standard

label battle_lumpi_wheelchair:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show lumpiwheelchair_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpiwheelchair_idle', 'attack': 'lumpiwheelchair_attack', 'hit': 'lumpiwheelchair_hit'}
    # USES THE NEW UNIQUE INTENT SET FOR LUMPI WHEELCHAIR
    $ lumpi_intents = get_enemy_intents("lumpi wheelchair")
    $ lumpi = Enemy('Lumpi (Wheelchair)', 40, enemy_sprites, lumpi_intents)
    $ bm = BattleManager(20, [lumpi], starting_slots=2, player_sprites=player_sprites)
    call battle_engine(bm) from _call_battle_engine_wheelchair
    if _return == 'win':
        jump .lumpiwheelchair_wins
    else:
        jump .lumpiwheelchair_loses
    label .lumpiwheelchair_wins:
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_5
        hide player
        return
    label .lumpiwheelchair_loses:
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_6
        'lumpi' 'huwhuahuwha i win'
        menu:
            'Retry Battle':
                jump battle_lumpi_wheelchair

label battle_serious_butter:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show seriousbutter_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'seriousbutter_idle', 'attack': 'seriousbutter_attack', 'hit': 'seriousbutter_hit'}
    # USES THE NEW UNIQUE INTENT SET FOR SERIOUS BUTTER
    $ butter_intents = get_enemy_intents("serious butter")
    $ butter = Enemy('butter', 100, enemy_sprites, butter_intents)
    $ bm = BattleManager(50, [butter], starting_slots=2, player_sprites=player_sprites)
    call battle_engine(bm, is_chaos=False) from _call_battle_engine_newenemy
    if _return == 'win':
        jump .newenemy_wins
    else:
        jump .newenemy_loses
    label .newenemy_wins:
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_7
        hide player
        return
    label .newenemy_loses:
        $ renpy.pause(0.1, hard=True)
        call battle_reset_camera from _call_battle_reset_camera_8
        menu:
            'Retry Battle':
                jump battle_serious_butter

label battle_boss_ava_butter:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    # USES UNIQUE INTENTS FOR BUTTER AND AVA
    $ butter_intents = get_enemy_intents("serious butter")
    $ butter = Enemy('butter', 100,{'idle': 'seriousbutter_idle', 'attack': 'seriousbutter_attack', 'hit': 'seriousbutter_hit'}, butter_intents)
    $ ava_intents = get_enemy_intents("ava")
    $ ava = Enemy('Ava', 999999, {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}, ava_intents)
    $ bm = BattleManager(500, [butter, ava], starting_slots=2, player_sprites=player_sprites)
    $ bm.initialize_skills(True)
    $ ava_attacked_once = False

    label .boss1_start_logic:
        $ bm.prepare_turn()
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    pos = Position(xalign=0.6 + (i * 0.15), yalign=0.5)
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
            $ pass
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_ava_new
            if skill.type == 'attack':
                if enemy.dodge_active:
                    "[enemy.name] dodged the attack!"
                    $ enemy.dodge_active = False
                else:
                    $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")
                    $ bm.take_damage(damage, target='enemy', enemy_idx=e_idx)
                    $ bm.gain_exp(damage * 5, character_type="player")
                    "[skill.name] deals [damage] damage to [enemy.name]!"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated!"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == 'barrier':
                $ bm.add_barrier(skill.damage)
                "You gain [skill.damage] Shields!"
            elif skill.type == 'dodge':
                $ bm.dodge_active = True
                "You prepare to dodge!"
            elif skill.type == 'buff':
                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")
                "[skill.name] activated! Damage increased by [skill.damage] for [skill.buff_duration] turns."
            elif skill.type == "energy":
                "You gained [skill.energy_regen] Energy!"
        elif isinstance(action, EnemyIntent):
            $ intent = action
            # Enemies no longer use cooldowns
            $ bm.enemy_intent = intent
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_anim_ava_butter_new
            else:
                call enemy_attack_anim(bm) from _call_intent_anim_ava_butter_default_new

            if intent.type == "attack":
                if bm.dodge_active:
                    "DODGED!"
                    $ bm.dodge_active = False
                else:
                    $ damage = intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                    $ bm.take_damage(damage, target='player')
                    $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)
                    "[enemy.name] deals [damage] damage with [intent.name]!"
            elif intent.type == "barrier":
                $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)
                "[enemy.name] gains [intent.damage] Shields!"
            elif intent.type == "dodge":
                $ enemy.dodge_active = True
                "[enemy.name] will dodge the next attack!"
            elif intent.type == "buff":
                $ bm.add_buff(intent.buff_type, intent.damage, intent.buff_duration, target="enemy", enemy_idx=e_idx)
                "[enemy.name] activated [intent.name]! Their damage increased by [intent.damage]!"
            elif intent.type == "energy":
                "[enemy.name] is recovering."
        if all(e.is_dead for e in bm.enemies):
            jump .boss1_victory
        if bm.player_hp <= 0:
            jump .boss1_defeat
        $ renpy.pause(0.5, hard=True)
        show expression bm.player_sprites["idle"] as player at fight_left
        $ e_idx += 1
        jump .boss1_resolution_core
    label .boss1_extra_turn:
        if not bm.enemies[0].is_dead and not bm.enemies[1].is_dead and not ava_attacked_once:
            $ ava_attacked_once = True
            $ renpy.show("ava_attack", tag="enemy_1", at_list=[Position(xalign=0.75, yalign=0.5)])
            play sound 'punch-140236.mp3' volume 2.0
            $ renpy.pause(0.5, hard=True)
            $ bm.take_damage(5, target='enemy', enemy_idx=0)
            $ bm.gain_exp(5 * 5, character_type="enemy", enemy_idx=1)
            'ava attacks butter for 5 damage! (Butter HP: [bm.enemies[0].hp])'
            'butter' 'HOLD ON why are you attacking me?'
            'ava' 'oh wait i forgot you are my ally'
            'ava' 'my bad gang'
            $ renpy.show("ava_idle", tag="enemy_1", at_list=[Position(xalign=0.75, yalign=0.5)])
        if bm.player_hp <= 0:
            jump .boss1_defeat
        $ bm.reduce_cooldowns()
        jump .boss1_start_logic
    label .boss1_victory:
        hide screen battle_screen
        return
    label .boss1_defeat:
        hide screen battle_screen
        return

label battle_boss_ava_butter_phase2:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    # USES UNIQUE INTENTS FOR SERIOUS BUTTER AND AVA
    $ butter_intents = get_enemy_intents("serious butter")
    $ butter = Enemy('butter', 100, {'idle': 'butter_idle', 'attack': 'butter_attack', 'hit': 'butter_hit'}, butter_intents)
    $ ava_intents = get_enemy_intents("ava")
    $ ava = Enemy('Ava', 500, {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}, ava_intents)
    $ bm = BattleManager(500, [butter, ava], starting_slots=2, player_sprites=player_sprites)
    $ bm.initialize_skills(True)

    label .boss2_start_logic:
        $ bm.prepare_turn()
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    pos = Position(xalign=0.6 + (i * 0.15), yalign=0.5)
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
            $ pass
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_ava2_new
            if skill.type == 'attack':
                if enemy.dodge_active:
                    "[enemy.name] dodged the attack!"
                    $ enemy.dodge_active = False
                else:
                    $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")
                    $ bm.take_damage(damage, target='enemy', enemy_idx=e_idx)
                    $ bm.gain_exp(damage * 5, character_type="player")
                    "[skill.name] deals [damage] damage to [enemy.name]!"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated!"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == 'barrier':
                $ bm.add_barrier(skill.damage)
                "You gain [skill.damage] Shields!"
            elif skill.type == 'dodge':
                $ bm.dodge_active = True
                "You prepare to dodge!"
            elif skill.type == 'buff':
                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")
                "[skill.name] activated! Damage increased by [skill.damage] for [skill.buff_duration] turns."
            elif skill.type == "energy":
                "You gained [skill.energy_regen] Energy!"
        elif isinstance(action, EnemyIntent):
            $ intent = action
            # Enemies no longer use cooldowns
            $ bm.enemy_intent = intent
            # Special logic for unique intent names can still be here if needed
            if intent.animation:
                call expression intent.animation pass (bm) from _call_intent_anim_ava_butter2_new
            else:
                call enemy_attack_anim(bm) from _call_intent_anim_ava_butter_default2_new

            if intent.type == "attack":
                if bm.dodge_active:
                    "DODGED!"
                    $ bm.dodge_active = False
                else:
                    $ damage = intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                    $ bm.take_damage(damage, target='player')
                    $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)
                    "[enemy.name] deals [damage] damage with [intent.name]!"
            elif intent.type == "barrier":
                $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)
                "[enemy.name] gains [intent.damage] Shields!"
            elif intent.type == "dodge":
                $ enemy.dodge_active = True
                "[enemy.name] will dodge the next attack!"
            elif intent.type == "buff":
                $ bm.add_buff(intent.buff_type, intent.damage, intent.buff_duration, target="enemy", enemy_idx=e_idx)
                "[enemy.name] activated [intent.name]! Their damage increased by [intent.damage]!"
            elif intent.type == "energy":
                "[enemy.name] is recovering."
        if all(e.is_dead for e in bm.enemies):
            jump .boss2_victory
        if bm.player_hp <= 0:
            jump .boss2_defeat
        $ renpy.pause(0.5, hard=True)
        show expression bm.player_sprites["idle"] as player at fight_left
        $ e_idx += 1
        jump .boss2_resolution_core
    label .boss2_extra_turn:
        show ava_attack as enemy_1 at Position(xalign=0.85, yalign=0.5):
            ease 0.2 xpos 0.35
            ease 0.2 xpos 0.85
        play sound 'audio/sword-slash-and-swing-185432.mp3' volume 2.0
        $ renpy.pause(1.0, hard=True)
        show ava_idle as enemy_1 at Position(xalign=0.85, yalign=0.5)
        $ bm.take_damage(50, target='player')
        $ bm.gain_exp(50 * 5, character_type="enemy", enemy_idx=1)
        'ava attacks for 50 damage! (Your HP: [bm.player_hp])'
        if bm.player_hp <= 0:
            jump .boss2_defeat
        $ bm.reduce_cooldowns()
        jump .boss2_start_logic
    label .boss2_victory:
        hide screen battle_screen
        return
    label .boss2_defeat:
        hide screen battle_screen
        menu:
            'Retry Battle':
                jump battle_boss_ava_butter_phase2

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
