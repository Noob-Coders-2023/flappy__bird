#Project by : Tina Amini,Zahra Ghasemi,Hasti Rezaiee :)
import pygame
import pygame 
import sys
import random

# START PYGAME MODULES
pygame.init()


def generate_pipe_rect():
    random_pipe = random.randrange(400,800)
    pipe_rect_top = pipe_image.get_rect(midbottom=(700, random_pipe -300))
    pipe_rect_bottom = pipe_image.get_rect(midtop=(700, random_pipe))
    return pipe_rect_top, pipe_rect_bottom


def move_pipe_rect(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    inside_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return pipes


def display_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
           main_screen.blit(pipe_image, pipe)
        else:
             reversed_pipes = pygame.transform.flip(pipe_image, False, True)
             main_screen.blit(pipe_image, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_image_rect.collidedict(pipe):
            return False
        if bird_image_rect.top <= -50 or bird_image_rect.bottom >= 900 
            return False  
    return True    

#VARIABLES
display_width = 576
display_height = 1024
floor_x = 0
gravity = 0.25
bird_movment = 0
pipe_list = []
game_status = True
#-------------#
create_pipe = pygame.USEREVENT
pygame.time.set_timer(create_pipe, 1200)
#-------------#
background_image = pygame.transform.scale2x(pygame.image.load("assets/img/bg2.png"))
floor_image = pygame.transform.scale2x(pygame.image.load("assets/img/floor.png")) 
bird_image = pygame.transform.scale2x(pygame.image.load("assets/img/red_bird_mid.png"))
pipe_image = pygame.transform.scale2x(pygame.image.load('assets/img/pipe_red.png'))

# rectangle  
bird_image_rect = bird_image .get_rect(canter=(100,570))




#Game Timer
clock = pygame.time.Clock
while True:
    for event in pygame.event.get():
      if event.type == pygame.Quit:
        #END PYGAME MODULES 
          pygame.quit()
          #TERMINATE PROGRAM
          sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
              bird_movment = 0
              bird_movment -= 8
      if event.type == create_pipe:
          pipe_list.extend(generate_pipe_rect())      
      
    # DISPLAY BG2.PMG   
    main_screen.blit(background_image, (0, 0))  

    if game_status:
        #Main Display In Game
        main_screen = pygame.display.set_mode ((display_width, display_height))
        #CHECK FOR COLLISIONS
        game_status = check_collision(pipe_list)
        #didplay bird image
        main_screen.blit(bird_image, bird_image_rect)
        # MPVE PIPES
        pipe_list = move_pipe_rect(pipe_list)  
        display_pipes(pipes) 
        # bird gravity and bird movment 
        bird_movment += gravity 
        bird_image_rect.centery += bird_movment


  
    #DISPLAY FLOOR PNG
    floor_x += 1
    main_screen.blit(floor_image, (floor_x + 576, 900)) 
    if floor_x <= -576 :
        floor_x = 0
     
    pygame.display.update()  #SET GAME SPEED
    clock.tick(90)
  

     


