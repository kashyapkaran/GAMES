import turtle
t = turtle.Pen()
t.speed(0)
t.width(2)
t.penup()
turtle.bgcolor("black")
# ask number of sides
sides = int(turtle.numinput("Number of sides",
                            "How many sides do you want in your 'KING OF SPIRALS'? 2-6 ",4,2,6))
colors = ["red","yellow","blue","green","purple","orange"]
#our outer spiral loop
for m in range(200):
    t.forward(m*4)
    position = t.position()
    heading = t.heading()
    print(position, heading)
    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.left(360/sides + 2)