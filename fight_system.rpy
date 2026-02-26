# BATTLE SYSTEM CORE LOGIC
init python:
    import random

    def get_serious_butter():
        intents = get_enemy_intents("butter")
        sprites = {'idle': 'seriousbutter_idle', 'attack': 'seriousbutter_attack', 'hit': 'seriousbutter_hit'}
        return Enemy('butter', 300, sprites, intents)

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
                Skill("interitus", cost=3, damage=9999999, energy_regen=2, desc="huahuahuaha!!", animation="chaos_normal_anim", card_image="card_chaos_normal"),
                Skill("Embrace", cost=5, damage=15, type="barrier", desc="COME HERE!!", cooldown=0, animation="chaos_block_anim", card_image="card_chaos_block"),
                Skill("Entropy", cost=0, energy_regen=12, type="energy", desc="everything falls apart eventually. might as well use it", animation="chaos_energy_anim", card_image="card_chaos_energy"),
                Skill("Cataclysm", cost=7, damage=18, cooldown=0, desc="oopsie", animation="chaos_hard_anim", card_image="card_chaos_hard"),
                Skill("dissolutum", cost=6, type="dodge", desc="Shift out of reality.", cooldown=0, animation="chaos_dodge_anim", card_image="card_chaos_dodge"),
                Skill("playing rough", cost=6, damage=10, type="buff", buff_type="damage", buff_duration=3, desc="Increases damage by 10 for 3 turns.", animation="chaos_buff_anim"),
                Skill("??????", cost=25, damage=100, cooldown=0, desc="??? ?????", animation="chaos_ultimate_anim", card_image="card_chaos_ultimate")

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
        elif name.lower() == "LAW":
            return [
                EnemyIntent("VERDICT", damage=10, desc="already judged you guilty", animation="serious_butter_normal_anim", type="attack"),
                EnemyIntent("ABSOLUTE RULE", damage=12, desc="law does not bend. neither does I", animation="serious_butter_block_anim", type="barrier", cooldown=3),
                EnemyIntent("ENFORCEMENT", damage=10, buff_type="every law has consequences", buff_duration=3, desc="Increases damage by 10 for 3 turns.", animation="serious_butter_energy_anim", type="buff", cooldown=4),
                EnemyIntent("BINDING JUDGMENT", damage=25, desc="a strike that carries the full weight of every law ever written. it shows.", animation="serious_butter_hard_anim", type="attack", cooldown=0),
                EnemyIntent("DUE PROCESS", desc="proper procedure must be followed. that attack was not it.", animation="serious_butter_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("SENTENCE", damage=80, desc="the verdict has been decided. there is no appeal. there is no negotiation.", animation="serious_butter_ultimate_anim", type="attack", cooldown=6)
            ]
        elif name.lower() == "lumpi":
            return [
                EnemyIntent("slash", damage=5, desc="very powerful sword", animation="lumpi_normal_anim", type="attack"),
                EnemyIntent("Nebula Veil", damage=4, desc="wrap myself in the fabric of space itself. good luck getting through that.", animation="lumpi_block_anim", type="barrier", cooldown=3),
                EnemyIntent("Moonlight Blessing", damage=5, buff_type="damage", buff_duration=3, desc="within my domain, my power is absolute.(Increases damage by 5 for 3 turns.)", animation="lumpi_energy_anim", type="buff", cooldown=4),
                EnemyIntent("Meteor Cleave", damage=8, desc="poweful attack", animation="lumpi_hard_anim", type="attack", cooldown=0),
                EnemyIntent("Spatial Shift", desc="simply moves through space itself.", animation="lumpi_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("Execution", damage=25, desc="very powerful attack.", animation="lumpi_ultimate_anim", type="attack", cooldown=6)
            ]
        elif name.lower() == "lumpi wheelchair":
            return [
                EnemyIntent("Tire Runover", damage=4, desc="Watch your toes.", animation="lumpi_wheelchair_normal_anim", type="attack"),
                EnemyIntent("Reinforced Frame", damage=4, desc="Adds 10 Defense.", animation="lumpi_wheelchair_block_anim", type="barrier", cooldown=3),
                EnemyIntent("Overdrive", damage=4, buff_type="damage", buff_duration=3, desc="Increases damage by 8 for 3 turns.", animation="lumpi_wheelchair_energy_anim", type="buff", cooldown=4),
                EnemyIntent("Turbo Charge", damage=7, desc="High speed impact.", animation="lumpi_wheelchair_hard_anim", type="attack", cooldown=0),
                EnemyIntent("Drift", desc="Will dodge the next attack.", animation="lumpi_wheelchair_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("SUPERSONIC CRASH", damage=15, desc="ULTIMATE: Breaking sound barrier.", animation="lumpi_wheelchair_ultimate_anim", type="attack", cooldown=6)
            ]
        elif name.lower() == "ava":
            return [
                EnemyIntent("poke", damage=6, desc="poke", animation="ava_normal_anim", type="attack"),
                EnemyIntent("ETERNAL RECORD", damage=8, desc="as long as a single soul remembers civilization, I cannot fall. history does not die easily.", animation="ava_block_anim", type="barrier", cooldown=3),
                EnemyIntent("RALLY", damage=15, buff_type="the spirit of a thousand civilizations surge through me. something something power of humanity.", buff_duration=3, desc="Increases damage by 15 for 3 turns.", animation="ava_energy_anim", type="buff", cooldown=4),
                EnemyIntent("CULTURAL IMPACT", damage=15, desc="a strike so significant it will be remembered for generations. probably.", animation="ava_hard_anim", type="attack", cooldown=0),
                EnemyIntent("WRITTEN IN HISTORY", desc="Will dodge the next attack.", animation="ava_dodge_anim", type="dodge", cooldown=3),
                EnemyIntent("END OF AN ERA", damage=60, desc="every civilization must fall before a new one rises. unfortunately for you, you are the civilization right now", animation="ava_ultimate_anim", type="attack", cooldown=6)
            ]
        return []

screen battle_screen(bm):
    $ p_name = "Chaos" if "chaos" in bm.player_sprites["idle"] else "Kare"

    # Settings button in top right
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
        xalign 0.95 yalign 0.05
        spacing 10
        for e_idx, enemy in enumerate(bm.enemies):
            if not enemy.is_dead:
                vbox:
                    spacing 2
                    text "[enemy.name]: [enemy.hp]/[enemy.max_hp]" size 20 color "#747474" xalign 1.0
                    bar value enemy.hp range enemy.max_hp xmaximum 250 xalign 1.0
                    if enemy.barrier > 0:
                        text "Defense: [enemy.barrier]" size 14 color "#6d6d6d" xalign 1.0

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


    # ── Battle slots: top center ──
    vbox:
        xalign 0.5 yalign 0.05
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

    # ── Confirm / Clear buttons ──
    textbutton "CONFIRM":
        xalign 0.95 yalign 0.8
        background Solid("#7e7e7e")
        padding (20, 10)
        text_size 30
        text_color "#fff"
        text_bold True
        text_outlines []
        action [Return("execute"), Play("sound", "audio/stu9-chime-2-356833.mp3", relative_volume=1.5)]

    # ── POPUPS ──
    $ display_skill = None
    if bm.hovered_skill and bm.hovered_skill == bm.selected_skill:
        $ display_skill = bm.hovered_skill
    elif bm.selected_skill and bm.selected_skill in bm.used_skills_this_turn:
        $ display_skill = bm.selected_skill

    if display_skill or bm.selected_intent:
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

        if bm.selected_intent:
            frame:
                background Solid("#8888887f")
                foreground "sketchy_bar_outline"
                xpos 0.85 yalign 0.5
                xanchor 0.5
                padding (30, 30)
                xminimum 400
                vbox:
                    spacing 15
                    text "[bm.enemies[bm.selected_enemy_index].name]'s Intent: [bm.selected_intent.name]" size 30 color "#333" xalign 0.5 bold True
                    if bm.selected_intent.damage > 0:
                        if bm.selected_intent.type == "attack":
                            text "Projected Damage: [bm.selected_intent.damage]" size 20 color "#444" xalign 0.5
                        elif bm.selected_intent.type == "barrier":
                            text "Projected Defense: [bm.selected_intent.damage]" size 20 color "#444" xalign 0.5
                        elif bm.selected_intent.type == "buff":
                            text "Damage Buff: +[bm.selected_intent.damage]" size 20 color "#444" xalign 0.5
                    text "[bm.selected_intent.desc]" size 18 color "#444" xalign 0.5 text_align 0.5

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
                    $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")
                    $ bm.take_damage(damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(damage * 5, character_type="player")
                    "[skill.name] deals [damage] damage to [enemy.name]"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_barrier_generic
                $ bm.add_barrier(skill.damage)
                "You gain [skill.damage] Defense"
            elif skill.type == "dodge":
                $ bm.is_dodged = False
                $ bm.dodge_active = True
            elif skill.type == "buff":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_buff_generic
                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")
                "[skill.name] Damage increased by [skill.damage] for [skill.buff_duration] turns."
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
