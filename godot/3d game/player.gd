extends KinematicBody

var speed = 10
var acceleration = 20
var gravity = 9.8
var jump = 5

var mouse_sensitivity = 0.05

var direction = Vector3()
var velocity = Vector3()
var fall = Vector3()

onready var head = $head
onready var aimcast = $head/Camera

func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
	
	
func _input(event):
	if event is InputEventMouseMotion:
		rotate_y(deg2rad(-event.relative.x * mouse_sensitivity)) 
		head.rotate_x(deg2rad(-event.relative.y * mouse_sensitivity))
		head.rotation.y = clamp(head.rotation.x, deg2rad(-90), deg2rad(90))
	
	if event is InputEventJoypadMotion:
		
		rotate_y(deg2rad(-event.relative.x * mouse_sensitivity)) 
		head.rotate_x(deg2rad(-event.relative.y * mouse_sensitivity))
		head.rotation.y = clamp(head.rotation.x, deg2rad(-90), deg2rad(90))

func _process(delta):
	
	direction = Vector3()
	
	if not is_on_floor():
		fall.y -= gravity * delta
	if is_on_floor():
		if Input.get_action_strength("jump"):
			fall.y = jump
	
	if Input.get_action_strength("ui_cancel"):
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
	
	if Input.get_action_strength("move_forward"):
		direction -= transform.basis.z
		
	elif Input.get_action_strength("move_backward"):
		direction += transform.basis.z
		
	if Input.get_action_strength("move_left"):
		direction -= transform.basis.x
		
	elif Input.get_action_strength("move_right"):
		direction += transform.basis.x
	

	direction = direction.normalized()
	velocity = velocity.linear_interpolate(direction * speed, acceleration * delta)
	velocity = move_and_slide(velocity,Vector3.UP)
	move_and_slide(fall,Vector3.UP)

#func _fixed_process(delta):
	#var right_analog_axis = Vector2(Input.get_joy_axis(0,JOY_AXIS_2),Input.get_joy_axis(0,JOY_AXIS_3))
	#rotate_y(deg2rad(-right_analog_axis.y * mouse_sensitivity)) 
	#head.rotate_x(deg2rad(-right_analog_axis.x * mouse_sensitivity))
	#head.rotation.x = clamp(head.rotation.x, deg2rad(-90), deg2rad(90))
	
	#$head.set_rotation(Vector3(0, right_analog_axis.angle(), 0))
	
	
	
	
