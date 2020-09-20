#part - 7(scoring),time - 0:00
#url down below


import turtle,time,random

delay =  0.1

#score
score=0
high_score=0

wn = turtle.Screen()
wn.title("snake")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#snake head
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#PEN
pen = turtle.Turtle()
pen.hideturtle()
pen.shape("square")
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
font = ("Courier",24,"normal")
pen.write("Score:0  High score:0",align="center", font=font)

#functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
    
def go_left():
    if head.direction != "right":
        head.direction = "left"
    
def go_right():
    if head.direction != "left":
        head.direction = "right"
        
        
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    
   
         
        
#keyboard bimding
wn.listen()

wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")


#main game loop
while True:
    wn.update()
    
    #check for a collision (border)
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)
            
            #clear the segment list 
        segments.clear()
        
        #reset delay
        delay = 0.1
        
        #reset score
        score = 0
        
        pen.clear()
        pen.write("score:{}  High score:{}".format(score, high_score),align="center",font=font)
    
    #check collision with food
    if head.distance(food) < 20:
        #move the food to random spot on the screen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        
        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        #shortern the delay
        delay -= 0.001
        
        #increase score
        score += 10
        
        if score > high_score:
            high_score=score
        pen.clear()
        pen.write("score:{}  High score:{}".format(score, high_score),align="center",font=font)
        
        #move the end segments first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
            
        #move segment 0  where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    move()
    
    #check for collision(body)
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)
                
            #clear the segments list
            segments.clear() 
            
            #reset score
            score = 0
            
            #reset delay
            delay = 0.1
        
            #update the score display
            pen.clear()
            pen.write("score:{}  High score:{}".format(score, high_score),align="center",font=font)
            
    
    time.sleep(delay)

wn.mainloop()