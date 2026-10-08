extends ColorRect

var current_puzzle: Puzzle = null
var player_ref: Node = null

@onready var question_label: Label = $QuestionLabel
@onready var answer_input: LineEdit = $AnswerInput
@onready var submit_button: Button = $SubmitButton

func _ready() -> void:
	visible = false
	if submit_button:
		submit_button.pressed.connect(_on_submit_pressed)

func activate(question: String, puzzle: Puzzle, player: Node = null) -> void:
	current_puzzle = puzzle
	player_ref = player
	question_label.text = question
	answer_input.text = ""
	visible = true
	answer_input.grab_focus()

func _on_submit_pressed() -> void:
	if current_puzzle == null:
		visible = false
		return

	var answer = answer_input.text.strip_edges().to_lower()
	var expected = current_puzzle.expected_answer.strip_edges().to_lower()

	if answer == expected:
		current_puzzle.solve(player_ref)
		visible = false
		answer_input.text = ""
		current_puzzle = null
		player_ref = null
		return

	question_label.text = "Resposta incorreta. Tente novamente."
	answer_input.text = ""
