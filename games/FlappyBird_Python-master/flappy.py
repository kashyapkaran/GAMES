#after collision
import pygame,sys,random


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
    new_bird = pygame.transform.rotate(bird, -bird_movment*7)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (50,bird_rect.centery))
    return new_bird,new_bird_rect 

def score_display(game_state):
    if game_state =='main_game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (144,100))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (144,100))
        screen.blit(score_surface,score_rect)
        
        high_score_surface = game_font.render(f'high score: {int(high_score)}',True,(255,255,255))
        high_score_rect = score_surface.get_rect(center = (144,425))
        screen.blit(high_score_surface,high_score_rect)

def update_score(score,high_score):
    if score > high_score:
        high_score = score
    return high_score

pygame.init()
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',30)
#game variables

gravity =0.15
bird_movment = 0
score = 0
high_score = 0

game_active = True

bg_surface = pygame.image.load('FlappyBird_Python-master/assets/background-day.png').convert()
floor_surface = pygame.image.load('FlappyBird_Python-master/assets/base.png').convert_alpha()
floor_x_pos = 0

bird_downflap = pygame.image.load('FlappyBird_Python-master/assets/yellowbird-downflap.png').convert_alpha()
bird_midflap = pygame.image.load('FlappyBird_Python-master/assets/yellowbird-midflap.png').convert_alpha()
bird_upflap = pygame.image.load('FlappyBird_Python-master/assets/yellowbird-upflap.png').convert_alpha()
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (50,256))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)


#bird_surface = pygame.image.load('FlappyBird_Python-master/assets/yellowbird-midflap.png').convert()
#bird_rect = bird_surface.get_rect(center = (50,256))

pipe_surface =  pygame.image.load('FlappyBird_Python-master/assets/pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1400)

pipe_height = [140,190,300]

game_over_surface = pygame.image.load('FlappyBird_Python-master/assets/message.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center = (144,256))
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
                score = 0
                
            
                
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1 
            else:
                screen.blit(game_over_surface,game_over_rect)
                high_score = update_score(score,high_score)
                score_display('game_over')
            bird_surface,bird_rect = bird_animation()    
                    
            
            
        
                
            
    screen.blit(bg_surface,(0,0))
    
    if game_active:
    
        bird_movment += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movment  
        screen.blit(rotated_bird,bird_rect)
        game_active = check_collision(pipe_list)
        
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        
        score += 0.01
        score_display('main_game')
    else:
        high_score = update_score(score, high_score)
        score_display('game_over')
        
        
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos =0
                 
        
        
    screen.blit(rotated_bird,bird_rect)
    
    
    pygame.display.update()
    clock.tick(70)
