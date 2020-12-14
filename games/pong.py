import turtle


wn = turtle.Screen()
wn.title("Pong by Karan ")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0) 
#score
score_a = 0
score_b = 0



#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-390,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(390,0)

#paddle a/b top/bottom
apad_top = paddle_a.ycor() +50
apad_bot = paddle_a.ycor() -50
bpad_top = paddle_b.ycor() +50
bpad_bot = paddle_b.ycor() -50

#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.speed(1) 
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = -1

#Pen

Pen  = turtle.Turtle()
Pen.speed(0)
Pen.color("white")
Pen.penup()
Pen.hideturtle()
Pen.goto(0,260)
Pen.write("Player A : 0  Player B : 0",align = "center",font=("Ink Free",24, "normal"))

def recalculatePaddleBoundaries():
    global apad_bot,apad_top,bpad_bot,bpad_top
    #paddle a/b top/bottom
    apad_top = paddle_a.ycor() +50
    apad_bot = paddle_a.ycor() -50
    bpad_top = paddle_b.ycor() +50
    bpad_bot = paddle_b.ycor() -50

def printval():
    print("a: "+str(apad_top)+","+str(apad_bot))
    print("b: "+str(bpad_top)+","+str(bpad_bot))
#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 100
    paddle_a.sety(y)
    recalculatePaddleBoundaries()
    printval()
    
def paddle_a_down():        
    y = paddle_a.ycor()            
    y -= 100
    paddle_a.sety(y)
    recalculatePaddleBoundaries()
    printval()
    
def paddle_b_up():    
    y = paddle_b.ycor()
    y += 100
    paddle_b.sety(y)
    recalculatePaddleBoundaries()
    printval()
    
def paddle_b_down(): 
       
    y = paddle_b.ycor()            
    y -= 100
    paddle_b.sety(y)
    recalculatePaddleBoundaries()
    printval()
    #keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
#main game loop
while True:
    wn.update()
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    
    #border checking (ball)
    if ball.ycor() > 300:
        ball.sety(290)
        ball.dy*= -1
     
   
    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy*= -1
        
        
    

    #boder checking (bat)
        
    if bpad_bot < -300:
        paddle_b.sety(-300)
        
        

    
        
    if bpad_top > 300:
        paddle_b.sety(300)
        
        
    if apad_bot < -300:
        paddle_a.sety(-300)
        

    
        
    if apad_top > 300:
        paddle_a.sety(300)
        
        
#score calculater       
    if ball.xcor() > 370:
        ball.setx(370)
        ball.dx *= -1
        if ball.ycor() >=bpad_bot and ball.ycor()<=bpad_top :            
            score_b += 1
            Pen.clear()
            Pen.write("Player a : {}  Player b : {}".format(score_a, score_b),align = "center",font=("Ink Free",24, "normal"))
        
    if ball.xcor() < -370:
        ball.setx(-370)
        ball.dx *= -1
        if ball.ycor() >=apad_bot and ball.ycor() <=apad_top : 
            score_a += 1
            Pen.clear()     
            Pen.write("Player A : {}  Player B : {}".format(score_a, score_b),align = "center",font=("Ink Free",24, "normal"))