#Project by : Tina Amini,Zahra Ghasemi,Hasti Rezaiee :)
import pygame
import pygame 
import sys
import random

# START PYGAME MODULES
pygame.init()


def generate_pipe_rect():
    pipe_rect = pipe_image.get_rect(midtop=(200, 500))
    return pipe_rect


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
bird.image = pygame.transform.scale2x(pygame.image.load("assets/img/red_bird_mid.png"))
pipe_image = pygame.transform.scale2x(pygame.image.load('assets/img/pipe_red.png'))

# rectangle  
bird.image.rec = bird_image .get_rect(canter=(100,570))



#Main Display In Game
main_screen = pygame.display.set_mode ((display_width, display_height))

#didplay bird image
main_screen.blit(bird_image, bird _image_rect)

#Game Timer
clock = pygame.time.Clock
while True:
    for event in pygame.event.get()
      if event.type == pygame.Quit:
        #END PYGAME MODULES 
          pygame.quit()
          #TERMINATE PROGRAM
          sys.exit()
      if event.type == pygame.KEYDOWN:
          if event.key == py .K_SPACE:
              bird_movment = 0
              bird_movment -= 8
      if event.type == create_pipe:
          pipe_list.append(generate_pipe_rect())      
      #DISPLAY BG2.PMG   
      main_screen.blit(background_image, (0, 0)) 
     
      # bird gravity and bird movment 
      bird_movment += gravity 
      bird._image_rect.centery += bird_movment
     
      #DISPLAY FLOOR PNG
      floor_x += 1
      main_screen.blit(floor_image, (floor_x + 576, 900)) 
      if floor_x <= -576 :
         floor_x = 0
     
      pygame.display.update()  #SET GAME SPEED
      clock.tick(90)
  

     


