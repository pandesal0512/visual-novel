extends Node

## ═══════════════════════════════════════════════════════
##  Main.gd — Autoload scene manager
##  Register in Project → Autoload as "Main"
## ═══════════════════════════════════════════════════════

var next_chapter : int    = 1
var next_line    : int    = 0
var battle_mode  : String = "kare"

const SCENES := {
	"Title":    "res://scenes/Title.tscn",
	"Dialogue": "res://scenes/Dialogue.tscn",
	"Battle":   "res://scenes/battle/BattleScreen.tscn",
}

func change_scene(name: String, params: Dictionary = {}) -> void:
	if params.has("chapter"): next_chapter = params.chapter
	if params.has("line"):    next_line    = params.line
	if params.has("mode"):    battle_mode  = params.mode
	var path := SCENES.get(name, "")
	if path == "":
		push_error("Main: unknown scene '%s'" % name)
		return
	get_tree().change_scene_to_file(path)

func go_title()    -> void: change_scene("Title")
func go_dialogue(chapter := 1, line := 0) -> void:
	change_scene("Dialogue", { "chapter": chapter, "line": line })
func go_battle(mode := "kare") -> void:
	change_scene("Battle", { "mode": mode })
