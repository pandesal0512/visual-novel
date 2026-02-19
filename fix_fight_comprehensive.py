
import re

with open('fight.rpy', 'rb') as f:
    content = f.read()

# 1. Add self.is_dodged = False to BattleManager.__init__
content = content.replace(b'self.show_energy_warning = False', b'self.show_energy_warning = False\r\n            self.is_dodged = False')

# 2. Modify animations to respect bm.is_dodged
# We'll use a regex to find all animations and wrap hit/sound lines
def wrap_anims(m):
    anim_content = m.group(0)
    # Wrap hit-related lines
    # Pattern: any line with sprites["hit"], player_sprites["hit"], play sound, camera:
    # but not lines that are already part of an if block
    lines = anim_content.split(b'\r\n')
    processed_lines = []
    for line in lines:
        if (b'sprites["hit"]' in line or
            b'player_sprites["hit"]' in line or
            b'play sound' in line or
            b'camera:' in line) and b'if not bm.is_dodged:' not in line:

            indent = re.match(b'^\s*', line).group()
            processed_lines.append(indent + b'if not bm.is_dodged:')
            processed_lines.append(b'    ' + line)
        else:
            processed_lines.append(line)
    return b'\r\n'.join(processed_lines)

content = re.sub(rb'label [a-z0-9_]+_anim\(bm\):.*?(?=\r\nlabel |\r\n#|\r\n\r\n|$)', wrap_anims, content, flags=re.DOTALL)

# 3. Standardize resolution blocks
def get_skill_block(suffix):
    return f"""            if skill.type == "attack":
                if enemy.dodge_active:
                    $ bm.is_dodged = True
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_at_dodge_{suffix}
                    $ dodge_anim = get_dodge_anim(enemy.name)
                    call expression dodge_anim pass (bm) from _call_enemy_dodge_anim_reactive_{suffix}
                    "[enemy.name] dodged the attack!"
                    $ enemy.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if skill.animation:
                        call expression skill.animation pass (bm) from _call_skill_anim_generic_{suffix}
                    $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")
                    $ bm.take_damage(damage, target="enemy", enemy_idx=e_idx)
                    $ bm.gain_exp(damage * 5, character_type="player")
                    "[skill.name] deals [damage] damage to [enemy.name]!"
                    if enemy.is_dead:
                        "[enemy.name] has been defeated!"
                        $ renpy.hide("enemy_" + str(e_idx))
            elif skill.type == "barrier":
                $ bm.add_barrier(skill.damage)
                "You gain [skill.damage] Defense!"
            elif skill.type == "dodge":
                $ bm.dodge_active = True
                "You prepare to dodge!"
            elif skill.type == "buff":
                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")
                "[skill.name] activated! Damage increased by [skill.damage] for [skill.buff_duration] turns."
            elif skill.type == "energy":
                "You gained [skill.energy_regen] Energy!" """.encode().replace(b'\n', b'\r\n')

def get_intent_block(suffix):
    return f"""            if intent.type == "attack":
                if bm.dodge_active:
                    $ bm.is_dodged = True
                    if intent.animation:
                        call expression intent.animation pass (bm) from _call_intent_anim_at_dodge_{suffix}
                    else:
                        call enemy_attack_anim(bm) from _call_intent_anim_default_at_dodge_{suffix}
                    $ p_name = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"
                    $ dodge_anim = get_dodge_anim(p_name)
                    call expression dodge_anim pass (bm) from _call_player_dodge_anim_reactive_{suffix}
                    "DODGED!"
                    $ bm.dodge_active = False
                    $ bm.is_dodged = False
                else:
                    $ bm.is_dodged = False
                    if intent.animation:
                        call expression intent.animation pass (bm) from _call_intent_anim_generic_{suffix}
                    else:
                        call enemy_attack_anim(bm) from _call_intent_anim_default_{suffix}
                    $ damage = intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)
                    $ bm.take_damage(damage, target="player")
                    $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)
                    "[enemy.name] deals [damage] damage with [intent.name]!"
            elif intent.type == "barrier":
                $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)
                "[enemy.name] gains [intent.damage] Defense!"
            elif intent.type == "dodge":
                $ enemy.dodge_active = True
                "[enemy.name] will dodge the next attack!"
            elif intent.type == "buff":
                $ bm.add_buff(intent.buff_type, intent.damage, intent.buff_duration, target="enemy", enemy_idx=e_idx)
                "[enemy.name] activated [intent.name]! Their damage increased by [intent.damage]!"
            elif intent.type == "energy":
                "[enemy.name] is recovering." """.encode().replace(b'\n', b'\r\n')

# Replace blocks in battle_engine
pattern_skill = rb'elif isinstance\(action, Skill\):.*?current_enemy_tag = "enemy_" \+ str\(e_idx\)\r\n\r\n.*?(?=elif isinstance\(action, EnemyIntent\):)'
content = re.sub(pattern_skill, lambda m: m.group(0).split(b'\r\n\r\n')[0] + b'\r\n\r\n' + get_skill_block("generic"), content, flags=re.DOTALL)

pattern_intent = rb'elif isinstance\(action, EnemyIntent\):.*?current_enemy_tag = "enemy_" \+ str\(e_idx\)\r\n\r\n.*?(?=if all\(e.is_dead for e in bm.enemies\):)'
content = re.sub(pattern_intent, lambda m: m.group(0).split(b'\r\n\r\n')[0] + b'\r\n\r\n' + get_intent_block("generic"), content, flags=re.DOTALL)

# Replace blocks in butter_ava_battle (boss1)
# Note: boss1 uses single quotes 'attack' etc.
content = content.replace(get_skill_block("generic"), get_skill_block("boss1").replace(b'"', b"'"))
content = content.replace(get_intent_block("generic"), get_intent_block("boss1").replace(b'"', b"'"))
# Wait, this replace might not work if they are not identical yet.

# I'll just do it for all occurrences of the resolution pattern
def replace_res(m):
    block = m.group(0)
    suffix = "generic"
    if b'boss1' in block: suffix = "boss1"
    if b'boss2' in block: suffix = "boss2"
    # Detect if Skill or Intent
    if b'skill.type' in block:
        return block.split(b'\r\n\r\n')[0] + b'\r\n\r\n' + get_skill_block(suffix)
    else:
        return block.split(b'\r\n\r\n')[0] + b'\r\n\r\n' + get_intent_block(suffix)

# Re-do with better regex
content = re.sub(rb'(elif isinstance\(action, Skill\):|elif isinstance\(action, EnemyIntent\):).*?current_enemy_tag = "enemy_" \+ str\(e_idx\)\r\n\r\n.*?(?=elif isinstance|if all\(e.is_dead for e in bm.enemies\):)', replace_res, content, flags=re.DOTALL)

# Fix boss1_extra_turn
content = content.replace(b'                $ renpy.show("ava_attack", tag="enemy_1", at_list=[Position(xalign=0.75, ypos=0.8, yanchor=1.0)])', b'                if not bm.is_dodged:\r\n                    $ renpy.show("ava_attack", tag="enemy_1", at_list=[Position(xalign=0.75, ypos=0.8, yanchor=1.0)])')
content = content.replace(b"                play sound 'punch-140236.mp3' volume 2.0", b"                if not bm.is_dodged:\r\n                    play sound 'punch-140236.mp3' volume 2.0")

# Fix boss2_extra_turn
content = content.replace(b'            show ava_attack as enemy_1 at Position(xalign=0.85, ypos=0.8, yanchor=1.0):', b'            if not bm.is_dodged:\r\n                show ava_attack as enemy_1 at Position(xalign=0.85, ypos=0.8, yanchor=1.0):')
content = content.replace(b"            play sound 'audio/sword-slash-and-swing-185432.mp3' volume 2.0", b"            if not bm.is_dodged:\r\n                play sound 'audio/sword-slash-and-swing-185432.mp3' volume 2.0")

# Ensure bm.is_dodged = True is set in extra turns
content = content.replace(b'                "[bm.enemies[0].name] dodged the attack from [bm.enemies[1].name]!"', b'                $ bm.is_dodged = True\r\n                "[bm.enemies[0].name] dodged the attack from [bm.enemies[1].name]!"')
content = content.replace(b'            "DODGED!"\r\n            $ bm.dodge_active = False', b'            $ bm.is_dodged = True\r\n            "DODGED!"\r\n            $ bm.dodge_active = False')

# And reset it
content = content.replace(b'            $ bm.enemies[0].dodge_active = False\r\n            else:', b'            $ bm.enemies[0].dodge_active = False\r\n            $ bm.is_dodged = False\r\n            else:')
# Actually better to reset at end of turn or after the attack
content = content.replace(b'            $ bm.is_dodged = False\r\n        if bm.player_hp <= 0:', b'        if bm.player_hp <= 0:') # Avoid double reset
# Reset it at the end of extra turns
content = re.sub(rb'(\'ava attacks butter for 5 damage! \(Butter HP: \[bm.enemies\[0\].hp\]\)\')', b'\\1\r\n            $ bm.is_dodged = False', content)
content = re.sub(rb'(\'ava attacks for 50 damage! \(Your HP: \[bm.player_hp\]\)\')', b'\\1\r\n            $ bm.is_dodged = False', content)

with open('fight.rpy', 'wb') as f:
    f.write(content)
