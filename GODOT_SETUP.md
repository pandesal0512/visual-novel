# From the Inside — Godot 4 Project Guide

## Project Settings
- **Display → Window → Size:** 1200 × 680
- **Display → Window → Stretch Mode:** `canvas_items`
- **Display → Window → Stretch Aspect:** `keep`

## Fonts  → `res://assets/fonts/`
- `CaveatBrush-Regular.ttf`
- `Caveat-Regular.ttf`
- `PatrickHand-Regular.ttf`

---

## Folder Structure
```
res://
├── assets/
│   ├── fonts/
│   ├── sprites/       ← kare_idle, butter_idle, chaos_idle, ava_idle
│   └── backgrounds/
├── scenes/
│   ├── Title.tscn + Title.gd       ← title + settings panel in one
│   ├── Dialogue.tscn + Dialogue.gd ← floating bubble (Variant C)
│   └── battle/
│       ├── BattleScreen.tscn + BattleScreen.gd
│       ├── CardUI.tscn + CardUI.gd
│       └── SlotUI.tscn + SlotUI.gd
├── data/
│   └── script.gd
└── Main.gd            ← Autoload
```

---

## Scene Map
```
Title (+ built-in settings overlay)
  └──→ Dialogue
         └──→ BattleScreen
                └──→ Dialogue (resume)
```
No separate Settings scene. Options panel lives inside Title.tscn as a hidden overlay — same pattern as your title_mixed.html mockup.

---

## ══ MAIN.GD — Autoload ════════════════════════════════

Register in **Project → Autoload** as `"Main"`.

---

## ══ TITLE SCREEN ══════════════════════════════════════

### Title.tscn — Node Tree
```
Title (Control)
│  Anchors Preset: Full Rect | Script: Title.gd
│
├── BG (ColorRect)  [%]              — white (#fff) or black (#000)
│
├── NotebookLines (Control)          — _draw() horizontal ruled lines
│     Z Index: 1 | Mouse Filter: Ignore
│
├── GrainOverlay (Control)           — _draw() diagonal grain lines
│     Z Index: 2 | Mouse Filter: Ignore
│
├── MarginLine (Control)             — _draw() red vertical line at x≈90
│     Z Index: 1 | Mouse Filter: Ignore
│
├── HolePunches (Control)            — _draw() 3 circles at x=54
│     Z Index: 10 | Mouse Filter: Ignore
│
├── CornerMarks (Control)  [%]       — _draw() 4 bracket corners, z=10
│
├── GlitchBars (Control)  [%]        — _draw() 3 horizontal bars; visible=false normally
│     Z Index: 3 | Mouse Filter: Ignore
│
├── TypebarStrip (Control)  [%]      — _draw() dashed strip at top
│     anchor_left=0, right=1, top=0 | custom_minimum_size: (0,4)
│
├── TopStamp (Label)                 — "A VISUAL NOVEL"  Caveat 13px letter-spacing 4
│     Position: x=120, y=18
│
├── StampDeco (VBoxContainer)        — top-right corner decoration
│     Position: x=900, y=20
│     ├── StampBig  (Label) — "DRAFT"  CaveatBrush 28px  (faint, rotated ~-3deg)
│     └── StampDate (Label) — "v0.1 — 2026"  Caveat 12px
│
├── TitleWrap (VBoxContainer)
│     Position: x=120, y=72 | Z Index: 10 | Separation: 4
│     ├── TitleLabel (Label)  [%]    — "TITLE :"  Caveat 13px letter-spacing 4
│     ├── TitleMain  (Label)  [%]    — "anytime"  CaveatBrush 160px line-spacing -0.1
│     ├── TitleUnderline (Control)   — custom_minimum_size (440,3), _draw() fills with ink
│     └── TitleSub   (Label)  [%]    — "a story about chaos, order, and one very bad day"
│                                       Caveat 15px italic
│
├── RightDeco (Label)                — "anytime"  CaveatBrush 80px vertical, very faint
│     anchor_right=1, Position: x=-60, y=80
│
├── Menu (VBoxContainer)  [%]
│     Position: x=120, y=470 | Separation: 6
│     ├── MenuRow0 (HBoxContainer)   — "01." + "Start New Game"
│     ├── MenuRow1 (HBoxContainer)   — "02." + "Continue"
│     ├── MenuRow2 (HBoxContainer)   — "03." + "Options"  ← opens panel
│     └── MenuRow3 (HBoxContainer)   — "04." + "Quit"
│     Each MenuRow: Mouse Filter Stop; script connects gui_input
│     Each num Label: Caveat 13px faint  |  Each item Label: CaveatBrush 26px
│
├── VersionLabel (Label)             — "v0.1"  Caveat 11px
│     anchor_right=1, anchor_bottom=1, Offset Right=-16, Bottom=-12
│
├── ScanlineSweep (Control)          — animated 2px line top→bottom, z=50
│
└── SettingsPanel (Control)  [%]
      Anchors Preset: Full Rect | Z Index: 50
      visible: false  (shown by script when "Options" clicked)
      Mouse Filter: Stop
      │
      ├── Backdrop (ColorRect)  [%]   — semi-transparent fill; click closes panel
      │     Anchors Preset: Full Rect
      │
      └── Card (PanelContainer)  [%]
            custom_minimum_size: (560, 0)
            anchor_left=0.5, right=0.5, top=0.5, bottom=0.5
            Offset Left=-280, Right=280, Top=-240, Bottom=240
            (StyleBoxFlat: white bg, 2px border)
            └── CardInner (VBoxContainer) padding 36 40 32 40
                  ├── SettingsTitle (Label)     — "Options"  CaveatBrush 36px
                  ├── SettingsLabelRow (Label)  — "GAME SETTINGS"  Caveat 11px faint
                  ├── SettingsDivider (Control) — custom_minimum_size (0,2), _draw()
                  ├── SettingsList (VBoxContainer)  [%]   Separation: 0
                  │     (rows built dynamically — see Title.gd)
                  │     Rows: Text Speed, Music Volume, SFX Volume,
                  │           Fullscreen, Skip Read Text, Language
                  └── BackBtn (Button)  [%]     — "← Back"  CaveatBrush 18px
```

**Each settings row (HBoxContainer):**
```
SettingRow (HBoxContainer)
  ├── RowNum   (Label)    — "01."  Caveat 11px faint
  ├── RowLabel (Label)    — "Text Speed"  CaveatBrush 20px  size_flags expand+fill
  └── RowControl          — HSlider / CheckButton / OptionButton
```

**Title.gd behaviors:**
- `state_a` (paper): white BG, black ink, grain visible
- `state_d` (chaos): black BG, white ink, glitch bars visible
- Random timer 8–15s fires a 0.4s chaos flash then reverts
- Settings saved with `ConfigFile → user://settings.cfg`

---

## ══ DIALOGUE SCREEN — Variant C ══════════════════════

**No bottom textbox.** Dialogue floats as a speech bubble near the speaking character. The bubble has a triangular tail pointing down toward the speaker's head. Sprites are full-height, maximally visible.

For Chaos scenes: bubble inverts (black bg, white text) + scanline overlay.

### Dialogue.tscn — Node Tree
```
Dialogue (Control)
│  Anchors Preset: Full Rect | Script: Dialogue.gd
│  Mouse Filter: Stop  (click anywhere advances)
│
├── BG (TextureRect)  [%]
│     Anchors Preset: Full Rect | Expand: Ignore | Stretch: Scale
│
├── BGLines (Control)               — _draw() subtle grid lines on BG
│     Z Index: 1 | Mouse Filter: Ignore
│
├── ScanlinesOverlay (Control)  [%] — _draw() scanlines; visible only chaos
│     Z Index: 2 | Mouse Filter: Ignore
│
├── CornerMarks (Control)  [%]      — _draw() 4 brackets, z=20
│
├── SpriteLayer (Control)
│     Z Index: 3 | Mouse Filter: Ignore
│     ├── SpriteLeft  (TextureRect)  [%]
│     │     anchor_left=0, bottom=1, top=0
│     │     Offset Left=100, Right=240, Top=0, Bottom=0
│     └── SpriteRight (TextureRect)  [%]
│           anchor_left=1, right=1, bottom=1, top=0
│           Offset Left=-240, Right=-100, Top=0, Bottom=0
│     (modulate.a: 1.0 for active speaker, 0.45 for inactive)
│
├── SpeechBubble (PanelContainer)  [%]
│     Z Index: 10
│     custom_minimum_size: (580, 0)
│     anchor_left=0, right=0, top=0, bottom=0
│     Position: set by script based on active speaker
│     (StyleBoxFlat: white bg, 2.5px black border, no rounding)
│     └── BubbleInner (VBoxContainer)  padding 28 32 28 32
│           ├── BubbleName (Label)  [%]   — CaveatBrush 20px
│           │     add_theme_color: black
│           │     border-bottom: 1px faint (HSeparator below)
│           ├── NameDivider (HSeparator)
│           └── BubbleText (RichTextLabel)  [%]
│                 BBCode: true | Fit Content: true
│                 Theme: PatrickHand 22px, line-spacing 1.6
│
├── BubbleTail (Control)  [%]       — _draw() triangle tail; positioned by script
│     Z Index: 9 | Mouse Filter: Ignore
│     custom_minimum_size: (24, 22)
│
├── AdvanceArrow (Label)  [%]       — "▼"  CaveatBrush 18px  color: #aaa
│     (positioned bottom-right of bubble by script)
│     Z Index: 11
│
├── SceneLabel (Label)  [%]         — "ch.01 — schoolyard · click to advance"
│     anchor_left=0, anchor_bottom=1
│     Offset Left=20, Bottom=-14
│     Caveat 13px, color rgba(0,0,0,0.25)
│     Z Index: 20
│
└── ChoicesPanel (VBoxContainer)  [%]
      visible: false | Z Index: 15
      Anchors: center (left=0.2, right=0.8, top=0.3, bottom=0.75)
      Separation: 12
      (choice buttons added dynamically)
```

**Bubble positioning logic (in Dialogue.gd):**
- `active == "left"` → bubble sits at roughly x=280, y=80 (right of left sprite)
- `active == "right"` → bubble sits at roughly x=340, y=80 (left of right sprite, mirrored)
- Bubble tail (BubbleTail) repositions to match: bottom-left of bubble for left speaker, bottom-right for right speaker
- Chaos mode: bubble BG = black, text = white, tail color flips

---

## ══ SCRIPT DATA FORMAT ════════════════════════════════

```gdscript
# res://data/script.gd
extends Node

const CHAPTERS : Array = [
  {
    "id": 1,
    "title": "schoolyard — after class",
    "background": "res://assets/backgrounds/schoolyard.png",
    "lines": [
      {
        "speaker":  "Kare",
        "sprite_l": "res://assets/sprites/kare_idle.png",
        "sprite_r": "res://assets/sprites/butter_idle.png",
        "active":   "left",
        "text":     "wait, hold on — you want me to fight you?",
      },
      {
        "speaker": "Kare",
        "active":  "left",
        "text":    "right now? i haven't even had lunch yet.",
      },
      {
        "speaker": "Butter",
        "active":  "right",
        "text":    "the verdict has been decided. there is no appeal.",
      },
      {
        "type":    "choice",
        "choices": [
          { "text": "fine. let's fight.", "goto": 4 },
          { "text": "i need a minute.",   "goto": 5 },
        ]
      },
      { "type": "battle", "mode": "kare" },
      {
        "speaker":  "Chaos",
        "active":   "left",
        "sprite_l": "res://assets/sprites/chaos_idle.png",
        "text":     "i did not mean to stay.",
        "chaos":    true,   # ← triggers dark mode bubble
      },
    ]
  }
]
```

---

## ══ RECOMMENDED BUILD ORDER ═══════════════════════════

1. **Main.gd autoload** — needed by everything else
2. **Title.tscn** — build the glitch/state system and settings panel here; it's self-contained
3. **Dialogue.tscn** — build bubble + typewriter; test with hardcoded text first
4. **SlotUI → CardUI → BattleScreen** — battle last
