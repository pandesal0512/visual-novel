extends PanelContainer

## ═══════════════════════════════════════════════════════
##  SlotUI.gd — single battle slot component
##  Attach to the root SlotUI (PanelContainer) node
## ═══════════════════════════════════════════════════════

signal clicked

var _data     : Dictionary = {}
var _is_chaos : bool       = false
var _ink      : Color      = Color.BLACK
var _paper    : Color      = Color.WHITE

@onready var slot_tag  : Label = %SlotTag
@onready var slot_name : Label = %SlotName
@onready var slot_val  : Label = %SlotVal

func setup(data: Dictionary, is_chaos: bool) -> void:
	_data     = data
	_is_chaos = is_chaos
	_ink      = Color.WHITE if is_chaos else Color.BLACK
	_paper    = Color.BLACK if is_chaos else Color.WHITE

	match data.get("owner", "empty"):
		"player":
			slot_tag.text    = "YOU"
			slot_tag.visible = true
			slot_name.text   = data.get("name", "")
			slot_val.text    = data.get("val", "")
			slot_val.visible = true
			_style_player()

		"enemy":
			slot_tag.text    = "ENEMY"
			slot_tag.visible = true
			slot_name.text   = data.get("name", "")
			slot_val.text    = data.get("val", "")
			slot_val.visible = true
			_style_enemy()

		"empty":
			slot_tag.visible = false
			slot_name.text   = "— open —"
			slot_val.visible = false
			_style_empty()

	slot_tag.add_theme_color_override("font_color",  Color(_ink, 0.4))
	slot_name.add_theme_color_override("font_color", _ink)
	slot_val.add_theme_color_override("font_color",  Color(_ink, 0.55))

func _style_empty() -> void:
	var sb := StyleBoxFlat.new()
	sb.bg_color = _paper
	sb.set_border_width_all(2)
	sb.border_color = Color(_ink, 0.3)
	# Dashed effect via draw_overrides (approximated with low opacity)
	add_theme_stylebox_override("panel", sb)
	slot_name.add_theme_color_override("font_color", Color(_ink, 0.3))

func _style_player() -> void:
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(_paper.r * 0.96, _paper.g * 0.96, _paper.b * 0.96)
	sb.set_border_width_all(2)
	sb.border_color = _ink
	add_theme_stylebox_override("panel", sb)

func _style_enemy() -> void:
	# Hatched background drawn via queue_redraw
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(_paper, 0.0)  # transparent — hatch drawn in _draw()
	sb.set_border_width_all(2)
	sb.border_color = _ink
	add_theme_stylebox_override("panel", sb)
	queue_redraw()

func _draw() -> void:
	if _data.get("owner") != "enemy": return
	# Draw diagonal hatch pattern
	var w := size.x
	var h := size.y
	var hatch_col := Color(_ink, 0.07)
	var step := 5.0
	var x := -h
	while x < w:
		draw_line(Vector2(x, 0), Vector2(x + h, h), hatch_col, 1.0)
		x += step

# ── Input ────────────────────────────────────────────────
func _gui_input(event: InputEvent) -> void:
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
			clicked.emit()
			accept_event()

# ── Hover feedback ───────────────────────────────────────
func _on_mouse_entered() -> void:
	if _data.get("owner") == "enemy":
		modulate = Color(1.1, 1.1, 1.1)

func _on_mouse_exited() -> void:
	modulate = Color.WHITE
