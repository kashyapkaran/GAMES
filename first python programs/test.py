# test
import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red","blue","yellow"]
for x in range(300):
    t.pencolor(colors[ x % 3])
    t.forward(2*x)
    t.left(120)
