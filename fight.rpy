# fight.rpy - Battle System Core

# --- Image Definitions (using real art filenames) ---
image kare_idle = "kare_idle.png"
image kare_attack = "kare_attack.png"
image kare_hit = "kare_hit.png"

image chaos_idle = "chaos_idle.png"
image chaos_attack = "chaos_attack.png"
image chaos_hit = "chaos_hit.png"

image butter_idle = "butter_idle.png"
image butter_attack = "butter_attack.png"
image butter_hit = "butter_hit.png"

image seriousbutter_idle = "seriousbutter_idle.png"
image seriousbutter_attack = "seriousbutter_attack.png"
image seriousbutter_hit = "seriousbutter_hit.png"

image lumpi_idle = "lumpi_idle.png"
image lumpi_attack = "lumpi_attack.png"
image lumpi_hit = "lumpi_hit.png"

image lumpiwheelchair_idle = "lumpiwheelchair_idle.png"
image lumpiwheelchair_attack = "lumpiwheelchair_attack.png"
image lumpiwheelchair_hit = "lumpiwheelchair_hit.png"

image ava_idle = "ava_idle.png"
image ava_attack = "ava_attack.png"
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
    xpos 0.35 ypos 0.5 anchor (0.5, 0.5)

transform fight_right:
    xpos 0.65 ypos 0.5 anchor (0.5, 0.5)

transform enemy_charge_right:
    ease 0.2 xpos 0.5
    ease 0.2 xpos 0.65

init python:
    class Skill:
        def __init__(self, name, cost=0, damage=0, energy_regen=0, cooldown=0, type="attack", desc="", animation=None, card_image=None):
            self.name = name
            self.cost = cost
            self.damage = damage
            self.energy_regen = energy_regen
            self.cooldown = cooldown
            self.current_cooldown = 0
            self.type = type
            self.desc = desc
            self.animation = animation
            self.card_image = card_image

    class EnemyIntent:
        def __init__(self, name, damage=0, desc="", animation=None, type="attack", cooldown=0):
            self.name = name
            self.damage = damage
            self.desc = desc
            self.animation = animation
            self.type = type
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
            self.dodge_active = False
            self.is_dead = False

        @property
        def intents(self):
            return self.full_intent_pool[:self.unlocked_intents_count]

    class BattleManager:
        def __init__(self, player_max_hp, enemies=None, starting_slots=2, player_sprites=None):
            self.player_hp = player_max_hp
            self.player_max_hp = player_max_hp
            self.player_energy = 10
            self.player_max_energy = 10
            self.player_barrier = 0
            self.enemies = enemies or []
            self.player_sprites = player_sprites or {"idle": "kare_idle", "attack": "kare_attack", "hit": "kare_hit"}
            self.current_max_slots = starting_slots
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
            self.dodge_active = False

        def initialize_skills(self, is_chaos):
            self.player_max_energy = 50 if is_chaos else 10
            self.player_energy = self.player_max_energy
            char_name = "chaos" if is_chaos else "kare"
            self.full_skill_pool = get_character_skills(char_name)
            self.player_skills = self.full_skill_pool[:2]
            self.skill_exp = 0

        def select_skill(self, skill, e_idx=-1, s_idx=-1):
            if self.selected_skill == skill and self.selected_slot_index == s_idx and self.selected_enemy_index == e_idx:
                self.selected_skill = None
                self.selected_enemy_index = -1
                self.selected_slot_index = -1
            else:
                self.selected_skill = skill
                self.selected_enemy_index = e_idx
                self.selected_slot_index = s_idx
            self.selected_intent = None

        def select_intent(self, intent, e_idx, s_idx):
            if self.selected_intent == intent and self.selected_enemy_index == e_idx and self.selected_slot_index == s_idx:
                self.selected_intent = None
            else:
                self.selected_intent = intent
                self.selected_enemy_index = e_idx
                self.selected_slot_index = s_idx
            self.selected_skill = None

        def add_to_slot(self, skill, e_idx, s_idx):
            if skill not in self.used_skills_this_turn and self.player_energy >= skill.cost and skill.current_cooldown == 0:
                if self.enemies[e_idx].slots[s_idx] is None:
                    self.enemies[e_idx].slots[s_idx] = skill
                    self.player_energy -= skill.cost
                    self.used_skills_this_turn.append(skill)
                    self.selected_skill = None
                    return True
            return False

        def remove_from_slot(self, e_idx, s_idx):
            action = self.enemies[e_idx].slots[s_idx]
            if isinstance(action, Skill):
                self.player_energy += action.cost
                if action in self.used_skills_this_turn: self.used_skills_this_turn.remove(action)
                self.enemies[e_idx].slots[s_idx] = None

        def clear_queue(self):
            for e_idx, enemy in enumerate(self.enemies):
                for s_idx in range(len(enemy.slots)):
                    if isinstance(enemy.slots[s_idx], Skill):
                        self.remove_from_slot(e_idx, s_idx)

        def prepare_turn(self):
            self.turn_count += 1
            if self.turn_count > 1: self.current_max_slots = min(10, self.current_max_slots + 1)
            self.used_skills_this_turn = []
            self.selected_skill = self.selected_intent = None
            self.player_energy = min(self.player_max_energy, self.player_energy + 2)
            for enemy in self.enemies:
                if not enemy.is_dead:
                    enemy.slots = [None] * self.current_max_slots
                    available = [i for i in enemy.intents if i.current_cooldown == 0] or [enemy.intents[0]]
                    indices = list(range(self.current_max_slots))
                    renpy.random.shuffle(indices)
                    for _ in range(max(1, self.current_max_slots // 2)):
                        if indices: enemy.slots[indices.pop()] = renpy.random.choice(available)

        def take_damage(self, amount, target="player", e_idx=0):
            if target == "player":
                if self.player_barrier > 0:
                    absorbed = min(self.player_barrier, amount)
                    self.player_barrier -= absorbed
                    amount -= absorbed
                self.player_hp = max(0, self.player_hp - amount)
            else:
                enemy = self.enemies[e_idx]
                if enemy.barrier > 0:
                    absorbed = min(enemy.barrier, amount)
                    enemy.barrier -= absorbed
                    amount -= absorbed
                enemy.hp = max(0, enemy.hp - amount)
                if enemy.hp <= 0: enemy.is_dead = True

        def gain_exp(self, amount, character_type="player", e_idx=0):
            if character_type == "player":
                self.skill_exp += amount
                while self.skill_exp >= self.skill_exp_max and len(self.player_skills) < len(self.full_skill_pool):
                    self.skill_exp -= self.skill_exp_max
                    self.player_skills.append(self.full_skill_pool[len(self.player_skills)])
            else:
                e = self.enemies[e_idx]
                e.skill_exp += amount
                while e.skill_exp >= e.skill_exp_max and e.unlocked_intents_count < len(e.full_intent_pool):
                    e.skill_exp -= e.skill_exp_max
                    e.unlocked_intents_count += 1

    def get_character_skills(name):
        if name.lower() == "kare":
            return [
                Skill("Blue Strike", 2, 5, 1, desc="Standard strike.", animation="kare_normal_anim", card_image="card_kare_normal"),
                Skill("Iron Guard", 3, 8, type="barrier", cooldown=1, animation="kare_block_anim", card_image="card_kare_block"),
                Skill("Breathe", 0, energy_regen=5, desc="Recover energy.", animation="kare_energy_anim", card_image="card_kare_energy"),
                Skill("Heavy Slash", 5, 12, cooldown=2, desc="Powerful swing.", animation="kare_hard_anim", card_image="card_kare_hard"),
                Skill("Swift Step", 4, type="dodge", cooldown=2, desc="Prepare to evade.", animation="kare_dodge_anim", card_image="card_kare_dodge"),
                Skill("Heroic Finisher", 15, 40, cooldown=5, desc="ULTIMATE blow.", animation="kare_ultimate_anim", card_image="card_kare_ultimate")
            ]
        elif name.lower() == "chaos":
            return [
                Skill("Chaos Bolt", 3, 8, 2, desc="Chaotic energy.", animation="chaos_normal_anim", card_image="card_chaos_normal"),
                Skill("Void Shield", 5, 15, type="barrier", cooldown=1, animation="chaos_block_anim", card_image="card_chaos_block"),
                Skill("Consume Soul", 0, energy_regen=12, desc="Void energy.", animation="chaos_energy_anim", card_image="card_chaos_energy"),
                Skill("Abyssal Crush", 7, 18, cooldown=2, desc="Gravity crush.", animation="chaos_hard_anim", card_image="card_chaos_hard"),
                Skill("Phase Shift", 6, type="dodge", cooldown=2, desc="Shift reality.", animation="chaos_dodge_anim", card_image="card_chaos_dodge"),
                Skill("Cataclysm", 25, 100, cooldown=5, desc="ULTIMATE end.", animation="chaos_ultimate_anim", card_image="card_chaos_ultimate")
            ]
        return []

    def get_enemy_intents(name):
        if name.lower() == "butter":
            return [
                EnemyIntent("Butter Knife", 4, animation="butter_normal_anim"),
                EnemyIntent("Hard Shell", 6, type="barrier", cooldown=1, animation="butter_block_anim"),
                EnemyIntent("Rest", type="energy", animation="butter_energy_anim"),
                EnemyIntent("Melting Slam", 10, cooldown=1, animation="butter_hard_anim"),
                EnemyIntent("Slippery", type="dodge", cooldown=2, animation="butter_dodge_anim"),
                EnemyIntent("Golden Spread", 30, cooldown=5, animation="butter_ultimate_anim")
            ]
        elif name.lower() == "serious butter":
            return [
                EnemyIntent("Serious Slash", 10, animation="serious_butter_normal_anim"),
                EnemyIntent("Armor of Serious", 20, type="barrier", cooldown=1, animation="serious_butter_block_anim"),
                EnemyIntent("Recuperate", type="energy", animation="serious_butter_energy_anim"),
                EnemyIntent("Decision", 25, cooldown=1, animation="serious_butter_hard_anim"),
                EnemyIntent("Calculated", type="dodge", cooldown=2, animation="serious_butter_dodge_anim"),
                EnemyIntent("MARKET CRASH", 80, cooldown=5, animation="serious_butter_ultimate_anim")
            ]
        elif name.lower() == "lumpi":
            return [
                EnemyIntent("Lump Kick", 3, animation="lumpi_normal_anim"),
                EnemyIntent("Lumpy Guard", 5, type="barrier", cooldown=1, animation="lumpi_block_anim"),
                EnemyIntent("Inhale", type="energy", animation="lumpi_energy_anim"),
                EnemyIntent("Lump Smash", 8, cooldown=1, animation="lumpi_hard_anim"),
                EnemyIntent("Bounce", type="dodge", cooldown=2, animation="lumpi_dodge_anim"),
                EnemyIntent("BIG LUMP", 25, cooldown=5, animation="lumpi_ultimate_anim")
            ]
        elif name.lower() == "lumpi wheelchair":
            return [
                EnemyIntent("Runover", 7, animation="lumpi_wheelchair_normal_anim"),
                EnemyIntent("Reinforced", 12, type="barrier", cooldown=1, animation="lumpi_wheelchair_block_anim"),
                EnemyIntent("Refuel", type="energy", animation="lumpi_wheelchair_energy_anim"),
                EnemyIntent("Turbo", 15, cooldown=1, animation="lumpi_wheelchair_hard_anim"),
                EnemyIntent("Drift", type="dodge", cooldown=2, animation="lumpi_wheelchair_dodge_anim"),
                EnemyIntent("SUPERSONIC", 50, cooldown=5, animation="lumpi_wheelchair_ultimate_anim")
            ]
        elif name.lower() == "ava":
            return [
                EnemyIntent("Magic Spark", 6, animation="ava_normal_anim"),
                EnemyIntent("Mana Veil", 10, type="barrier", cooldown=1, animation="ava_block_anim"),
                EnemyIntent("Meditate", type="energy", animation="ava_energy_anim"),
                EnemyIntent("Arcane Blast", 15, cooldown=1, animation="ava_hard_anim"),
                EnemyIntent("Blink", type="dodge", cooldown=2, animation="ava_dodge_anim"),
                EnemyIntent("COSMIC BURST", 60, cooldown=5, animation="ava_ultimate_anim")
            ]
        return []

screen battle_screen(bm):
    $ p_name = "Chaos" if "chaos" in bm.player_sprites["idle"] else "Kare"
    # --- Monochrome Bar Styles ---
    style_prefix "sketchy"

    vbox:
        xalign 0.05 yalign 0.05 spacing 5
        text "[p_name]: [bm.player_hp]/[bm.player_max_hp]" size 24 color "#ffffff" outlines [(2, "#000000")]
        bar value bm.player_hp range bm.player_max_hp xmaximum 300
        hbox:
            spacing 20
            vbox:
                text "Energy: [bm.player_energy]/[bm.player_max_energy]" size 20 color "#eeeeee"
                bar value bm.player_energy range bm.player_max_energy xmaximum 200
            if bm.player_barrier > 0:
                vbox:
                    text "Barrier: [bm.player_barrier]" size 20 color "#cccccc"
                    bar value bm.player_barrier range max(20, bm.player_barrier) xmaximum 100
    vbox:
        xalign 0.95 yalign 0.05 spacing 10
        for e in bm.enemies:
            if not e.is_dead:
                vbox:
                    spacing 2
                    text "[e.name]: [e.hp]/[e.max_hp]" size 20 color "#ffffff" xalign 1.0 outlines [(2, "#000000")]
                    bar value e.hp range e.max_hp xmaximum 250 xalign 1.0
                    hbox:
                        xalign 1.0 spacing 4
                        text "Unlock: " size 12 color "#bbbbbb"
                        bar value e.skill_exp range e.skill_exp_max xmaximum 150 ysize 6 yalign 0.5
    vbox:
        xalign 0.5 yalign 0.05 spacing 10
        for e_idx, e in enumerate(bm.enemies):
            if not e.is_dead:
                hbox:
                    spacing 10 xalign 0.5
                    for s_idx in range(bm.current_max_slots):
                        $ action = e.slots[s_idx]
                        if action is None:
                            button:
                                action If(bm.selected_skill, Function(bm.add_to_slot, bm.selected_skill, e_idx, s_idx))
                                background Frame(Solid("#333333"), 2, 2) padding (10, 5) xminimum 80 yminimum 40
                                text "EMPTY" size 16 color "#555555" xalign 0.5
                        elif isinstance(action, EnemyIntent):
                            button:
                                action Function(bm.select_intent, action, e_idx, s_idx)
                                background Frame(Solid("#111111"), 2, 2) padding (10, 5) xminimum 80 yminimum 40
                                vbox:
                                    text "ENEMY" size 12 color "#aaaaaa" xalign 0.5
                                    text "[action.name]" size 16 color "#ffffff" xalign 0.5
                        else:
                            button:
                                action Function(bm.select_skill, action, e_idx, s_idx)
                                background Frame(Solid("#555555"), 2, 2) padding (10, 5) xminimum 80 yminimum 40
                                vbox:
                                    text "YOU" size 12 color "#dddddd" xalign 0.5
                                    text "[action.name]" size 16 color "#ffffff" xalign 0.5
    vbox:
        xalign 0.5 ypos 0.98 yanchor 1.0 spacing 5
        hbox:
            xalign 0.5 spacing 4
            text "Next skill: " size 13 color "#ffffff"
            bar value bm.skill_exp range bm.skill_exp_max xmaximum 600 ysize 8 yalign 0.5
        hbox:
            spacing 15 xalign 0.5
            for s in bm.player_skills:
                $ can = s.current_cooldown == 0 and s not in bm.used_skills_this_turn
                button:
                    action Function(bm.select_skill, s) sensitive can
                    background (Solid("#888888") if bm.selected_skill == s else (Solid("#333333cc") if can else Solid("#111111cc")))
                    xsize 140 ysize 180
                    if s.card_image:
                        add s.card_image
                    if s.current_cooldown > 0:
                        text "[s.current_cooldown]" size 40 color "#ffffff" xalign 0.5 yalign 0.5 outlines [(2, "#000")]
                    elif s in bm.used_skills_this_turn:
                        text "USED" size 20 color "#444444" xalign 0.5 yalign 0.5
    textbutton "CONFIRM":
        xalign 0.95 yalign 0.8 background Solid("#ffffff") padding (20, 10)
        text_size 30 text_color "#000000" text_bold True action Return("execute")
        activate_sound Audio("audio/confirm.mp3", volume=0.5)
    if bm.selected_skill or bm.selected_intent:
        frame:
            background Solid("#000000aa") xalign 0.5 yalign 0.5 padding (30, 30) xminimum 400
            vbox:
                spacing 15 xalign 0.5
                if bm.selected_skill:
                    if bm.selected_skill.card_image:
                        add bm.selected_skill.card_image xalign 0.5
                    text "[bm.selected_skill.name]" size 30 color "#ffffff" bold True
                    text "Cost: [bm.selected_skill.cost] Energy" size 20 color "#dddddd"
                    if bm.selected_skill.damage > 0:
                        text "Damage: [bm.selected_skill.damage]" size 20 color "#ffffff"
                    text "[bm.selected_skill.desc]" size 18 color "#bbbbbb" text_align 0.5
                    if bm.selected_skill in bm.used_skills_this_turn:
                        textbutton "REMOVE":
                            action [Function(bm.remove_from_slot, bm.selected_enemy_index, bm.selected_slot_index), SetField(bm, "selected_skill", None)]
                            background Solid("#ffffff") padding (10, 5) text_color "#000"
                else:
                    text "Enemy: [bm.selected_intent.name]" size 30 color "#ffffff" bold True
                    if bm.selected_intent.damage > 0:
                        text "Damage: [bm.selected_intent.damage]" size 20 color "#ffffff"
                    text "[bm.selected_intent.desc]" size 18 color "#bbbbbb" text_align 0.5

# Define sketchy bar style
style sketchy_bar:
    left_bar Solid("#ffffff")
    right_bar Solid("#333333")
    ysize 15

style sketchy_vbar:
    top_bar Solid("#333333")
    bottom_bar Solid("#ffffff")
    xsize 15

label battle_reset_camera:
    camera:
        perspective False gl_depth False
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    return

label battle_engine(bm, is_chaos=False, is_boss1=False):
    $ bm.initialize_skills(is_chaos)
    $ ava_attacked_once = False
    label .start:
        $ bm.prepare_turn()
        show expression bm.player_sprites["idle"] as player at fight_left
        python:
            for i, e in enumerate(bm.enemies):
                if not e.is_dead: renpy.show(e.sprites["idle"], at_list=[Position(xalign=0.6+(i*0.15), yalign=0.5)], tag="enemy_"+str(i))
                else: renpy.hide("enemy_"+str(i))
        show screen battle_screen(bm)
        $ ui.interact()
        hide screen battle_screen
        $ current_slot = 0
        $ bm.dodge_active = False
    label .exec_loop:
        if current_slot >= bm.current_max_slots:
            if is_boss1 and not bm.enemies[0].is_dead and not bm.enemies[1].is_dead and not ava_attacked_once:
                $ ava_attacked_once = True
                show ava_attack as enemy_1 at Position(xalign=0.75, yalign=0.5)
                play sound "punch-140236.mp3"
                $ bm.take_damage(5, target="enemy", e_idx=0)
                "ava attacks butter for 5 damage!"
                "butter" "HOLD ON why are you attacking me?"
                "ava" "my bad gang"
                show ava_idle as enemy_1 at Position(xalign=0.75, yalign=0.5)
            python:
                for s in bm.player_skills:
                    if s.current_cooldown > 0: s.current_cooldown -= 1
                for e in bm.enemies:
                    for i in e.full_intent_pool:
                        if i.current_cooldown > 0: i.current_cooldown -= 1
            jump .start
        $ e_idx = 0
    label .res_loop:
        if e_idx >= len(bm.enemies):
            $ current_slot += 1
            jump .exec_loop
        $ enemy = bm.enemies[e_idx]
        if enemy.is_dead:
            $ e_idx += 1
            jump .res_loop
        $ action = enemy.slots[current_slot]
        $ current_enemy_tag = "enemy_" + str(e_idx)
        if isinstance(action, Skill):
            $ action.current_cooldown = action.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + action.energy_regen)
            if action.animation:
                call expression action.animation pass (bm)
            if action.type == "attack":
                if enemy.dodge_active:
                    "[enemy.name] dodged!"
                    $ enemy.dodge_active = False
                else:
                    $ bm.take_damage(action.damage, target="enemy", e_idx=e_idx)
                    $ bm.gain_exp(action.damage * 5)
                    "[action.name] deals [action.damage] damage!"
            elif action.type == "barrier":
                $ bm.player_barrier += action.damage
                "Gained [action.damage] Block!"
            elif action.type == "dodge":
                $ bm.dodge_active = True
                "Preparing to dodge!"
        elif isinstance(action, EnemyIntent):
            $ action.current_cooldown = action.cooldown
            if action.animation:
                call expression action.animation pass (bm)
            if action.type == "attack":
                if bm.dodge_active:
                    "DODGED!"
                    $ bm.dodge_active = False
                else:
                    $ bm.take_damage(action.damage)
                    $ bm.gain_exp(action.damage * 5, "enemy", e_idx)
                    "[enemy.name] deals [action.damage] damage!"
            elif action.type == "barrier":
                $ enemy.barrier += action.damage
                "[enemy.name] gained Block!"
            elif action.type == "dodge":
                $ enemy.dodge_active = True
                "[enemy.name] will dodge!"
        if all(e.is_dead for e in bm.enemies):
            return "win"
        if bm.player_hp <= 0:
            return "lose"
        if isinstance(action, (Skill, EnemyIntent)):
            $ renpy.pause(0.5)
        $ e_idx += 1
        jump .res_loop

# --- Animations ---
label kare_normal_anim(bm):
    show kare_normal_sprite as player at fight_left:
        ease 0.1 xpos 0.4
        ease 0.1 xpos 0.35
    play sound "punch-140236.mp3"
    $ renpy.pause(0.5)
    show kare_idle as player at fight_left
    return

label kare_hard_anim(bm):
    show kare_hard_sprite as player at fight_left:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.35
    play sound "audio/sword-slash-and-swing-185432.mp3"
    $ renpy.pause(0.8)
    show kare_idle as player at fight_left
    return

label kare_block_anim(bm):
    show kare_block_sprite as player at fight_left
    play sound "Berserk Clang Sound Effect.mp3"
    $ renpy.pause(0.5)
    show kare_idle as player at fight_left
    return

label kare_dodge_anim(bm):
    show kare_dodge_sprite as player at fight_left:
        ease 0.2 xpos 0.25
        ease 0.2 xpos 0.35
    $ renpy.pause(0.5)
    show kare_idle as player at fight_left
    return

label kare_energy_anim(bm):
    show kare_energy_sprite as player at fight_left
    play sound "audio/item-pickup-37089.mp3"
    $ renpy.pause(0.5)
    show kare_idle as player at fight_left
    return

label kare_ultimate_anim(bm):
    show kare_ultimate_sprite as player at fight_left:
        ease 0.3 xpos 0.6
        ease 0.3 xpos 0.35
    play sound "audio/sword-slash-and-swing-185432.mp3"
    $ renpy.pause(1.2)
    show kare_idle as player at fight_left
    return

# (Simplified other animations follow the same pattern)
label chaos_normal_anim(bm):
    show chaos_normal_sprite as player at fight_left
    play sound "punch-140236.mp3"
    $ renpy.pause(0.5)
    show chaos_idle as player at fight_left
    return
label chaos_hard_anim(bm):
    show chaos_hard_sprite as player at fight_left
    play sound "audio/sword-slash-and-swing-185432.mp3"
    $ renpy.pause(0.8)
    show chaos_idle as player at fight_left
    return
label chaos_block_anim(bm):
    show chaos_block_sprite as player at fight_left
    play sound "Berserk Clang Sound Effect.mp3"
    $ renpy.pause(0.5)
    show chaos_idle as player at fight_left
    return
label chaos_dodge_anim(bm):
    show chaos_dodge_sprite as player at fight_left
    $ renpy.pause(0.5)
    show chaos_idle as player at fight_left
    return
label chaos_energy_anim(bm):
    show chaos_energy_sprite as player at fight_left
    $ renpy.pause(0.5)
    show chaos_idle as player at fight_left
    return
label chaos_ultimate_anim(bm):
    show chaos_ultimate_sprite as player at fight_left
    play sound "audio/magic-spark.mp3"
    $ renpy.pause(1.2)
    show chaos_idle as player at fight_left
    return

# --- Enemy Animation Fallbacks ---
label butter_normal_anim(bm):
    $ renpy.show("butter_normal_sprite", tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    play sound "audio/sword-slash-and-swing-185432.mp3"
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label butter_hard_anim(bm):
    $ renpy.show("butter_hard_sprite", tag=current_enemy_tag, at_list=[fight_right, enemy_charge_right])
    $ renpy.pause(0.8)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label butter_block_anim(bm):
    $ renpy.show("butter_block_sprite", tag=current_enemy_tag, at_list=[fight_right])
    play sound "Berserk Clang Sound Effect.mp3"
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label butter_dodge_anim(bm):
    $ renpy.show("butter_dodge_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label butter_ultimate_anim(bm):
    $ renpy.show("butter_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right])
    play sound "audio/single-gunshot-62-hp-37188.mp3"
    $ renpy.pause(1.2)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label butter_energy_anim(bm):
    $ renpy.show("butter_energy_sprite", tag=current_enemy_tag, at_list=[fight_right])
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

# (And so on for other enemies...)
label serious_butter_normal_anim(bm):
    $ renpy.show("serious_butter_normal_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label serious_butter_hard_anim(bm):
    $ renpy.show("serious_butter_hard_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.8)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label serious_butter_block_anim(bm):
    $ renpy.show("serious_butter_block_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label serious_butter_dodge_anim(bm):
    $ renpy.show("serious_butter_dodge_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label serious_butter_ultimate_anim(bm):
    $ renpy.show("serious_butter_ultimate_sprite", tag=current_enemy_tag)
    $ renpy.pause(1.2)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label serious_butter_energy_anim(bm):
    $ renpy.show("serious_butter_energy_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label lumpi_normal_anim(bm):
    $ renpy.show("lumpi_normal_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label lumpi_hard_anim(bm):
    $ renpy.show("lumpi_hard_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.8)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label lumpi_block_anim(bm):
    $ renpy.show("lumpi_block_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label lumpi_dodge_anim(bm):
    $ renpy.show("lumpi_dodge_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label lumpi_ultimate_anim(bm):
    $ renpy.show("lumpi_ultimate_sprite", tag=current_enemy_tag)
    $ renpy.pause(1.2)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label lumpi_energy_anim(bm):
    $ renpy.show("lumpi_energy_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label lumpi_wheelchair_normal_anim(bm):
    $ renpy.show("lumpi_wheelchair_normal_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label lumpi_wheelchair_hard_anim(bm):
    $ renpy.show("lumpi_wheelchair_hard_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.8)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label lumpi_wheelchair_block_anim(bm):
    $ renpy.show("lumpi_wheelchair_block_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label lumpi_wheelchair_dodge_anim(bm):
    $ renpy.show("lumpi_wheelchair_dodge_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label lumpi_wheelchair_ultimate_anim(bm):
    $ renpy.show("lumpi_wheelchair_ultimate_sprite", tag=current_enemy_tag)
    $ renpy.pause(1.2)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label lumpi_wheelchair_energy_anim(bm):
    $ renpy.show("lumpi_wheelchair_energy_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

label ava_normal_anim(bm):
    $ renpy.show("ava_normal_sprite", tag=current_enemy_tag)
    play sound "audio/magic-spark.mp3"
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label ava_hard_anim(bm):
    $ renpy.show("ava_hard_sprite", tag=current_enemy_tag)
    play sound "audio/magic-spark.mp3"
    $ renpy.pause(0.8)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label ava_block_anim(bm):
    $ renpy.show("ava_block_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label ava_dodge_anim(bm):
    $ renpy.show("ava_dodge_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label ava_ultimate_anim(bm):
    $ renpy.show("ava_ultimate_sprite", tag=current_enemy_tag)
    play sound "audio/magic-spark.mp3"
    $ renpy.pause(1.2)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return
label ava_energy_anim(bm):
    $ renpy.show("ava_energy_sprite", tag=current_enemy_tag)
    $ renpy.pause(0.5)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    return

# --- Specific Battle Wrappers ---
label battle_butter_simple:
    scene bg with fade
    $ sprites = {'idle': 'butter_idle', 'attack': 'butter_attack', 'hit': 'butter_hit'}
    $ e = Enemy('Butter', 15, sprites, get_enemy_intents("butter"))
    $ bm = BattleManager(10, [e])
    call battle_engine(bm) from _call_battle_engine_butter_1
    return

label battle_lumpi_standard:
    scene bg with fade
    $ sprites = {'idle': 'lumpi_idle', 'attack': 'lumpi_attack', 'hit': 'lumpi_hit'}
    $ e = Enemy('Lumpi', 25, sprites, get_enemy_intents("lumpi"))
    $ bm = BattleManager(15, [e], starting_slots=4)
    call battle_engine(bm) from _call_battle_engine_lumpi_1
    return

label battle_lumpi_wheelchair:
    scene bg with fade
    $ sprites = {'idle': 'lumpiwheelchair_idle', 'attack': 'lumpiwheelchair_attack', 'hit': 'lumpiwheelchair_hit'}
    $ e = Enemy('Lumpi (Wheelchair)', 40, sprites, get_enemy_intents("lumpi wheelchair"))
    $ bm = BattleManager(20, [e], starting_slots=6)
    call battle_engine(bm) from _call_battle_engine_wheelchair_1
    return

label battle_serious_butter:
    scene bg with fade
    $ sprites = {'idle': 'seriousbutter_idle', 'attack': 'seriousbutter_attack', 'hit': 'seriousbutter_hit'}
    $ e = Enemy('Serious Butter', 100, sprites, get_enemy_intents("serious butter"))
    $ bm = BattleManager(50, [e], starting_slots=8)
    call battle_engine(bm) from _call_battle_engine_serious_1
    return

label battle_boss_ava_butter:
    scene bg with fade
    $ b_sprites = {'idle': 'butter_idle', 'attack': 'butter_attack', 'hit': 'butter_hit'}
    $ a_sprites = {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}
    $ butter = Enemy('Butter', 500, b_sprites, get_enemy_intents("butter"))
    $ ava = Enemy('Ava', 999999, a_sprites, get_enemy_intents("ava"))
    $ bm = BattleManager(500, [butter, ava], starting_slots=2, player_sprites={'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'})
    call battle_engine(bm, is_chaos=True, is_boss1=True) from _call_battle_engine_boss1_1
    return

label battle_boss_ava_butter_phase2:
    scene bg with fade
    $ b_sprites = {'idle': 'butter_idle', 'attack': 'butter_attack', 'hit': 'butter_hit'}
    $ a_sprites = {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}
    $ butter = Enemy('Serious Butter', 500, b_sprites, get_enemy_intents("serious butter"))
    $ ava = Enemy('Ava', 500, a_sprites, get_enemy_intents("ava"))
    $ bm = BattleManager(500, [butter, ava], starting_slots=10, player_sprites={'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'})
    call battle_engine(bm, is_chaos=True) from _call_battle_engine_boss2_1
    return

label battle_credits:
    scene black with fade
    show screen scrolling_credits
    $ renpy.pause(25.0, hard=True)
    hide screen scrolling_credits
    return

screen scrolling_credits:
    add Solid("#ffffff")
    vbox:
        xalign 0.5 spacing 40 at credits_scroll
        text "Thank you for playing!" size 40 xalign 0.5
        null height 200
        text "THE END" size 60 xalign 0.5 bold True
        null height 700
        text "this game probably wasted an hour of your life" size 40 xalign 0.5
        null height 200

transform credits_scroll:
    ypos 1080
    linear 30.0 ypos -2000
