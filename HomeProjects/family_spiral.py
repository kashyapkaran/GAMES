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
for x in range (300):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)],font = ("Ink Free", int ((x+4)/4) ))
    t.left(360/len(family) + 2)