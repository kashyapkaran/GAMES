extends KinematicBody2D

var speed = 400

func _physics_process(delta):
	var velocity = Vector2.ZERO
	move_and_slide(velocity * speed)
