import turtle,random,time


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("dodge it!")
wn.setup(width=600,height=600)
wn.tracer(0)

lives = 10


#function
def go_left():
    player.direction = "left"
    
def go_right():
    player.direction = "right"

#create player
player = turtle.Turtle()
player.shape("square")
player.speed(0)
player.color("blue")
player.penup()
player.goto(0, -250)
player.direction = "stop"


#create many enemies
enemies = []

#create enemies

for _ in range(10):
    enemy = turtle.Turtle()
    enemy.shape("square")
    enemy.speed(0)
    enemy.color("red")
    enemy.penup()
    enemy.goto(0,250)
    enemy.speed = random.randint(1,4)
    enemies.append(enemy)


#create pen
pen = turtle.Turtle()
pen.hideturtle()
pen.shape("square")
pen.speed(0)
pen.color("blue")
pen.penup()
pen.goto(0, 250)
font = ("Courier",24,"normal")
pen.write("Lives:{}".format(lives), align="center",font=font)

#keyboard binding
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
def main():
    global lives
    #main game loop
    while True:
        wn.update()
        if player.direction == "left":
            x = player.xcor()
            x -= 3
            player.setx(x)

        if player.direction == "right":
            x = player.xcor()
            x += 3
            player.setx(x)

        #move the enemies
        for enemy in enemies:
            y = enemy.ycor()
            y-= enemy.speed
            enemy.sety(y)

        #check if of the screen
            if y < -300:
                x = random.randint(-290,290)
                y = random.randint(200,300)
                enemy.goto(x,y)

            #check for collision
            if enemy.distance(player) < 20:
                x = random.randint(-290,290)
                y = random.randint(200,300)
                enemy.goto(x,y)
                lives -= 1
                pen.clear()
                pen.write("Lives:{}".format(lives), align="center",font=font)

        if lives <= 0:
            pen.clear()
            pen.write("GAME OVER! ".format(), align="center",font=font)
            time.sleep(3)
            pen.clear()
            lives = 10
            pen.write("Lives:{}".format(lives), align="center", font=font)

            main()


main()
wn.mainloop()