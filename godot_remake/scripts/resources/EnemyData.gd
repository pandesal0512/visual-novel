extends Resource
class_name EnemyData

@export var enemy_name: String = "Enemy"
@export var max_hp: int = 100
@export var intents: Array[EnemyIntentData] = []

@export_group("Sprites")
@export var idle_sprite: Texture2D
@export var attack_sprite: Texture2D
@export var hit_sprite: Texture2D
