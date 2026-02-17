image kare_idle = Solid("#4444ff", xsize=200, ysize=400)
image kare_attack = Solid("#6666ff", xsize=200, ysize=400)
image kare_hit = Solid("#ff4444", xsize=200, ysize=400)

image chaos_idle = Solid("#440044", xsize=200, ysize=400)
image chaos_attack = Solid("#660066", xsize=200, ysize=400)
image chaos_hit = Solid("#ff0000", xsize=200, ysize=400)

image butter_idle = Solid("#ffcc00", xsize=200, ysize=400)
image butter_attack1 = Solid("#ffff00", xsize=200, ysize=400)
image butter_attack2 = Solid("#ffaa00", xsize=200, ysize=400)
image butter_attack3 = Solid("#ffffff", xsize=200, ysize=400)
image butter_hit = Solid("#ff4444", xsize=200, ysize=400)

image ava_idle = Solid("#ff8888", xsize=200, ysize=400)
image ava_attack = Solid("#ffaaaa", xsize=200, ysize=400)
image ava_hit = Solid("#ff0000", xsize=200, ysize=400)

image lumpi_idle = Solid("#88ff88", xsize=200, ysize=400)
image lumpi_attack = Solid("#aaffaa", xsize=200, ysize=400)
image lumpi_hit = Solid("#ff0000", xsize=200, ysize=400)

image normalbutter_idle = Solid("#ffcc00", xsize=200, ysize=400)
image normalbutter_attack = Solid("#ffff00", xsize=200, ysize=400)
image normalbutter_hit = Solid("#ff4444", xsize=200, ysize=400)

image newenemy_idle = Solid("#555", xsize=200, ysize=400)
image newenemy_attack1 = Solid("#777", xsize=200, ysize=400)
image newenemy_hit = Solid("#ff0000", xsize=200, ysize=400)

image kare_strike_sprite = Solid("#4444ff", xsize=250, ysize=450)
image chaos_strike_sprite = Solid("#440044", xsize=250, ysize=450)
image kare_power_slash_sprite = Solid("#4444ff", xsize=250, ysize=450)
image chaos_power_slash_sprite = Solid("#440044", xsize=250, ysize=450)
image kare_barrier_pose = Solid("#4444ff", xsize=250, ysize=450)
image chaos_barrier_pose = Solid("#440044", xsize=250, ysize=450)
image kare_dodge_pose = Solid("#4444ff", xsize=250, ysize=450)
image chaos_dodge_pose = Solid("#440044", xsize=250, ysize=450)
image kare_meditate_pose = Solid("#4444ff", xsize=250, ysize=450)
image chaos_meditate_pose = Solid("#440044", xsize=250, ysize=450)
image enemy_glare_sprite = Solid("#ffffff", xsize=100, ysize=100)

image card_attack = Solid("#880000", xsize=140, ysize=180)
image card_barrier = Solid("#000088", xsize=140, ysize=180)
image card_dodge = Solid("#888800", xsize=140, ysize=180)
image card_buff = Solid("#008800", xsize=140, ysize=180)
image card_energy = Solid("#008888", xsize=140, ysize=180)
image card_ultimate = Solid("#444444", xsize=140, ysize=180)

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
        def __init__(self, name, damage=0, desc="", animation=None):
            self.name = name
            self.damage = damage
            self.desc = desc
            self.animation = animation

    class Enemy:
        def __init__(self, name, max_hp, sprites, intents):
            self.name = name
            self.hp = max_hp
            self.max_hp = max_hp
            self.sprites = sprites
            self.intents = intents
            self.slots = []
            self.barrier = 0
            self.buffs = []
            self.is_dead = False

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

            self.starting_slots = starting_slots
            self.current_max_slots = starting_slots
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
            self.player_max_energy = 50 if is_chaos else 10
            self.player_energy = self.player_max_energy
            self.full_skill_pool = get_default_skills(is_chaos)
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
            if self.turn_count > 1:
                self.current_max_slots = min(10, self.current_max_slots + 1)

            self.used_skills_this_turn = []
            self.selected_skill = None
            self.selected_intent = None
            self.selected_enemy_index = -1
            self.selected_slot_index = -1

            if self.turn_count >= 1:
                self.skill_exp += 50
                if self.skill_exp >= self.skill_exp_max:
                    self.skill_exp = 0
                    if len(self.player_skills) < len(self.full_skill_pool):
                        new_skill = self.full_skill_pool[len(self.player_skills)]
                        self.player_skills.append(new_skill)

            self.player_energy = min(self.player_max_energy, self.player_energy + 10)

            for enemy in self.enemies:
                if not enemy.is_dead:
                    enemy.slots = [None] * self.current_max_slots
                    num_enemy_slots = max(1, self.current_max_slots // 2)
                    available_indices = list(range(self.current_max_slots))
                    renpy.random.shuffle(available_indices)
                    for _ in range(num_enemy_slots):
                        idx = available_indices.pop()
                        if enemy.intents:
                            enemy.slots[idx] = renpy.random.choice(enemy.intents)

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
                if skill.current_cooldown > 0:
                    skill.current_cooldown -= 1

    def get_default_skills(is_chaos=False):
        if is_chaos:
            return [
                Skill("Chaos Strike", cost=8, damage=15, energy_regen=5, desc="Powerful chaos strike. Regens 5 energy.", animation="player_strike_anim", card_image="card_attack"),
                Skill("Chaos Block", cost=10, damage=20, type="barrier", desc="Gain 20 Block. 1 turn cooldown.", cooldown=1, animation="player_block_anim", card_image="card_barrier"),
                Skill("Chaos Dodge", cost=12, type="dodge", desc="Avoid next attack. Next attack deals double damage. 2 turn cooldown.", cooldown=2, animation="player_dodge_anim", card_image="card_dodge"),
                Skill("Void Slash", cost=15, damage=40, cooldown=2, desc="Devastating slash from the void. 2 turn cooldown.", animation="player_power_slash_anim", card_image="card_attack"),
                Skill("Chaos Wrath", cost=15, damage=10, cooldown=3, type="buff", buff_type="damage", buff_duration=3, desc="Increase damage by 10 for 3 turns.", animation="player_meditate_anim", card_image="card_buff"),
                Skill("Entropy", cost=0, energy_regen=15, desc="Regen 15 energy. Concept of chaos.", animation="player_meditate_anim", card_image="card_energy"),
                Skill("Chaos Blast", cost=20, damage=60, cooldown=3, desc="Concentrated chaos energy. High damage.", animation="player_strike_anim", card_image="card_attack"),
                Skill("Time Warp", cost=10, damage=0, energy_regen=20, cooldown=2, desc="Warp time to regen energy.", animation=None, card_image="card_energy"),
                Skill("Overload", cost=30, damage=100, cooldown=5, desc="Ultimate attack. Huge damage.", animation="player_power_slash_anim", card_image="card_ultimate")
            ]
        return [
            Skill("Strike", cost=2, damage=3, energy_regen=1, desc="Basic attack. Regens 1 energy.", animation="player_strike_anim", card_image="card_attack"),
            Skill("Block", cost=3, damage=5, type="barrier", desc="Gain 5 Block. 1 turn cooldown.", cooldown=1, animation="player_block_anim", card_image="card_barrier"),
            Skill("Dodge", cost=4, type="dodge", desc="Avoid next attack. Next attack deals double damage. 2 turn cooldown.", cooldown=2, animation="player_dodge_anim", card_image="card_dodge"),
            Skill("Power Slash", cost=5, damage=8, cooldown=2, desc="Strong attack. 2 turn cooldown.", animation="player_power_slash_anim", card_image="card_attack"),
            Skill("Meditate", cost=0, energy_regen=4, desc="Regen 4 energy. No damage.", animation="player_meditate_anim", card_image="card_energy")
        ]

screen battle_screen(bm):
    # ── Player stats: top left ──
    vbox:
        xalign 0.05 yalign 0.05
        spacing 5
        xmaximum 400
        text "Chaos: [bm.player_hp]/[bm.player_max_hp]" size 24 color "#ff4444" outlines [(2, "#000")]
        bar value bm.player_hp range bm.player_max_hp xmaximum 300

        hbox:
            spacing 20
            vbox:
                text "Energy: [bm.player_energy]/[bm.player_max_energy]" size 20 color "#44ff44" outlines [(1, "#000")]
                bar value bm.player_energy range bm.player_max_energy xmaximum 200
            if bm.player_barrier > 0:
                vbox:
                    text "Barrier: [bm.player_barrier]" size 20 color "#4444ff" outlines [(1, "#000")]
                    bar value bm.player_barrier range max(20, bm.player_barrier) xmaximum 100

        hbox:
            spacing 5
            for buff in bm.player_buffs:
                frame:
                    background Solid("#660")
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
                    text "[enemy.name]: [enemy.hp]/[enemy.max_hp]" size 20 color "#ff4444" xalign 1.0 outlines [(2, "#000")]
                    bar value enemy.hp range enemy.max_hp xmaximum 250 xalign 1.0
                    if enemy.barrier > 0:
                        text "Barrier: [enemy.barrier]" size 14 color "#4444ff" xalign 1.0
                    hbox:
                        xalign 1.0
                        spacing 5
                        for buff in enemy.buffs:
                            frame:
                                background Solid("#622")
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
                                        action Function(bm.select_intent, action, e_idx, s_idx)
                                        background Solid("#622")
                                        padding (10, 5)
                                        xminimum 80
                                        yminimum 40
                                        vbox:
                                            text "ENEMY" size 12 color "#ffaaaa" xalign 0.5
                                            text "[action.name]" size 16 color "#fff" xalign 0.5
                                elif isinstance(action, Skill):
                                    button:
                                        action Function(bm.select_skill, action)
                                        background Solid("#226")
                                        padding (10, 5)
                                        xminimum 80
                                        yminimum 40
                                        vbox:
                                            text "YOU" size 12 color "#aaaaff" xalign 0.5
                                            text "[action.name]" size 16 color "#fff" xalign 0.5

    # ── Skill description popup: shows when a card is selected.
    # Positioned center-screen but does NOT use a full-screen blocking button overlay.
    # The slots above are still fully clickable through this popup.
    if bm.selected_skill:
        frame:
            background Solid("#000c")
            xalign 0.5 yalign 0.5
            padding (30, 30)
            xminimum 400
            vbox:
                spacing 15
                text "[bm.selected_skill.name]" size 30 color "#fff" xalign 0.5 bold True
                text "Cost: [bm.selected_skill.cost] Energy" size 20 color "#44ff44" xalign 0.5
                if bm.selected_skill.damage > 0:
                    text "Damage: [bm.selected_skill.damage]" size 20 color "#ff4444" xalign 0.5
                text "[bm.selected_skill.desc]" size 18 color "#ccc" xalign 0.5 text_align 0.5
                if bm.selected_skill.cooldown > 0:
                    text "Cooldown: [bm.selected_skill.cooldown] turns" size 18 color "#ff4444" xalign 0.5

                if bm.selected_skill in bm.used_skills_this_turn:
                    $ e_idx, s_idx = bm.get_skill_slot_info(bm.selected_skill)
                    if e_idx != -1:
                        textbutton "REMOVE FROM SLOT":
                            action [Function(bm.remove_from_slot, e_idx, s_idx), SetField(bm, "selected_skill", None)]
                            xalign 0.5
                            background Solid("#622")
                            padding (10, 5)

                $ pass

    # ── Enemy intent popup ──
    if bm.selected_intent:
        frame:
            background Solid("#300c")
            xalign 0.5 yalign 0.5
            padding (30, 30)
            xminimum 400
            vbox:
                spacing 15
                text "[bm.enemies[bm.selected_enemy_index].name] ATTACK: [bm.selected_intent.name]" size 30 color "#ffaaaa" xalign 0.5 bold True
                if bm.selected_intent.damage > 0:
                    text "Projected Damage: [bm.selected_intent.damage]" size 20 color "#ff4444" xalign 0.5
                text "[bm.selected_intent.desc]" size 18 color "#ccc" xalign 0.5 text_align 0.5

                $ pass

    # ── Skill cards: bottom ──
    vbox:
        xalign 0.5 ypos 0.96 yanchor 1.0
        spacing 5

        hbox:
            xalign 0.5
            spacing 4
            text "Next skill: " size 13 color "#3cff00" outlines [(1,"#000")]
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
                    background Frame(card_bg, 4, 4)
                    padding (5, 5)
                    xminimum 140
                    yminimum 180

                    if skill.card_image:
                        add skill.card_image
                    else:
                        vbox:
                            spacing 5
                            xalign 0.5 yalign 0.5
                            text "[skill.name]" size 18 color name_col xalign 0.5 bold True
                            text "Cost: [skill.cost]" size 14 color "#44ff44" xalign 0.5

                    if skill.current_cooldown > 0:
                        text "[skill.current_cooldown]" size 40 color "#ff4444" align (0.5, 0.5) bold True outlines [(2, "#000")]
                    elif skill in bm.used_skills_this_turn:
                        text "USED" size 20 color "#888" align (0.5, 0.5) bold True outlines [(1, "#000")]

    # ── Confirm / Clear buttons ──
    $ has_player_action = any(isinstance(s, Skill) for enemy in bm.enemies for s in enemy.slots)
    textbutton "CONFIRM":
        xalign 0.95 yalign 0.8
        background Solid("#f00")
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

label reset_camera:
    camera:
        perspective False
        gl_depth False
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    return

label generic_battle(bm, is_chaos=False):
    $ bm.initialize_skills(is_chaos)

    label .turn_start:
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

    label .selection_phase:
        $ result = ui.interact()
        if result == "execute":
            jump .execution_phase
        jump .selection_phase

    label .execution_phase:
        hide screen battle_screen
        $ current_slot_idx = 0
        $ bm.dodge_active = False

    label .execution_loop:
        if current_slot_idx >= bm.current_max_slots:
            jump .turn_end

        $ e_idx = 0
    label .interleaved_loop:
        if e_idx >= len(bm.enemies):
            $ current_slot_idx += 1
            jump .execution_loop

        $ enemy = bm.enemies[e_idx]
        if enemy.is_dead:
            $ e_idx += 1
            jump .interleaved_loop

        $ action = enemy.slots[current_slot_idx]
        if action is None:
            $ pass
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)
            $ current_enemy_tag = "enemy_" + str(e_idx)

            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_generic

            if skill.type == "attack":
                $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")
                if bm.dodge_active == "success":
                    $ damage *= 2
                    $ bm.dodge_active = False
                $ bm.take_damage(damage, target="enemy", enemy_idx=e_idx)
                "[skill.name] targets [enemy.name]! Dealt [damage] damage!"
                if enemy.is_dead:
                    "[enemy.name] has been defeated!"
                    $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.add_barrier(skill.damage)
            elif skill.type == "dodge":
                $ bm.dodge_active = True
            elif skill.type == "buff":
                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")

        elif isinstance(action, EnemyIntent):
            $ bm.enemy_intent = action
            $ current_enemy_tag = "enemy_" + str(e_idx)

            if action.animation:
                call expression action.animation pass (bm) from _call_intent_anim_generic
            else:
                call enemy_attack_anim(bm) from _call_intent_anim_default

            if bm.dodge_active:
                "DODGED!"
                $ bm.dodge_active = "success"
            else:
                $ damage = action.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                $ bm.take_damage(damage, target="player")
                "[enemy.name] attacks! Took [damage] damage!"

        if all(e.is_dead for e in bm.enemies):
            jump .victory
        if bm.player_hp <= 0:
            jump .defeat

        $ renpy.pause(0.5)
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, e in enumerate(bm.enemies):
                if not e.is_dead:
                    renpy.show(e.sprites["idle"], tag="enemy_" + str(i))

        $ e_idx += 1
        jump .interleaved_loop

    label .turn_end:
        $ bm.reduce_cooldowns()
        $ bm.update_buffs()
        jump .turn_start

    label .victory:
        hide screen battle_screen
        python:
            for i in range(len(bm.enemies)):
                renpy.hide("enemy_" + str(i))
        return "win"

    label .defeat:
        hide screen battle_screen
        python:
            for i in range(len(bm.enemies)):
                renpy.hide("enemy_" + str(i))
        return "lose"

label player_strike_anim(bm):
    $ p_tag = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
    $ sprite = p_tag + "_strike_sprite"
    $ enemy = bm.enemies[e_idx]
    $ renpy.show(sprite, at_list=[fight_left], tag="player")
    $ renpy.show(enemy.sprites["hit"], at_list=[fight_right], tag=current_enemy_tag)
    show expression sprite as player at fight_left:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.35
    camera:
        ease 0.2 xpos 0.1 ypos -0.1 zoom 1.2
        ease 0.2 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "punch-140236.mp3" volume 1.0
    $ renpy.pause(1.0)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(enemy.sprites["idle"], at_list=[fight_right], tag=current_enemy_tag)
    return

label player_power_slash_anim(bm):
    $ p_tag = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
    $ sprite = p_tag + "_power_slash_sprite"
    $ enemy = bm.enemies[e_idx]
    $ renpy.show(sprite, at_list=[fight_left], tag="player")
    $ renpy.show(enemy.sprites["hit"], at_list=[fight_right], tag=current_enemy_tag)
    show expression sprite as player at fight_left:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.35
    camera:
        ease 0.2 xpos 0.1 ypos -0.1 zoom 1.2
        ease 0.2 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "audio/sword-slash-and-swing-185432.mp3" volume 2.0
    $ renpy.pause(1.0)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ renpy.show(enemy.sprites["idle"], at_list=[fight_right], tag=current_enemy_tag)
    return

label player_block_anim(bm):
    $ p_tag = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
    $ sprite = p_tag + "_barrier_pose"
    show expression sprite as player at fight_left
    play sound "Berserk Clang Sound Effect.mp3" volume 1.0
    "You brace yourself!"
    $ renpy.pause(1.0)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label player_dodge_anim(bm):
    $ p_tag = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
    $ sprite = p_tag + "_dodge_pose"
    show expression sprite as player at fight_left
    "You prepare to dodge! (Avoid next attack & x2 Damage)"
    $ renpy.pause(1.0)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label player_meditate_anim(bm):
    $ p_tag = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
    $ sprite = p_tag + "_meditate_pose"
    show expression sprite as player at fight_left
    "You focus your mind..."
    $ renpy.pause(1.0)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label enemy_butter_slash_anim(bm):
    $ renpy.show("butter_attack1", at_list=[fight_right, enemy_charge_right], tag=current_enemy_tag)
    if bm.dodge_active:
        "MISS!"
    else:
        show expression bm.player_sprites["hit"] as player at fight_left
    play sound "audio/sword-slash-and-swing-185432.mp3" volume 2.0
    $ renpy.pause(0.5)
    return

label enemy_butter_gun_anim(bm):
    $ renpy.show("butter_attack3", at_list=[fight_right], tag=current_enemy_tag)
    if bm.dodge_active:
        "EVADE!"
    else:
        show expression bm.player_sprites["hit"] as player at fight_left
    camera:
        ease 0.1 xpos -0.05 ypos -0.05 zoom 1.1
        ease 0.1 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "audio/single-gunshot-62-hp-37188.mp3" volume 3.0
    $ renpy.pause(0.5)
    return

label enemy_butter_blade_anim(bm):
    $ renpy.show("butter_attack2", at_list=[fight_right, enemy_charge_right], tag=current_enemy_tag)
    if bm.dodge_active:
        "MISS!"
    else:
        show expression bm.player_sprites["hit"] as player at fight_left
    play sound "audio/sword-slash-and-swing-185432.mp3" volume 3.0
    $ renpy.pause(0.5)
    return

label enemy_sword_anim(bm):
    $ enemy = bm.enemies[e_idx]
    $ renpy.show("butter_attack1", at_list=[fight_right, enemy_charge_right], tag=current_enemy_tag)
    if bm.dodge_active:
        "MISS!"
    else:
        show expression bm.player_sprites["hit"] as player at fight_left
    camera:
        ease 0.2 xpos -0.1 ypos -0.1 zoom 1.2
        ease 0.2 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "audio/sword-slash-and-swing-185432.mp3" volume 2.0
    $ renpy.pause(1.0)
    $ renpy.show(enemy.sprites["idle"], at_list=[fight_right], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label enemy_gun_anim(bm):
    $ enemy = bm.enemies[e_idx]
    $ renpy.show("butter_attack3", at_list=[fight_right], tag=current_enemy_tag)
    if bm.dodge_active:
        "EVADE!"
    else:
        show expression bm.player_sprites["hit"] as player at fight_left
    camera:
        ease 0.1 xpos -0.05 ypos -0.05 zoom 1.1
        ease 0.1 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "audio/single-gunshot-62-hp-37188.mp3" volume 2.0
    $ renpy.pause(1.0)
    $ renpy.show(enemy.sprites["idle"], at_list=[fight_right], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label enemy_glare_anim(bm):
    $ renpy.show("enemy_glare_sprite", at_list=[fight_right], tag=current_enemy_tag)
    "Someone glares at you intensely!"
    $ renpy.pause(1.0)
    $ enemy = bm.enemies[e_idx]
    $ renpy.show(enemy.sprites["idle"], at_list=[fight_right], tag=current_enemy_tag)
    return

label enemy_attack_anim(bm):
    $ enemy = bm.enemies[e_idx]
    $ renpy.show(enemy.sprites["attack"], at_list=[fight_right, enemy_charge_right], tag=current_enemy_tag)
    show expression bm.player_sprites["hit"] as player at fight_left
    camera:
        ease 0.2 xpos -0.1 ypos -0.1 zoom 1.2
        ease 0.2 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "Berserk Clang Sound Effect.mp3" volume 1.0
    $ renpy.pause(1.0)
    $ renpy.show(enemy.sprites["idle"], at_list=[fight_right], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    $ p_tag = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
    if enemy.name == "Butter":
        if bm.player_barrier > 0:
            "[p_tag]" "haha i blocked"
        else:
            "[p_tag]" "OWWWWW"
    elif enemy.name == "Lumpi":
        if bm.player_barrier > 0:
            "lumpi" "You think you can block my sword?!"
        else:
            "lumpi" "HYAAA!!"
            "[p_tag]" "OWWWWW"
    return

label lumpi_back_pain_anim(bm):
    "lumpi" "thats it im gonna get serious im locki- ow MY BACK!!!"
    return

label simple_battle_graphics:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show normalbutter_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'normalbutter_idle', 'attack': 'normalbutter_attack', 'hit': 'normalbutter_hit'}
    $ butter_intents = [
        EnemyIntent('Blade Strike', damage=2, desc='Butter strikes with a swift blade.', animation='enemy_butter_blade_anim'),
        EnemyIntent('Gaze', damage=0, desc='Butter is preparing something... wait for it.', animation=None)
    ]
    $ butter = Enemy('Butter', 15, enemy_sprites, butter_intents)
    $ bm = BattleManager(10, [butter], starting_slots=2, player_sprites=player_sprites)
    call generic_battle(bm) from _call_generic_battle_butter
    if _return == 'win':
        jump .player_wins
    else:
        jump .player_loses
    label .player_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera
        hide player
        with fade
        'yay win'
        return
    label .player_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_1
        hide player
        'You were defeated by butter...'
        return

label lumpi_battle:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show lumpi_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpi_idle', 'attack': 'lumpi_attack', 'hit': 'lumpi_hit'}
    $ lumpi_intents = [
        EnemyIntent('Sword Slash', damage=3, desc='Lumpi slashes with his legendary (broken) sword.', animation='enemy_attack_anim'),
        EnemyIntent('Back Pain', damage=0, desc='Lumpi has back pain and skips his turn. This is your chance!', animation='lumpi_back_pain_anim')
    ]
    $ lumpi = Enemy('Lumpi', 25, enemy_sprites, lumpi_intents)
    $ bm = BattleManager(15, [lumpi], starting_slots=4, player_sprites=player_sprites)
    call generic_battle(bm) from _call_generic_battle_lumpi
    if _return == 'win':
        jump .lumpi_wins
    else:
        jump .lumpi_loses
    label .lumpi_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_2
        hide player
        return
    label .lumpi_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_3
        'You were defeated by Lumpi...'
        menu:
            'Retry Battle':
                jump lumpi_battle

label lumpiwheelchair_battle:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show lumpiwheelchair_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpiwheelchair_idle', 'attack': 'lumpiwheelchair_attack', 'hit': 'lumpiwheelchair_hit'}
    $ lumpi_intents = [
        EnemyIntent('Ram', damage=5, desc='Lumpi rams you with his high-speed wheelchair.', animation='enemy_attack_anim'),
        EnemyIntent('Glare', damage=0, desc='Lumpi glares at you intensely. He is getting focused!', animation='enemy_glare_anim')
    ]
    $ lumpi = Enemy('Lumpi (Wheelchair)', 40, enemy_sprites, lumpi_intents)
    $ bm = BattleManager(20, [lumpi], starting_slots=6, player_sprites=player_sprites)
    call generic_battle(bm) from _call_generic_battle_wheelchair
    if _return == 'win':
        jump .lumpiwheelchair_wins
    else:
        jump .lumpiwheelchair_loses
    label .lumpiwheelchair_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_4
        hide player
        return
    label .lumpiwheelchair_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_5
        'lumpi' 'huwhuahuwha i win'
        menu:
            'Retry Battle':
                jump lumpiwheelchair_battle

label newenemy_battle:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show chaos_idle as player at fight_left
    show newenemy_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ enemy_sprites = {'idle': 'newenemy_idle', 'attack': 'newenemy_attack1', 'hit': 'newenemy_hit'}
    $ butter_intents = [
        EnemyIntent('Sword Slash', damage=4, desc='Butter strikes with a swift sword slash.', animation='enemy_butter_slash_anim'),
        EnemyIntent('Gun Shot', damage=6, desc='Butter fires his weapon! high damage.', animation='enemy_butter_gun_anim'),
        EnemyIntent('Blade Strike', damage=4, desc='A powerful blade strike.', animation='enemy_butter_blade_anim')
    ]
    $ butter = Enemy('Butter', 100, enemy_sprites, butter_intents)
    $ bm = BattleManager(50, [butter], starting_slots=8, player_sprites=player_sprites)
    call generic_battle(bm, is_chaos=True) from _call_generic_battle_newenemy
    if _return == 'win':
        jump .newenemy_wins
    else:
        jump .newenemy_loses
    label .newenemy_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_6
        hide player
        return
    label .newenemy_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_7
        menu:
            'Retry Battle':
                jump newenemy_battle

label butter_ava_battle:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ butter_intents = [
        EnemyIntent('Sword Slash', damage=4, desc='Butter strikes with a swift sword slash.', animation='enemy_butter_slash_anim'),
        EnemyIntent('Gun Shot', damage=6, desc='Butter fires his weapon! high damage.', animation='enemy_butter_gun_anim'),
        EnemyIntent('Blade Strike', damage=4, desc='A powerful blade strike.', animation='enemy_butter_blade_anim')
    ]
    $ butter = Enemy('Butter', 500, {'idle': 'butter_idle', 'attack': 'butter_attack1', 'hit': 'butter_hit'}, butter_intents)
    $ ava_intents = [
        EnemyIntent('Stare', damage=0, desc='Ava is watching intently.', animation=None),
        EnemyIntent('Magic Spark', damage=3, desc='A small burst of magic.', animation='enemy_attack_anim')
    ]
    $ ava = Enemy('Ava', 999999, {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}, ava_intents)
    $ bm = BattleManager(500, [butter, ava], starting_slots=2, player_sprites=player_sprites)
    $ bm.initialize_skills(True)
    $ ava_attacked_once = False

    label .turn_start:
        $ bm.prepare_turn()
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    pos = Position(xalign=0.6 + (i * 0.15), yalign=0.5)
                    renpy.show(enemy.sprites["idle"], at_list=[pos], tag=tag)
        show screen battle_screen(bm)
    label .selection_phase:
        $ result = ui.interact()
        if result == 'execute':
            jump .execution_phase
        jump .selection_phase
    label .execution_phase:
        hide screen battle_screen
        $ current_slot_idx = 0
        $ bm.dodge_active = False
    label .execution_loop:
        if current_slot_idx >= bm.current_max_slots:
            jump .ava_turn
        $ e_idx = 0
    label .interleaved_loop:
        if e_idx >= len(bm.enemies):
            $ current_slot_idx += 1
            jump .execution_loop
        $ enemy = bm.enemies[e_idx]
        if enemy.is_dead:
            $ e_idx += 1
            jump .interleaved_loop
        $ action = enemy.slots[current_slot_idx]
        $ current_enemy_tag = "enemy_" + str(e_idx)
        if action is None:
            $ pass
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_ava
            if skill.type == 'attack':
                $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")
                if bm.dodge_active == "success":
                    $ damage *= 2
                    $ bm.dodge_active = False
                $ bm.take_damage(damage, target='enemy', enemy_idx=e_idx)
                "[skill.name] targets [enemy.name]! Dealt [damage] damage!"
                if enemy.is_dead:
                    "[enemy.name] has been defeated!"
                    $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == 'barrier':
                $ bm.add_barrier(skill.damage)
            elif skill.type == 'dodge':
                $ bm.dodge_active = True
            elif skill.type == 'buff':
                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")
        elif isinstance(action, EnemyIntent):
            $ bm.enemy_intent = action
            if action.animation:
                call expression action.animation pass (bm) from _call_intent_anim_ava_butter
            else:
                call enemy_attack_anim(bm) from _call_intent_anim_ava_butter_default
            if bm.dodge_active:
                "DODGED!"
                $ bm.dodge_active = "success"
            else:
                $ damage = action.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                $ bm.take_damage(damage, target='player')
                "[enemy.name] attacks! Took [damage] damage!"
        if all(e.is_dead for e in bm.enemies):
            jump .victory
        if bm.player_hp <= 0:
            jump .defeat
        $ renpy.pause(0.5)
        show expression bm.player_sprites["idle"] as player at fight_left
        $ e_idx += 1
        jump .interleaved_loop
    label .ava_turn:
        if not bm.enemies[0].is_dead and not bm.enemies[1].is_dead:
            $ renpy.show("ava_attack", tag="enemy_1", at_list=[Position(xalign=0.75, yalign=0.5)])
            play sound 'punch-140236.mp3' volume 2.0
            $ renpy.pause(0.5)
            $ bm.take_damage(5, target='enemy', enemy_idx=0)
            'ava attacks butter for 5 damage! (Butter HP: [bm.enemies[0].hp])'
            if not ava_attacked_once:
                $ ava_attacked_once = True
                'butter' 'HOLD ON why are you attacking me?'
                'ava' 'oh wait i forgot you are my ally'
                'ava' 'my bad gang'
            $ renpy.show("ava_idle", tag="enemy_1", at_list=[Position(xalign=0.75, yalign=0.5)])
        if bm.player_hp <= 0:
            jump .defeat
        $ bm.reduce_cooldowns()
        jump .turn_start
    label .victory:
        hide screen battle_screen
        return
    label .defeat:
        hide screen battle_screen
        return

label butter_ava_battle2:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ butter_intents = [
        EnemyIntent('Sword Slash', damage=8, desc='Butter strikes with a swift sword slash.', animation='enemy_butter_slash_anim'),
        EnemyIntent('Gun Shot', damage=12, desc='Butter fires his weapon! high damage.', animation='enemy_butter_gun_anim'),
        EnemyIntent('Blade Strike', damage=8, desc='A powerful blade strike.', animation='enemy_butter_blade_anim')
    ]
    $ butter = Enemy('Butter', 500, {'idle': 'butter_idle', 'attack': 'butter_attack1', 'hit': 'butter_hit'}, butter_intents)
    $ ava_intents = [
        EnemyIntent('Magic Blast', damage=10, desc='Ava unleashes magic.', animation='enemy_attack_anim'),
        EnemyIntent('Heal Butter', damage=0, desc='Ava heals Butter.', animation=None)
    ]
    $ ava = Enemy('Ava', 500, {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}, ava_intents)
    $ bm = BattleManager(500, [butter, ava], starting_slots=10, player_sprites=player_sprites)
    $ bm.initialize_skills(True)

    label .turn_start:
        $ bm.prepare_turn()
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, enemy in enumerate(bm.enemies):
                if not enemy.is_dead:
                    tag = "enemy_" + str(i)
                    pos = Position(xalign=0.6 + (i * 0.15), yalign=0.5)
                    renpy.show(enemy.sprites["idle"], at_list=[pos], tag=tag)
        show screen battle_screen(bm)
    label .selection_phase:
        $ result = ui.interact()
        if result == 'execute':
            jump .execution_phase
        jump .selection_phase
    label .execution_phase:
        hide screen battle_screen
        $ current_slot_idx = 0
        $ bm.dodge_active = False
    label .execution_loop:
        if current_slot_idx >= bm.current_max_slots:
            jump .ava_turn
        $ e_idx = 0
    label .interleaved_loop:
        if e_idx >= len(bm.enemies):
            $ current_slot_idx += 1
            jump .execution_loop
        $ enemy = bm.enemies[e_idx]
        if enemy.is_dead:
            $ e_idx += 1
            jump .interleaved_loop
        $ action = enemy.slots[current_slot_idx]
        $ current_enemy_tag = "enemy_" + str(e_idx)
        if action is None:
            $ pass
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_ava2
            if skill.type == 'attack':
                $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")
                if bm.dodge_active == "success":
                    $ damage *= 2
                    $ bm.dodge_active = False
                $ bm.take_damage(damage, target='enemy', enemy_idx=e_idx)
                "[skill.name] targets [enemy.name]! Dealt [damage] damage!"
                if enemy.is_dead:
                    "[enemy.name] has been defeated!"
                    $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == 'barrier':
                $ bm.add_barrier(skill.damage)
            elif skill.type == 'dodge':
                $ bm.dodge_active = True
            elif skill.type == 'buff':
                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")
        elif isinstance(action, EnemyIntent):
            $ bm.enemy_intent = action
            if action.name == "Heal Butter" and not bm.enemies[0].is_dead:
                $ bm.enemies[0].hp = min(bm.enemies[0].max_hp, bm.enemies[0].hp + 50)
                "Ava heals Butter for 50 HP!"
            else:
                if action.animation:
                    call expression action.animation pass (bm) from _call_intent_anim_ava_butter2
                else:
                    call enemy_attack_anim(bm) from _call_intent_anim_ava_butter_default2
                if bm.dodge_active:
                    "DODGED!"
                    $ bm.dodge_active = "success"
                else:
                    $ damage = action.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                    $ bm.take_damage(damage, target='player')
                    "[enemy.name] attacks! Took [damage] damage!"
        if all(e.is_dead for e in bm.enemies):
            jump .victory
        if bm.player_hp <= 0:
            jump .defeat
        $ renpy.pause(0.5)
        show expression bm.player_sprites["idle"] as player at fight_left
        $ e_idx += 1
        jump .interleaved_loop
    label .ava_turn:
        show ava_attack as enemy_1 at Position(xalign=0.85, yalign=0.5):
            ease 0.2 xpos 0.35
            ease 0.2 xpos 0.85
        play sound 'audio/sword-slash-and-swing-185432.mp3' volume 2.0
        $ renpy.pause(1.0)
        show ava_idle as enemy_1 at Position(xalign=0.85, yalign=0.5)
        $ bm.take_damage(50, target='player')
        'ava attacks for 50 damage! (Your HP: [bm.player_hp])'
        if bm.player_hp <= 0:
            jump .defeat
        $ bm.reduce_cooldowns()
        jump .turn_start
    label .victory:
        hide screen battle_screen
        return
    label .defeat:
        hide screen battle_screen
        menu:
            'Retry Battle':
                jump butter_ava_battle2

label credits:
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
