#rossete4py
import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
t.width(3)
number_of_circles = int(turtle.numinput("Number of circles",
                     "How many circles do you want in your rosette?", 6))
for x in range(number_of_circles):
    t.pencolor("red")
    t.circle(200)
    t.pencolor("purple")
    t.circle(150)
    t.left(360/number_of_circles)
