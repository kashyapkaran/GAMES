import math,random
sprites = []
class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1
        self.state = "splash"


    def start_level(self):
        sprites.clear()

        # add player
        sprites.append(player)

        # add missile
        for missile in missiles:
            sprites.append(missile)

        # add enemies
        for _ in range(self.level):
            x = random.randint(-self.width / 2, self.width / 2)
            y = random.randint(-self.height / 2, self.height / 2)
            dx = random.randint(-2, 2)
            dy = random.randint(-2, 2)
            sprites.append(Enemy(x, y, "square", "red"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

        for _ in range(self.level):
            x = random.randint(-self.width / 2, self.width / 2)
            y = random.randint(-self.height / 2, self.height / 2)
            dx = random.randint(-2, 2)
            dy = random.randint(-2, 2)
            sprites.append(Powerup(x, y, "circle", "blue"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

    def render_boder(self, pen, x_offset, y_offset):
        pen.color("white")
        pen.width(3)
        pen.penup()

        left = -self.width / 2.0 - x_offset
        right = self.width / 2.0 - x_offset
        top = self.height / 2.0 - y_offset
        bottom = -self.height / 2.0 - y_offset

        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

    def render_info(self, pen, score, active_enemies=0):
        pen.color("#222255")
        pen.penup()
        pen.goto(400, 0)
        pen.shape("square")
        pen.setheading(90)
        pen.shapesize(10, 32, None)
        pen.stamp()

        pen.color("white")
        pen.width(3)
        pen.goto(300, 400)
        pen.pendown()
        pen.goto(300, -400)

        pen.penup()
        pen.color("white")
        character_pen.scale = 1.0
        character_pen.draw_string(pen, "SPACE ARENA", 400, 270)
        character_pen.draw_string(pen, "SCORE {}".format(score), 400, 240, )
        character_pen.draw_string(pen, "ENEMIES {}".format(active_enemies), 400, 210)
        character_pen.draw_string(pen, "LIVES {}".format(player.lives), 400, 180)
        character_pen.draw_string(pen, "LEVEL {}".format(game.level), 400, 150)

    def start(self):
        self.state = "playing"

game = Game(700, 500)

class Sprite():
    # constructor
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0.0
        self.acceleration = 0.1 / 9
        self.health = 100
        self.max_health = 100
        self.width = 20
        self.height = 20
        self.state = "active"
        self.radar = 200
        self.max_dx = 5
        self.max_dy = 5

    def is_collision(self, other):
        if self.x < other.x + other.width and \
                self.x + self.width > other.x and \
                self.y < other.y + other.height and \
                self.y + self.height > other.y:
            return True
        else:
            return False

    def bounce(self, other):
        temp_dx = self.dx
        temp_dy = self.dy

        self.dx = other.dx
        self.dy = other.dy

        other.dy = temp_dy
        other.dx = temp_dx

    def update(self):
        self.heading += self.da
        self.heading %= 360

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust

        self.x += self.dx
        self.y += self.dy

        self.boder_check()

    def boder_check(self):
        if self.x > game.width / 2.0 - 10:
            self.x = game.width / 2.0 - 10
            self.dx *= -1

        elif self.x < -game.width / 2.0 + 10:
            self.x = -game.width / 2.0 + 10
            self.dx *= -1

        if self.y > game.height / 2.0 - 10:
            self.y = game.height / 2.0 - 10
            self.dy *= -1

        elif self.y < -game.height / 2.0 + 10:
            self.y = -game.height / 2.0 + 10
            self.dy *= -1

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()

            self.render_health_meter(pen, x_offset, y_offset)

    def render_health_meter(self, pen, x_offset, y_offset):
        # draw health meter
        pen.goto(self.x - x_offset - 10, self.y - y_offset + 20)
        pen.width(3)
        pen.pendown()
        pen.setheading(0)

        if self.health / self.max_health < 0.3:
            pen.color("red")
        elif self.health / self.max_health < 0.7:
            pen.color("yellow")
        else:
            pen.color("green")

        pen.fd(20.0 * (self.health / self.max_health))

        if self.health != self.max_health:
            pen.color("grey")
            pen.fd(20 * ((self.max_health - self.health) / self.max_health))

        pen.penup()


class CharacterPen():
    def __init__(self, color="white", scale=1.0):
        self.color = color
        self.scale = scale

        self.characters = {}
        self.characters["1"] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["2"] = ((-5, 10), (5, 10), (5, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["3"] = ((-5, 10), (5, 10), (5, 0), (0, 0), (5, 0), (5, -10), (-5, -10))
        self.characters["4"] = ((-5, 10), (-5, 0), (5, 0), (2, 0), (2, 5), (2, -10))
        self.characters["5"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10))
        self.characters["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
        self.characters["7"] = ((-5, 10), (5, 10), (0, -10))
        self.characters["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
        self.characters["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
        self.characters["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))

        self.characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
        self.characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5, 0), (5, -10), (-5, -10))
        self.characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
        self.characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
        self.characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
        self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
        self.characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
        self.characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))
        self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
        self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
        self.characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
        self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
        self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
        self.characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
        self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
        self.characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
        self.characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10))
        self.characters["V"] = ((-5, 10), (0, -10), (5, 10))
        self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10))
        self.characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))
        self.characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))
        self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0, 0), (0, -10))
        self.characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))

        self.characters["-"] = ((-3, 0), (3, 0))

    def draw_string(self, pen, str, x, y):
        pen.width(2)
        pen.color(self.color)

        # center text
        x -= 15 * self.scale * ((len(str) - 1) / 2)
        for character in str:
            self.draw_character(pen, character, x, y)
            x += 15 * self.scale

    def draw_character(self, pen, character, x, y):
        scale = self.scale

        if character in "abcdefghijklmnopqrstuvwxyz":
            scale *= 0.8

        character = character.upper()

        # Check if the character  is in the dictionary
        if character in self.characters:
            pen.penup()
            xy = self.characters[character][0]
            pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.pendown()
            for i in range(1, len(self.characters[character])):
                xy = self.characters[character][i]
                pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.penup()