import turtle

wn = turtle.Screen()


pen = turtle.Pen()
pen.speed(0)


def erase():
    pen.pencolor("white")
    pen.width(50)
    
def unerase():
    pen.color("black")
    pen.width(1)
    
def orange():
    pen.color("orange")
    
    
wn.listen()

wn.onkeypress(erase, "e")
wn.onkeypress(unerase, "1")
wn.onkeypress(orange, "2")


wn.onscreenclick(pen.setpos)

wn.mainloop()