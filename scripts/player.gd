extends CharacterBody2D

@export var velocidade := 220.0

var nearby_interactable: Interactable = null
var inventory: Dictionary = {}

@onready var interaction_label: Label = $"../InteractionLabel"

func _ready() -> void:
	$InteractionArea.area_entered.connect(_on_interaction_area_entered)
	$InteractionArea.area_exited.connect(_on_interaction_area_exited)
	interaction_label.visible = false

func _physics_process(_delta: float) -> void:
	var direcao = Input.get_vector("move_left", "move_right", "move_up", "move_down")
	velocity = direcao * velocidade
	move_and_slide()

	if Input.is_action_just_pressed("interact"):
		if nearby_interactable != null:
			nearby_interactable.interact(self)
			interaction_label.visible = false
			nearby_interactable = null

func _on_interaction_area_entered(area: Area2D) -> void:
	if area is Interactable:
		nearby_interactable = area
		interaction_label.text = "%s (E)" % area.get_prompt()
		interaction_label.visible = true

func _on_interaction_area_exited(area: Area2D) -> void:
	if area == nearby_interactable:
		nearby_interactable = null
		interaction_label.visible = false

func add_item(item_id: String, item_name: String = "") -> void:
	inventory[item_id] = item_name
	print("Inventário: %s" % inventory)

func has_item(item_id: String) -> bool:
	return inventory.has(item_id)
