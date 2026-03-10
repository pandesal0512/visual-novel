extends Control

## ═══════════════════════════════════════════════════════
##  Title.gd
##  Handles: paper/chaos visual states, random glitch flash,
##           menu navigation, built-in settings overlay
## ═══════════════════════════════════════════════════════

# ── Visual state ─────────────────────────────────────────
enum TitleState { PAPER, CHAOS }
var _state : TitleState = TitleState.PAPER

var _ink   : Color = Color.BLACK
var _paper : Color = Color.WHITE

# ── Node refs ─────────────────────────────────────────────
@onready var bg              : ColorRect     = %BG
@onready var corner_marks    : Control       = %CornerMarks
@onready var glitch_bars     : Control       = %GlitchBars
@onready var typebar_strip   : Control       = %TypebarStrip
@onready var title_label     : Label         = %TitleLabel
@onready var title_main      : Label         = %TitleMain
@onready var title_sub       : Label         = %TitleSub
@onready var menu            : VBoxContainer = %Menu
@onready var settings_panel  : Control       = %SettingsPanel
@onready var backdrop        : ColorRect     = %Backdrop
@onready var settings_list   : VBoxContainer = %SettingsList
@onready var back_btn        : Button        = %BackBtn

# ── Settings data ──────────────────────────────────────────
var _cfg := ConfigFile.new()
const CFG_PATH := "user://settings.cfg"

var _settings := {
	"text_speed":     7,
	"music_volume":   80,
	"sfx_volume":     100,
	"fullscreen":     false,
	"skip_read":      true,
	"language":       "English",
}

# ── Glitch timer ────────────────────────────────────────────
var _glitch_timer : Timer

# ── Lifecycle ────────────────────────────────────────────────
func _ready() -> void:
	_load_settings()
	_apply_state(TitleState.PAPER)
	_wire_menu()
	_build_settings_rows()
	settings_panel.visible = false

	backdrop.gui_input.connect(_on_backdrop_input)
	back_btn.pressed.connect(close_settings)

	# Wire draw signals
	corner_marks.draw.connect(_draw_corners)
	glitch_bars.draw.connect(_draw_glitch_bars)
	typebar_strip.draw.connect(_draw_typebar)

	_start_glitch_timer()

# ── Visual state ──────────────────────────────────────────────
func _apply_state(state: TitleState) -> void:
	_state = state
	_ink   = Color.WHITE if state == TitleState.CHAOS else Color.BLACK
	_paper = Color.BLACK if state == TitleState.CHAOS else Color.WHITE

	bg.color = _paper
	glitch_bars.visible = (state == TitleState.CHAOS)

	var faint := Color(_ink, 0.3)

	title_label.add_theme_color_override("font_color", Color(_ink, 0.5))
	title_main.add_theme_color_override("font_color",  _ink)
	title_sub.add_theme_color_override("font_color",   Color(_ink, 0.55))

	corner_marks.queue_redraw()
	typebar_strip.queue_redraw()
	glitch_bars.queue_redraw()

	_restyle_menu()
	_restyle_settings_card()

func _restyle_menu() -> void:
	for row in menu.get_children():
		if not row is HBoxContainer: continue
		var children := row.get_children()
		if children.size() >= 2:
			var num_lbl  : Label = children[0]
			var item_lbl : Label = children[1]
			num_lbl.add_theme_color_override("font_color",  Color(_ink, 0.35))
			item_lbl.add_theme_color_override("font_color", _ink)

func _restyle_settings_card() -> void:
	if not is_node_ready(): return
	backdrop.color = Color(_paper, 0.88)
	# Card panel style
	var card := settings_panel.get_node("Card")
	if not card: return
	var sb := StyleBoxFlat.new()
	sb.bg_color = _paper
	sb.set_border_width_all(2)
	sb.border_color = Color(_ink, 0.2)
	card.add_theme_stylebox_override("panel", sb)
	# Retint all labels inside
	for child in card.find_children("*", "Label", true, false):
		child.add_theme_color_override("font_color", _ink)

# ── Menu wiring ────────────────────────────────────────────────
func _wire_menu() -> void:
	var rows := menu.get_children()
	for i in rows.size():
		var row := rows[i]
		row.mouse_filter = Control.MOUSE_FILTER_STOP
		row.gui_input.connect(_on_menu_row_input.bind(i))
		row.mouse_entered.connect(_on_menu_hover.bind(i))
		row.mouse_exited.connect(_on_menu_unhover)

func _on_menu_hover(idx: int) -> void:
	var rows := menu.get_children()
	for i in rows.size():
		var item : Label = rows[i].get_children()[1]
		item.add_theme_color_override("font_color",
			_ink if i == idx else Color(_ink, 0.3))

func _on_menu_unhover() -> void:
	for row in menu.get_children():
		var item : Label = row.get_children()[1]
		item.add_theme_color_override("font_color", _ink)

func _on_menu_row_input(event: InputEvent, idx: int) -> void:
	if not (event is InputEventMouseButton
			and event.button_index == MOUSE_BUTTON_LEFT
			and event.pressed):
		return
	match idx:
		0: Main.go_dialogue(1, 0)                          # Start New Game
		1: Main.go_dialogue(Main.next_chapter, Main.next_line) # Continue
		2: open_settings()                                  # Options
		3: get_tree().quit()                                # Quit

# ── Settings overlay ────────────────────────────────────────────
func open_settings() -> void:
	settings_panel.visible = true

func close_settings() -> void:
	settings_panel.visible = false
	_save_settings()

func _on_backdrop_input(event: InputEvent) -> void:
	if event is InputEventMouseButton and event.pressed:
		close_settings()

func _build_settings_rows() -> void:
	_add_slider_row("01.", "Text Speed",    "text_speed",    1, 10)
	_add_slider_row("02.", "Music Volume",  "music_volume",  0, 100)
	_add_slider_row("03.", "SFX Volume",    "sfx_volume",    0, 100)
	_add_toggle_row("04.", "Fullscreen",    "fullscreen")
	_add_toggle_row("05.", "Skip Read Text","skip_read")
	_add_option_row("06.", "Language",      "language", ["English", "Filipino", "日本語"])

func _add_slider_row(num: String, label: String, key: String, mn: int, mx: int) -> void:
	var row    := HBoxContainer.new()
	var num_lb := Label.new()
	var lbl    := Label.new()
	var slider := HSlider.new()
	var val_lb := Label.new()

	num_lb.text = num
	lbl.text    = label
	lbl.size_flags_horizontal = Control.SIZE_EXPAND_FILL

	slider.min_value    = mn
	slider.max_value    = mx
	slider.value        = _settings[key]
	slider.custom_minimum_size = Vector2(140, 0)
	slider.value_changed.connect(func(v):
		_settings[key] = int(v)
		val_lb.text = str(int(v)) + ("%" if mx == 100 else "")
	)
	val_lb.text = str(int(_settings[key])) + ("%" if mx == 100 else "")
	val_lb.custom_minimum_size.x = 36

	row.add_theme_constant_override("separation", 12)
	for n in [num_lb, lbl, slider, val_lb]: row.add_child(n)
	_style_row(row)
	settings_list.add_child(row)

func _add_toggle_row(num: String, label: String, key: String) -> void:
	var row    := HBoxContainer.new()
	var num_lb := Label.new()
	var lbl    := Label.new()
	var toggle := CheckButton.new()

	num_lb.text = num
	lbl.text    = label
	lbl.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	toggle.button_pressed = _settings[key]
	toggle.toggled.connect(func(v): _settings[key] = v)

	row.add_theme_constant_override("separation", 12)
	for n in [num_lb, lbl, toggle]: row.add_child(n)
	_style_row(row)
	settings_list.add_child(row)

func _add_option_row(num: String, label: String, key: String, options: Array) -> void:
	var row    := HBoxContainer.new()
	var num_lb := Label.new()
	var lbl    := Label.new()
	var opt    := OptionButton.new()

	num_lb.text = num
	lbl.text    = label
	lbl.size_flags_horizontal = Control.SIZE_EXPAND_FILL

	for o in options: opt.add_item(o)
	var cur_idx := options.find(_settings[key])
	if cur_idx >= 0: opt.select(cur_idx)
	opt.item_selected.connect(func(i): _settings[key] = options[i])

	row.add_theme_constant_override("separation", 12)
	for n in [num_lb, lbl, opt]: row.add_child(n)
	_style_row(row)
	settings_list.add_child(row)

func _style_row(row: HBoxContainer) -> void:
	row.add_theme_constant_override("separation", 12)
	var sb := StyleBoxFlat.new()
	sb.content_margin_top    = 10
	sb.content_margin_bottom = 10
	# bottom border only
	sb.border_width_bottom = 1
	sb.border_color        = Color(_ink, 0.08)
	sb.bg_color            = Color.TRANSPARENT
	row.add_theme_stylebox_override("panel", sb)

# ── Persist settings ────────────────────────────────────────────
func _load_settings() -> void:
	if _cfg.load(CFG_PATH) == OK:
		for key in _settings.keys():
			if _cfg.has_section_key("settings", key):
				_settings[key] = _cfg.get_value("settings", key)

func _save_settings() -> void:
	for key in _settings.keys():
		_cfg.set_value("settings", key, _settings[key])
	_cfg.save(CFG_PATH)

# ── Glitch timer ──────────────────────────────────────────────
func _start_glitch_timer() -> void:
	_glitch_timer = Timer.new()
	_glitch_timer.one_shot = true
	_glitch_timer.timeout.connect(_fire_chaos_flash)
	add_child(_glitch_timer)
	_glitch_timer.start(randf_range(8.0, 15.0))

func _fire_chaos_flash() -> void:
	_apply_state(TitleState.CHAOS)
	await get_tree().create_timer(0.4).timeout
	_apply_state(TitleState.PAPER)
	_glitch_timer.start(randf_range(8.0, 15.0))

# ── _draw callbacks ────────────────────────────────────────────
func _draw_corners() -> void:
	var s  := corner_marks.size
	var c  := _ink
	var w  := 26.0
	var mg := 18.0
	var t  := 2.5
	# TL
	corner_marks.draw_rect(Rect2(mg, mg, w, t), c)
	corner_marks.draw_rect(Rect2(mg, mg, t, w), c)
	# TR
	corner_marks.draw_rect(Rect2(s.x - mg - w, mg, w, t), c)
	corner_marks.draw_rect(Rect2(s.x - mg - t, mg, t, w), c)
	# BL
	corner_marks.draw_rect(Rect2(mg, s.y - mg - t, w, t), c)
	corner_marks.draw_rect(Rect2(mg, s.y - mg - w, t, w), c)
	# BR
	corner_marks.draw_rect(Rect2(s.x - mg - w, s.y - mg - t, w, t), c)
	corner_marks.draw_rect(Rect2(s.x - mg - t, s.y - mg - w, t, w), c)

func _draw_typebar() -> void:
	var w    := typebar_strip.size.x
	var h    := 4.0
	var step := 4.0
	var x    := 0.0
	while x < w:
		typebar_strip.draw_rect(Rect2(x, 0, 2, h), _ink)
		x += step

func _draw_glitch_bars() -> void:
	if _state != TitleState.CHAOS: return
	var w := glitch_bars.size.x
	var bars := [[175.0, 7.0], [415.0, 3.0], [555.0, 5.0]]
	for b in bars:
		glitch_bars.draw_rect(Rect2(0, b[0], w, b[1]), Color(1, 1, 1, 0.06))
