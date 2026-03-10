extends CanvasLayer
class_name DialogueSystem

# --- UI References ---
@onready var textbox_label: Label = $TextBox/Label
@onready var speaker_label: Label = $TextBox/SpeakerName
@onready var portrait_left: TextureRect = $Portraits/Left
@onready var portrait_right: TextureRect = $Portraits/Right
@onready var anim_player: AnimationPlayer = $AnimationPlayer

# --- Signals ---
signal dialogue_finished()

# --- State ---
var dialogue_queue: Array = []
var is_waiting_for_input: bool = false

func _input(event):
	if is_waiting_for_input and event.is_action_pressed("ui_accept"):
		advance_dialogue()

func say(speaker: String, text: String, side: String = "left"):
	dialogue_queue.append({
		"speaker": speaker,
		"text": text,
		"side": side
	})

	if not is_waiting_for_input:
		advance_dialogue()

func advance_dialogue():
	if dialogue_queue.is_empty():
		is_waiting_for_input = false
		dialogue_finished.emit()
		return

	var current = dialogue_queue.pop_front()
	is_waiting_for_input = true

	speaker_label.text = current.speaker
	textbox_label.text = current.text

	# Handle sprite focus (dimming the other side)
	if current.side == "left":
		portrait_left.modulate = Color.WHITE
		portrait_right.modulate = Color.GRAY
	else:
		portrait_left.modulate = Color.GRAY
		portrait_right.modulate = Color.WHITE

func hide_textbox():
	$TextBox.hide()

func show_textbox():
	$TextBox.show()
