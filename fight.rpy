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
        def __init__(self, player_max_hp, enemy_max_hp, enemy_name, player_sprites=None, enemy_sprites=None):
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

            self.queue = []
            self.enemy_intent = None
            self.enemy_intents = []
            self.dodge_active = False
            self.player_skills = []
            self.turn_count = 0

        def add_to_queue(self, skill):
            if self.player_mana >= skill.cost and skill.current_cooldown == 0:
                # Allow multiple instances only for skills without cooldown
                if skill.cooldown > 0 and skill in self.queue:
                    return False
                self.queue.append(skill)
                self.player_mana -= skill.cost
                return True
            return False

        def remove_from_queue(self, index):
            skill = self.queue.pop(index)
            self.player_mana += skill.cost

        def clear_queue(self):
            for skill in self.queue:
                self.player_mana += skill.cost
            self.queue = []

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
            Skill("Strike", cost=2, damage=3, mana_regen=1, desc="Basic attack. Regens 1 mana.", animation="player_attack_anim"),
            Skill("Power Slash", cost=5, damage=8, cooldown=2, desc="Strong attack. 2 turn cooldown.", animation="player_attack_anim"),
            Skill("Barrier", cost=3, type="barrier", desc="Gain 5 Barrier. 1 turn cooldown.", cooldown=1, animation="player_defend_anim"),
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
        if bm.enemy_intent:
            frame:
                background Solid("#0008")
                xalign 1.0
                padding (10, 5)
                vbox:
                    text "INTENT: [bm.enemy_intent.name]" size 18 color "#ffaa00" xalign 1.0
                    text "[bm.enemy_intent.desc]" size 14 color "#ccc" xalign 1.0

    # Queue display (Selected Cards)
    frame:
        background Solid("#0004")
        xalign 0.5 yalign 0.15
        padding (10, 10)
        hbox:
            spacing 10
            text "Queue:" size 18 color "#fff" yalign 0.5
            for i, skill in enumerate(bm.queue):
                textbutton "[skill.name]":
                    action Function(bm.remove_from_queue, i)
                    text_size 20
                    background Solid("#666")
                    padding (5, 2)
            if not bm.queue:
                text "None" size 18 color "#888" yalign 0.5

    # Card selection (Available Skills)
    hbox:
        xalign 0.5 yalign 0.95
        spacing 15
        for skill in bm.player_skills:
            $ can_use = bm.player_mana >= skill.cost and skill.current_cooldown == 0
            $ in_queue_count = bm.queue.count(skill)

            button:
                action If(can_use, Function(bm.add_to_queue, skill))
                sensitive can_use
                background Frame(Solid("#333e") if can_use else Solid("#111e"), 4, 4)
                padding (10, 10)
                xminimum 140
                yminimum 180
                vbox:
                    spacing 5
                    text "[skill.name]" size 22 color ("#fff" if can_use else "#666") xalign 0.5 bold True
                    text "Cost: [skill.cost]" size 16 color "#44ff44" xalign 0.5
                    null height 5
                    text "[skill.desc]" size 14 xmaximum 120 xalign 0.5 text_align 0.5
                    if skill.current_cooldown > 0:
                        null height 10
                        text "CD: [skill.current_cooldown]" size 18 color "#ff4444" xalign 0.5 bold True

    # Controls
    if bm.queue:
        textbutton "CONFIRM":
            xalign 0.95 yalign 0.8
            background Solid("#f00")
            padding (20, 10)
            text_size 30
            text_color "#fff"
            text_bold True
            action Return("execute")

    if bm.queue:
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

# BUTTER BATTLE - FIXED VERSION
# GENERIC BATTLE ENGINE
label generic_battle(bm):
    $ bm.player_skills = get_default_skills()

    label .turn_start:
        $ bm.turn_count += 1

        # Determine Enemy Intent
        if not bm.enemy_intents:
            $ bm.enemy_intents = [EnemyIntent("Attack", damage=2, desc="A basic attack.", animation="enemy_attack_anim")]

        $ bm.enemy_intent = renpy.random.choice(bm.enemy_intents)

        # Mana recovery at start of turn
        $ bm.player_mana = min(bm.player_max_mana, bm.player_mana + 2)

        show screen battle_screen(bm)

    label .selection_phase:
        $ result = ui.interact()
        if result == "execute":
            jump .execution_phase
        jump .selection_phase

    label .execution_phase:
        $ current_queue = list(bm.queue)
        $ bm.queue = [] # Clear queue after starting execution

    label .execution_loop:
        if not current_queue:
            jump .enemy_turn

        $ skill = current_queue.pop(0)

        # 1. Set Cooldown
        $ skill.current_cooldown = skill.cooldown

        # 2. Mana Regen
        $ bm.player_mana = min(bm.player_max_mana, bm.player_mana + skill.mana_regen)

        # 3. Call Animation
        if skill.animation:
            call expression skill.animation pass (bm) from _call_skill_anim_generic

        # 4. Apply Effects
        if skill.type == "attack":
            $ damage = skill.damage
            if bm.dodge_active:
                $ damage *= 2
                $ bm.dodge_active = False
            $ bm.take_damage(damage, target="enemy")
        elif skill.type == "barrier":
            $ bm.add_barrier(5)
        elif skill.type == "dodge":
            $ bm.dodge_active = True

        # Check if enemy is defeated
        if bm.enemy_hp <= 0:
            jump .victory

        $ renpy.pause(0.5)
        jump .execution_loop

    label .enemy_turn:
        # Enemy Turn
        if bm.enemy_intent:
            if bm.enemy_intent.animation:
                call expression bm.enemy_intent.animation pass (bm) from _call_enemy_anim_generic
            else:
                call enemy_attack_anim(bm) from _call_enemy_anim_default

            $ bm.take_damage(bm.enemy_intent.damage, target="player")

        if bm.player_hp <= 0:
            jump .defeat

        $ bm.reduce_cooldowns()
        $ bm.reduce_cooldowns()
        jump .turn_start

    label .victory:
        hide screen battle_screen
        return "win"

    label .defeat:
        hide screen battle_screen
        return "lose"

# --- Generic Animations ---

label player_attack_anim(bm):
    $ player_idle = bm.player_sprites["idle"]
    $ player_attack = bm.player_sprites["attack"]
    $ enemy_hit = bm.enemy_sprites["hit"]
    $ enemy_idle = bm.enemy_sprites["idle"]

    hide expression player_idle
    show expression player_attack at fight_left
    show expression enemy_hit at fight_right

    show expression player_attack at fight_left:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.35

    camera:
        ease 0.2 xpos 0.1 ypos -0.1 zoom 1.2
        ease 0.3 xpos 0.0 ypos 0.0 zoom 1.0

    play sound "punch-140236.mp3" volume 1.0
    $ renpy.pause(0.5)

    hide expression player_attack
    hide expression enemy_hit
    show expression player_idle at fight_left
    show expression enemy_idle at fight_right
    return

label player_defend_anim(bm):
    play sound "Berserk Clang Sound Effect.mp3" volume 1.0
    "You brace yourself! (+5 Barrier)"
    return

label player_dodge_anim(bm):
    "You prepare to dodge! (Next attack x2 Damage)"
    return

label player_meditate_anim(bm):
    "You focus your mind... (+4 Mana)"
    return

label enemy_attack_anim(bm):
    $ enemy_idle = bm.enemy_sprites["idle"]
    $ enemy_attack = bm.enemy_sprites["attack"]
    $ player_hit = bm.player_sprites["hit"]
    $ player_idle = bm.player_sprites["idle"]

    hide expression enemy_idle
    show expression enemy_attack at fight_right
    show expression player_hit at fight_left

    show expression enemy_attack at fight_right:
        ease 0.2 xpos 0.5
        ease 0.2 xpos 0.65

    camera:
        ease 0.2 xpos -0.1 ypos -0.1 zoom 1.2
        ease 0.3 xpos 0.0 ypos 0.0 zoom 1.0

    play sound "Berserk Clang Sound Effect.mp3" volume 1.0
    $ renpy.pause(0.5)

    hide expression enemy_attack
    hide expression player_hit
    show expression enemy_idle at fight_right
    show expression player_idle at fight_left

    if bm.enemy_name == "Butter":
        if bm.player_barrier > 0:
            "kare" "haha i blocked"
        else:
            "kare" "OWWWWW"
        if bm.enemy_intent.name == "Double Hit":
            "kare" "YOU ATTACKED TWICE THATS NOT FAIR!!"
            "butter" "whats not fair is you blocking"
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
    # Initialize camera and scene
    camera:
        perspective False
        gl_depth False

    scene bg at truecenter
    show kare_idle at fight_left
    show normalbutter_idle at fight_right

    $ renpy.pause(0.5, hard='True')

    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'normalbutter_idle', 'attack': 'normalbutter_attack', 'hit': 'normalbutter_hit'}
    $ bm = BattleManager(10, 15, 'Butter', player_sprites, enemy_sprites)
    $ bm.enemy_intents = [
        EnemyIntent('Nudge', damage=2, desc='A weak nudge.', animation='enemy_attack_anim'),
        EnemyIntent('Double Hit', damage=5, desc='Butter attacks twice! (Total 5 damage)', animation='enemy_attack_anim')
    ]

    call generic_battle(bm) from _call_generic_battle_butter

    if _return == 'win':
        jump .player_wins
    else:
        jump .player_loses

    # Victory Screen
    label .player_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera
        hide kare_idle
        hide kare_attack
        hide kare_hit
        hide normalbutter_idle
        hide normalbutter_attack
        hide normalbutter_hit
        with fade
        'yay win'
        return

    # Defeat Screen
    label .player_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_1
        hide kare_idle
        hide kare_attack
        hide kare_hit
        hide normalbutter_idle
        hide normalbutter_attack
        hide normalbutter_hit
        'You were defeated by butter...'
        return
# Image definitions for LUMPI
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
    # Initialize camera and scene for lumpi
    camera:
        perspective False
        gl_depth False

    scene bg at truecenter
    show kare_idle at fight_left
    show lumpi_idle at fight_right

    $ renpy.pause(0.5, hard='True')

    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpi_idle', 'attack': 'lumpi_attack', 'hit': 'lumpi_hit'}
    $ bm = BattleManager(15, 25, 'Lumpi', player_sprites, enemy_sprites)
    $ bm.enemy_intents = [
        EnemyIntent('Sword Slash', damage=3, desc='Lumpi slashes with his sword.', animation='enemy_attack_anim'),
        EnemyIntent('Back Pain', damage=0, desc='Lumpi has back pain and skips his turn.', animation='lumpi_back_pain_anim')
    ]

    call generic_battle(bm) from _call_generic_battle_lumpi

    if _return == 'win':
        jump .lumpi_wins
    else:
        jump .lumpi_loses

    # Victory Screen for Lumpi
    label .lumpi_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_2
        hide kare_idle
        hide lumpi_idle
        return

    # Defeat Screen for Lumpi
    label .lumpi_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_3
        'You were defeated by Lumpi...'
        menu:
            'Retry Battle':
                jump lumpi_battle
# LUMPIWHEELCHAIR BATTLE


# Image definitions for LUMPIWHEELCHAIR
image lumpiwheelchair_idle:
    "lumpi_wheelchair.png"
    pause 1.0
    "lumpi_wheelchair.png"
    pause 1.0
    repeat

image lumpiwheelchair_attack:
    "lumpi_wheelchair.png"
    pause 0.3
    "lumpi_wheelchair.png"
    pause 0.7
    repeat

image lumpiwheelchair_hit:
    "lumpi_wheelchair.png"
    pause 1.0
    repeat

# LUMPIWHEELCHAIR BATTLE
label lumpiwheelchair_battle:
    # Initialize camera and scene
    camera:
        perspective False
        gl_depth False

    scene bg at truecenter
    show kare_idle at fight_left
    show lumpiwheelchair_idle at fight_right

    $ renpy.pause(0.5, hard='True')

    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpiwheelchair_idle', 'attack': 'lumpiwheelchair_attack', 'hit': 'lumpiwheelchair_hit'}
    $ bm = BattleManager(20, 40, 'Lumpi (Wheelchair)', player_sprites, enemy_sprites)
    $ bm.enemy_intents = [
        EnemyIntent('Ram', damage=5, desc='Lumpi rams you with his wheelchair.', animation='enemy_attack_anim'),
        EnemyIntent('Glare', damage=2, desc='Lumpi glares at you.', animation='enemy_attack_anim')
    ]

    call generic_battle(bm) from _call_generic_battle_wheelchair

    if _return == 'win':
        jump .lumpiwheelchair_wins
    else:
        jump .lumpiwheelchair_loses

    label .lumpiwheelchair_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_4
        hide kare_idle
        hide lumpiwheelchair_idle
        return

    label .lumpiwheelchair_loses:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_5
        'lumpi' 'huwhuahuwha i win'
        menu:
            'Retry Battle':
                jump lumpiwheelchair_battle
# VARIED ATTACK BATTLE TEMPLATE
# Each attack randomly picks from different sprites and sounds
# ============================================

# Image definitions - You need MULTIPLE attack sprites for variety
image newenemy_idle:
    "butter_serious_idle.png"
    pause 1.0
    repeat

# Attack variant 1
image newenemy_attack1:
    "butter_serious_attack1.png"
    pause 0.3
    "butter_serious_attack2.png"
    pause 0.7
    repeat

# Attack variant 2 (DIFFERENT animation)
image newenemy_attack2:
    "butter_serious_attack1.png"
    pause 2
    "butter_serious_attack2.png"
    pause 0.7
    repeat

# Attack variant 3 (DIFFERENT animation)
image newenemy_attack3:
    "butter_serious_altattack1.png"
    pause 2
    "butter_serious_altattack2.png"
    pause 0.7
    repeat

image newenemy_hit:
    "butter_serious_hurt.png"
    pause 1.0
    repeat

# VARIED ATTACK BATTLE
label newenemy_battle:
    camera:
        perspective False
        gl_depth False

    scene bg at truecenter
    show kare_idle at fight_left
    show newenemy_idle at fight_right

    $ renpy.pause(0.5, hard='True')

    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'newenemy_idle', 'attack': 'newenemy_attack1', 'hit': 'newenemy_hit'}
    $ bm = BattleManager(50, 100, 'Butter', player_sprites, enemy_sprites)
    $ bm.enemy_intents = [
        EnemyIntent('Sword Slash', damage=4, desc='A quick slash.', animation='enemy_attack_anim'),
        EnemyIntent('Heavy Strike', damage=6, desc='A heavy hit.', animation='enemy_attack_anim'),
        EnemyIntent('Gaze', damage=0, desc='Butter is preparing something.', animation=None)
    ]

    call generic_battle(bm) from _call_generic_battle_newenemy

    if _return == 'win':
        jump .newenemy_wins
    else:
        jump .newenemy_loses

    label .newenemy_wins:
        $ renpy.pause(0.1)
        call reset_camera from _call_reset_camera_6
        hide kare_idle
        hide newenemy_idle
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
    "ava_fight.png"
    pause 0.7
    repeat

image ava_hit:
    "ava_fight.png"
    pause 1.0
    repeat

# Butter serious sprites for battle
image butter_idle:
    "butter_serious_idle.png"
    pause 1.0
    repeat

image butter_attack1:
    "butter_serious_attack1.png"
    pause 0.3
    "butter_serious_attack2.png"
    pause 0.7
    repeat

image butter_attack2:
    "butter_serious_attack1.png"
    pause 2
    "butter_serious_attack2.png"
    pause 0.7
    repeat

image butter_attack3:
    "butter_serious_altattack1.png"
    pause 2
    "butter_serious_altattack2.png"
    pause 0.7
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
    "chaos_attack.png"
    pause 0.7

image chaos_hit:
    "chaos_hurt.png"
    pause 1.0


# BATTLE WITH AVA SWITCHING SIDES
# ============================================

# Additional image definitions for Ava
image ava_idle:
    "ava_fight.png"
    pause 1.0
    repeat

image ava_attack:
    "ava_fight.png"
    pause 0.3
    "ava_fight.png"
    pause 0.7
    repeat

image ava_hit:
    "ava_fight.png"
    pause 1.0
    repeat

# Butter serious sprites for battle
image butter_idle:
    "butter_serious_idle.png"
    pause 1.0
    repeat

image butter_attack1:
    "butter_serious_attack1.png"
    pause 0.3
    "butter_serious_attack2.png"
    pause 0.7
    repeat

image butter_attack2:
    "butter_serious_attack1.png"
    pause 2
    "butter_serious_attack2.png"
    pause 0.7
    repeat

image butter_attack3:
    "butter_serious_altattack1.png"
    pause 2
    "butter_serious_altattack2.png"
    pause 0.7
    repeat

image butter_hit:
    "butter_serious_hurt.png"
    pause 1.0
    repeat

# BATTLE WITH AVA

label butter_ava_battle:
    camera:
        perspective False
        gl_depth False

    scene bg at truecenter
    show chaos_idle at fight_left
    show butter_idle at fight_right
    show ava_idle at Position(xalign=0.5, yalign=0.5)

    $ renpy.pause(0.5, hard='True')

    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ enemy_sprites = {'idle': 'butter_idle', 'attack': 'butter_attack1', 'hit': 'butter_hit'}
    $ bm = BattleManager(500, 999999999999, 'Butter and Ava', player_sprites, enemy_sprites)
    $ bm.player_skills = get_default_skills()
    $ bm.enemy_intents = [EnemyIntent('Butter Attack', damage=5, desc='Butter attacks.', animation='enemy_attack_anim')]

    $ ava_on_player_side = True
    $ ava_attacked_once = False

    label .turn_start:
        $ bm.turn_count += 1
        $ bm.enemy_intent = renpy.random.choice(bm.enemy_intents)
        $ bm.player_mana = min(bm.player_max_mana, bm.player_mana + 2)
        show screen battle_screen(bm)

    label .selection_phase:
        $ result = ui.interact()
        if result == 'execute':
            jump .execution_phase
        jump .selection_phase

    label .execution_phase:
        $ current_queue = list(bm.queue)
        $ bm.queue = []

    label .execution_loop:
        if not current_queue:
            jump .enemy_turn
        $ skill = current_queue.pop(0)
        $ skill.current_cooldown = skill.cooldown
        $ bm.player_mana = min(bm.player_max_mana, bm.player_mana + skill.mana_regen)
        if skill.animation:
            call expression skill.animation pass (bm) from _call_skill_anim_ava
        if skill.type == 'attack':
            $ damage = skill.damage
            if bm.dodge_active:
                $ damage *= 2
                $ bm.dodge_active = False
            $ bm.take_damage(damage, target='enemy')
        elif skill.type == 'barrier':
            $ bm.add_barrier(5)
        elif skill.type == 'dodge':
            $ bm.dodge_active = True
        if bm.enemy_hp <= 0:
            jump .victory
        $ renpy.pause(0.5)
        jump .execution_loop

    label .enemy_turn:

        # AVA'S TURN - Story Event
        if not ava_attacked_once:
            $ ava_attacked_once = True
            hide chaos_idle
            hide butter_idle
            hide ava_idle
            show chaos_idle at fight_left
            show butter_hit at fight_right
            show ava_attack at Position(xalign=0.5, yalign=0.5)
            show ava_attack at Position(xalign=0.5, yalign=0.5):
                ease 0.2 xpos 0.65
                ease 0.2 xpos 0.5
            play sound 'punch-140236.mp3' volume 2.0
            $ renpy.pause(1.0)
            $ bm.take_damage(5, target='enemy')
            'ava attacks butter for 5 damage'
            hide ava_attack
            hide butter_hit
            show butter_idle at fight_right
            show ava_idle at Position(xalign=0.5, yalign=0.5)
            'butter' 'HOLD ON why are you attacking me?'
            'ava' 'oh wait i forgot you are my ally'
            $ ava_on_player_side = False
            show ava_idle at Position(xalign=0.5, yalign=0.5):
                ease 0.5 xalign 0.85
            $ renpy.pause(0.7)
        elif not ava_on_player_side:
            hide chaos_idle
            hide butter_idle
            hide ava_idle
            show chaos_hit at fight_left
            show butter_idle at fight_right
            show ava_attack at Position(xalign=0.85, yalign=0.5)
            show ava_attack at Position(xalign=0.85, yalign=0.5):
                ease 0.2 xpos 0.35
                ease 0.2 xpos 0.85
            play sound 'audio/sword-slash-and-swing-185432.mp3' volume 2.0
            $ renpy.pause(1.0)
            hide ava_attack
            hide chaos_hit
            show chaos_idle at fight_left
            show ava_idle at Position(xalign=0.85, yalign=0.5)
            $ bm.take_damage(60, target='player')
            'ava attacks for 60 damage'

        # Butter Turn
        call enemy_attack_anim(bm) from _call_enemy_anim_ava_butter
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
    show chaos_idle at fight_left
    show butter_idle at fight_right
    show ava_idle at Position(xalign=0.85, yalign=0.5)

    $ renpy.pause(0.5, hard='True')

    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ enemy_sprites = {'idle': 'butter_idle', 'attack': 'butter_attack1', 'hit': 'butter_hit'}
    $ bm = BattleManager(500, 999, 'Butter and Ava', player_sprites, enemy_sprites)
    $ bm.player_skills = get_default_skills()
    $ bm.enemy_intents = [EnemyIntent('Butter Attack', damage=10, desc='Butter attacks.', animation='enemy_attack_anim')]

    label .turn_start:
        $ bm.turn_count += 1
        $ bm.enemy_intent = renpy.random.choice(bm.enemy_intents)
        $ bm.player_mana = min(bm.player_max_mana, bm.player_mana + 2)
        show screen battle_screen(bm)

    label .selection_phase:
        $ result = ui.interact()
        if result == 'execute':
            jump .execution_phase
        jump .selection_phase

    label .execution_phase:
        $ current_queue = list(bm.queue)
        $ bm.queue = []

    label .execution_loop:
        if not current_queue:
            jump .enemy_turn
        $ skill = current_queue.pop(0)
        $ skill.current_cooldown = skill.cooldown
        $ bm.player_mana = min(bm.player_max_mana, bm.player_mana + skill.mana_regen)
        if skill.animation:
            call expression skill.animation pass (bm) from _call_skill_anim_ava2
        if skill.type == 'attack':
            $ damage = skill.damage
            if bm.dodge_active:
                $ damage *= 2
                $ bm.dodge_active = False
            $ bm.take_damage(damage, target='enemy')
        elif skill.type == 'barrier':
            $ bm.add_barrier(5)
        elif skill.type == 'dodge':
            $ bm.dodge_active = True
        if bm.enemy_hp <= 0:
            jump .victory
        $ renpy.pause(0.5)
        jump .execution_loop

    label .enemy_turn:

        # Ava Turn
        hide chaos_idle
        hide butter_idle
        hide ava_idle
        show chaos_hit at fight_left
        show butter_idle at fight_right
        show ava_attack at Position(xalign=0.85, yalign=0.5)
        show ava_attack at Position(xalign=0.85, yalign=0.5):
            ease 0.2 xpos 0.35
            ease 0.2 xpos 0.85
        play sound 'audio/sword-slash-and-swing-185432.mp3' volume 2.0
        $ renpy.pause(1.0)
        hide ava_attack
        hide chaos_hit
        show chaos_idle at fight_left
        show ava_idle at Position(xalign=0.85, yalign=0.5)
        $ bm.take_damage(50, target='player')
        'ava attacks for 50 damage!'

        # Butter Turn
        call enemy_attack_anim(bm) from _call_enemy_anim_ava_butter2
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

    # Wait exactly 30 seconds (can't skip)
    $ renpy.pause(25.0, hard=True)

    hide screen scrolling_credits

    # Credits end, return to wherever you called from
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