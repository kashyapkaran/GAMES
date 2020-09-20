import turtle

wn = turtle.Screen()
wn.setup(600,600)

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
font = ("Courier",100,"normal")
global chance

chance = 0

#make the standing lines

#pen.setposition(x, y)
pen.penup()
pen.setposition(-100, 300)
pen.pendown()
pen.setposition(-100, -300)
pen.penup()
pen.setposition(100, 300)
pen.pendown()
pen.setposition(100, -300)

#make the sleeping lines
pen.penup()
pen.setposition(-300,100)
pen.pendown()
pen.setposition(300, 100)
pen.penup()
pen.setposition(-300,-100)
pen.down()
pen.setposition(300,-100)

#make a square around it 
pen.penup()
pen.setposition(-300,300)
pen.pendown()
pen.setpos(300, 300)
pen.right(90)
pen.forward(600)
pen.right(90)
pen.forward(600)
pen.right(90)
pen.forward(600)

pen.penup()
pen.hideturtle()


def draw(x, y):
    global chance
    pen.penup()
    pen.setpos(x, y)
    cursor_x = x
    cursor_y = y
    
    if cursor_x > -300 and cursor_x < -100 and cursor_y > 100 and cursor_y < 300:   
        pen.setpos(-200,150)
        
    elif cursor_x > -100 and cursor_x < 100 and cursor_y > 100 and cursor_y < 300:
        pen.setpos(0,150)
    
    elif cursor_x > 100 and cursor_x < 300 and cursor_y > 100 and cursor_y < 300:
        pen.setpos(200,150)
    
    elif cursor_x > -300 and cursor_x < -100 and cursor_y > -100 and cursor_y < 100:
        pen.setpos(-200, -50) 
        
    elif cursor_x > -100 and cursor_x < 100 and cursor_y > -100 and cursor_y < 100:
        pen.setpos(0, -50)
        
    elif cursor_x > 100 and cursor_x < 300 and  cursor_y > -100 and cursor_y < 100:
        pen.setpos(200, -50)
        
    elif cursor_x > -300 and cursor_x <-100 and cursor_y > -300 and cursor_y < -100:
        pen.setpos(-200, -250)     
        
    elif cursor_x > -100 and cursor_x < 100 and cursor_y > -300 and cursor_y < -100:
        pen.setpos(0, -250)
        
    elif cursor_x > 100 and cursor_x < 300 and cursor_y > -300 and cursor_y < -100:
        pen.setpos(200, -250)

    if chance%2 == 0:
        pen.write("O",align="center", font=font)
    else:
        pen.write("x",align="center", font=font)
    
    chance = chance+1

    

    
wn.onscreenclick(draw)
    

wn.mainloop()