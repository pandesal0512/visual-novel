init offset = 0
# CHARACTER BATTLE ANIMATIONS
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
    $ renpy.show("serious_butter_normal_sprite", tag=current_enemy_tag, at_list=[fight_right])
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
    if not bm.is_dodged:
        show expression bm.player_sprites["hit"] as player at fight_left
    $ renpy.pause(1, hard=True)
    $ renpy.show(bm.enemies[e_idx].sprites["idle"], tag=current_enemy_tag)
    show expression bm.player_sprites["idle"] as player at fight_left
    return

label lumpi_hard_anim(bm):
    $ renpy.show("lumpi_hard_sprite", tag=current_enemy_tag, at_list=[fight_right,enemy_charge_right])
    if not bm.is_dodged:
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
    $ renpy.show("lumpi_wheelchair_ultimate_sprite", tag=current_enemy_tag, at_list=[fight_right])
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
