extends KinematicBody2D
class_name Actor
''' https://youtu.be/Mc13Z2gboEk?t=1053 '''

func _physics_process(delta: float) -> void:
	move_and_slide()
