import turtle

wn = turtle.Screen()
wn.bgcolor("purple")


t = turtle.Pen()
t.speed(0)
t.color("red")

for x in range(200):
    t.forward(2*x)
    t.left(90)


wn.mainloop()