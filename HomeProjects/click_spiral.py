import turtle
import random

wn = turtle.Screen()

t = turtle.Pen()
t.speed(0)
wn.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","grey"]


def spiral(x, y):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
        


wn.onscreenclick(spiral)

wn.mainloop()