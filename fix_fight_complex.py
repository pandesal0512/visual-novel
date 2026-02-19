
import re

with open('fight.rpy', 'rb') as f:
    lines = f.readlines()

# 1. Add self.is_dodged = False to BattleManager.__init__
for i, line in enumerate(lines):
    if b'self.show_energy_warning = False' in line:
        lines.insert(i + 1, b'            self.is_dodged = False\r\n')
        break

# 2. Modify animations to respect bm.is_dodged
# We look for lines that show "hit" or play sounds in animations
# From line ~974 onwards are animations
new_lines = []
in_animation = False
for line in lines:
    # Detect start of an animation label
    if line.startswith(b'label ') and b'_anim(bm):' in line:
        in_animation = True
        new_lines.append(line)
        continue

    if in_animation:
        # Detect end of animation (return or next label)
        if line.startswith(b'label ') or line.startswith(b'#') or line.strip() == b'':
            if line.startswith(b'label '):
                in_animation = b'_anim(bm):' in line
            else:
                in_animation = False # End of animations section potentially
            new_lines.append(line)
            continue

        # Wrapped lines that should be conditional
        if (b'sprites["hit"]' in line or
            b'player_sprites["hit"]' in line or
            b'play sound' in line or
            b'camera:' in line): # camera shakes/zooms also skipped on dodge

            indent = re.match(b'^\s*', line).group()
            new_lines.append(indent + b'if not bm.is_dodged:\r\n')
            new_lines.append(b'    ' + line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

lines = new_lines

# 3. Update resolution blocks in battle_engine, butter_ava_battle, butter_ava_battle2
# I will define the standard block for Skill and EnemyIntent resolution

def get_skill_block(suffix):
    return [
        b'            if skill.type == "attack":\r\n',
        b'                if enemy.dodge_active:\r\n',
        b'                    $ bm.is_dodged = True\r\n',
        b'                    if skill.animation:\r\n',
        b'                        call expression skill.animation pass (bm) from _call_skill_anim_at_dodge' + suffix.encode() + b'\r\n',
        b'                    $ dodge_anim = get_dodge_anim(enemy.name)\r\n',
        b'                    call expression dodge_anim pass (bm) from _call_enemy_dodge_anim_reactive' + suffix.encode() + b'\r\n',
        b'                    "[enemy.name] dodged the attack!"\r\n',
        b'                    $ enemy.dodge_active = False\r\n',
        b'                    $ bm.is_dodged = False\r\n',
        b'                else:\r\n',
        b'                    $ bm.is_dodged = False\r\n',
        b'                    if skill.animation:\r\n',
        b'                        call expression skill.animation pass (bm) from _call_skill_anim_generic' + suffix.encode() + b'\r\n',
        b'                    $ damage = skill.damage + bm.get_total_buff_value("damage", target="player")\r\n',
        b'                    $ bm.take_damage(damage, target="enemy", enemy_idx=e_idx)\r\n',
        b'                    $ bm.gain_exp(damage * 5, character_type="player")\r\n',
        b'                    "[skill.name] deals [damage] damage to [enemy.name]!"\r\n',
        b'                    if enemy.is_dead:\r\n',
        b'                        "[enemy.name] has been defeated!"\r\n',
        b'                        $ renpy.hide("enemy_" + str(e_idx))\r\n',
        b'            elif skill.type == "barrier":\r\n',
        b'                $ bm.add_barrier(skill.damage)\r\n',
        b'                "You gain [skill.damage] Defense!"\r\n',
        b'            elif skill.type == "dodge":\r\n',
        b'                $ bm.dodge_active = True\r\n',
        b'                "You prepare to dodge!"\r\n',
        b'            elif skill.type == "buff":\r\n',
        b'                $ bm.add_buff(skill.buff_type, skill.damage, skill.buff_duration, target="player")\r\n',
        b'                "[skill.name] activated! Damage increased by [skill.damage] for [skill.buff_duration] turns."\r\n',
        b'            elif skill.type == "energy":\r\n',
        b'                "You gained [skill.energy_regen] Energy!"\r\n'
    ]

def get_intent_block(suffix):
    return [
        b'            if intent.type == "attack":\r\n',
        b'                if bm.dodge_active:\r\n',
        b'                    $ bm.is_dodged = True\r\n',
        b'                    if intent.animation:\r\n',
        b'                        call expression intent.animation pass (bm) from _call_intent_anim_at_dodge' + suffix.encode() + b'\r\n',
        b'                    else:\r\n',
        b'                        call enemy_attack_anim(bm) from _call_intent_anim_default_at_dodge' + suffix.encode() + b'\r\n',
        b'                    $ p_name = "chaos" if "chaos" in bm.player_sprites["idle"] else "kare"\r\n',
        b'                    $ dodge_anim = get_dodge_anim(p_name)\r\n',
        b'                    call expression dodge_anim pass (bm) from _call_player_dodge_anim_reactive' + suffix.encode() + b'\r\n',
        b'                    "DODGED!"\r\n',
        b'                    $ bm.dodge_active = False\r\n',
        b'                    $ bm.is_dodged = False\r\n',
        b'                else:\r\n',
        b'                    $ bm.is_dodged = False\r\n',
        b'                    if intent.animation:\r\n',
        b'                        call expression intent.animation pass (bm) from _call_intent_anim_generic' + suffix.encode() + b'\r\n',
        b'                    else:\r\n',
        b'                        call enemy_attack_anim(bm) from _call_intent_anim_default' + suffix.encode() + b'\r\n',
        b'                    $ damage = intent.damage + bm.get_total_buff_value("damage", target="enemy", enemy_idx=e_idx)\r\n',
        b'                    $ bm.take_damage(damage, target="player")\r\n',
        b'                    $ bm.gain_exp(damage * 5, character_type="enemy", enemy_idx=e_idx)\r\n',
        b'                    "[enemy.name] deals [damage] damage with [intent.name]!"\r\n',
        b'            elif intent.type == "barrier":\r\n',
        b'                $ bm.add_barrier(intent.damage, target="enemy", enemy_idx=e_idx)\r\n',
        b'                "[enemy.name] gains [intent.damage] Defense!"\r\n',
        b'            elif intent.type == "dodge":\r\n',
        b'                $ enemy.dodge_active = True\r\n',
        b'                "[enemy.name] will dodge the next attack!"\r\n',
        b'            elif intent.type == "buff":\r\n',
        b'                $ bm.add_buff(intent.buff_type, intent.damage, intent.buff_duration, target="enemy", enemy_idx=e_idx)\r\n',
        b'                "[enemy.name] activated [intent.name]! Their damage increased by [intent.damage]!"\r\n',
        b'            elif intent.type == "energy":\r\n',
        b'                "[enemy.name] is recovering."\r\n'
    ]

# Find and replace blocks
final_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    # battle_engine
    if b'elif isinstance(action, Skill):' in line and b'battle_engine' in str(lines[i-10:i+1]): # Rough context check
         # Find where it ends
         start_idx = i + 1
         # ... find intent ...
         j = i + 1
         while j < len(lines) and b'elif isinstance(action, EnemyIntent):' not in lines[j]:
             j += 1
         # Replace skill block
         # I need to keep the first few lines of elif
         final_lines.append(line)
         final_lines.append(lines[i+1]) # $ skill = action
         final_lines.append(lines[i+2]) # $ skill.current_cooldown
         final_lines.append(lines[i+3]) # $ bm.player_energy
         final_lines.append(lines[i+4]) # $ current_enemy_tag
         final_lines.append(lines[i+5]) # empty line
         final_lines.extend(get_skill_block("_generic"))
         i = j
         continue

    if b'elif isinstance(action, EnemyIntent):' in line and b'battle_engine' in str(lines[i-40:i+1]):
         final_lines.append(line)
         final_lines.append(lines[i+1]) # $ intent = action
         final_lines.append(lines[i+2]) # $ intent.current_cooldown
         final_lines.append(lines[i+3]) # $ bm.enemy_intent
         final_lines.append(lines[i+4]) # $ current_enemy_tag
         final_lines.append(lines[i+5]) # empty line
         final_lines.extend(get_intent_block("_generic"))
         # Skip until Turn End
         j = i + 1
         while j < len(lines) and b'if all(e.is_dead for e in bm.enemies):' not in lines[j]:
             j += 1
         i = j
         continue

    # I'll just do it manually for boss1 and boss2 to be safe with line numbers
    final_lines.append(line)
    i += 1

with open('fight.rpy', 'wb') as f:
    f.writelines(final_lines)
