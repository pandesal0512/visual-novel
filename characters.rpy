define kare_neutral = Character("kare", color ="#ffffff")
define butter_neutral = Character("butter", color ="#ffffff")
define kare_hurt = Character("kare", color ="#ffffff")
define kare_male = Character("kare", color ="#ffffff")
define karemale_hurt = Character("kare", color ="#ffffff")

image kare neutral = "kare_neutral.png"
image butter neutral = "butter_neutral.png"
image butter punch = "one_punch.png"
image kare hurt = "kare_hurt.png"
image flash = "flash.png"

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
    pause 2.0
    "kare_idle"

image kare_hit:
    "kare_hit.png"
    pause 2.0
    "kare_idle"

image butter_idle:
    "butter_idle.png"
    pause 1.0
    "butter_idle.png"
    pause 1.0
    repeat

image butter_attack:
    "butter_attack1.png"
    pause 0.3
    "butter_attack2.png"
    pause 2.0

image butter_hit:
    "butter_hit.png"
    pause 2.0
    "butter_idle"



