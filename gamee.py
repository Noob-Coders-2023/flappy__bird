#Project by : Tina Amini,Zahra Ghasemi,Hasti Rezaiee :)

import pygame 
import sys
import random

# START PYGAME MODULES
pygame.init()


def generate_pipe_rect():

    pipe_rect=pipe_image.get_rect(midtop=(200,500))
    return pipe_rect

def move_pipe_rect(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    return pipes
#VARIABLES
display_width = 576
display_height = 1024
floor_x = 0
gravity = 0.25
bird_movment = 0
pipe_list = []
#-------------#
create_pipe = pygame.USEREVENT
pygame.time.set_timer(create_pipe, 1200)
#-------------#
background_image = pygame.transform.scale2x(pygame.image.load("assets/img/bg2.png"))
floor_image = pygame.transform.scale2x(pygame.image.load("assets/img/floor.png"))
bird_image = pygame.transform.scale2x(pygame.image.load("assets/img/red_bird_mid_flap.png"))
pipe_image = pygame.transform.scale2x(pygame.image.load('assets/img/pipe_red.png'))

# rectangle  
bird_image_rect=bird_image.get_rect(center=(100,520))



#GAME DISPLAY
main_screen = pygame.display.set_mode((display_width, display_height))



#Game Timer
clock = pygame.time.Clock()


#GAME LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             #END PYGAME MODULES
             pygame.quit()
             #TERMINATE PROGRAM
             sys.exit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                bird_movment = 0
                bird_movment -= 8
        if event.type == create_pipe:
                pipe_list.append(generate_pipe_rect())
    #DISPLAY BG2.PMG
    main_screen.blit(background_image, (0, 0))

    # DISPLAY BIRD IMAGE
    main_screen.blit(bird_image, bird_image_rect)

    #FLOOR GRAVITY AND BIRD MOVMENT
    bird_movment += gravity
    bird_image_rect.centery += bird_movment

    #DISPLAY FLOOR PNG
    floor_x -= 1
    main_screen.blit(floor_image, (floor_x , 900))
    main_screen.blit(floor_image, (floor_x + 576, 900))
    if floor_x <= -576:
        floor_x = 0
     
    pygame.display.update()
    #SET GAME SPEED
    clock.tick(90)


     


