extends KinematicBody2D

const UP = Vector2(0, -1)
const GRAVITY = 2.7
const JUMP_HEIGHT = -260
const SPEED = 330

var motion = Vector2()  #.ZERO

func _physics_process(delta):
	

	
	if (Input.is_action_pressed("ui_right")):
		motion.x = SPEED
		
	elif (Input.is_action_pressed("ui_left")):
		motion.x = -SPEED
		
	else:
		motion.x = 0
	
	motion.y += GRAVITY
	
	if is_on_floor() or is_on_wall():
		if Input.is_action_just_pressed("ui_up"):
			motion.y = JUMP_HEIGHT
				
	if motion.y >= 600 :
		get_tree().quit()
		
			
	motion = move_and_slide(motion, UP)

