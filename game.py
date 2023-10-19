# Project by : Tina Amini,Zahra Ghasemi,Hasti Rezaiee :)
import time

import pygame
import pygame
import sys
import random

# START PYGAME MODULES
pygame.init()

# VARIABLES
display_width = 576
display_height = 800
floor_x = 0
gravity = 0.25
bird_movement = 0
pipe_list = []
game_status = True
bg_x = 0
bird_list_index = 0
game_font=pygame.font.Font('assets/font/flappy.TTF',40)
score=0
high_score =0
active_score= True


# -------------#
background_image = pygame.transform.scale(pygame.image.load("assets/img/bg2.png"), (576, 800))
floor_image = pygame.transform.scale(pygame.image.load("assets/img/floor.png"), (576, 300))

bird_image_down = pygame.transform.scale(pygame.image.load("assets/img/red_bird_down_flap.png"), (50, 50))
bird_image_up = pygame.transform.scale(pygame.image.load("assets/img/red_bird_down_flap.png"), (50, 50))
bird_image_maid = pygame.transform.scale(pygame.image.load("assets/img/red_bird_mid_flap.png"), (50, 50))
bird_list = [bird_image_up, bird_image_maid, bird_image_down]
bird_image = bird_list[bird_list_index]

pipe_image = pygame.transform.scale(pygame.image.load('assets/img/pipe_red.png'), (100, 500))
game_over_image=pygame.transform.scale(pygame.image.load('assets/img/message.png'), (150, 400))
game_over_image_rect=game_over_image.get_rect(center=(288,352))
def generate_pipe_rect():
    random_pipe = random.randrange(300, 600)
    pipe_rect_top = pipe_image.get_rect(midbottom=(700, random_pipe -200))
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
    global active_score
    for pipe in pipes:
        if bird_image_rect.colliderect(pipe):
            active_score=True
            return False
        if bird_image_rect.top<=-50 or bird_image_rect.bottom>=900:
            active_score = True
            return False
    return True


def bird_animition():
    new_bird = bird_list[bird_list_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_image_rect.centery))
    return new_bird, new_bird_rect

def display_score(status):
    if status =='active':
        text1=game_font.render(str(score),False,(255,255,255))
        text1_rect=text1.get_rect(center=(288,100))
        main_screen.blit(text1,text1_rect)
    if status == 'game_over':
        # SCORE
        text1 = game_font.render(f'Score : {score}', False, (255, 255, 255))
        text1_rect = text1.get_rect(center=(288, 100))
        main_screen.blit(text1, text1_rect)
        # HIGH SCORE
        text2 = game_font.render(
            f'HighScore : {high_score}', False, (255, 255, 255))
        text2_rect = text2.get_rect(center=(288, 600))
        main_screen.blit(text2, text2_rect)

def update_score():
    global score,high_score,active_score
    if pipe_list:
        for pipe in pipe_list:
            if 95<pipe.centerx<105 and active_score:
                score+=1
                active_score=False
            if pipe.centerx<0:
                active_score=True
    if score>high_score:
        high_score=score
    return high_score
# -------------#
creat_pipe = pygame.USEREVENT
creat_flap = pygame.USEREVENT +1
pygame.time.set_timer(creat_pipe,1200)
pygame.time.set_timer(creat_flap,100)

# rectangle
bird_image_rect = bird_image.get_rect(center=(100, 420))
# GAME DISPLAY
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
        # move bird
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8
            if event.key == pygame.K_r and game_status == False:
                game_status = True
                pipe_list.clear()
                bird_image_rect.center = (100, 50)
                bird_movement = 0
                score=0
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird_movement = 0
            bird_movement -= 8
        if event.type == creat_pipe:
            pipe_list.extend(generate_pipe_rect())

        if event.type == creat_flap:
            if bird_list_index < 2 :
                bird_list_index += 1
            else:
                bird_list_index = 0
            bird_image, bird_image_rect = bird_animition()
    # display bg
    bg_x -= 0.1
    main_screen.blit(background_image, (bg_x, 0))
    main_screen.blit(background_image, (bg_x + 576, 0))
    if bg_x <= -576:
        bg_x = 0

    # display ground
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
        #SHOW SCORE
        update_score()
        display_score('active')

    else:

        display_score('game_over')
        main_screen.blit(game_over_image,game_over_image_rect)

    pygame.display.update()
    # SET GAME SPEED
    clock.tick(90)
