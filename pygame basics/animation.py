import pygame,sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('attack_1.png'))
        self.sprites.append(pygame.image.load('attack_2.png'))
        self.sprites.append(pygame.image.load('attack_3.png'))
        self.sprites.append(pygame.image.load('attack_4.png'))
        self.sprites.append(pygame.image.load('attack_5.png'))
        self.sprites.append(pygame.image.load('attack_6.png'))
        self.sprites.append(pygame.image.load('attack_7.png'))
        self.sprites.append(pygame.image.load('attack_8.png'))
        self.sprites.append(pygame.image.load('attack_9.png'))
        self.sprites.append(pygame.image.load('attack_10.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating == True

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]


#general setup
pygame.init()
clock = pygame.time.Clock()

#game screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("animation")

#creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            player.animate()

    #drawing
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)

