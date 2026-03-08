################################################################################
##  battle_screen.rpy
##
##  Drop-in replacement for your existing battle screen block.
##  Matches the HTML mockup exactly: single-enemy and multi-enemy,
##  Kare mode and Chaos mode, all interactions, intent bar, skill popup,
##  chaos number box, hover states, CONFIRM button.
##
##  HOW TO INTEGRATE
##  ─────────────────────────────────────────────────────────────────────────
##  1. Replace your existing  screen battle_screen(bm):  block entirely
##     with the one in this file.
##
##  2. Merge the  style / transform / image / init python  blocks at the
##     bottom of this file with whatever you already have.  Anything
##     prefixed  b_  is new.  Keep your existing items untouched.
##
##  3. In BattleManager.__init__ make sure these three fields exist:
##
##       self.selected_intent  = None   # EnemyIntent clicked in slot strip
##       self.hovered_skill    = None   # Skill currently hovered in hand
##       self.hovered_card_idx = -1     # index of that card (-1 = none)
##
##  4. In BattleManager.prepare_turn reset all three:
##
##       self.selected_intent  = None
##       self.hovered_skill    = None
##       self.hovered_card_idx = -1
##
##  5. In your engine_start_logic (wherever you clear state at turn start)
##     also kill chaos_anim_val so the number box never leaks:
##
##       store.chaos_anim_val = None   # or:  del store.chaos_anim_val
##
##  ─────────────────────────────────────────────────────────────────────────
##  ASSUMED BattleManager API  (field names must match exactly)
##  ─────────────────────────────────────────────────────────────────────────
##    bm.player_name          str
##    bm.player_hp            int
##    bm.player_max_hp        int
##    bm.player_energy        int
##    bm.player_max_energy    int
##    bm.player_barrier       int       (0 = no barrier)
##    bm.player_buffs         list of (name_str, amount_int, turns_left_int)
##    bm.is_chaos             bool
##    bm.turn_count           int
##    bm.current_max_slots    int
##    bm.skill_exp            int
##    bm.skill_exp_max        int
##    bm.player_skills        list[Skill]     (current hand)
##    bm.used_skills_this_turn  list[Skill]
##    bm.selected_skill       Skill | None
##    bm.selected_intent      EnemyIntent | None    ← NEW
##    bm.hovered_skill        Skill | None          ← NEW
##    bm.hovered_card_idx     int                   ← NEW
##    bm.enemies              list[Enemy]     (all enemies, incl. dead)
##    bm.show_energy_warning  bool
##
##    enemy.name              str
##    enemy.hp / .max_hp      int
##    enemy.barrier           int
##    enemy.buffs             list of (name_str, amount_int)
##    enemy.still_standing_triggered  bool
##    enemy.is_dead           bool
##    enemy.skill_exp / .skill_exp_max  int
##    enemy.slots             list[ None | EnemyIntent | Skill ]
##                            length == bm.current_max_slots
##
##    skill.name / .type / .damage / .cost / .icon / .desc
##    skill.cooldown / .current_cooldown
##
##    intent.name / .damage / .desc
##
##    bm.select_skill(skill)
##    bm.add_to_slot(skill, enemy_idx, slot_idx)
##    bm.remove_from_slot(enemy_idx, slot_idx)
##
##  ─────────────────────────────────────────────────────────────────────────
##  ASSUMED GLOBALS  (define once, anywhere in your project)
##  ─────────────────────────────────────────────────────────────────────────
##    ink(chaos)         → "#000000" or "#ffffff"
##    paper(chaos)       → "#ffffff" or "#000000"
##    ink_light(chaos)   → "#666666" or "#888888"
##    ink_faint(chaos)   → "#aaaaaa" or "#333333"
##    paper_dark(chaos)  → "#f0f0f0" or "#111111"
##    paper_mid(chaos)   → "#e0e0e0" or "#1a1a1a"
##    scramble_hp(val)   → scrambled string (chaos only)
##    get_typebar(type, chaos)  → displayable
##
##  Minimal fallback defines are included at the bottom of this file —
##  un-comment them if you don't already have your own versions.
################################################################################


################################################################################
##  SCREEN
################################################################################

screen battle_screen(bm):

    ## ── colour shortcuts ──────────────────────────────────────────────────────
    $ _ch  = getattr(bm, "is_chaos", False)
    $ _k   = ink(_ch)
    $ _kl  = ink_light(_ch)
    $ _kf  = ink_faint(_ch)
    $ _p   = paper(_ch)
    $ _pd  = paper_dark(_ch)
    $ _pm  = paper_mid(_ch)

    ## ── layout helpers ────────────────────────────────────────────────────────
    $ _live    = [e for e in bm.enemies if not e.is_dead]
    $ _multi   = len(_live) > 1
    $ _row_h   = 70 if _multi else 80    ## height per slot row in px
    $ _n_rows  = len(_live)
    $ _strip_h = _row_h * _n_rows + 4   ## total slot-strip height
    $ _cards_h = 150                     ## cards section height

    ## keep chaos animations refreshing
    if _ch:
        timer 0.05 repeat True action NullAction()


    ## ══════════════════════════════════════════════════════════════════════════
    ## 1. TOP BAR
    ##    zorder 5  →  always above scene sprites (zorder ~0)
    ## ══════════════════════════════════════════════════════════════════════════
    frame:
        xfill True
        ypos 0
        ysize (310 if _multi else 195)
        background (_p + "ff")
        xpadding 24
        top_padding 14 bottom_padding 12
        zorder 5

        hbox:
            xfill True yalign 0.0

            ## ── PLAYER column ───────────────────────────────────────────────
            vbox:
                xsize 560 spacing 7

                ## Name  (chaos: glitch animation)
                if _ch:
                    text bm.player_name:
                        style "b_charname"
                        at chaos_name_glitch
                else:
                    text bm.player_name:
                        style "b_charname"

                ## HP
                hbox:
                    spacing 10 yalign 0.5
                    text "HP":
                        style "b_label" min_width 60
                    if _ch:
                        text (scramble_hp(bm.player_hp) + " / " + scramble_hp(bm.player_max_hp)):
                            style "b_big_stat" at chaos_hp_glitch
                    else:
                        frame:
                            xsize 200 ysize 14 yalign 0.5
                            background _pm
                            frame:
                                xsize int(200 * max(0, bm.player_hp) // max(1, bm.player_max_hp))
                                yfill True background _k
                        text (str(bm.player_hp) + " / " + str(bm.player_max_hp)):
                            style "b_stat_nums"

                ## Energy
                hbox:
                    spacing 10 yalign 0.5
                    text "Energy":
                        style "b_label" min_width 60
                    frame:
                        xsize 200 ysize 14 yalign 0.5
                        background _pm
                        frame:
                            xsize int(200 * max(0, bm.player_energy) // max(1, bm.player_max_energy))
                            yfill True background _k
                    text (str(bm.player_energy) + " / " + str(bm.player_max_energy)):
                        style "b_stat_nums"

                ## Status chips
                hbox:
                    spacing 6 yoffset 2
                    if bm.player_barrier > 0:
                        frame:
                            background _pm padding (10, 2)
                            text ("DEF " + str(bm.player_barrier)):
                                style "b_chip"
                    for _bn, _ba, _bt in bm.player_buffs:
                        frame:
                            background _pm padding (10, 2)
                            text (_bn + " +" + str(_ba) + " (" + str(_bt) + "t)"):
                                style "b_chip" color _kl

            ## ── CENTER column (turn badge) ───────────────────────────────────
            vbox:
                xsize 200 yalign 0.0 xalign 0.5 spacing 5

                frame:
                    xalign 0.5 background _pd padding (16, 4)
                    text ("Turn " + str(bm.turn_count) + " \u00b7 " + str(bm.current_max_slots) + " slots"):
                        style "b_turn_badge"

                if _multi:
                    $ _tnames = " + ".join(e.name for e in _live)
                    text (_tnames + "\nteam fight"):
                        style "b_faint" size 13 xalign 0.5 text_align 0.5

            ## ── ENEMY column ────────────────────────────────────────────────
            vbox:
                xalign 1.0 spacing 8

                for _ei, _e in enumerate(_live):
                    vbox:
                        xalign 1.0 spacing 4

                        text _e.name:
                            style "b_charname"
                            size (28 if _multi else 34)
                            xalign 1.0

                        ## HP bar (right-to-left)
                        hbox:
                            xalign 1.0 spacing 10 yalign 0.5
                            text (str(_e.hp) + " / " + str(_e.max_hp)):
                                style "b_stat_nums"
                            frame:
                                xsize (160 if _multi else 200) ysize 14 yalign 0.5
                                background _pm
                                frame:
                                    xsize int((160 if _multi else 200) * max(0, _e.hp) // max(1, _e.max_hp))
                                    xalign 1.0 yfill True
                                    background (
                                        _k if _e.hp > _e.max_hp * 0.3
                                        else ("hp_low_hatch_chaos" if _ch else "hp_low_hatch")
                                    )
                            text "HP":
                                style "b_label" min_width 36 text_align 1.0

                        ## Status chips
                        hbox:
                            xalign 1.0 spacing 4
                            if _e.still_standing_triggered:
                                frame:
                                    background _pm padding (6, 2)
                                    text "STILL STANDING":
                                        style "b_chip" size 12 italic True
                            if _e.barrier > 0:
                                frame:
                                    background _pm padding (6, 2)
                                    text ("DEF " + str(_e.barrier)):
                                        style "b_chip" size 12
                            for _bn, _ba in _e.buffs:
                                frame:
                                    background _pm padding (6, 2)
                                    text (_bn + " +" + str(_ba)):
                                        style "b_chip" size 12

                        ## Skill unlock exp bar (single-enemy mode only)
                        if not _multi:
                            hbox:
                                xalign 1.0 spacing 8 yalign 0.5
                                text "skill unlock":
                                    style "b_exp_label"
                                frame:
                                    xsize 140 ysize 8 yalign 0.5
                                    background _pm
                                    frame:
                                        xsize int(140 * max(0, _e.skill_exp) // max(1, _e.skill_exp_max))
                                        yfill True background _k

                        ## Divider between enemies in multi-enemy mode
                        if _multi and _ei < len(_live) - 1:
                            frame:
                                xalign 1.0 xsize 360 ysize 1
                                background _kf yoffset 4


    ## ══════════════════════════════════════════════════════════════════════════
    ## 2. SLOT STRIP
    ##    Anchored yalign 1.0 so it floats just above the cards section.
    ##    One row per live enemy, each _row_h pixels tall.
    ##    CONFIRM button is a fixed-width column on the right.
    ## ══════════════════════════════════════════════════════════════════════════
    frame:
        yalign 1.0
        yoffset (-_cards_h)
        xfill True ysize _strip_h
        background (_p + "f0")
        xpadding 0 ypadding 0
        zorder 5
        if _ch:
            at chaos_slots_shake

        hbox:
            xfill True yfill True

            ## ── one row per live enemy ───────────────────────────────────────
            vbox:
                xfill True yfill True spacing 0

                for _ei, _e in enumerate(bm.enemies):
                    if not _e.is_dead:

                        ## row divider (not before the first row)
                        if _ei > 0:
                            frame:
                                xfill True ysize 1 background _kf

                        hbox:
                            xfill True ysize _row_h
                            left_padding 20 right_padding 8
                            spacing 10 yalign 0.5

                            ## Row label
                            text (_e.name.split()[0] + "'s\nrow"):
                                style "b_faint"
                                min_width 72 yalign 0.5 size 14 text_align 0.0

                            ## Slot cells
                            hbox:
                                xfill True yalign 0.5 spacing 6

                                for _si in range(bm.current_max_slots):
                                    $ _slot = _e.slots[_si]

                                    frame:
                                        xsize int(1050 // bm.current_max_slots)
                                        ysize (_row_h - 12)
                                        yalign 0.5

                                        ## ── EMPTY ──────────────────────────
                                        if _slot is None:
                                            background _p
                                            foreground ("slot_dashed_chaos" if _ch else "slot_dashed")
                                            text (u"\u2014 open \u2014"):
                                                style "b_faint" size 13
                                                xalign 0.5 yalign 0.5
                                            if bm.selected_skill is not None:
                                                imagebutton:
                                                    xfill True yfill True
                                                    idle   Solid("#00000000")
                                                    hover  Solid(_k + "22")
                                                    action Function(bm.add_to_slot, bm.selected_skill, _ei, _si)
                                                    insensitive Solid("#00000000")

                                        ## ── ENEMY INTENT ───────────────────
                                        elif isinstance(_slot, EnemyIntent):
                                            background ("slot_hatch_chaos" if _ch else "slot_hatch")
                                            foreground ("slot_border_chaos" if _ch else "slot_border")
                                            vbox:
                                                xalign 0.5 yalign 0.5 spacing 0
                                                text "ENEMY":
                                                    style "b_slot_tag" color _kl xalign 0.5
                                                text _slot.name:
                                                    style "b_slot_name" xalign 0.5
                                            if _slot.damage > 0:
                                                text str(_slot.damage):
                                                    style "b_slot_val" xalign 0.97 yalign 0.92
                                            ## click → toggle intent description bar
                                            imagebutton:
                                                xfill True yfill True
                                                idle  Solid("#00000000")
                                                hover Solid(_k + "14")
                                                action If(
                                                    bm.selected_intent is _slot,
                                                    true  = SetField(bm, "selected_intent", None),
                                                    false = SetField(bm, "selected_intent", _slot)
                                                )

                                        ## ── PLAYER SKILL ───────────────────
                                        elif isinstance(_slot, Skill):
                                            background _pd
                                            foreground ("slot_border_chaos" if _ch else "slot_border")
                                            vbox:
                                                xalign 0.5 yalign 0.5 spacing 0
                                                text "YOU":
                                                    style "b_slot_tag" color _k xalign 0.5
                                                text _slot.name:
                                                    style "b_slot_name" xalign 0.5
                                            if _slot.damage > 0:
                                                text str(_slot.damage):
                                                    style "b_slot_val" xalign 0.97 yalign 0.92
                                            ## click → remove from slot
                                            ## (subtle red hover = "this is removable")
                                            imagebutton:
                                                xfill True yfill True
                                                idle  Solid("#00000000")
                                                hover Solid("#ff000018")
                                                action Function(bm.remove_from_slot, _ei, _si)

            ## ── CONFIRM button ───────────────────────────────────────────────
            frame:
                xsize 140 yfill True
                background _p
                padding (10, 0)

                textbutton "CONFIRM":
                    style "b_confirm_btn"
                    background        Solid(_k)
                    hover_background  Solid(_pm)
                    text_color        _p
                    text_hover_color  _k
                    insensitive_background Solid(_k + "55")
                    action Return("execute")
                    xalign 0.5 yalign 0.5
                    xsize 118


    ## ══════════════════════════════════════════════════════════════════════════
    ## 3. INTENT BAR
    ##    Only visible when bm.selected_intent is not None.
    ##    Appears just above the slot strip.
    ## ══════════════════════════════════════════════════════════════════════════
    if bm.selected_intent is not None:
        $ _si_obj = bm.selected_intent
        $ _iy = -(_cards_h + _strip_h + 2)
        $ _ititle = (
            _si_obj.name
            + (u" \u2014 " + str(_si_obj.damage) + " damage" if _si_obj.damage > 0 else "")
        )

        frame:
            xfill True
            yalign 1.0 yoffset _iy
            left_margin 24 right_margin 24
            background (_p + "ee")
            left_padding 18 right_padding 18
            top_padding 8 bottom_padding 8
            foreground ("intent_accent_chaos" if _ch else "intent_accent")
            zorder 4

            hbox:
                spacing 14 yalign 0.5
                text _ititle:
                    style "b_intent_title"
                text _si_obj.desc:
                    style "b_intent_desc"


    ## ══════════════════════════════════════════════════════════════════════════
    ## 4. CARDS SECTION  (bottom 150 px)
    ## ══════════════════════════════════════════════════════════════════════════
    frame:
        yalign 1.0 xfill True ysize _cards_h
        background (_p + "f7")
        xpadding 24 ypadding 10
        zorder 5

        vbox:
            spacing 8

            ## Header: "your cards"  +  skill exp bar
            hbox:
                xfill True yalign 0.5
                text "your cards":
                    style "b_faint"
                hbox:
                    xalign 1.0 spacing 8 yalign 0.5
                    text "next skill:":
                        style "b_faint"
                    frame:
                        xsize 260 ysize 8 yalign 0.5
                        background _pm
                        frame:
                            xsize int(260 * max(0, bm.skill_exp) // max(1, bm.skill_exp_max))
                            yfill True background _k

            ## Card row
            hbox:
                spacing 12

                for _ci in range(len(bm.player_skills)):
                    $ _skill = bm.player_skills[_ci]
                    $ _oncd  = _skill.current_cooldown > 0 or _skill in bm.used_skills_this_turn
                    $ _sel   = bm.selected_skill is _skill
                    $ _hov   = bm.hovered_card_idx == _ci

                    frame:
                        xsize 108 ysize 100
                        ## Lift when selected or hovered (matches the CSS)
                        yoffset (-10 if (_sel or _hov) else 0)
                        background _p
                        foreground (
                            ("card_selected_chaos" if _ch else "card_selected") if _sel
                            else ("card_hover_chaos"  if _ch else "card_hover")  if _hov
                            else None
                        )

                        vbox:
                            xfill True

                            ## Type stripe
                            add get_typebar(_skill.type, _ch) xsize 108 ysize (8 if _skill.type == "ultimate" else 5)

                            ## Icon
                            frame:
                                xfill True ysize 52 background _p
                                text (_skill.icon if _skill.icon else "?"):
                                    size 26 xalign 0.5 yalign 0.5 color _k

                            ## Separator line
                            frame:
                                xfill True ysize 1 background _kf

                            ## Name + stats
                            frame:
                                xfill True background _p
                                left_padding 6 right_padding 6
                                top_padding 4 bottom_padding 4
                                vbox:
                                    spacing 1
                                    text _skill.name:
                                        style "b_card_name"
                                    hbox:
                                        xfill True
                                        text (str(_skill.damage) + " dmg" if _skill.damage > 0 else _skill.type):
                                            style "b_card_stat"
                                        if _skill.cooldown > 0:
                                            text ("cd:" + str(_skill.cooldown)):
                                                style "b_card_stat" xalign 1.0

                        ## Energy cost bubble (top-right corner)
                        frame:
                            xalign 1.0 yalign 0.0
                            xoffset -5 yoffset 8
                            xsize 20 ysize 20
                            background _k
                            text str(_skill.cost):
                                size 13 xalign 0.5 yalign 0.5 color _p

                        ## Selected tint
                        if _sel:
                            add Solid(_k + "1a")

                        ## Cooldown / used overlay
                        if _oncd:
                            frame:
                                xfill True yfill True
                                background (_p + "cc")
                                if _skill.current_cooldown > 0:
                                    text str(_skill.current_cooldown):
                                        style "b_cooldown_num"
                                        xalign 0.5 yalign 0.5
                                else:
                                    text "USED":
                                        style "b_card_name" color _kf
                                        xalign 0.5 yalign 0.5

                        ## Interactive overlay (hover + click)
                        if not _oncd:
                            imagebutton:
                                xfill True yfill True
                                idle        Solid("#00000000")
                                hover       Solid(_k + "14")
                                hovered     [SetField(bm, "hovered_card_idx", _ci),
                                             SetField(bm, "hovered_skill",    _skill)]
                                unhovered   [If(bm.hovered_card_idx == _ci,
                                               true = SetField(bm, "hovered_card_idx", -1)),
                                             If(bm.hovered_skill is _skill,
                                               true = SetField(bm, "hovered_skill",    None))]
                                action      Function(bm.select_skill, _skill)
                                insensitive Solid("#00000000")


    ## ══════════════════════════════════════════════════════════════════════════
    ## 5. SKILL POPUP
    ##    Shown only while a card is hovered.
    ##    Anchored just above the cards section on the left side.
    ## ══════════════════════════════════════════════════════════════════════════
    if bm.hovered_skill is not None:
        $ _hs = bm.hovered_skill

        frame:
            xpos 24
            yalign 1.0 yoffset (-_cards_h - 8)
            xsize 200
            background _pd
            padding (16, 14)
            foreground ("card_popup_chaos" if _ch else "card_popup")
            zorder 8

            vbox:
                spacing 5

                text _hs.name:
                    style "b_popup_name"
                text ("Cost: " + str(_hs.cost) + " Energy"):
                    style "b_popup_line"
                if _hs.damage > 0:
                    text ("Damage: " + str(_hs.damage)):
                        style "b_popup_line"
                if _hs.cooldown > 0:
                    text ("Cooldown: " + str(_hs.cooldown) + " turns"):
                        style "b_popup_line"
                frame:
                    xfill True ysize 1 background _kf yoffset 2
                text _hs.desc:
                    style "b_intent_desc" size 15


    ## ══════════════════════════════════════════════════════════════════════════
    ## 6. CHAOS NUMBER BOX
    ##    Only during execution phase (store.chaos_anim_val is set by
    ##    your chaos_number_anim label).  Cleared at turn start so it
    ##    never appears during the selection phase.
    ## ══════════════════════════════════════════════════════════════════════════
    if _ch and getattr(store, "chaos_anim_val", None) is not None:
        frame:
            xalign 0.35 yalign 0.34
            background "#000000"
            padding (28, 12)
            foreground "chaos_box_border"
            at chaos_glitch
            zorder 10

            vbox:
                spacing 4
                text getattr(store, "chaos_anim_label", "DAMAGE"):
                    style "b_faint" size 18 color "#888888" xalign 0.5
                text str(store.chaos_anim_val):
                    font "fonts/CaveatBrush-Regular.ttf"
                    size 68 color "#ffffff" xalign 0.5


    ## ══════════════════════════════════════════════════════════════════════════
    ## 7. ENERGY WARNING
    ## ══════════════════════════════════════════════════════════════════════════
    if bm.show_energy_warning:
        timer 2.0 action SetField(bm, "show_energy_warning", False)
        frame:
            background Solid("#cc0000ee")
            padding (36, 14)
            xalign 0.5 yalign 0.36
            zorder 10
            text "NOT ENOUGH ENERGY":
                color "#ffffff" size 48 bold True

    ## ── Settings / pause ─────────────────────────────────────────────────────
    textbutton "Settings":
        xpos 12 ypos 12
        action ShowMenu("preferences")
        style "b_settings_btn"
        zorder 5


################################################################################
##  STYLES
##  All prefixed b_  to avoid collisions with your existing styles.
##  Change font paths to match your project layout.
################################################################################

define FONT_BRUSH  = "fonts/CaveatBrush-Regular.ttf"
define FONT_CAVEAT = "fonts/Caveat-Regular.ttf"
define FONT_HAND   = "fonts/PatrickHand-Regular.ttf"

style b_charname:
    font  FONT_BRUSH
    size  34
    color "#000000"

style b_label:
    font  FONT_CAVEAT
    size  15
    color "#666666"

style b_stat_nums:
    font  FONT_CAVEAT
    size  14
    color "#666666"

style b_big_stat:
    font  FONT_BRUSH
    size  38
    color "#ffffff"

style b_turn_badge:
    font  FONT_CAVEAT
    size  14
    color "#666666"

style b_faint:
    font  FONT_CAVEAT
    size  13
    color "#aaaaaa"

style b_chip:
    font  FONT_CAVEAT
    size  13
    color "#333333"

style b_exp_label:
    font  FONT_CAVEAT
    size  12
    color "#aaaaaa"

style b_slot_tag:
    font   FONT_CAVEAT
    size   10
    color  "#aaaaaa"
    bold   True
    kerning 1

style b_slot_name:
    font  FONT_BRUSH
    size  14
    color "#000000"

style b_slot_val:
    font  FONT_CAVEAT
    size  11
    color "#666666"

style b_intent_title:
    font  FONT_BRUSH
    size  17
    color "#000000"

style b_intent_desc:
    font   FONT_HAND
    size   13
    color  "#666666"
    italic True

style b_card_name:
    font  FONT_BRUSH
    size  13
    color "#000000"

style b_card_stat:
    font  FONT_CAVEAT
    size  11
    color "#666666"

style b_cooldown_num:
    font  FONT_BRUSH
    size  30
    color "#000000"

style b_popup_name:
    font  FONT_BRUSH
    size  20
    color "#000000"

style b_popup_line:
    font  FONT_CAVEAT
    size  14
    color "#333333"

style b_confirm_btn:
    font  FONT_BRUSH
    size  20
    color "#ffffff"

style b_settings_btn is default:
    font  FONT_CAVEAT
    size  15
    color "#aaaaaa"


################################################################################
##  TRANSFORMS
##  Only new ones added here.  Keep all your existing transforms.
################################################################################

transform chaos_name_glitch:
    ## Player name flickers in chaos mode
    block:
        alpha 1.0
        pause 4.5
        alpha 0.4
        pause 0.08
        alpha 1.0
        pause 0.07
        alpha 0.7
        pause 0.05
        alpha 1.0
        repeat

transform chaos_hp_glitch:
    ## HP number briefly shifts sideways in chaos mode
    block:
        xoffset 0
        pause 5.0
        xoffset -3
        pause 0.06
        xoffset 2
        pause 0.04
        xoffset 0
        repeat

transform chaos_slots_shake:
    ## Slot strip gentle wobble during chaos selection
    block:
        xoffset 0 yoffset 0
        pause 7.0
        xoffset  1  yoffset -1
        pause 0.06
        xoffset -1  yoffset  1
        pause 0.05
        xoffset  0  yoffset  0
        repeat

transform chaos_glitch:
    ## Chaos number box glitch during execution phase
    block:
        xoffset 0
        pause 0.4
        xoffset -4
        pause 0.06
        xoffset  3
        pause 0.04
        xoffset  0
        repeat


################################################################################
##  COLOUR HELPERS
##  Un-comment ONLY if you don't already have your own versions.
################################################################################

# define ink        = lambda c: "#ffffff" if c else "#000000"
# define paper      = lambda c: "#000000" if c else "#ffffff"
# define ink_light  = lambda c: "#888888" if c else "#666666"
# define ink_faint  = lambda c: "#333333" if c else "#aaaaaa"
# define paper_dark = lambda c: "#111111" if c else "#f0f0f0"
# define paper_mid  = lambda c: "#1a1a1a" if c else "#e0e0e0"

## scramble_hp — un-comment if you don't already have one
# init python:
#     import random as _rng
#     _SC = "0123456789#$@?!"
#     def scramble_hp(val):
#         return "".join(_rng.choice(_SC) if _rng.random() < 0.35 else ch for ch in str(val))


################################################################################
##  DISPLAYABLE HELPERS
##
##  Each image is a simple Solid/Frame fallback so the screen works
##  immediately without any image assets.  Replace each one with your
##  own image file once you've made the artwork.
##
##  For the border/dashed effects you probably want:
##    slot_dashed   → a Frame() with a dashed CSS-like border image
##    slot_hatch    → a diagonal hatch pattern image
##    intent_accent → a Frame() with a thick left border only
##    card_popup    → a Frame() with a 2-px solid border
################################################################################

image slot_dashed        = Frame(Solid("#aaaaaa"), 1, 1)
image slot_dashed_chaos  = Frame(Solid("#333333"), 1, 1)
image slot_hatch         = Solid("#00000008")
image slot_hatch_chaos   = Solid("#ffffff08")
image slot_border        = Frame(Solid("#000000"), 2, 2)
image slot_border_chaos  = Frame(Solid("#ffffff"), 2, 2)
image intent_accent      = Frame(Solid("#000000"), 4, 0, 0, 0)
image intent_accent_chaos= Frame(Solid("#ffffff"), 4, 0, 0, 0)
image card_popup         = Frame(Solid("#000000"), 2, 2)
image card_popup_chaos   = Frame(Solid("#ffffff"), 2, 2)
image card_selected      = Frame(Solid("#000000"), 2, 2)
image card_selected_chaos= Frame(Solid("#ffffff"), 2, 2)
image card_hover         = Frame(Solid("#00000033"), 2, 2)
image card_hover_chaos   = Frame(Solid("#ffffff33"), 2, 2)
image chaos_box_border   = Frame(Solid("#ffffff"), 2, 2)
image hp_low_hatch       = Solid("#000000")
image hp_low_hatch_chaos = Solid("#ffffff")


################################################################################
##  get_typebar  helper
##
##  Returns the coloured stripe displayed at the top of each card.
##  Replace Solid() calls with your actual stripe image assets.
################################################################################

init python:
    def get_typebar(skill_type, chaos):
        ## Kare-mode colours (black on white)
        _kare = {
            "attack":  "#000000",
            "barrier": "#555555",
            "dodge":   "#333333",
            "energy":  "#222222",
            "buff":    "#444444",
            "ultimate":"#000000",
        }
        ## Chaos-mode colours (white on black)
        _chaos = {
            "attack":  "#ffffff",
            "barrier": "#aaaaaa",
            "dodge":   "#cccccc",
            "energy":  "#999999",
            "buff":    "#bbbbbb",
            "ultimate":"#ffffff",
        }
        palette = _chaos if chaos else _kare
        col = palette.get(skill_type, "#000000" if not chaos else "#ffffff")
        return Solid(col)
