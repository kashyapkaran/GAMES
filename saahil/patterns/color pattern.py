#square spirall
import turtle
pen = turtle.Pen()
pen.speed(0)
pen.pencolor('green')
turtle.bgcolor('black')
for x in range(1000):
    pen.forward(2*x)
    pen.left(140)
