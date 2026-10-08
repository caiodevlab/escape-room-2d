extends Area2D
class_name Interactable

@export var prompt: String = "Interagir"
@export var message: String = "Você interagiu com o objeto."
@export var one_time_use: bool = true

signal interacted

var is_active: bool = true

func get_prompt() -> String:
	return prompt

func interact() -> void:
	if not is_active:
		return

	is_active = not one_time_use
	interacted.emit()
	print(message)

	if not one_time_use:
		modulate = Color(0.7, 0.7, 0.7, 1.0)
