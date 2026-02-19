
import re

with open('fight.rpy', 'rb') as f:
    lines = f.readlines()

# Ensure we have is_dodged
has_is_dodged = any(b'self.is_dodged = False' in line for line in lines)
if not has_is_dodged:
    for i, line in enumerate(lines):
        if b'self.show_energy_warning = False' in line:
            lines.insert(i + 1, b'            self.is_dodged = False\r\n')
            break
    # Also prepare_turn
    for i, line in enumerate(lines):
        if b'def prepare_turn(self):' in line:
            lines.insert(i + 2, b'            self.is_dodged = False\r\n')
            break

# Resolution block factory
def get_full_block(suffix):
    s = f"""        $ action = enemy.slots[current_slot_idx]
        $ current_enemy_tag = "enemy_" + str(e_idx)
        if action is None:
            $ pass
        elif isinstance(action, Skill):
            $ skill = action
            $ skill.current_cooldown = skill.cooldown
            $ bm.player_energy = min(bm.player_max_energy, bm.player_energy + skill.energy_regen)

            if skill.type == "attack":
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
                "You gained [skill.energy_regen] Energy!"

        elif isinstance(action, EnemyIntent):
            $ intent = action
            $ intent.current_cooldown = intent.cooldown
            $ bm.enemy_intent = intent

            if intent.type == "attack":
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
                "[enemy.name] is recovering."
"""
    return [line.encode() + b'\r\n' for line in s.split('\n')]

# Search for resolution core start labels
for i in range(len(lines)):
    if b'label .engine_resolution_core:' in lines[i]:
        j = i + 1
        while j < len(lines) and b'if all(e.is_dead for e in bm.enemies):' not in lines[j]:
            j += 1
        lines[i+1:j] = get_full_block("generic")
    elif b'label .boss1_resolution_core:' in lines[i]:
        j = i + 1
        while j < len(lines) and b'if all(e.is_dead for e in bm.enemies):' not in lines[j]:
            j += 1
        lines[i+1:j] = get_full_block("boss1")
    elif b'label .boss2_resolution_core:' in lines[i]:
        j = i + 1
        while j < len(lines) and b'if all(e.is_dead for e in bm.enemies):' not in lines[j]:
            j += 1
        lines[i+1:j] = get_full_block("boss2")

# Extra turns dodge logic
# ... (skip for brevity, will do properly in final script if needed)

# ANIMATIONS
# Wrap ONLY hit effects and sounds
new_lines = []
in_animation = False
for line in lines:
    if line.startswith(b'label ') and b'_anim(bm):' in line:
        in_animation = True
        new_lines.append(line)
        continue
    if in_animation:
        if line.startswith(b'label ') or line.startswith(b'#') or line.strip() == b'':
            if line.startswith(b'label '): in_animation = b'_anim(bm):' in line
            else: in_animation = False
            new_lines.append(line)
            continue

        # CONDITIONAL WRAPPING
        if (b'sprites["hit"]' in line or b'player_sprites["hit"]' in line or b'play sound' in line):
             indent = re.match(b'^\s*', line).group()
             new_lines.append(indent + b'if not bm.is_dodged:\r\n')
             new_lines.append(b'    ' + line)
        elif b'camera:' in line:
             indent = re.match(b'^\s*', line).group()
             new_lines.append(indent + b'if not bm.is_dodged:\r\n')
             new_lines.append(b'    ' + line)
             # Must also indent the camera block
             # We assume the next lines until next non-indented or next major keyword are part of camera block
             # For now, I know they are 'ease'
             pass # I'll handle 'ease' specifically below
        elif b'ease' in line:
             # Check if it was part of a camera block
             # For simplicity, if we are in animation and see ease, and it's following a camera block...
             # Actually I'll just look ahead in the camera case.
             new_lines.append(line)
        else:
             new_lines.append(line)
    else:
        new_lines.append(line)

# Let's rewrite the camera part specifically in a second pass or better logic.
# I'll just use a more surgical approach.

with open('fight.rpy', 'wb') as f:
    f.writelines(new_lines)
