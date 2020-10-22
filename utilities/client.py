#https://youtu.be/F257x_E6H4k?list=PLzMcBGfZo4-kR7Rh-7JCVDN8lm3Utumvq

import pygame
from network import Network
width = 500
height = 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("client")

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        
        if keys[pygame.K_UP]:
            self.y -= self.vel
        
        if keys[pygame.K_DOWN]:
            self.y += self.vel
    
        self.update()
    
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str1):
    print("inside readpos "+str(str1))
    str1 = str1.split(",")
    #str1 = str(str1).split(",")
    print("str1 "+str1[0]+":"+str(len(str1)))
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    print("gepos"+str(n.getPos()))
    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    print(startPos[0])
    print("Player p "+ str(p.x)+str(p.y))
    p2 = Player(0,0,100,100,(255,0,0))
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        print(str(n.send(make_pos((p.x, p.y)))))
        p2pos = read_pos(str(n.send(make_pos((p.x, p.y)))))
        p2.x = p2pos[0]
        p2.y = p2pos[1]
        p2.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        #input("Press any key1")
        p.move()
        #input("Press any key2")
        redrawWindow(win, p, p2)



main()
    
    
    