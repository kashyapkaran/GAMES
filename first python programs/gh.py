import pygame,sys,random
from pygame.transform

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,450))
    screen.blit(floor_surface,(floor_x_pos + 288,450))
    
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (600,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (600,random_pipe_pos -130))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom < 312:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
            
            
        else:
            screen.blit(pipe_surface,pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -50 or bird_rect.bottom >= 450:
        return False

    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird,-bird_movment * 3,1)
    return new_bird 


pygame.init()
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

#game variables

gravity =0.15
bird_movment = 0

game_active = True

bg_surface = pygame.image.load('FlappyBird_Python-master/assets/background-day.png').convert()
floor_surface = pygame.image.load('FlappyBird_Python-master/assets/base.png').convert_alpha()
floor_x_pos = 0

bird_surface = pygame.image.load('FlappyBird_Python-master/assets/yellowbird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center = (50,256))

pipe_surface =  pygame.image.load('FlappyBird_Python-master/assets/pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1400)

pipe_height = [140,190,300]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE and game_active:
                bird_movment = 0
                bird_movment -= 6
                
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (50,200)
                bird_movment = 0
                
                
            
                
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            
        
                
            
    screen.blit(bg_surface,(0,0))
    
    if game_active:
    
        bird_movment += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movment
        screen.blit(rotated_bird,bird_rect)
        game_active = check_collision(pipe_list)
        
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos =0
                 
        
        
    screen.blit(bird_surface,bird_rect)
    
    
    pygame.display.update()
    clock.tick(120)
