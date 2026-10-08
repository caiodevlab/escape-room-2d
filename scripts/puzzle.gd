extends Interactable
class_name Puzzle

@export var question: String = "Qual é a resposta?"
@export var expected_answer: String = "42"
@export var reward_item: String = "pista"
@export var reward_name: String = "Pista"
@export var success_message: String = "Resposta correta!"

var solved: bool = false

func interact(player: Node = null) -> void:
	if solved:
		print("Esse enigma já foi resolvido.")
		return

	var panel = get_tree().root.get_node_or_null("/root/Main/AnswerPanel")
	if panel != null and panel.has_method("activate"):
		panel.activate(question, self, player)
		return

	print("Painel de resposta não encontrado.")

func solve(player: Node = null) -> void:
	if player != null and player.has_method("add_item"):
		player.add_item(reward_item, reward_name)
		solved = true
		print(success_message)
