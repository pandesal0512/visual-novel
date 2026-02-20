label start:

play music "digital-alarm-clock-151920.mp3" fadein 1.0 volume 1.0 fadeout 1.0
scene sleep
""
""
stop music fadeout 1.0


scene room
with fade
 
show kare neutral
"kare" "huh what the"
"kare" "oh no its uhh late time"
"kare" "im gonna go school"





play music "normal1.mp3" fadein 1.0 volume 0.5 
scene outside
with fade


show kare neutral at left
"kare" "ugh"
"kare" "im tired"
"kare" "im gonna be late"
"kare" "huh"


show butter neutral with moveinright


play sound "Loud glass breaking sound.mp3"  volume 0.5
"CRASDH"

"butter" " OW watch it stupid"
"kare"  "nah u watch it"
"butter" " excuse me?!!?"
"kare"  "yea im late because of u"
"butter" "nah u trippin"
"kare"  "i have no time for this i gotta go to school"
"butter" "nah you're not going anywhere"
"butter" "not until you say sorry and pay for your damage"
"kare"  "what damage?"
hide  kare neutral
hide butter neutral
show butter punch  with dissolve
play sound "20 February_2025.mp3" fadein 1.0 volume 0.8 fadeout 1.0
"butter" "this damage"
hide butter punch
play sound "Flashbang Sound Effect.mp3" fadein 1.0 volume 0.3 fadeout 1.0
show flash
with dissolve
"kare" "o-"
scene outside
with fade



show kare hurt 
"kare" "owie"
"kare" "..."

stop music fadeout 3.0

play music "classroom.mp3" fadein 1.0 volume 0.5 fadeout 1.0

scene classroom

show kare hurt 

"kare" "goodmorning"
hide kare hurt
show teacher_neutral 

"teacher" "afternoon, actually.  5 hours late"
hide teacher_neutral
show kare hurt  

"kare" "oh"
hide kare hurt
show teacher_neutral 
"teacher" "sit down" 
hide teacher_neutral

show kare hurt at right 

show dobe_neutral at left
"dobe" "uhm.. kare"
"dobe" "what happened to your head?"
"kare" "just a headache"
"dobe" "oh. here i have a medecine"
"dobe" "it can help with headache"
"kare" "thanks"

hide kare hurt 
show kare_neutral at right
"dobe" "yourwelcome"

hide dobe_neutral
"teacher"  "Bugs bite some people more than others because of a combination of factors including body heat, carbon dioxide exhalation, body odor (from sweat and skin bacteria), blood type, genetics, and even the color of clothing you wear, which can attract certain insects; essentially, some people naturally emit chemical signals that are more appealing to bugs than others. 
Key reasons why bugs might be attracted to you:
Carbon dioxide: Mosquitoes and other biting insects are drawn to the carbon dioxide you exhale when breathing. 
Body heat: Higher body temperature can make you more noticeable to bugs. 
Sweat and skin bacteria: The chemicals in your sweat, including lactic acid, and the bacteria on your skin can attract biting insects. 
Blood type: Some studies suggest that certain blood types may be slightly more attractive to mosquitoes. 
Pregnancy: Pregnant women often produce more carbon dioxide and may be more attractive to biting insects. 
Clothing color: Dark colors tend to attract more bugs than lighter colors." 


"kare" "..."
"kare" "...."
"kare" "?"
show butter neutral at left
"butter" "?"
"kare" "you again?!"
"kare" "were in the same class? school even?!"
"butter" "ofcourse! how did you not notice with my uniform"
"kare" "why the hell are you going into the opposite direction where the school at if you were also going to this school?!"
"butter" "..."


play sound "20 February_2025.mp3" fadein 1.0 volume 0.8 fadeout 1.0
show butter punch with dissolve
"" 
stop music fadeout 3.0

play music "battle1.mp3" fadein 5.0 volume 0.5 fadeout 1.0

show block_punch
""
"butter" "?!"
"kare"  "no"
"butter" "smh"


play sound "minigun_hold.mp3" fadein 1.0 volume 0.3 fadeout 1.0
show minigun_hold with dissolve
"kare" "?!"
"kare" "where did you pull out that minigun?!!?"
"butter" "you want to know?"
"butter" "i honestly don't know"

show minigun_shoot with dissolve
play sound "minigun_shoot.mp3" fadein 1.0 volume 0.3 fadeout 1.0 loop

"teacher" "What can you do to prevent bug bites? well just use insect repellent: Apply insect repellent containing DEET or other effective ingredients to exposed skin. 
Wear protective clothing: Cover your skin with long sleeves and pants when in buggy areas. 
Stay indoors during peak bug hours: Avoid being outside during dusk and dawn when mosquitoes are most active. 
Reduce body odor: Shower regularly and wear clean clothes. 
Consider your environment: If you live in an area with a high mosquito population, take extra precautions."

"butter" "stop dodging it!!!!!"
"kare" "stop shooting me!!!"
"butter" "ok"
"butter" "wait nvm"

label choices:
"kare" "ahhh what do i do"

menu:
    "grab a handgun out of nowhere":
        "kare" "huh? wheres my handgun"
    "summon a sword":
        "kare" "eh? the sword didnt show up?"
  


"game" "the developer doesnt know how to code that yet"

"kare" "FUCK"

scene classroom
   
show dobe_neutral at left
show kare_neutral at right

"dobe" "kare what is happening? why is she shooting you"
"kare" "do i look like i know!!!"
"dobe" "who is she?"
"kare" "i dont know, we ran by each other this morning and also the person who got me a headache"
"dobe" "ooooohhh"
"dobe" "don't worry kare i got something for you"
"kare" "what is it?"

show rpg7
"dobe" "a RPG-7!!!"
"kare" "how did you where did you get that?!"  
"dobe" "i honestly don't know"
"kare" "i gotta get outa here"  

stop sound fadeout 3.0
scene classroom

show kare_neutral at left
show butter_neutral at right

"butter" "nuh uh!!! you are not leaving!!!" 
"kare"  "what do you want?!"
"butter" "..."
"butter" "the moment we bumped into each other,i think i recognize who you are now"
"kare" "what? we literally just met 5 hours ago"
"butter" "do you not remember?"
"kare" "nope"
"butter" "i'll make you remember then"
"kare" "huh"

play sound "Explosion Sound Effect.mp3" volume 2.0
show flash
with dissolve
scene school


show kare_neutral at left
show butter_neutral at right
"kare" "...?"
"kare" "are we outside school"
"kare" "in an instant?! how."

hide kare_neutral
hide butter_neutral

call battle_butter_simple from _call_simple_battle_graphics
    
# After battle ends, return to story
scene school
with fade
show kare_neutral at left
show butter_neutral at right
    
"kare" "haaah... so tired"
"butter" "..."
    
menu:
    "summon a tank":
        "kare" "cmon i need something"
    "grab a glock 17 out of nowhere":
        "kare" "cmon i need something"
  
"game" "like i said bro theres no code for that ye-"
"kare" "this no good game dev man hire some team already!!"
"tuumatae" "fuck you"
"butter" "who are you talking to"
"kare" "dobe!!!!"
show dobe_neutral at center
"dobe" "dobe"
"kare" "give me something!!!"
"dobe" "ok"
"ACQUIRED WEAPONRY ASSETS somehow"
"kare" "thanks dobe"

"kare" "can i get a tank now"
"TANK ACQUIRED"
play sound "Building Collapse Destruction Sound Effect.mp3" fadein 1.0 volume 2.0 fadeout 1.0
show tank with dissolve
"butter" "A TANK?!"
"kare" "ha! you are so dead now"
"kare" "..."
"kare" "uhm.. how do i operate this"

play sound "Nuclear explosion sound effect.mp3"  fadein 1.0 volume 2.0 fadeout 03.0
"butter" "i cast nuclear bomb!!! "

scene school
show kare_neutral at left
show dobe_neutral at right
"kare" "what did she say?"

"dobe" "i think she said like nucle-"

show flash with dissolve
show nuke
"kare" "WHAT THE HELL!!!"
"kare" "WHY DID YOU BOMB THE CITY"
"butter" "oh uh i forgot to set the coordinates"
"dobe" "don't worry, ive seen this before"
"kare" "uuuuhh give me some kind of uh time machine that can bring me back before the nuclear explosion or something"
"WEAPONRY ASSETS COOLDOWN 30948543HOURS"
"kare" "WHAT"
"butter" "lol!! you cant escape now!"
"butter" "interdimensional portal gun!!"
"butter" "well im off now goodbye"
"kare" "nuh uh"
"butter" "hey!!! get off me!!"

"butter" "get off!!"

hide nuke
scene flash  
stop music fadeout 3.0

play sound "Time Warp Sound Effect.mp3" volume 1.0 fadeout 3.0

show kare_male at left
"kare" "ah.. where am i.."
show dobe_neutral at right
"dobe" "ah kare! found you!"
play music "normal1.mp3" fadein 1.0 volume 0.5 
"dobe" "..."
"dobe" "kare whats with the new haircut"
"kare" "?"
"kare" "dobe..."
"kare" "i think im a guy now"
show butter_male at center
"butter" "WHAT why did you follow me"
"kare" "because we dont want to be oblitered to dust by that nuke"
"butter" "fair"
"dobe" "where are we?"
"butter" "whats with the haircut bro"
"butter" "?!"
"butter" "did i just called you bro?"
"dobe" "isnt that a gender neutral thing"
"butter" "nah i never said that word in my life "
"butter" "its probably this interdimensional portal gun that changed us"
"dobe" "uhm i dont think thats how entering other dimesions works"
"butter" "anyway since you guys are not dead yet we'll have to continue our battle"
"kare" "why are you trying to kill me anyway?"
hide kare_male 
hide dobe_neutral
"butter" "it all happened back in"
"kare" "i aint listening to all that"
"butter" "..."
play sound "20 February_2025.mp3" fadein 1.0 volume 0.8 fadeout 1.0
show butter punch 
with dissolve
""

scene flash

show karehurt_male at center 
"kare" "can you stop spamming the same move"
"kare" "can we just go back to our dimension already, uhm the one you didn't destroyed yet"
show karehurt_male at left
show butter_male at right 
"butter" "ok"
play sound "Time Warp Sound Effect.mp3" volume 1.0 fadeout 3.0
play music "calm1.mp3" fadein 1.0 volume 0.5 fadeout 1.0
scene outside

show kare_neutral at left
show butter_neutral at right 
show dobe_neutral at center
"kare" "finally back to normal"
"dobe" "yeah!! normal!!"
"butter" "just like yesterday"
"kare" "a normal yesterday"
"dobe" "say that again?"
"kare" "hey im kare by the way whats yours?"
"butter" "im butter" 
"kare" "oh butter that sounds a bit familiar"
"kare" "hey.. what happened yesterday again?"

scene outside

show butter neutral at center
"butter" "uuuh i honestly dont rememb-"
play sound "Flashbang Sound Effect.mp3" volume 0.6
show flash with dissolve
show butter_uhm with dissolve
"butter" "..."
"kare" "uhm butter?"
"dobe" "did she broken?"
"kare" "i think she needs ibuprofen"
stop music
play music "Wind Sound SOUND EFFECT - No Copyright.mp3" fadein 1.0 fadeout 1.0
show sleep with dissolve
"it seems she has failed to eradicate you"
scene outside

show lumpi_nuetral at right
""
show kare neutral at left
"kare" "?"
"kare" "who you?"
"lumpi" "i am lumpi, i will be replacing that failure from now on and"
"kare" "replacing? wdym"
"lumpi" "..."

scene flash

show lumpi_grab with dissolve

"lumpi" "don't you have any manners!!!, when someone is talking you dont talk over them!!"
"lumpi" "i am here to stop you this day this now and today!!"
show lumpi_grab2 with dissolve
"kare" "stop me? lady what are you talking about"
"lumpi" "it all happened back when you-"
"kare" "who?"
"lumpi" "you"
"kare" "cares"
"lumpi" "..."
"lumpi""i understand why you are needed to be out of this planet now"
"dobe" "kare!!!"
stop music
play sound "jump.mp3" volume 2.0
show lumpi_grab3 with dissolve
"kare" "im gonna need some context lady"
"kare" "also im tired af can i go home pls i just went to another dimension a mere minute ago"
"lumpi" "you want to go home?"
"kare" "yup"
"lumpi" "then ill bring you there!! ill end it right here and right now!!!"
scene flash
play music "battle2.mp3" fadein 3.0 volume 0.5 fadeout 1.0
show moon
play sound "Meteorite Impact.mp3" fadein 1.0 fadeout 2.0 volume 2.0
"lumpi" "HHHYAAAAHHH!!!!!!"

"kare" "oh"
show kare_owie
"kare" "ouch"
"SHES ONE SHOT!!! SHES ONE SHOT!!!"
hide kare_owie
hide moon
scene flash 
show lumpi_yell with dissolve
play sound "Crowd Battle Scream.mp3" volume 2.0
"lumpi" "JUMP HER"
show lumpi_army with dissolve
"kare" "tf ???"
"kare" "WHO ARE YOU PEOPLE!!!"
show kare_owie
"kare" "oh hell nah"

menu:
    "summon a robot titan":
        "kare" "MEGA ROBO SOMETHING!!!!" 
        "MEGA ROBO SOMETHING ACQUIRED"
        play sound "Building Collapse Destruction Sound Effect.mp3" volume 3.0
        "kare" "finally"
        show supermegarobot
        ""
        play sound "Laser sound effects.mp3" fadein 1.0 volume 3.0 fadeout 1.0 
        "kare" "haha!!! i am at the advantage"
        "lumpi" "man you guys are trash"

        scene outside
        show lumpi_nuetral at center
        "lumpi" "fine, ill do it myself"
        show supermegarobot_destroyed
        play sound "deadrobot.mp3" fadeout 5.0 volume 2.0
        "kare" "my cool robot!!!"
        play sound "Building Collapse Destruction Sound Effect.mp3" fadein 1.0 volume 2.0 fadeout 1.0 
   
       
        "lumpi" "hey!!!"
        "kare" "huh"
        "kare" "ah... this stick will do"
        
    
    "grab a stick":
        "kare" "uhm i forgot how to do the weapon thing but this will do"
        show kare_stick
        "lumpi" "HUH how is a stick doing numbers to a thousand army???"
        "person" "im tired, boss"

        scene outside
        show lumpi_nuetral at center
        "lumpi" "fine, ill do it myself"
        "lumpi" "hey!!!"
        "kare" "huh"

call battle_lumpi_standard from _call_lumpi_battle

play sound "Berserk Clang Sound Effect.mp3" volume 2.0
show kare_lumpi_fight with dissolve
"lumpi" "what the"
"kare" "bro how is your sword losing to a stick i just found"
"lumpi" "HOW IS MY SWORD LOSING TO A STICK SHE JUST FOUND?!!?"
"kare" "idk"
"lumpi" "(shes more powerful than i expected, im so stupid i should've brought more people)"
"lumpi" "tsk"
"dobe" "ah kare!! i found you"
"kare" "dobe!!"
"lumpi" "back off kid this place is too dangerous!!!"
"dobe"  "kare who is this lady"
"kare" "idk just some random old lady who wants beef with me like butter"
"kare" "where is butter anyway"
"dobe" "uh shes just staring at the void so i left her"
"kare" "oh ok"
stop music 
"lumpi" "SILENCE"
"lumpi" "..."
"lumpi" "excluding you background music"
"background music" ":D"
play music "battle2.mp3"  volume 0.3 fadeout 1.0
"kare" "lady can you hop off me already?"
scene outside
show lumpi_nuetral at center
"lumpi" "no! you are not suppose to be walking!!!"
"lumpi" "hey you, child!! you are not suppose to be near that thing!! do you have any idea who you are with right now!! that thing will soon destroy the world and everything just by her presence!! "
hide lumpi_nuetral
show dobe_neutral at center
"dobe" "who?"
hide dobe_neutral
show lumpi_nuetral at center
"lumpi" "her!!"
hide lumpi_nuetral
show dobe_neutral at center
"dobe" "oh"
hide dobe_neutral
show lumpi_nuetral at center
"lumpi" "..."
"lumpi" "so-"
hide lumpi_nuetral
show dobe_neutral at center
"dobe" "kare has been my day 1, if she one day becomes a villain and drestroy the world i will be by her side, if the world is against her, i am against the world."
hide dobe_neutral
show lumpi_nuetral at center
"lumpi" "so be it."
"lumpi" "LEGENDARY SWORD OF SPACE"
"dobe" "DISABLITY GUN!!!!"
play sound "Gunshot Sound Effect.mp3" volume 3.0
"lumpi" "what the hell does that do-"
show disabledlumpi with dissolve
"lumpi" "MY LEGS"
"kare" "thats our chance!! jump her!!!"
"lumpi" "NO YOU DON'T!!!"

call battle_lumpi_wheelchair from _call_lumpiwheelchair_battle

show realmexpansion with dissolve
"lumpi/dobe/kare" "REALM EXPANSION:"
"lumpi/dobe/kare" "FINITE SPACE!!! I EAT CHALK!!!!  SCENE OF █████!!! "
"lumpi" "HA!!! MINE WINS "
"lumpi" "within this space you cannot escape nor hide "
play sound "audio/scary-siren-air-raid-tornado-nuke-7010.mp3"  fadein 1.0 volume 10.0 fadeout 03.0
"dobe" "I CAST NUCLEAR BOMB"
"lumpi" "ARE YOU A DUMBASS!! WE ARE TRAPPED IN HERE, YOU ARE GOING TO GET ALL OF US KILLED WITHIN THIS SPACE"
play sound "audio/nuke-333673.mp3" volume 2.0
show lumpi_hurt with dissolve
"lumpi" "tsk we are outside again"
"lumpi" "i wont even question how we survived"
"lumpi" "i need to get rid of her before it gets worse"
"lumpi" "...?"
"lumpi" "huh?"
show butter_stand with dissolve
"lumpi" "is that..."
"kare" "butter?"
"butter" "..."
play sound "20 February_2025.mp3"  fadein 1.0 volume 2.0 fadeout 03.0
show butter_punch with dissolve
"..."
stop music
play music "Wind Sound SOUND EFFECT - No Copyright.mp3" fadein 1.0 volume 5.0
"kare" "augh.."
hide butter_stand
hide butter_punch with dissolve
show lumpi_hurt with dissolve
"lumpi" "ah.."
"lumpi" "finally some backup.."
"lumpi" "i wont be alone anymore"
"lumpi" "butter"
"lumpi" "go get that tiny one ill get the main one"
"butter" "..."
"butter" "no"
"butter" "im going for her, not you"
"lumpi" "what? i said-"
show sleep with dissolve

show butter_scene with dissolve
"butter" "..."
"butter" "kare, no..."
"butter" "CHAOS.."
"butter" "cease your life"
"butter" "and go back where you should belong.."
"butter" "conclude this fatuous game of yours."
show kare_scene with dissolve
"kare" "..."
"kare" "?"
hide kare_scene
show butter_scene with dissolve
"butter" "stubborn as always"
"butter" "everywhere you journey, every atoms of you spread throughout all over the place, far and near, in every corner, in every quarter, all over the map."
"butter" "you will only bring annihilation to this world if you keep on living in that form of yours"
"butter" "where did you even find that pitiful body of yours"
"butter" "ill pay no heed for that matter, you have been quite the trouble after mother O has been absent."
hide butter_scene
show kare_scene with dissolve
"kare" "what the FUCK are you talking about"
"butter" "haaaah..."
stop music

play music "battle1.mp3" fadein 0.5 volume 0.5 fadeout 1.0
show karebutterfight with dissolve
"butter" "i had enough of your childish behavior"
"kare" "what???"
"butter" "haah.. It must be that pile of flesh of yours that is the reason you fail to recall."
"butter" "worry not, i will beat the shit out of you until that empty head of yours resurrect it"
play sound "Berserk Clang Sound Effect.mp3" volume 2.0
show karebutterfight2 with dissolve
"kare" "gaughh!!!!!"
"butter" "stop resisting!!"
"kare" "aren't you also in a pile of flesh destroying everything?"
"kare" "you cannot be the one to talk..."
"butter" "don't lecture me CHAOS, have you even listened to everything i said?"
"butter" "everything thats happened here this day because of you, every reason why everyone around you is destroying everything"
"butter" "even me!!! CHAOS!!! your mere presence made me launch a nuke!! "
"kare" "dont give every fault of yours to me!!!!!"
"kare" "my name is not whatever you're calling me!!!! "
"butter" "SILENCE!!!!!"
menu:

    "interitus":
        "butter" "no you dont!!"

    "dissolutum":
        "butter" "no you dont!!"

    "evanesco":
        "butter" "no you dont!!"


"butter" "interdimensional portal gun!!!" 
"butter" "(i have to get her out of this world, every bits of her power is manifesting every second..)"
play sound "Meteorite Impact.mp3" fadein 1.0 fadeout 1.0 volume 1.0
"butter" "HYAAAAH!!!"
"kare" "augh"
show karebutterfight3 with dissolve
"kare" "stop this"
"butter" "not until you surrender!!!"
play sound "Time Warp Sound Effect.mp3" fadein 1.0 fadeout 1.0 volume 1.0
"kare" "ahhk.."
play sound "Berserk Clang Sound Effect.mp3" volume 2.0
"butter" "persistent as always "
"kare" "..."
play sound "Time Warp Sound Effect.mp3" fadein 1.0 fadeout 1.0 volume 1.0
"butter" "meow!!"
play sound "Berserk Clang Sound Effect.mp3" volume 2.0
"kare" "meow meow"
play sound "teleport-90137.mp3" fadein 1.0 fadeout 1.0 volume 1.0
"kare" "uughhh.."
"kare" "?!?"
"butter" "fret not CHAOS we're almost there"
"butter" "HA!"
play sound "Berserk Clang Sound Effect.mp3" volume 2.0
"kare" "aaugh!!"
play sound "Time Warp Sound Effect.mp3" fadein 1.0 fadeout 1.0 volume 1.0
"kare" "ugh"
play sound "minigun_shoot.mp3" fadein 1.0 fadeout 1.0 volume 0.3
"kare" "...gun"
"butter" "tsk"
play sound "Berserk Clang Sound Effect.mp3" volume 2.0
"butter" "HAAH!!!"
play sound "Meteorite Impact.mp3" volume 2.0
"butter" "shield!!"
"butter" "enough!!!!!!"
play sound "Laser sound effects.mp3" fadein 1.0 fadeout 1.0 volume 3.0
"kare" "gaah!!"
"kare" "haaah..."
play sound "Berserk Clang Sound Effect.mp3" volume 2.0
"butter" "HAAAH!!!!!!"
call battle_serious_butter from _call_newenemy_battle
show portal_kick with dissolve 
play sound "teleport-90137.mp3" fadein 1.0 fadeout 1.0 volume 1.0
"kare" "AH"
stop music
play music "Big house fire sound effect.mp3" fadein 1.0 fadeout 3.0 volume 0.6
show sleep with dissolve
hide portal_kick
show butter_real with dissolve
"kare" "haaah"
"kare" "haaah...cough..."
"butter" "..."
"butter" "why do you want to stay here so bad.."
"butter" "you are not suppose to be here."
"butter" "you are not suppose to inhabit with humanity"
"butter" "please just let me make this easy for me, and you"
"butter" "will you?"
menu:

    "interitus":
        "butter" "!!!"

    "dissolutum":
        "butter" "!!!"

    "evanesco":
        "butter" "!!!"

play sound "explosion-large-129051.mp3" volume 3.0
scene sleep
"butter" "GAAAGHGHH!!!!!"
"butter ""AAAUHH..."
"butter" "haaah..."
"butter" "you would not listen..."
play sound "punch-140236.mp3" volume 7.0
show kare_real with dissolve
"kare" "..."
play sound "punch-140236.mp3" volume 7.0
"kare" "hhngh.."
play sound "breeze-of-blood-122253.mp3" volume 7.0
""
show kare_real with dissolve
play sound "punch-140236.mp3" volume 7.0
scene sleep
""
show kare_real with dissolve
play sound "punch-140236.mp3" volume 7.0
scene sleep
""
show kare_real with dissolve
play sound "breeze-of-blood-122253.mp3" volume 7.0
""
show kare_real with dissolve
play sound "punch-140236.mp3" volume 7.0
scene sleep
""
show kare_real with dissolve
play sound "punch-140236.mp3" volume 7.0
scene sleep
show kare_real with dissolve
play sound "punch-140236.mp3" volume 7.0
scene sleep
""
show kare_real with dissolve
play sound "punch-140236.mp3" volume 7.0
scene sleep
""
show kare_real with dissolve
play sound "punch-140236.mp3" volume 7.0
scene sleep
""
show kare_real with dissolve
play sound "punch-140236.mp3" volume 7.0
scene sleep
stop music

"..."
"...."
"sis!!!"
"sister!!!"
play music "おーたむうぉーきんぐ @ フリーBGM DOVA-SYNDROME OFFICIAL YouTube CHANNEL.mp3"  fadein 1.0 fadeout 1.0 volume 1.0
scene placeidk

show chaos_neutral
"CHAOS" "sister!!!sister!!!!"
"CHAOS" "look i found a fish!!!!"
hide chaos_neutral
show order_neutral 
"ORDER" "..."
"ORDER" "thats a frog, CHAOS."
hide order_neutral
show chaos_neutral
"CHAOS" "whats the difference?? i heard all fish lives in the water and this frog is swimming"
hide chaos_neutral
show order_neutral 
"ORDER" "..."
show sleep with dissolve
scene placeidk
show chaos_neutral 
"CHAOS" "sister!!!sister!!!!"
"CHAOS" "im bored!!!!"
"CHAOS" "i found some weird looking things like us somehwere!!!"
hide chaos_neutral
show order_neutral 
"ORDER" "..."
"ORDER" "those are humans, CHAOS."
"ORDER" "also how did you even find-"
hide order_neutral
show chaos_neutral
"CHAOS" "waaauhh!! humans?? can i play with them??"
hide chaos_neutral
show order_neutral 
"ORDER" "no"
hide order_neutral
show chaos_neutral
"CHAOS" "WAAAAAAAAAAHHHHHHH!!!!!!!!!!"
show sleep with dissolve
scene placeidk
show chaos_neutral at left
show order_neutral at right
"ORDER" "CHAOS."
"ORDER" "im just gonna go get milk"
"ORDER" "so do NOT go anywhere"
"CHAOS" "ok!"
"ORDER" "...."
show sleep with dissolve
scene placeidk
show chaos_neutral at center
"CHAOS" "..."
hide chaos_neutral with dissolve
"CHAOS" "sneaky sneaky"
scene city
show chaos_neutral with dissolve 
"CHAOS" "wwoooaaah pretty!!!"
"CHAOS" "oh!!! its a people!!!"
"CHAOS" "hello friend!!! can we be friends!!!!"
hide chaos_neutral
show kare neutral with dissolve
"kare" "...?"
hide kare_neutral
show flash
with dissolve
show chaos_smile
"CHAOS" "hello!!!"
"kare" "erm.. go home little kid im late for school"
"CHAOS" "no!! im bored!!"
"kare" "wheres your parents?"
"CHAOS" "parents?"
"kare" "uhm.. the one who takes care of you?"
"kare" "dont tell me..."
"CHAOS" "oh! my sister!!!"
"kare" "oh thats good, yes."
"kare" "your sister"
"kare" "go home!!!"
"CHAOS" "no!"
"kare" "ugh i need to hurry to school"
"CHAOS" "school?"
"kare" "ugh where do you live?"
"CHAOS" "uuuuh i forgot"
"kare" "WHAT"
"CHAOS" "thats ok sister will find me!!"
"kare" "..."
"kare" "(i could sell this kid to some shady people and make some quick cash)"
"kare" "(WHAT WHO WAS THAT)"
"kare" "(its me, your inner thoughts!!!)"
"kare" "(what- get out)"
"CHAOS" "umm lady?"
"kare" "huh?"
"kare" "ah- ahaha i got a little zoned out my bad"
"CHAOS" "oh!! okay!!!"
"CHAOS" "lets play today!!!!"
"kare" "uhm.. i guess skipping school wont be bad"
"kare" "sure"
stop music fadeout 0.5
play music "audio/Crowd panic sound effect.mp3" volume 0.6
play sound "audio/Big house fire sound effect.mp3" volume 0.6
show city_burn
"kare" "...."
"kare" "..."
"kare" "ahh..."
"kare" "im going to need to move to another country..."
"CHAOS" "huahwahwahwahwwa!!! that was fun!!!"
"kare" "come on lets go before somebody finds us..."
stop music
stop sound
hide City_Burn
play music "audio/ふわふわ夢牧場 @ フリーBGM DOVA-SYNDROME OFFICIAL YouTube CHANNEL.mp3" fadein 1.0 volume 1 fadeout 1.0
scene city
show kare_neutral at left
show chaos_neutral at right
"CHAOS" "hey human what do i call you!!"
"kare" "um.. you mean my name? im kare"
"CHAOS" "wowow!! im my sister calls me CHAOS"
"kare" "make sense"
"kare" "is your sister your only family?"
"kare" "you dont have parents?"
"CHAOS" "nope!! just my sister and friend!!"
"kare" "friend?"
"CHAOS" "yyeahyeahyea!! shes so cute!!!"
"CHAOS" "we play together all the time!!!"
show bg with dissolve
scene placeidk
hide city
hide kare_neutral 
hide chaos_neutral


show order_neutral at right
"ORDER" "CHAOS, ive found my new bearer"
"ORDER" "her name is butter."
"ORDER" "be nice to her"
"ORDER" "she's a little shy at first but im sure you two will get along"
show butter_shy at center with moveinbottom
"ORDER" "come on now butter greet her"
"butter" "um..."
hide order_neutral 
show chaos_neutral at center
hide butter_shy
"CHAOS" "wowowoaooawow!!"
hide chaos_neutral
show butter_shy at center
"butter" "auntie CHAOS..."
"butter" "shes...scary"
show chaos_neutral at center
hide butter_shy
"CHAOS" "auntie?"
hide chaos_neutral
show butter_shy at center
show order_neutral at right
"ORDER" "CHAOS stop scaring her"
hide order_neutral
hide butter_shy
show chaos_neutral
hide butter_shy
"CHAOS" "hehehe"
hide chaos_neutral
show butter_shy at center
"butter" "..."
show chaos_neutral
hide butter_shy
"CHAOS" "im not scary!!"
hide chaos_neutral
show butter_shy at center
"butter" "..."
show chaos_neutral
hide butter_shy
"CHAOS" "im your friend now!!"
hide chaos_neutral
show butter_shy at center
"butter" "..."
show chaos_neutral
hide butter_shy
"CHAOS" "lets play together!!!"
hide chaos_neutral
show butter_shy at center
show bg with dissolve   
"butter" "..."

hide butter_shy
scene city 
hide placeidk


show kare_neutral at right
show chaos_neutral at left
"kare" "uhm"
"kare" "CHAOS? hello?"
"kare" "why are you just staring at the sky"
hide kare_neutral
show kare_neutral at center
"kare" "come on let-"
play sound "audio/glitch-sound-effect-450447.mp3" volume 2.0
hide chaos_neutral with pixellate
"kare" "wh"
"kare" "where"
"kare" "ia awie r"
"kare" "where did you go"
"kare" "uagh"
"kare" "..."
"kare" "who was i talking to"
"kare" "i might be schizo"
show bg with dissolve
stop sound

hide chaos_smile
hide city_burn
scene placeidk
show order_neutral 
"ORDER" "CHAOS im home."
"ORDER" "..."

"ORDER" "im stupid"
stop music
show sleep with dissolve
hide order_neutral 
play music "audio/Big house fire sound effect.mp3" volume 0.6

show chaos_ouchie
"CHAOS" "..."
"butter" "ah.."
"butter" "there you are."
"butter" "come with me CHAOS, mother is waiti-"
play sound "audio/heavy-cineamtic-hit-166888.mp3" volume 3.0
show bg with dissolve
hide chaos_ouchie
show chaos_kick
"butter" "HGHAGHHH"
hide chaos_kick
stop music
play sound "audio/Time Warp Sound Effect.mp3" volume 3.0
show butter_owie
"butter" "uagh.."
"CHAOS" "bully"
hide butter_owie
show boutpunch
"butter" "you..."
"CHAOS" "!!"
hide boutpunch
show boutpunch2
"butter" "im really tired you know that"
"CHAOS" "blehblehblehbulbleh"






stop music 
play music "陽気な男 @ フリーBGM DOVA-SYNDROME OFFICIAL YouTube CHANNEL.mp3" fadein 1.0 volume 0.5 fadeout 1.0  
"ava" "STOP FIGHTING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
"butter" "!?!"
show avaaura    
"CHAOS,butter" "..."
"butter" "huh"
"CHAOS" "wow that person looks so cool"
"ava" "thanks"
hide avaaura
show huh
"ava" "you!! villain!!"
hide huh
show huh2
"butter" "are you pointing at me?"
"ava" "YES!! you better stop hurting that poor human right now!!"
"butter" "wh- huh who are you exactly?"
hide huh2
show ava
"ava" "i am... ava!!! the one and only bearer of CIVILIZATION!!"
"butter" "...?"
"ava" "bearer of CIVILIZATION!!!"
"butter" "i heard it the first time"
"ava" "you are gonna face concequences for causing damage to humanity!!!"

"butter" "which side are you fool"
"butter" "and what kind of bearer of civilization wears something like that"
"ava" "i am in the humanity side!!!"
"butter" "FYI im trying to bring order to humanity"
"butter" "this brat right here is the one causing all this destruction"
"ava" "oh"
"ava" "my bad gang"
scene city
hide ava
hide placeidk


play sound "audio/dapup.mp3" 
$ renpy.movie_cutscene("video/dapup.webm", stop_music=False)
show ava_sprite at right
show butter_neutral at left
"butter" "whwhat the how did you make me do that"
"ava" "anyway!! whatever is causing the destruction will be stopped!!!!"
"ava" "fellow small one, with our combined power we will be unstoppable!!! hauhauha!!"
"butter" "excuse me?"
"butter" "first of all im not your ally"
"butter" "also im not small"
"butter" "there is no way im teaming up with you"
"ava" "what whats wrong with teaming up"
"butter" "i'd rather not"
"ava" "too late we're teaming up"
"butter" "HEY YOU DON'T GET TO DECIDE THA-"

stop music
play music "audio/swing swing @ フリーBGM DOVA-SYNDROME OFFICIAL YouTube CHANNEL.mp3" volume 0.8
call battle_boss_ava_butter from _call_butter_ava_battle
scene city 
show ava_sprite at center
"ava" "HA!! just so you know that you can not kill me until all humanity is wiped which would be impossible by the fact that there are currently 8 billion people in the world so you would take about 943482348234924 years to kill all of them and also the fact that "
hide butter_neutral
hide ava_sprite 
show kare_chaos at center
"CHAOS" "i understand it now"
hide kare_chaos
show ava_sprite at center
"ava" "what do you mean"
play sound "audio/finger-click-455199.mp3" volume 5.0
show earth
play music "audio/invisibility-spell-98622.mp3" volume 3.0

"ava" "huh"
"ava" "..."
hide earth
$ renpy.movie_cutscene("video/awnaw.webm", stop_music=False)
"ava" "WHAAAAAT!!!!!"
"ava" "oh naw!!!"

"CHAOS" "you not as powerful as you say now huwahuwhauwhauhwa"
stop music
play music "audio/(Free) Horror Ambiance - Ominous Background Music.mp3" volume 1.0
show deathcall
"DEATH" "yes hello?"
"DEATH" "what?"
"DEATH" "mass extinction?"
"DEATH" "what are you talking about"


"DEATH" "..."
scene city
hide deathcall

show death_neutral at center

"DEATH" "WHO THE HELL KILLED ALL THE HUMANS!!!!!!!!"
hide death_neutral
show death_neutral at right 
show ava_sprite at left
"ava" "DEATH... thank god you're here"
"DEATH" "IM GONNA BE UNEMPLOYED!!!!"

hide death_neutral 
hide ava_sprite 
show lifecall
"LIFE" "yes hello?"
"LIFE" "mass extinction?"
"LIFE" "..."
"LIFE" "oh just humans, not other lifeforms?"
"LIFE" "yeah im not dealing with that"
"LIFE" "good riddance"
show sleep with dissolve
scene bg
hide lifecall
call battle_boss_ava_butter_phase2 from _call_butter_ava_battle2

show ava_sprite at center
"ava" "..."
"ava" "theres only one way to fix this"
"ava" "we are gonna make more humans"
hide ava_sprite
show death_neutral at center
"DEATH" "but how are we gonna do that?"
show ava_sprite at center
hide death_neutral
"ava" "WE ARE GOING TO REPRODUCE"
show death_neutral at center
hide ava_sprite
"DEATH" "huh"
show ava_sprite at center
hide death_neutral
"ava" "YES, WE ARE!! IVE BEEN WAITING FOR THIS!!!"
show death_neutral at center
hide ava_sprite
"DEATH" "you did?"
hide death_neutral


show order_neutral
"ORDER" "what the hell is going on here"
hide order_neutral
show kare_chaos
"CHAOS" "a-"
show order_neutral
hide kare_chaos
"ORDER" "...?"
"ORDER" "CHAOS... finally found you."
"ORDER" "you've made quite a mess after my absence, though that seems to be my fault..."
"ORDER" "anyway what mess did you do this time?"
hide order_neutral
show kare_chaos at left
show order_neutral at right
"CHAOS" "uhm.. humanity extinction"
"ORDER" "ah.."
"ORDER" "don't worry lets put it back to normal"
hide order_neutral
hide kare_chaos
show butter_neutral
"butter" "WHA-"
show earth 
play sound "audio/magic-03-278824.mp3" volume 2.0 
stop music
play music "audio/春のキッチン @ フリーBGM DOVA-SYNDROME OFFICIAL YouTube CHANNEL.mp3" volume 0.6



"ORDER" "and done"
hide earth
show order_neutral at right
show butter_neutral at left
"butter" "MOTHER?! if you could do that why didn't you stop her earlier?!"
"ORDER" "uhm"
"ORDER" "im lazy"
"probably the readers" "ermm thats just bad writing"
"ORDER" "shut up"
"butter" "who are you talking to"
"ORDER" "anyway this isnt the first time this twerp committed mass extinction"
"butter" "..."
"ORDER" "im taking her back lets go home"
hide order_neutral
hide butter_neutral
show kare_chaos at center
"CHAOS" "wait sis!!"
"CHAOS " "my friend kare"
"CHAOS" "i think im stuck in her body"
hide kare_chaos
show order_neutral at right
show butter_neutral at left
"ORDER" "come to think of it you do look a tad bit different... you grew a lot more"
"butter" "..."
hide order_neutral
hide butter_neutral
show kare_chaos at center
"CHAOS" "how can we fix my friend's body"
hide kare_chaos
show order_neutral at right
show butter_neutral at left
"ORDER" "oh its simple"
"ORDER" "we'll have to probably most likely definetely destroy it"
hide order_neutral
hide butter_neutral
show kare_chaos at center
"CHAOS" "wwhat"
hide kare_chaos
show order_neutral at right
show butter_neutral at left
"ORDER" "destroy the vessel"
"ORDER" "and you will be released along with the other one"
"ORDER" "its like hmm think of it like your current body is an eggshell"
"ORDER" "and the human is the yolk and you are the eggwhites"
"ORDER" "we have to break it so you can come out"
hide order_neutral
hide butter_neutral
show kare_chaos at center
"CHAOS" "waah i understand!!"
"CHAOS" "sister whats an egg!!"
hide kare_chaos
show order_neutral at right
show butter_neutral at left
"ORDER" "yes"
"ORDER" "anyway butter execute her"
"butter" "okay"
hide order_neutral
hide butter_neutral
show kare_chaos at center
"CHAOS" "a-"
play sound "audio/sword-slash-and-swing-185432.mp3" volume 2.0 
hide kare_chaos with pixellate
show kare_stupid at left
show chaos_neutral at right
"kare" "hhuh"
"CHAOS" "waaah kare ur back"
"kare" "wh huh wh huh huh au oau au"
"kare" "wh huh wh "
"kare" "aoaok uah o a"
hide kare_stupid at left
hide chaos_neutral at right
show butter neutral at right
show order_neutral at left
"butter" "erm"
"ORDER" "dont worry she'll be fine"
hide butter neutral at right
hide order_neutral at left
show dobe_neutral at left
show kare_stupid at right
"dobe" "kare!!"
"kare" "douh!!"
"dobe" "uhm.."
"ORDER" "shes fine"
"dobe" "ok"
hide dobe_neutral at left
hide kare_stupid at right
show lumpi_nuetral at left
"lumpi" "ugh..."
show order_neutral at right
"ORDER" "lumpi.."
"lumpi" "dont even talk to me"
"ORDER" "ooh? still a bit pissed at me?"
"lumpi" "..."
"ORDER" "and i thought we could work together again"
"lumpi" "..."
"lumpi" "hahh.. shut up"
"ORDER" "if you say so"
hide lumpi_nuetral
hide order_neutral
show kare_stupid at left
show chaos_neutral at right
"CHAOS" "i guess i have to go now kare"
"CHAOS" "i had lots of fun playing with you"
"CHAOS" "promise me we'll play together again in the future"
"kare" "haueh ho!! (HELL NO)"
"CHAOS" "YAY!! ill see you next time!!"
hide kare_stupid at left
hide chaos_neutral at right
show time_neutral 
play sound "audio/jump.mp3" volume 2.0 
"TIME" "GUYS THE WORLD IS ABOUT TO END!!!!!"
"TIME" "WE NEED TO STOP THIS!!!!!"
"TIME" "I KNOW WHO THE CULPRIT IS!!!!!"
"TIME" "ITS THE ONE WHO HAS BEEN CAUSING ALL THIS SINCE THE BEGINNING OF TIME!!!!!"
"lumpi" "erm its over buddy"
"butter" "the world is fine now"
"TIME" "wha huh"
"DEATH" "yeah its pretty much resolved"
"TIME" "but..but"
"butter" "for a concept that has been around since the beginning of time you sure are late"
"ava" "who invited you!?"
"lumpi" "go home TIME"
"TIME" "hw..sniff..ok"
hide time_neutral
show order_neutral at center
show chaos_neutral at right
show butter_neutral at left
"ORDER" "...i guess its time to go home"
"ORDER" "see you all when the world is in chaos again"
"CHAOS" "BYEBYE!!!!!!"
"butter" "farewell"
"butter" "oh by the way i still go to school so ill see you guys tommorow"
hide order_neutral at center
hide chaos_neutral at right
hide butter_neutral at left
show dobe_neutral at right
show kare_stupid at left
"dobe" "really? we're still classmates?"
"kare" "oau (HELL NO)"
"butter" "yup"
"dobe" "hm? you sound normal again"
"dobe" "weren't you speaking all formal and fancy earlier?"
show order_neutral at center
show chaos_neutral at right
show butter_neutral at left
hide dobe_neutral
hide kare_stupid
"ORDER" "oh thats because butter"
"butter" "MOTHER SHSHUT UP"
play sound "audio/Time Warp Sound Effect.mp3" volume 2.0 
"..."
hide order_neutral at center
hide chaos_neutral at right
hide butter_neutral at left
show dobe_neutral at center
hide kare_stupid
stop music
play music "audio/ふわふわ夢牧場 @ フリーBGM DOVA-SYNDROME OFFICIAL YouTube CHANNEL.mp3"  fadein 1.0 volume 1.0 fadeout 1.0
"dobe" "and they're gone"
"dobe" "cmon kare lets go back"
show kare_neutral at left
hide dobe_neutral
show dobe_neutral at right
"kare" "yeah.."
"dobe" "oh you're back to normal"
show walk
"kare" "ugh... im never talking to any strange weirdos again"
"dobe" "im glad you are okay, kare"
"kare" "hah.. thanks dobe"
"kare" "wait how did you hold off that old lady for that long?"
"dobe" "you were aware during that whole time?"
"kare" "yeah.."
"kare" "it feels more like im dreaming though"
"dobe" "ohh.."
"kare" "so? how did you hold her off?"
"dobe" "yes"
"kare" "ohh.."
"kare" "you're pretty strong"
"dobe" "thanks"
hide walk
show byebye
"kare" "ill be stopping here, see you tommorow"
"dobe" "see you tommorow kare"
show sleep with dissolve
hide byebye
call battle_credits


 


return