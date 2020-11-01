#falling skies
#by karan
#time -0:00 ,part - 7

import turtle,random

score = 0
lives = 3
delay = 0.03

wn = turtle.Screen()
wn.title("falling skies")
wn.bgcolor("white")
wn.setup(width=800,height=600)
wn.tracer(0)
#register shape
turtle.register_shape("broccoli.gif")
turtle.register_shape("boy.gif")
turtle.register_shape("candy.gif")

#Add the player
player = turtle .Turtle()
player.speed(0)
player.shape("boy.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"
#create list of good guys
good_guys= []

#Add the good guys
for _ in range(20):
    good_guy = turtle .Turtle()
    good_guy.speed(0)
    good_guy.shape("candy.gif")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(-100, 250)
    good_guy.speed = random.randint(1,4)
    good_guys.append(good_guy)
    
#create list of bad guys
bad_guys= []

#Add the good guys
for _ in range(7):
    bad_guy = turtle .Turtle()
    bad_guy.speed(0)
    bad_guy.shape("broccoli.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(100, 250)
    bad_guy.speed = random.randint(1,4)
    bad_guys.append(bad_guy)
    
#make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0, 260)
font = ("Courier",24,"normal")
pen.write("Score: {} Lives: {}".format(score,lives), align="center", font=font)

    
#function
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"
    
#keyboard binding
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
#main game loop
while True:
    #update screen
    wn.update()
    #move the player
    if player.direction == "left":
            x = player.xcor()
            x -= 3
            player.setx(x)
            
    if player.direction == "right":
            x = player.xcor()
            x += 3
            player.setx(x)
        
    #move the good guys 
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)
         
        #check if of the screen    
        if y <-300:
            x = random.randint(-390,390)
            y = random.randint(300,400)
            good_guy.goto(x,y)
            
        #check for collision with the player
        if good_guy.distance(player)< 40:            
            x = random.randint(-390,390)
            y = random.randint(300,400)
            good_guy.goto(x,y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score,lives), align="center", font=font)
            
            
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)
         
        #check if of the screen    
        if y <-300:
            x = random.randint(-390,390)
            y = random.randint(300,400)
            bad_guy.goto(x,y)
            
            #check for collision with the player
        if bad_guy.distance(player)< 40:            
            x = random.randint(-390,390)
            y = random.randint(300,400)
            bad_guy.goto(x,y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score,lives), align="center", font=font)
    
    
            

wn.mainloop()