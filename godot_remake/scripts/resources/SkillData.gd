extends Resource
class_name SkillData

@export var skill_name: String = "Skill"
@export var icon: String = "S"
@export_multiline var description: String = ""
@export var cost: int = 0
@export var damage: int = 0
@export var energy_regen: int = 0
@export var cooldown: int = 0
@export_enum("attack", "barrier", "energy", "dodge", "buff", "ultimate", "unravel", "fracture", "corrode", "inversion", "collapse", "leech", "overload") var skill_type: String = "attack"

@export_group("Buffs")
@export var buff_type: String = ""
@export var buff_duration: int = 0

@export_group("Visuals")
@export var card_image: Texture2D
@export var animation_name: String = ""
@export var is_chaos_skill: bool = false
