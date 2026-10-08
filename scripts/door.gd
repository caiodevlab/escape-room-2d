extends Interactable
class_name Door

@export var required_item: String = ""
@export var lock_message: String = "A porta está trancada."
@export var unlock_message: String = "Porta destrancada."
@export var locked_color: Color = Color(0.78, 0.24, 0.24, 1.0)
@export var unlocked_color: Color = Color(0.25, 0.75, 0.35, 1.0)

var is_open: bool = false

func interact(player: Node = null) -> void:
	if is_open:
		print("A porta já está aberta.")
		return

	if required_item != "" and player != null and player.has_method("has_item") and player.has_item(required_item):
		is_open = true
		modulate = unlocked_color
		print(unlock_message)
		return

	print(lock_message)
	modulate = locked_color
