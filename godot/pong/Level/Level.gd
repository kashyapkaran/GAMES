extends Node

var PlayerScore = -2
var opponentScore = -1

func _on_Left_body_entered(body):
	$Ball.position = Vector2(512,300)
	opponentScore += 1
	get_tree().call_group('BallGroup','stop_ball')
	$CountDownTimer.start()
	$ScoreSound.play()
	
func _on_Right_body_entered(body):
	$Ball.position = Vector2(512,300)
	PlayerScore += 1
	get_tree().call_group('BallGroup','stop_ball')
	$CountDownTimer.start()
	$ScoreSound.play()
	
func _process(delta):
	$PlayerScore.text = str(PlayerScore)
	$OpponentScore.text = str(opponentScore)


func _on_CountDownTimer_timeout():
	get_tree().call_group('BallGroup','restart_ball')



