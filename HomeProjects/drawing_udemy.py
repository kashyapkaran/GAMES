import turtle

t = turtle.Pen()
wn = turtle.Screen()
t.speed(0)
wn.bgcolor("blue")

t.pencolor("green")
t.width(99)
wn.onscreenclick(t.setpos)


wn.mainloop()