# Project by : Tina Amini,Zahra Ghasemi,Hasti Rezaiee :)
import pygame
import pygame
import sys
import random

# START PYGAME MODULES
pygame.init()


def generate_pipe_rect():
    random_pipe = random.randrange(300,600)
    pipe_rect_top = pipe_image.get_rect(midbottom=(700, random_pipe - 200))
    pipe_rect_bottom = pipe_image.get_rect(midtop=(700, random_pipe))
    return pipe_rect_top, pipe_rect_bottom


def move_pipe_rect(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    inside_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return inside_pipes


def display_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 500:
            main_screen.blit(pipe_image, pipe)
        else:
            reversed_pipes = pygame.transform.flip(pipe_image, False, True)
            main_screen.blit(reversed_pipes, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_image_rect.colliderect(pipe):
            return False
        if bird_image_rect.top <= -50 or bird_image_rect.bottom >=650:
            return False
    return True


# VARIABLES
display_width = 576
display_height = 800
floor_x = 0
gravity = 0.25
bird_movement = 0
pipe_list = []
game_status = True
bg_x = 0
# -------------#
creat_pipe = pygame.USEREVENT
pygame.time.set_timer(creat_pipe, 1200)
# -------------#
background_image = pygame.transform.scale(pygame.image.load("assets/img/bg2.png"), (576, 800))
floor_image = pygame.transform.scale(pygame.image.load("assets/img/floor.png"),(576, 300))
bird_image = pygame.transform.scale(pygame.image.load("assets/img/red_bird_mid_flap.png"), (50, 50))
pipe_image = pygame.transform.scale(pygame.image.load('assets/img/pipe_red.png'), (100, 500))

# rectangle
bird_image_rect = bird_image.get_rect(center=(100, 420))
#GAME DISPLAY
main_screen = pygame.display.set_mode((display_width, display_height))


# Game Timer
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # END PYGAME MODULES
            pygame.quit()
            # TERMINATE PROGRAM
            sys.exit()
        #move bird
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8
            if event.key == pygame.K_r and game_status == False:
                    game_status = True
                    pipe_list.clear()
                    bird_image_rect.center = (100, 50)
                    bird_movement = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
                bird_movement = 0
                bird_movement -= 8
        if event.type == creat_pipe:
                pipe_list.extend(generate_pipe_rect())
    # display bg
    bg_x -= 0.1
    main_screen.blit(background_image, (bg_x, 0))
    main_screen.blit(background_image, (bg_x + 576, 0))
    if bg_x <= -576:
        bg_x = 0

    #display ground
    floor_x -= 1
    main_screen.blit(floor_image, (floor_x, 650))
    main_screen.blit(floor_image, (floor_x + 576, 650))
    if floor_x <= -576:
        floor_x = 0


    if game_status:
        # check collision
        check_collision(pipe_list)
        # display bird
        main_screen.blit(bird_image, bird_image_rect)
        # move pipes
        pipe_list = move_pipe_rect(pipe_list)
        display_pipes(pipe_list)
        # check  for collision
        game_status = check_collision(pipe_list)
        # floor gravity and movement
        bird_movement += gravity
        bird_image_rect.centery += bird_movement

    pygame.display.update()
    # SET GAME SPEED
    clock.tick(90)