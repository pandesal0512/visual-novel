extends Control

## ═══════════════════════════════════════════════════════
##  Dialogue.gd — Variant C: Floating Speech Bubble
##  No textbox. Dialogue floats near the active speaker.
##  Bubble tail points down toward the speaker's head.
##  Chaos mode inverts colors + adds scanlines.
## ═══════════════════════════════════════════════════════

# ── Node refs ────────────────────────────────────────────
@onready var bg               : TextureRect    = %BG
@onready var scanlines_overlay: Control        = %ScanlinesOverlay
@onready var corner_marks     : Control        = %CornerMarks
@onready var sprite_left      : TextureRect    = %SpriteLeft
@onready var sprite_right     : TextureRect    = %SpriteRight
@onready var speech_bubble    : PanelContainer = %SpeechBubble
@onready var bubble_name      : Label          = %BubbleName
@onready var bubble_text      : RichTextLabel  = %BubbleText
@onready var bubble_tail      : Control        = %BubbleTail
@onready var advance_arrow    : Label          = %AdvanceArrow
@onready var scene_label      : Label          = %SceneLabel
@onready var choices_panel    : VBoxContainer  = %ChoicesPanel

# ── State ─────────────────────────────────────────────────
var _lines      : Array = []
var _index      : int   = 0
var _is_typing  : bool  = false
var _full_text  : String = ""
var _is_chaos   : bool  = false
var _active_side: String = "left"  # "left" or "right"

var _ink   : Color = Color.BLACK
var _paper : Color = Color.WHITE

# Bubble layout constants
const BUBBLE_W       := 580.0
const BUBBLE_X_LEFT  := 280.0  # bubble left edge when speaker is left sprite
const BUBBLE_X_RIGHT := 340.0  # bubble left edge when speaker is right sprite (mirrored)
const BUBBLE_Y       := 80.0
const TAIL_OFFSET_X  := 40.0   # tail x from left edge of bubble

var text_speed : float = 40.0  # chars/sec; overridden by settings

var _type_tween  : Tween = null
var _arrow_tween : Tween = null

# ── Lifecycle ─────────────────────────────────────────────
func _ready() -> void:
	choices_panel.visible    = false
	advance_arrow.visible    = false
	speech_bubble.visible    = false
	scanlines_overlay.visible = false

	# Draw callbacks
	corner_marks.draw.connect(_draw_corners)
	scanlines_overlay.draw.connect(_draw_scanlines)
	bubble_tail.draw.connect(_draw_tail)

	_start_arrow_bounce()
	_load_chapter(Main.next_chapter)

# ── Chapter loading ────────────────────────────────────────
func _load_chapter(id: int) -> void:
	var script_data = load("res://data/script.gd").new()
	for ch in script_data.CHAPTERS:
		if ch.get("id") != id: continue
		_lines = ch.get("lines", [])
		_index = Main.next_line
		# Background
		var bg_path : String = ch.get("background", "")
		if bg_path != "":
			bg.texture = load(bg_path)
		# Scene label
		scene_label.text = "ch.%02d — %s · click to advance" % [id, ch.get("title", "")]
		_show_line()
		return

# ── Show current line ──────────────────────────────────────
func _show_line() -> void:
	if _index >= _lines.size():
		_end_chapter()
		return

	var line : Dictionary = _lines[_index]

	match line.get("type", ""):
		"choice": _show_choices(line.get("choices", [])); return
		"battle": _trigger_battle(line.get("mode", "kare")); return
		"end":    _end_chapter(); return

	# Apply chaos mode flag
	_is_chaos = line.get("chaos", false)
	_apply_mode()

	# Sprites
	_update_sprites(line)

	# Speaker + bubble
	_active_side = line.get("active", "left")
	var speaker  : String = line.get("speaker", "")
	_update_bubble_position()
	bubble_name.text = speaker
	speech_bubble.visible = true

	# Typewriter
	_full_text = line.get("text", "")
	_play_typewriter(_full_text)

# ── Mode (normal vs chaos) ────────────────────────────────
func _apply_mode() -> void:
	if _is_chaos:
		_ink   = Color.WHITE
		_paper = Color.BLACK
		scanlines_overlay.visible = true
	else:
		_ink   = Color.BLACK
		_paper = Color.WHITE
		scanlines_overlay.visible = false

	scanlines_overlay.queue_redraw()
	corner_marks.queue_redraw()
	bubble_tail.queue_redraw()
	_restyle_bubble()
	scene_label.add_theme_color_override("font_color", Color(_ink, 0.25))

func _restyle_bubble() -> void:
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(_paper, 0.97)
	sb.set_border_width_all(2)  # close to 2.5px
	sb.border_color = _ink
	sb.corner_radius_top_left     = 0
	sb.corner_radius_top_right    = 0
	sb.corner_radius_bottom_left  = 0
	sb.corner_radius_bottom_right = 0
	speech_bubble.add_theme_stylebox_override("panel", sb)

	bubble_name.add_theme_color_override("font_color", _ink)
	bubble_text.add_theme_color_override("default_color", _ink)
	advance_arrow.add_theme_color_override("font_color", Color(_ink, 0.55))

# ── Bubble positioning ─────────────────────────────────────
func _update_bubble_position() -> void:
	var bx : float
	if _active_side == "left":
		bx = BUBBLE_X_LEFT
	else:
		# Mirror: right sprite is at ~960px; place bubble to its left
		bx = size.x - BUBBLE_X_LEFT - BUBBLE_W
		bx = max(bx, BUBBLE_X_RIGHT)

	speech_bubble.position = Vector2(bx, BUBBLE_Y)
	speech_bubble.custom_minimum_size.x = BUBBLE_W

	# Position tail below bubble, aligned with speaker
	# We place BubbleTail just below the bubble's bottom edge
	# Script positions it after the bubble size is known (deferred)
	_position_tail.call_deferred()

	# Advance arrow inside bubble (bottom-right)
	# Position relative to bubble in _position_tail too
	advance_arrow.position = Vector2(
		bx + BUBBLE_W - 40,
		BUBBLE_Y + speech_bubble.size.y - 30
	)

func _position_tail() -> void:
	# Called deferred so speech_bubble.size is populated
	var bpos := speech_bubble.position
	var bh   := speech_bubble.size.y

	var tail_x : float
	if _active_side == "left":
		tail_x = bpos.x + TAIL_OFFSET_X
	else:
		# Mirror tail to bottom-right of bubble
		tail_x = bpos.x + BUBBLE_W - TAIL_OFFSET_X - 24

	bubble_tail.position = Vector2(tail_x, bpos.y + bh)
	bubble_tail.queue_redraw()

	# Also update advance arrow now we have correct height
	advance_arrow.position = Vector2(
		bpos.x + BUBBLE_W - 40,
		bpos.y + bh - 30
	)

# ── Sprites ────────────────────────────────────────────────
func _update_sprites(line: Dictionary) -> void:
	var active := line.get("active", "left")
	var path_l : String = line.get("sprite_l", "")
	var path_r : String = line.get("sprite_r", "")

	if path_l != "":
		sprite_left.texture = load(path_l)
		sprite_left.visible = true
	if path_r != "":
		sprite_right.texture = load(path_r)
		sprite_right.visible = true

	sprite_left.modulate.a  = 1.0 if active == "left"  else 0.45
	sprite_right.modulate.a = 1.0 if active == "right" else 0.45

# ── Typewriter ─────────────────────────────────────────────
func _play_typewriter(text: String) -> void:
	advance_arrow.visible         = false
	bubble_text.text              = text
	bubble_text.visible_characters = 0
	_is_typing                    = true

	var duration : float = text.length() / text_speed
	if _type_tween: _type_tween.kill()
	_type_tween = create_tween()
	_type_tween.tween_property(bubble_text, "visible_characters", text.length(), duration)
	_type_tween.tween_callback(_on_type_done)

func _on_type_done() -> void:
	_is_typing            = false
	advance_arrow.visible = true
	# Reposition after text height is finalized
	_position_tail.call_deferred()

func _skip_typewriter() -> void:
	if _type_tween: _type_tween.kill()
	bubble_text.visible_characters = -1
	_on_type_done()

# ── Input: click / space / enter ───────────────────────────
func _gui_input(event: InputEvent) -> void:
	if choices_panel.visible: return
	var is_click := event is InputEventMouseButton \
		and event.button_index == MOUSE_BUTTON_LEFT and event.pressed
	var is_key   := event is InputEventKey and event.pressed \
		and event.keycode in [KEY_SPACE, KEY_ENTER, KEY_KP_ENTER]
	if is_click or is_key:
		if _is_typing: _skip_typewriter()
		else:
			_index += 1
			_show_line()

# ── Choices ────────────────────────────────────────────────
func _show_choices(choices: Array) -> void:
	advance_arrow.visible = false
	choices_panel.visible = true
	for c in choices_panel.get_children(): c.queue_free()

	for choice : Dictionary in choices:
		var btn := Button.new()
		btn.text = choice.get("text", "")
		btn.size_flags_horizontal = Control.SIZE_EXPAND_FILL

		var sb := StyleBoxFlat.new()
		sb.bg_color = _paper
		sb.set_border_width_all(2)
		sb.border_color = _ink
		sb.content_margin_top = 10; sb.content_margin_bottom = 10
		sb.content_margin_left = 20; sb.content_margin_right = 20
		btn.add_theme_stylebox_override("normal", sb)
		btn.add_theme_color_override("font_color", _ink)

		var goto : int = choice.get("goto", _index + 1)
		btn.pressed.connect(func():
			choices_panel.visible = false
			for ch in choices_panel.get_children(): ch.queue_free()
			_index = goto
			_show_line()
		)
		choices_panel.add_child(btn)

# ── Battle ─────────────────────────────────────────────────
func _trigger_battle(mode: String) -> void:
	var tween := create_tween()
	tween.tween_property(self, "modulate:a", 0.0, 0.4)
	tween.tween_callback(func(): Main.go_battle(mode))

# ── Chapter end ────────────────────────────────────────────
func _end_chapter() -> void:
	var tween := create_tween()
	tween.tween_property(self, "modulate:a", 0.0, 0.6)
	tween.tween_callback(func(): Main.go_title())

# ── Advance arrow bounce ────────────────────────────────────
func _start_arrow_bounce() -> void:
	if _arrow_tween: _arrow_tween.kill()
	_arrow_tween = create_tween().set_loops()
	_arrow_tween.tween_property(advance_arrow, "position:y",
		advance_arrow.position.y + 4, 0.6).set_trans(Tween.TRANS_SINE)
	_arrow_tween.tween_property(advance_arrow, "position:y",
		advance_arrow.position.y,     0.6).set_trans(Tween.TRANS_SINE)

# ── _draw callbacks ─────────────────────────────────────────

func _draw_corners() -> void:
	var s  := corner_marks.size
	var c  := _ink
	var w  := 20.0
	var mg := 12.0
	var t  := 2.0
	corner_marks.draw_rect(Rect2(mg,           mg,           w, t), c)
	corner_marks.draw_rect(Rect2(mg,           mg,           t, w), c)
	corner_marks.draw_rect(Rect2(s.x-mg-w,     mg,           w, t), c)
	corner_marks.draw_rect(Rect2(s.x-mg-t,     mg,           t, w), c)
	corner_marks.draw_rect(Rect2(mg,           s.y-mg-t,     w, t), c)
	corner_marks.draw_rect(Rect2(mg,           s.y-mg-w,     t, w), c)
	corner_marks.draw_rect(Rect2(s.x-mg-w,     s.y-mg-t,     w, t), c)
	corner_marks.draw_rect(Rect2(s.x-mg-t,     s.y-mg-w,     t, w), c)

func _draw_scanlines() -> void:
	var w := scanlines_overlay.size.x
	var h := scanlines_overlay.size.y
	var y := 0.0
	while y < h:
		scanlines_overlay.draw_rect(Rect2(0, y, w, 1.0), Color(0, 0, 0, 0.12))
		y += 4.0

func _draw_tail() -> void:
	# Triangle tail: wide at top, point at bottom
	# Points: top-left (0,0), top-right (24,0), bottom-center (mirrored side)
	var tail_color := _ink
	var fill_color := Color(_paper, 0.97)

	# Outer triangle (border color)
	var outer := PackedVector2Array([
		Vector2(0, 0),
		Vector2(24, 0),
		Vector2(12, 22),
	])
	bubble_tail.draw_colored_polygon(outer, tail_color)

	# Inner triangle (fill) — slightly inset to fake border
	var inner := PackedVector2Array([
		Vector2(2.5, 0),
		Vector2(21.5, 0),
		Vector2(12, 18),
	])
	bubble_tail.draw_colored_polygon(inner, fill_color)
