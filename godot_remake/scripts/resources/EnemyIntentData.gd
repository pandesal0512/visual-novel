extends Resource
class_name EnemyIntentData

@export var intent_name: String = "Attack"
@export var damage: int = 0
@export_multiline var description: String = ""
@export_enum("attack", "barrier", "energy", "dodge", "buff", "precedent", "sentence_passed", "the_bill", "recidivism", "accumulated_weight") var intent_type: String = "attack"
@export var cooldown: int = 0

@export_group("Buffs")
@export var buff_type: String = ""
@export var buff_duration: int = 0

@export_group("Visuals")
@export var animation_name: String = ""
@export var card_image: Texture2D
