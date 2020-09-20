#drawing board
#credits karan 

import turtle,time

delay  = 0.1

#set up screen
wn = turtle.Screen()
wn.title("drawing board")
wn.bgcolor("green")
wn.setup(width =  600,height = 600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.goto(0,0)
head.direction = "stop"
head.pencolor("black")


#functions
def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"
    
def go_left():
    head.direction = "left"
    
def go_right():
    head.direction = "right"
    
def stop():
    head.direction = "stop"
    
def erase():
    head.pencolor("green") 
    
def black():
    head.pencolor("black")
    
def orange():
    head.pencolor("orange")
    
def purple():
    head.pencolor("purple")
    
def blue():
    head.pencolor("blue")
    
def red():
    head.pencolor("red")
    
def yellow():
    head.pencolor("yellow")
    
#def blue

def move():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y + 10)
    
    if head.direction == "down" :
        y = head.ycor()
        head.sety(y - 10)
        
    if head.direction == "left" :
        x = head.xcor()
        head.setx(x - 10)
        
    if head.direction == "right" :
        x = head.xcor()
        head.setx(x + 10)

#keyboard binding 
wn.listen()

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

wn.onkeyrelease(stop, "Up")
wn.onkeyrelease(stop, "Down")
wn.onkeyrelease(stop, "Left")
wn.onkeyrelease(stop, "Right")

wn.onkeyrelease(stop, "w")
wn.onkeyrelease(stop, "s")
wn.onkeyrelease(stop, "a")
wn.onkeyrelease(stop, "d")

wn.onkeypress(erase, "e")

wn.onkeypress(black, "1")
wn.onkeypress(orange, "2")
wn.onkeypress(purple, "3")
wn.onkeypress(blue, "4")
wn.onkeypress(red, "5")
wn.onkeypress(yellow, "6")

#main  game loop
while True:
    wn.update()

    move()  
    
    time.sleep(delay)


wn.mainloop()