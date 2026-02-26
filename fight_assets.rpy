# BATTLE ASSETS AND TRANSFORMS




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

# --- Sketch UI Placeholders ---
image bg = Solid("#ffffff")
image ui_bg = Solid("#ffffff")

# Helper to create an outline image (1px black border with transparent center)
image sketchy_outline_img = Composite((100, 100),
    (0, 0),  Solid("#6d6d6d", xsize=100, ysize=2),   # top, 2px
    (0, 98), Solid("#6d6d6d", xsize=100, ysize=2),   # bottom, 2px
    (0, 2),  Solid("#6d6d6d", xsize=2,   ysize=96),  # left, 2px
    (98, 2), Solid("#6d6d6d", xsize=2,   ysize=96),  # right, 2px
)
image sketchy_bar_outline = Frame("sketchy_outline_img", 2, 2, 2, 2)
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
