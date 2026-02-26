label simple_battle_graphics(skill_overrides=None):
    $ _skipping = None
    $ config.allow_skipping = False
    camera:
        perspective False
        gl_depth False
    scene bg at truecenter
    show kare_idle as player at fight_left
    show butter_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ butter = get_butter()
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 10, "cost": 1, "energy_regen": 2},
        "punch":            {"damage": 20, "cooldown": 1},
        "super cool kick":  {"damage": 50, "cost": 12, "cooldown": 4},
        "Defense":          {"damage": 15, "cost": 2, "cooldown": 1},
        "Focus":            {"damage": 10, "cost": 3, "buff_duration": 5, "cooldown": 3},
        "yummers":          {"energy_regen": 8, "cooldown": 2},
        "evade":            {"cost": 2, "cooldown": 2},
    }
    $ bm = BattleManager(300, [butter], starting_slots=2, player_sprites=player_sprites, starting_energy=20, max_energy=20, tutorial=True, skill_overrides=skill_overrides)
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
    scene bg at truecenter
    show kare_idle as player at fight_left
    show lumpi_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpi_idle', 'attack': 'lumpi_attack', 'hit': 'lumpi_hit'}
    # USES THE NEW UNIQUE INTENT SET FOR LUMPI
    $ lumpi_intents = get_enemy_intents("lumpi")
    $ lumpi = Enemy('Lumpi', 300, enemy_sprites, lumpi_intents)
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 10, "cost": 1, "energy_regen": 2},
        "punch":            {"damage": 20, "cooldown": 1},
        "super cool kick":  {"damage": 50, "cost": 12, "cooldown": 4},
        "Defense":          {"damage": 15, "cost": 2, "cooldown": 1},
        "Focus":            {"damage": 10, "cost": 3, "buff_duration": 5, "cooldown": 3},
        "yummers":          {"energy_regen": 8, "cooldown": 2},
        "evade":            {"cost": 2, "cooldown": 2},
    }
    $ bm = BattleManager(400, [lumpi], starting_slots=2, player_sprites=player_sprites, starting_energy=30, max_energy=30, skill_overrides=skill_overrides)
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
    scene bg at truecenter
    show kare_idle as player at fight_left
    show lumpiwheelchair_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ enemy_sprites = {'idle': 'lumpiwheelchair_idle', 'attack': 'lumpiwheelchair_attack', 'hit': 'lumpiwheelchair_hit'}
    # USES THE NEW UNIQUE INTENT SET FOR LUMPI WHEELCHAIR
    $ lumpi_intents = get_enemy_intents("lumpi wheelchair")
    $ lumpi = Enemy('Lumpi (Wheelchair)', 350, enemy_sprites, lumpi_intents)
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 10, "cost": 1, "energy_regen": 2},
        "punch":            {"damage": 20, "cooldown": 1},
        "super cool kick":  {"damage": 50, "cost": 12, "cooldown": 4},
        "Defense":          {"damage": 15, "cost": 2, "cooldown": 1},
        "Focus":            {"damage": 10, "cost": 3, "buff_duration": 5, "cooldown": 3},
        "yummers":          {"energy_regen": 8, "cooldown": 2},
        "evade":            {"cost": 2, "cooldown": 2},
    }
    $ bm = BattleManager(500, [lumpi], starting_slots=2, player_sprites=player_sprites, starting_energy=40, max_energy=40, dobe_helps=True, skill_overrides=skill_overrides)
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
    scene bg at truecenter
    show kare_idle as player at fight_left
    show seriousbutter_idle as enemy_0 at fight_right
    $ renpy.pause(0.5, hard=True)
    $ player_sprites = {'idle': 'kare_idle', 'attack': 'kare_attack', 'hit': 'kare_hit'}
    $ butter = get_serious_butter()
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 10, "cost": 1, "energy_regen": 2},
        "punch":            {"damage": 20, "cooldown": 1},
        "super cool kick":  {"damage": 50, "cost": 12, "cooldown": 4},
        "Defense":          {"damage": 15, "cost": 2, "cooldown": 1},
        "Focus":            {"damage": 10, "cost": 3, "buff_duration": 5, "cooldown": 3},
        "yummers":          {"energy_regen": 8, "cooldown": 2},
        "evade":            {"cost": 2, "cooldown": 2},
    }
    $ bm = BattleManager(600, [butter], starting_slots=2, player_sprites=player_sprites, starting_energy=50, max_energy=50, skill_overrides=skill_overrides)
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
    scene bg at truecenter
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ butter = get_serious_butter()
    $ ava_intents = get_enemy_intents("ava")
    $ ava = Enemy('Ava', 999999, {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}, ava_intents)
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 10, "cost": 1, "energy_regen": 2},
        "punch":            {"damage": 20, "cooldown": 1},
        "super cool kick":  {"damage": 50, "cost": 12, "cooldown": 4},
        "Defense":          {"damage": 15, "cost": 2, "cooldown": 1},
        "Focus":            {"damage": 10, "cost": 3, "buff_duration": 5, "cooldown": 3},
        "yummers":          {"energy_regen": 8, "cooldown": 2},
        "evade":            {"cost": 2, "cooldown": 2},
    }
    $ bm = BattleManager(1000, [butter, ava], starting_slots=2, player_sprites=player_sprites, starting_energy=100, max_energy=100, is_chaos=True, skill_overrides=skill_overrides)
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
                    $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")
                    $ bm.take_damage(damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(damage * 5, character_type="player")
                    "[skill.name] deals [damage] damage to [enemy.name]!"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated!"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_barrier_boss1
                $ bm.add_barrier(skill.damage)
                "You gain [skill.damage] Defense!"
            elif skill.type == "dodge":
                $ bm.is_dodged = False
                $ bm.dodge_active = True
            elif skill.type == "buff":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_buff_boss1
                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")
                "[skill.name] activated! Damage increased by [skill.damage] for [skill.buff_duration] turns."
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
    scene bg at truecenter
    $ player_sprites = {'idle': 'chaos_idle', 'attack': 'chaos_attack', 'hit': 'chaos_hit'}
    $ butter = get_serious_butter()
    $ ava_intents = get_enemy_intents("ava")
    $ ava = Enemy('Ava', 300, {'idle': 'ava_idle', 'attack': 'ava_attack', 'hit': 'ava_hit'}, ava_intents)
    $ skill_overrides = skill_overrides or {
        "slap":             {"damage": 10, "cost": 1, "energy_regen": 2},
        "punch":            {"damage": 20, "cooldown": 1},
        "super cool kick":  {"damage": 50, "cost": 12, "cooldown": 4},
        "Defense":          {"damage": 15, "cost": 2, "cooldown": 1},
        "Focus":            {"damage": 10, "cost": 3, "buff_duration": 5, "cooldown": 3},
        "yummers":          {"energy_regen": 8, "cooldown": 2},
        "evade":            {"cost": 2, "cooldown": 2},
    }
    $ bm = BattleManager(1000, [butter, ava], starting_slots=2, player_sprites=player_sprites, starting_energy=100, max_energy=100, is_chaos=True, skill_overrides=skill_overrides)
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
                    $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")
                    $ bm.take_damage(damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(damage * 5, character_type="player")
                    "[skill.name] deals [damage] damage to [enemy.name]!"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated!"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_barrier_boss2
                $ bm.add_barrier(skill.damage)
                "You gain [skill.damage] Defense!"
            elif skill.type == "dodge":
                $ bm.is_dodged = False
                $ bm.dodge_active = True
            elif skill.type == "buff":
                $ bm.is_dodged = False
                if skill.animation:
                    call expression skill.animation pass (bm) from _call_skill_anim_buff_boss2
                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")
                "[skill.name] activated! Damage increased by [skill.damage] for [skill.buff_duration] turns."
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
        window hide
        jump .boss2_start_logic
    label .boss2_victory:
        $ config.allow_skipping = True
        $ battle_mode = False
        $ quick_menu = True
        hide screen battle_screen
        return
    label .boss2_defeat:
        $ config.allow_skipping = True
        $ battle_mode = False
        $ quick_menu = True
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
