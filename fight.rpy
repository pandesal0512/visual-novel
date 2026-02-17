init python:
    import random

    class Skill:
        def __init__(self, name, cost=0, damage=0, mana_regen=0, cooldown=0, type="attack", desc="", animation=None):
            self.name = name
            self.cost = cost
            self.damage = damage
            self.mana_regen = mana_regen
            self.cooldown = cooldown
            self.current_cooldown = 0
            self.type = type # "attack", "barrier", "dodge"
            self.desc = desc
            self.animation = animation # Label to call for animation

    class EnemyIntent:
        def __init__(self, name, damage=0, desc="", animation=None):
            self.name = name
            self.damage = damage
            self.desc = desc
            self.animation = animation

    class BattleManager:
        def __init__(self, player_max_hp, enemy_max_hp, enemy_name, starting_slots=2, player_sprites=None, enemy_sprites=None):
            self.player_hp = player_max_hp
            self.player_max_hp = player_max_hp
            self.player_mana = 10
            self.player_max_mana = 10
            self.player_barrier = 0
            self.enemy_hp = enemy_max_hp
            self.enemy_max_hp = enemy_max_hp
            self.enemy_name = enemy_name

            self.player_sprites = player_sprites or {"idle": "kare_idle", "attack": "kare_attack", "hit": "kare_hit"}
            self.enemy_sprites = enemy_sprites or {"idle": "enemy_idle", "attack": "enemy_attack", "hit": "enemy_hit"}

            self.starting_slots = starting_slots
            self.current_max_slots = starting_slots
            self.slots = [None] * self.current_max_slots # None, Skill, or EnemyIntent

            self.enemy_intents = []
            self.dodge_active = False
            self.player_skills = []
            self.used_skills_this_turn = set()
            self.turn_count = 0
            self.selected_skill = None
            self.selected_intent = None
            self.selected_slot_index = -1

        def select_skill(self, skill):
            if self.selected_skill == skill:
                self.selected_skill = None
            else:
                self.selected_skill = skill
            self.selected_intent = None
            self.selected_slot_index = -1

        def select_intent(self, intent, index):
            if self.selected_intent == intent and self.selected_slot_index == index:
                self.selected_intent = None
                self.selected_slot_index = -1
            else:
                self.selected_intent = intent
                self.selected_slot_index = index
            self.selected_skill = None

        def add_to_slot(self, skill, index):
            if skill in self.used_skills_this_turn:
                return False
            if self.player_mana >= skill.cost and skill.current_cooldown == 0:
                if self.slots[index] is None:
                    self.slots[index] = skill
                    self.player_mana -= skill.cost
                    self.used_skills_this_turn.add(skill)
                    self.selected_skill = None # Close description after putting in slot
                    return True
            return False

        def remove_from_slot(self, index):
            action = self.slots[index]
            if isinstance(action, Skill):
                self.player_mana += action.cost
                self.used_skills_this_turn.remove(action)
                self.slots[index] = None

        def clear_queue(self):
            for i in range(len(self.slots)):
                if isinstance(self.slots[i], Skill):
                    self.remove_from_slot(i)

        def get_skill_slot_index(self, skill):
            for idx, s in enumerate(self.slots):
                if s == skill:
                    return idx
            return -1

        def prepare_turn(self):
            # Increase slots each turn
            if self.turn_count > 1:
                self.current_max_slots = min(10, self.current_max_slots + 1)

            self.slots = [None] * self.current_max_slots
            self.used_skills_this_turn = set()
            self.selected_skill = None
            self.selected_intent = None
            self.selected_slot_index = -1
            self.player_mana = min(self.player_max_mana, self.player_mana + 2)

            # Fill enemy slots (roughly half)
            num_enemy_slots = max(1, self.current_max_slots // 2)
            available_indices = list(range(self.current_max_slots))
            renpy.random.shuffle(available_indices)

            for _ in range(num_enemy_slots):
                idx = available_indices.pop()
                if self.enemy_intents:
                    self.slots[idx] = renpy.random.choice(self.enemy_intents)

        def take_damage(self, amount, target="player"):
            if target == "player":
                if self.player_barrier > 0:
                    absorbed = min(self.player_barrier, amount)
                    self.player_barrier -= absorbed
                    amount -= absorbed

                self.player_hp = max(0, self.player_hp - amount)
            else:
                self.enemy_hp = max(0, self.enemy_hp - amount)

        def heal_player(self, amount):
            self.player_hp = min(self.player_max_hp, self.player_hp + amount)

        def add_barrier(self, amount):
            self.player_barrier += amount

        def reduce_cooldowns(self):
            for skill in self.player_skills:
                if skill.current_cooldown > 0:
                    skill.current_cooldown -= 1

    def get_default_skills():
        return [
            Skill("Strike", cost=2, damage=3, mana_regen=1, desc="Basic attack. Regens 1 mana.", animation="player_strike_anim"),
            Skill("Power Slash", cost=5, damage=8, cooldown=2, desc="Strong attack. 2 turn cooldown.", animation="player_power_slash_anim"),
            Skill("Barrier", cost=3, type="barrier", desc="Gain 5 Barrier. 1 turn cooldown.", cooldown=1, animation="player_barrier_anim"),
            Skill("Dodge", cost=4, type="dodge", desc="Next attack deals double damage. 2 turn cooldown.", cooldown=2, animation="player_dodge_anim"),
            Skill("Meditate", cost=0, mana_regen=4, desc="Regen 4 mana. No damage.", animation="player_meditate_anim")
        ]

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

# Image definitions for KARE
image kare_idle:
    "kare_idle.png"
    pause 1.0
    "kare_idle.png"
    pause 1.0
    repeat

image kare_attack:
    "kare_attack1.png"
    pause 0.3
    "kare_attack2.png"
    pause 0.7
    repeat

image kare_hit:
    "kare_hit.png"
    pause 1.0
    repeat

# Image definitions for NORMAL BUTTER
image normalbutter_idle:
    "butter_idle.png"
    pause 1.0
    "butter_idle.png"
    pause 1.0
    repeat

image normalbutter_attack:
    "butter_attack1.png"
    pause 0.3
    "butter_attack2.png"
    pause 0.7
    repeat

image normalbutter_hit:
    "butter_hit.png"
    pause 1.0
    repeat

# Battle UI Screen
screen battle_screen(bm):
    # Player Stats
    vbox:
        xalign 0.05 yalign 0.05
        spacing 5
        xmaximum 400
        text "You: [bm.player_hp]/[bm.player_max_hp]" size 24 color "#ff4444" outlines [(2, "#000")]
        bar value bm.player_hp range bm.player_max_hp xmaximum 300

        hbox:
            spacing 20
            vbox:
                text "Mana: [bm.player_mana]/[bm.player_max_mana]" size 20 color "#44ff44" outlines [(1, "#000")]
                bar value bm.player_mana range bm.player_max_mana xmaximum 200
            if bm.player_barrier > 0:
                vbox:
                    text "Barrier: [bm.player_barrier]" size 20 color "#4444ff" outlines [(1, "#000")]
                    bar value bm.player_barrier range max(20, bm.player_barrier) xmaximum 100

    # Enemy Stats
    vbox:
        xalign 0.95 yalign 0.05
        spacing 5
        xmaximum 400
        text "[bm.enemy_name]: [bm.enemy_hp]/[bm.enemy_max_hp]" size 24 color "#ff4444" xalign 1.0 outlines [(2, "#000")]
        bar value bm.enemy_hp range bm.enemy_max_hp xmaximum 300 xalign 1.0

    # Slots
    frame:
        background Solid("#0006")
        xalign 0.5 yalign 0.15
        padding (15, 15)
        vbox:
            spacing 5
            text "Battle Slots (Select a card below, then click an empty slot):" size 16 color "#aaa" xalign 0.5
            hbox:
                spacing 10
                xalign 0.5
                for i in range(bm.current_max_slots):
                    $ action = bm.slots[i]
                    if action is None:
                        $ can_add = bm.selected_skill is not None and bm.player_mana >= bm.selected_skill.cost
                        button:
                            action If(can_add, Function(bm.add_to_slot, bm.selected_skill, i))
                            background Solid("#333")
                            padding (10, 5)
                            xminimum 80
                            yminimum 40
                            text "EMPTY" size 16 color "#555" xalign 0.5
                    elif isinstance(action, EnemyIntent):
                        button:
                            action Function(bm.select_intent, action, i)
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

    # Description Popup (if a skill is selected)
    if bm.selected_skill:
        frame:
            background Solid("#000c")
            xalign 0.5 yalign 0.5
            padding (30, 30)
            xminimum 400
            vbox:
                spacing 15
                text "[bm.selected_skill.name]" size 30 color "#fff" xalign 0.5 bold True
                text "Cost: [bm.selected_skill.cost] Mana" size 20 color "#44ff44" xalign 0.5
                if bm.selected_skill.damage > 0:
                    text "Damage: [bm.selected_skill.damage]" size 20 color "#ff4444" xalign 0.5
                text "[bm.selected_skill.desc]" size 18 color "#ccc" xalign 0.5 text_align 0.5
                if bm.selected_skill.cooldown > 0:
                    text "Cooldown: [bm.selected_skill.cooldown] turns" size 18 color "#ff4444" xalign 0.5

                if bm.selected_skill in bm.used_skills_this_turn:
                    $ slot_idx = bm.get_skill_slot_index(bm.selected_skill)
                    textbutton "REMOVE FROM SLOT":
                        action [Function(bm.remove_from_slot, slot_idx), SetField(bm, "selected_skill", None)]
                        xalign 0.5
                        background Solid("#622")
                        padding (10, 5)

                if bm.selected_skill in bm.used_skills_this_turn:
                    textbutton "CLOSE":
                        action SetField(bm, "selected_skill", None)
                        xalign 0.5
                        background Solid("#444")
                        padding (10, 5)

    # Enemy Intent Popup
    if bm.selected_intent:
        frame:
            background Solid("#300c")
            xalign 0.5 yalign 0.5
            padding (30, 30)
            xminimum 400
            vbox:
                spacing 15
                text "ENEMY ATTACK: [bm.selected_intent.name]" size 30 color "#ffaaaa" xalign 0.5 bold True
                if bm.selected_intent.damage > 0:
                    text "Projected Damage: [bm.selected_intent.damage]" size 20 color "#ff4444" xalign 0.5
                text "[bm.selected_intent.desc]" size 18 color "#ccc" xalign 0.5 text_align 0.5

                textbutton "CLOSE":
                    action SetField(bm, "selected_intent", None)
                    xalign 0.5
                    background Solid("#444")
                    padding (10, 5)

    # Card selection (Available Skills)
    hbox:
        xalign 0.5 yalign 0.95
        spacing 15
        for skill in bm.player_skills:
            $ is_selected = bm.selected_skill == skill
            $ can_use = skill.current_cooldown == 0 and skill not in bm.used_skills_this_turn

            button:
                action Function(bm.select_skill, skill)
                sensitive (skill.current_cooldown == 0 and skill not in bm.used_skills_this_turn)
                background Frame(Solid("#555") if is_selected else (Solid("#333e") if can_use else Solid("#111e")), 4, 4)
                padding (10, 10)
                xminimum 140
                yminimum 180
                vbox:
                    spacing 5
                    text "[skill.name]" size 22 color ("#fff" if can_use else "#666") xalign 0.5 bold True
                    text "Cost: [skill.cost]" size 16 color "#44ff44" xalign 0.5
                    if skill.current_cooldown > 0:
                        null height 10
                        text "CD: [skill.current_cooldown]" size 18 color "#ff4444" xalign 0.5 bold True
                    elif skill in bm.used_skills_this_turn:
                        null height 10
                        text "USED" size 18 color "#888" xalign 0.5 bold True

    # Controls
    $ has_player_action = any(isinstance(s, Skill) for s in bm.slots)
    if has_player_action:
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

# GENERIC BATTLE ENGINE
label generic_battle(bm):
    $ bm.player_skills = get_default_skills()

    label .turn_start:
        $ bm.turn_count += 1
        $ bm.prepare_turn()

        show expression bm.player_sprites["idle"] as player at fight_left
        show expression bm.enemy_sprites["idle"] as enemy at fight_right
        show screen battle_screen(bm)

    label .selection_phase:
        $ result = ui.interact()
        if result == "execute":
            jump .execution_phase
        jump .selection_phase

    label .execution_phase:
        hide screen battle_screen
        $ current_slot_idx = 0
        $ bm.dodge_active = False # Reset dodge status at start of turn execution

    label .execution_loop:
        if current_slot_idx >= bm.current_max_slots:
            jump .turn_end

        $ action = bm.slots[current_slot_idx]

        if action is None:
            $ pass
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_mana = min(bm.player_max_mana, bm.player_mana + skill.mana_regen)
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_generic
            if skill.type == "attack":
                $ damage = skill.damage
                if bm.dodge_active == "success":
                    $ damage *= 2
                    $ bm.dodge_active = False # Use up dodge bonus
                $ bm.take_damage(damage, target="enemy")
                "[skill.name]! Dealt [damage] damage! (Enemy HP: [bm.enemy_hp])"
            elif skill.type == "barrier":
                $ bm.add_barrier(5)
            elif skill.type == "dodge":
                $ bm.dodge_active = True
        elif isinstance(action, EnemyIntent):
            $ bm.enemy_intent = action
            if bm.dodge_active:
                "DODGED!"
                $ bm.dodge_active = "success" # Mark as successful dodge for next attack bonus
            else:
                if action.animation:
                    call expression action.animation pass (bm) from _call_intent_anim_generic
                else:
                    call enemy_attack_anim(bm) from _call_intent_anim_default
                $ bm.take_damage(action.damage, target="player")
                "[action.name]! Took [action.damage] damage! (Your HP: [bm.player_hp])"

        # Check Win/Loss
        if bm.enemy_hp <= 0:
            jump .victory
        if bm.player_hp <= 0:
            jump .defeat

        $ renpy.pause(0.5)
        $ current_slot_idx += 1
        jump .execution_loop

    label .turn_end:
        $ bm.reduce_cooldowns()
        jump .turn_start

    label .victory:
        hide screen battle_screen
        return "win"

    label .defeat:
        hide screen battle_screen
        return "lose"

# --- Player Skill Animations ---

label player_strike_anim(bm):
    show expression "kare_strike_sprite" as player at fight_left
    show expression bm.enemy_sprites["hit"] as enemy at fight_right
    show expression "kare_strike_sprite" as player at fight_left:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.35
    camera:
        ease 0.2 xpos 0.1 ypos -0.1 zoom 1.2
        ease 0.2 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "punch-140236.mp3" volume 1.0
    $ renpy.pause(1.0)
    show expression bm.player_sprites["idle"] as player at fight_left
    show expression bm.enemy_sprites["idle"] as enemy at fight_right
    return

label player_power_slash_anim(bm):
    show expression "kare_power_slash_sprite" as player at fight_left
    show expression bm.enemy_sprites["hit"] as enemy at fight_right
    show expression "kare_power_slash_sprite" as player at fight_left:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.35
    camera:
        ease 0.2 xpos 0.1 ypos -0.1 zoom 1.2
        ease 0.2 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "audio/sword-slash-and-swing-185432.mp3" volume 2.0
    $ renpy.pause(1.0)
    show expression bm.player_sprites["idle"] as player at fight_left
    show expression bm.enemy_sprites["idle"] as enemy at fight_right
    return

label player_barrier_anim(bm):
    show expression "kare_barrier_pose" as player at fight_left
    play sound "Berserk Clang Sound Effect.mp3" volume 1.0
    "You brace yourself! (+5 Barrier)"
    $ renpy.pause(1.0)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label player_dodge_anim(bm):
    show expression "kare_dodge_pose" as player at fight_left
    "You prepare to dodge! (Avoid next attack & x2 Damage)"
    $ renpy.pause(1.0)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label player_meditate_anim(bm):
    show expression "kare_meditate_pose" as player at fight_left
    "You focus your mind... (+4 Mana)"
    $ renpy.pause(1.0)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

# --- Enemy Intent Animations ---

label enemy_sword_anim(bm):
    show expression "enemy_sword_sprite" as enemy at fight_right
    show expression bm.player_sprites["hit"] as player at fight_left
    show expression "enemy_sword_sprite" as enemy at fight_right:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.65
    camera:
        ease 0.2 xpos -0.1 ypos -0.1 zoom 1.2
        ease 0.2 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "audio/sword-slash-and-swing-185432.mp3" volume 2.0
    $ renpy.pause(1.0)
    show expression bm.enemy_sprites["idle"] as enemy at fight_right
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label enemy_gun_anim(bm):
    show expression "enemy_gun_sprite" as enemy at fight_right
    show expression bm.player_sprites["hit"] as player at fight_left
    camera:
        ease 0.1 xpos -0.05 ypos -0.05 zoom 1.1
        ease 0.1 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "audio/single-gunshot-62-hp-37188.mp3" volume 2.0
    $ renpy.pause(1.0)
    show expression bm.enemy_sprites["idle"] as enemy at fight_right
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label enemy_glare_anim(bm):
    show expression "enemy_glare_sprite" as enemy at fight_right
    "Lumpi glares at you intensely!"
    $ renpy.pause(1.0)
    show expression bm.enemy_sprites["idle"] as enemy at fight_right
    return

label enemy_attack_anim(bm):
    $ enemy_attack = bm.enemy_sprites["attack"]
    $ player_hit = bm.player_sprites["hit"]
    show expression enemy_attack as enemy at fight_right
    show expression player_hit as player at fight_left
    show expression enemy_attack as enemy at fight_right:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.65
    camera:
        ease 0.2 xpos -0.1 ypos -0.1 zoom 1.2
        ease 0.2 xpos 0.0 ypos 0.0 zoom 1.0
    play sound "Berserk Clang Sound Effect.mp3" volume 1.0
    $ renpy.pause(1.0)
    $ enemy_idle = bm.enemy_sprites["idle"]
    $ player_idle = bm.player_sprites["idle"]
    show expression enemy_idle as enemy at fight_right
    show expression player_idle as player at fight_left

    if bm.enemy_name == "Butter":
        if bm.player_barrier > 0:
            "kare" "haha i blocked"
        else:
            "kare" "OWWWWW"
    elif bm.enemy_name == "Lumpi":
        if bm.player_barrier > 0:
            "lumpi" "You think you can block my sword?!"
        else:
            "lumpi" "HYAAA!!"
            "kare" "OWWWWW"
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
    show normalbutter_idle as enemy at fight_right
    $ renpy.pause(0.5, hard='True')
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'normalbutter_idle', 'attack': 'normalbutter_attack', 'hit': 'normalbutter_hit'}
    $ bm = BattleManager(10, 15, 'Butter', starting_slots=2, player_sprites=player_sprites, enemy_sprites=enemy_sprites)
    $ bm.enemy_intents = [
        EnemyIntent('Nudge', damage=2, desc='A weak nudge. Butter moves a bit.', animation='enemy_attack_anim'),
        EnemyIntent('Double Hit', damage=5, desc='Butter attacks twice! Watch out!', animation='enemy_attack_anim')
    ]
    call generic_battle(bm) from _call_generic_battle_butter
    if _return == 'win':
        jump .player_wins
    else:
        jump .player_loses
    label .player_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera
        hide player
        hide enemy
        with fade
        'yay win'
        return
    label .player_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_1
        hide player
        hide enemy
        'You were defeated by butter...'
        return

image lumpi_idle:
    "lumpi_idle.png"
    pause 1.0
    "lumpi_idle.png"
    pause 1.0
    repeat
image lumpi_attack:
    "lumpi_attack1.png"
    pause 0.3
    "lumpi_attack2.png"
    pause 0.7
    repeat
image lumpi_hit:
    "lumpi_hit.png"
    pause 1.0
    repeat
image lumpi_wheelchair:
    "lumpi_wheelchair.png"
    pause 1.0
    repeat

label lumpi_battle:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show lumpi_idle as enemy at fight_right
    $ renpy.pause(0.5, hard='True')
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpi_idle', 'attack': 'lumpi_attack', 'hit': 'lumpi_hit'}
    $ bm = BattleManager(15, 25, 'Lumpi', starting_slots=4, player_sprites=player_sprites, enemy_sprites=enemy_sprites)
    $ bm.enemy_intents = [
        EnemyIntent('Sword Slash', damage=3, desc='Lumpi slashes with his legendary (broken) sword.', animation='enemy_attack_anim'),
        EnemyIntent('Back Pain', damage=0, desc='Lumpi has back pain and skips his turn. This is your chance!', animation='lumpi_back_pain_anim')
    ]
    call generic_battle(bm) from _call_generic_battle_lumpi
    if _return == 'win':
        jump .lumpi_wins
    else:
        jump .lumpi_loses
    label .lumpi_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_2
        hide player
        hide enemy
        return
    label .lumpi_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_3
        'You were defeated by Lumpi...'
        menu:
            'Retry Battle':
                jump lumpi_battle

image lumpiwheelchair_idle:
    "lumpi_wheelchair.png"
    pause 1.0
    repeat
image lumpiwheelchair_attack:
    "lumpi_wheelchair.png"
    pause 0.3
    repeat
image lumpiwheelchair_hit:
    "lumpi_wheelchair.png"
    pause 1.0
    repeat

label lumpiwheelchair_battle:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show lumpiwheelchair_idle as enemy at fight_right
    $ renpy.pause(0.5, hard='True')
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpiwheelchair_idle', 'attack': 'lumpiwheelchair_attack', 'hit': 'lumpiwheelchair_hit'}
    $ bm = BattleManager(20, 40, 'Lumpi (Wheelchair)', starting_slots=6, player_sprites=player_sprites, enemy_sprites=enemy_sprites)
    $ bm.enemy_intents = [
        EnemyIntent('Ram', damage=5, desc='Lumpi rams you with his high-speed wheelchair.', animation='enemy_attack_anim'),
        EnemyIntent('Glare', damage=0, desc='Lumpi glares at you intensely. He is getting focused!', animation='enemy_glare_anim')
    ]
    call generic_battle(bm) from _call_generic_battle_wheelchair
    if _return == 'win':
        jump .lumpiwheelchair_wins
    else:
        jump .lumpiwheelchair_loses
    label .lumpiwheelchair_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_4
        hide player
        hide enemy
        return
    label .lumpiwheelchair_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_5
        'lumpi' 'huwhuahuwha i win'
        menu:
            'Retry Battle':
                jump lumpiwheelchair_battle

image newenemy_idle:
    "butter_serious_idle.png"
    pause 1.0
    repeat
image newenemy_attack1:
    "butter_serious_attack1.png"
    pause 0.3
    "butter_serious_attack2.png"
    pause 0.7
    repeat
image newenemy_hit:
    "butter_serious_hurt.png"
    pause 1.0
    repeat

label newenemy_battle:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show newenemy_idle as enemy at fight_right
    $ renpy.pause(0.5, hard='True')
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'newenemy_idle', 'attack': 'newenemy_attack1', 'hit': 'newenemy_hit'}
    $ bm = BattleManager(50, 100, 'Butter', starting_slots=8, player_sprites=player_sprites, enemy_sprites=enemy_sprites)
    $ bm.enemy_intents = [
        EnemyIntent('Sword Slash', damage=4, desc='A quick, precise slash from Butter.', animation='enemy_sword_anim'),
        EnemyIntent('Gun Shot', damage=6, desc='Butter pulls out a gun?! Watch out!', animation='enemy_gun_anim'),
        EnemyIntent('Gaze', damage=0, desc='Butter is preparing something... wait for it.', animation=None)
    ]
    call generic_battle(bm) from _call_generic_battle_newenemy
    if _return == 'win':
        jump .newenemy_wins
    else:
        jump .newenemy_loses
    label .newenemy_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_6
        hide player
        hide enemy
        return
    label .newenemy_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_7
        menu:
            'Retry Battle':
                jump newenemy_battle

image ava_idle:
    "ava_fight.png"
    pause 1.0
    repeat
image ava_attack:
    "ava_fight.png"
    pause 0.3
    repeat
image ava_hit:
    "ava_fight.png"
    pause 1.0
    repeat
image butter_idle:
    "butter_serious_idle.png"
    pause 1.0
    repeat
image butter_attack1:
    "butter_serious_attack1.png"
    pause 0.3
    repeat
image butter_hit:
    "butter_serious_hurt.png"
    pause 1.0
    repeat
image chaos_idle:
    "chaos_idle.png"
    pause 0.3
image chaos_attack:
    "chaos_attack.png"
    pause 0.3
image chaos_hit:
    "chaos_hurt.png"
    pause 1.0

label butter_ava_battle:
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show chaos_idle as player at fight_left
    show butter_idle as enemy at fight_right
    show ava_idle as ava at Position(xalign=0.5, yalign=0.5)
    $ renpy.pause(0.5, hard='True')
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ enemy_sprites = {'idle': 'butter_idle', 'attack': 'butter_attack1', 'hit': 'butter_hit'}
    $ bm = BattleManager(500, 999999999999, 'Butter and Ava', starting_slots=10, player_sprites=player_sprites, enemy_sprites=enemy_sprites)
    $ bm.player_skills = get_default_skills()
    $ bm.enemy_intents = [EnemyIntent('Butter Attack', damage=5, desc='Butter attacks with precise intent.', animation='enemy_attack_anim')]
    $ ava_on_player_side = True
    $ ava_attacked_once = False

    label .turn_start:
        $ bm.turn_count += 1
        $ bm.prepare_turn()
        show expression bm.player_sprites["idle"] as player at fight_left
        show expression bm.enemy_sprites["idle"] as enemy at fight_right
        show expression 'ava_idle' as ava at Position(xalign=0.5 if ava_on_player_side else 0.85, yalign=0.5)
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
        $ action = bm.slots[current_slot_idx]
        if action is None:
            $ pass
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_mana = min(bm.player_max_mana, bm.player_mana + skill.mana_regen)
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_ava
            if skill.type == 'attack':
                $ damage = skill.damage
                if bm.dodge_active == "success":
                    $ damage *= 2
                    $ bm.dodge_active = False
                $ bm.take_damage(damage, target='enemy')
                "[skill.name]! Dealt [damage] damage! (Enemy HP: [bm.enemy_hp])"
            elif skill.type == 'barrier':
                $ bm.add_barrier(5)
            elif skill.type == 'dodge':
                $ bm.dodge_active = True
        elif isinstance(action, EnemyIntent):
            $ bm.enemy_intent = action
            if bm.dodge_active:
                'DODGED!'
                $ bm.dodge_active = 'success'
            else:
                call enemy_attack_anim(bm) from _call_intent_anim_ava_butter_v2
                $ bm.take_damage(bm.enemy_intent.damage, target='player')
                "[bm.enemy_intent.name]! Took [bm.enemy_intent.damage] damage! (Your HP: [bm.player_hp])"
        if bm.enemy_hp <= 0:
            jump .victory
        if bm.player_hp <= 0:
            jump .defeat
        $ renpy.pause(0.5)
        $ current_slot_idx += 1
        jump .execution_loop
    label .ava_turn:
        if not ava_attacked_once:
            $ ava_attacked_once = True
            show ava_attack as ava at Position(xalign=0.5, yalign=0.5):
                ease 0.2 xpos 0.65
                ease 0.2 xpos 0.5
            play sound 'punch-140236.mp3' volume 2.0
            $ renpy.pause(1.0)
            $ bm.take_damage(5, target='enemy')
            'ava attacks butter for 5 damage! (Butter HP: [bm.enemy_hp])'
            show ava_idle as ava at Position(xalign=0.5, yalign=0.5)
            'butter' 'HOLD ON why are you attacking me?'
            'ava' 'oh wait i forgot you are my ally'
            $ ava_on_player_side = False
            show ava_idle as ava:
                ease 0.2 xalign 0.85
            $ renpy.pause(0.7)
        elif not ava_on_player_side:
            show ava_attack as ava at Position(xalign=0.85, yalign=0.5):
                ease 0.2 xpos 0.35
                ease 0.2 xpos 0.85
            play sound 'audio/sword-slash-and-swing-185432.mp3' volume 2.0
            $ renpy.pause(1.0)
            show ava_idle as ava at Position(xalign=0.85, yalign=0.5)
            $ bm.take_damage(60, target='player')
            'ava attacks for 60 damage! (Your HP: [bm.player_hp])'
        call enemy_attack_anim(bm) from _call_enemy_anim_ava_butter_final
        $ bm.take_damage(bm.enemy_intent.damage, target='player')
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
    show chaos_idle as player at fight_left
    show butter_idle as enemy at fight_right
    show ava_idle as ava at Position(xalign=0.85, yalign=0.5)
    $ renpy.pause(0.5, hard='True')
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ enemy_sprites = {'idle': 'butter_idle', 'attack': 'butter_attack1', 'hit': 'butter_hit'}
    $ bm = BattleManager(500, 999, 'Butter and Ava', starting_slots=10, player_sprites=player_sprites, enemy_sprites=enemy_sprites)
    $ bm.player_skills = get_default_skills()
    $ bm.enemy_intents = [EnemyIntent('Butter Attack', damage=10, desc='Butter attacks with overwhelming force.', animation='enemy_attack_anim')]
    label .turn_start:
        $ bm.turn_count += 1
        $ bm.prepare_turn()
        show expression bm.player_sprites["idle"] as player at fight_left
        show expression bm.enemy_sprites["idle"] as enemy at fight_right
        show ava_idle as ava at Position(xalign=0.85, yalign=0.5)
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
        $ action = bm.slots[current_slot_idx]
        if action is None:
            $ pass
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_mana = min(bm.player_max_mana, bm.player_mana + skill.mana_regen)
            if skill.animation:
                call expression skill.animation pass (bm) from _call_skill_anim_ava2
            if skill.type == 'attack':
                $ damage = skill.damage
                if bm.dodge_active == "success":
                    $ damage *= 2
                    $ bm.dodge_active = False
                $ bm.take_damage(damage, target='enemy')
                "[skill.name]! Dealt [damage] damage! (Enemy HP: [bm.enemy_hp])"
            elif skill.type == 'barrier':
                $ bm.add_barrier(5)
            elif skill.type == 'dodge':
                $ bm.dodge_active = True
        elif isinstance(action, EnemyIntent):
            $ bm.enemy_intent = action
            if bm.dodge_active:
                'DODGED!'
                $ bm.dodge_active = 'success'
            else:
                call enemy_attack_anim(bm) from _call_intent_anim_ava_butter_v22
                $ bm.take_damage(bm.enemy_intent.damage, target='player')
                "[bm.enemy_intent.name]! Took [bm.enemy_intent.damage] damage! (Your HP: [bm.player_hp])"
        if bm.enemy_hp <= 0:
            jump .victory
        if bm.player_hp <= 0:
            jump .defeat
        $ renpy.pause(0.5)
        $ current_slot_idx += 1
        jump .execution_loop
    label .ava_turn:
        show ava_attack as ava at Position(xalign=0.85, yalign=0.5):
            ease 0.2 xpos 0.35
            ease 0.2 xpos 0.85
        play sound 'audio/sword-slash-and-swing-185432.mp3' volume 2.0
        $ renpy.pause(1.0)
        show ava_idle as ava at Position(xalign=0.85, yalign=0.5)
        $ bm.take_damage(50, target='player')
        'ava attacks for 50 damage! (Your HP: [bm.player_hp])'
        call enemy_attack_anim(bm) from _call_enemy_anim_ava_butter2_final
        $ bm.take_damage(bm.enemy_intent.damage, target='player')
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
