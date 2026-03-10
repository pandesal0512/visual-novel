# Godot 4 Remake Implementation Guide

This guide will walk you through setting up the core mechanics of your game in Godot 4, using the foundation already created.

## 1. Requirements
* **Godot 4.2+**: Ensure you are using a recent version of Godot 4 for compatibility with the GDScript 2.0 and Shader features provided.
* **Assets**: Export your PNG images from the Ren'Py project (portraits, icons, background) and place them in an `assets/` folder in your Godot project.

---

## 2. Project Structure
Organize your Godot project like this:
```text
res://
├── assets/             # Images and Audio
├── resources/
│   ├── skills/         # .tres files for attacks/buffs
│   └── enemies/        # .tres files for enemies
├── scripts/
│   ├── resources/      # SkillData.gd, EnemyData.gd, etc.
│   ├── BattleManager.gd
│   └── DialogueSystem.gd
├── shaders/
│   ├── WobblyFrame.gdshader
│   └── ChaosGlitch.gdshader
└── scenes/
    ├── BattleScene.tscn
    └── VN_Scene.tscn
```

---

## 3. Step-by-Step Setup

### Step 1: Resource Creation
You don't need to write code to create new skills or enemies!
1. Right-click in the Godot **FileSystem** dock.
2. Select **Create New -> Resource**.
3. Search for `SkillData` (or `EnemyData`).
4. Save it (e.g., `punch.tres`).
5. Use the **Inspector** on the right to fill in the damage, cost, description, and drag-and-drop your PNG icon into the `Card Image` slot.

### Step 2: Setting up the Battle Scene
1. Create a new 2D Scene named `BattleScene`.
2. Add a `Node` and name it `BattleManager`. Attach the `BattleManager.gd` script to it.
3. **UI Layout**:
   - Create a `CanvasLayer` for your HUD.
   - Add `ProgressBar` nodes for Player HP, Enemy HP, and Energy.
   - Add a `HBoxContainer` at the bottom to hold your "Card" buttons.
   - Add a `Label` for the Turn Count.

### Step 3: Wiring UI to Code (The "Glue" Script)
Create a new script called `BattleUI.gd` and attach it to your HUD node. This script connects the logic to the visuals:

```gdscript
extends Control

@onready var manager = $"../BattleManager" # Path to your BattleManager node

func _ready():
    # Connect signals from the logic to the UI
    manager.player_hp_changed.connect(_on_player_hp_updated)
    manager.enemy_hp_changed.connect(_on_enemy_hp_updated)
    manager.turn_started.connect(_on_new_turn)

func _on_player_hp_updated(val):
    $PlayerHPBar.value = val

func _on_new_turn(num):
    $TurnLabel.text = "Turn: " + str(num)
    _update_card_hand()

func _update_card_hand():
    # Clear old buttons
    for child in $CardHBox.get_children():
        child.queue_free()

    # Create new buttons for each skill
    for skill in manager.player_skills:
        var btn = Button.new()
        btn.text = skill.skill_name
        btn.pressed.connect(manager.add_skill_to_slot.bind(skill, 0, 0)) # Basic example
        $CardHBox.add_child(btn)
```

### Step 4: Implementing Visual Effects (Shaders)
To get that "Paper and Ink" or "Chaos" look:
1. Select a UI Frame or Sprite.
2. In the **Inspector**, go to **CanvasItem -> Material**.
3. Create a new `ShaderMaterial`.
4. In the **Shader** slot, drag and drop `WobblyFrame.gdshader`.
5. You will see the parameters (Strength, Speed) appear. Tweak them to get the right "wobble."

---

## 4. "Chaos Mode" Specifics
The `BattleManager.gd` already includes the randomization logic for Chaos mode.
To trigger the visual glitches:
1. In your `BattleUI.gd`, when `manager.is_chaos` is true, access the Material of your character portraits:
```gdscript
func _process(_delta):
    if manager.is_chaos:
        # Occasionally trigger the glitch shader via script
        character_portrait.material.set_shader_parameter("trigger", 1.0)
    else:
        character_portrait.material.set_shader_parameter("trigger", 0.0)
```

---

## 5. Visual Novel (Dialogue) Sequences
Use the `DialogueSystem.gd` for your story parts:
1. Add a `DialogueSystem` node to your scene.
2. It requires a specific child structure:
   - `TextBox` (Panel)
     - `Label` (Text)
     - `SpeakerName` (Label)
   - `Portraits` (Node2D)
     - `Left` (TextureRect)
     - `Right` (TextureRect)
3. Call it from any script:
```gdscript
$DialogueSystem.say("Kare", "ugh... im gonna be late", "left")
$DialogueSystem.say("Butter", "OW watch it", "right")
```

---

## 6. Key Differences from Ren'Py
* **Signals vs. Jumps**: Instead of `jump label`, Godot uses `signals`. When HP reaches 0, the `BattleManager` emits `battle_lost`. You should connect this signal to a function that shows your "Game Over" screen.
* **Resources**: Use them for everything! Items, Skills, Enemies, and حتی Stage data. This keeps your project clean.
* **Nodes**: Everything is a Node. Your sprites, your UI, and even your game logic.
