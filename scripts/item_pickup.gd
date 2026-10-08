extends Interactable
class_name ItemPickup

@export var item_id: String = "item"
@export var item_name: String = "Item"

func interact(player: Node = null) -> void:
	if not is_active:
		return

	if player != null and player.has_method("add_item"):
		player.add_item(item_id, item_name)
		print("Item coletado: %s" % item_name)

	is_active = false
	visible = false
	queue_free()
