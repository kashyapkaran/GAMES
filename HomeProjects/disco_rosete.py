import turtle
t = turtle.Pen()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
# ask number of sides
sides = int(turtle.numinput("Number of sides",
                            "How many sides do you want in your disco rossete? 2-11 ",4,2,11))
colors = ["red","yellow","blue","green","orange","purple","white","brown","gray","pink"]
#our outer spiral loop
for m in range(200):
    position = t.position()
    heading = t.heading()
    print(position, heading)
    for n in range(int(m/2)):
        t.circle(200)
        t.pencolor(colors[n%sides])
    t.setpos(position)
    t.setheading(heading)
    t.left(360/sides)