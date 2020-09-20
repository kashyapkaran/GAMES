#spiralfamily.py
import turtle 
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","brown","gray","pink"]
family = []
#ask for the first name
name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
# Keep asking for names
while name != "" :
    #add their name to family list
    family.append(name)
    #ask for another name,or end
    name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
    
#draw a spiral of names on the screen
for m in range(200):
    t.forward(m*4)
    position = t.position()
    heading = t.heading()
    for n in range(len(family)):
        t.pendown()
        t.pencolor(colors[n%len(family)%10])
        t.write(family[n%len(family)], font=("Arial",int((m+4)/4), "bold"))
        t.right(360/len(family))
        t.width(m/20)
        t.penup()
        t.forward(m//2)
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/len(family) + 3)