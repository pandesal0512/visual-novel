extends PanelContainer

## ═══════════════════════════════════════════════════════
##  CardUI.gd — single card component
##  Attach to the root CardUI (PanelContainer) node
## ═══════════════════════════════════════════════════════

signal clicked

var _data     : Dictionary = {}
var _is_chaos : bool       = false
var _ink      : Color      = Color.BLACK
var _paper    : Color      = Color.WHITE

@onready var type_bar     : Control        = %TypeBar
@onready var icon_label   : Label          = %Icon
@onready var card_name    : Label          = %CardName
@onready var stat_left    : Label          = %StatLeft
@onready var stat_right   : Label          = %StatRight
@onready var cost_badge   : Label          = %CostBadge
@onready var cd_overlay   : PanelContainer = %CooldownOverlay
@onready var cd_label     : Label          = %CDLabel

func setup(data: Dictionary, is_chaos: bool) -> void:
	_data     = data
	_is_chaos = is_chaos
	_ink      = Color.WHITE if is_chaos else Color.BLACK
	_paper    = Color.BLACK if is_chaos else Color.WHITE

	icon_label.text = data.get("icon", "?")
	card_name.text  = data.get("name", "")
	cost_badge.text = str(data.get("cost", 0))

	# Stat display
	var dmg : int = data.get("dmg", 0)
	var nrg : int = data.get("nrg", 0)
	if dmg > 0:
		stat_left.text  = "%d dmg" % dmg
		stat_right.text = ""
	elif nrg > 0:
		stat_left.text  = "+%d nrg" % nrg
		stat_right.text = ""
	else:
		stat_left.text  = data.get("type", "")
		stat_right.text = ""

	var cd : int = data.get("cd", 0)
	if cd > 0:
		stat_right.text = "cd:%d" % cd

	# Cooldown overlay
	var on_cd : bool = data.get("on_cd", false)
	cd_overlay.visible = on_cd
	if on_cd:
		cd_label.text = str(cd)

	_apply_theme()
	type_bar.queue_redraw()

func _apply_theme() -> void:
	# Panel background
	var panel_sb := StyleBoxFlat.new()
	panel_sb.bg_color = _paper
	panel_sb.set_border_width_all(2)
	panel_sb.border_color = _ink
	add_theme_stylebox_override("panel", panel_sb)

	# Text colors
	card_name.add_theme_color_override("font_color", _ink)
	stat_left.add_theme_color_override("font_color",  Color(_ink, 0.55))
	stat_right.add_theme_color_override("font_color", Color(_ink, 0.4))

	# Cost badge — inverted square
	cost_badge.add_theme_color_override("font_color", _paper)
	var cost_sb := StyleBoxFlat.new()
	cost_sb.bg_color = _ink
	cost_badge.add_theme_stylebox_override("normal", cost_sb)

	# Cooldown overlay
	if cd_overlay:
		var cd_sb := StyleBoxFlat.new()
		cd_sb.bg_color = Color(_paper, 0.82)
		cd_overlay.add_theme_stylebox_override("panel", cd_sb)
		cd_label.add_theme_color_override("font_color", _ink)

	# Icon filter (grayscale handled by modulate if needed)
	if _is_chaos:
		icon_label.add_theme_color_override("font_color", Color.WHITE)
	else:
		icon_label.add_theme_color_override("font_color", Color.BLACK)

# ── TypeBar draws the pattern for each card type ────────
func _on_type_bar_draw() -> void:
	if not type_bar or not _data: return
	var w   : float = type_bar.size.x
	var h   : float = type_bar.size.y
	var col : Color = _ink

	match _data.get("type", "attack"):
		"attack":
			type_bar.draw_rect(Rect2(0, 0, w, h), col)

		"ultimate":
			# Thicker solid bar
			type_bar.draw_rect(Rect2(0, 0, w, h), col)

		"barrier":
			# Alternating solid/transparent blocks (horizontal stripes)
			var step := 8.0
			var x := 0.0
			while x < w:
				type_bar.draw_rect(Rect2(x, 0, min(4.0, w - x), h), col)
				x += step

		"dodge":
			# Diagonal stripes
			var step := 6.0
			var x := 0.0
			while x < w:
				type_bar.draw_rect(Rect2(x, 0, min(3.0, w - x), h), col)
				x += step

		"energy":
			# Fine horizontal stripes
			var step := 4.0
			var x := 0.0
			while x < w:
				type_bar.draw_rect(Rect2(x, 0, min(2.0, w - x), h), col)
				x += step

		"buff":
			# Reverse diagonal
			var step := 6.0
			var x := w
			while x > 0:
				type_bar.draw_rect(Rect2(x - 3, 0, min(3.0, x), h), col)
				x -= step

func _ready() -> void:
	# Connect TypeBar's draw signal once it's in the tree
	if type_bar:
		type_bar.draw.connect(_on_type_bar_draw)

# ── Input — click to emit signal ────────────────────────
func _gui_input(event: InputEvent) -> void:
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
			if not _data.get("on_cd", false):
				clicked.emit()
				accept_event()

# ── Hover lift animation ─────────────────────────────────
func _on_mouse_entered() -> void:
	if _data.get("on_cd", false): return
	var tween := create_tween().set_trans(Tween.TRANS_CUBIC).set_ease(Tween.EASE_OUT)
	tween.tween_property(self, "position:y", position.y - 8, 0.12)

func _on_mouse_exited() -> void:
	if _data.get("on_cd", false): return
	var tween := create_tween().set_trans(Tween.TRANS_CUBIC).set_ease(Tween.EASE_OUT)
	tween.tween_property(self, "position:y", position.y + 8, 0.12)
