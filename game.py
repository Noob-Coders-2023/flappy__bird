#Project by : Tina Amini,Zahra Ghasemi,Hasti Rezaiee :)
import pygame
import pygame as pg
import sys
import random
  #VARIABLES
display_width = 576
display_height = 1024
background_image = pygame.image.load("assets/img/bg2.png")

# START PYGAME MODULES
pygame.init()

#Main Display In Game
main_screen = pygame.display.set_mode ((display_width, display_height))

#Game Timer
clock = pygame.time.Clock
while True:
    for event in pygame.event.get()
       if event.type == pygame.Quit:
        #END PYGAME MODULES 
          pygame.quit()
          #TERMINATE PROGRAM
          sys.exit()
      main_screen.blit(background_image, (0, 0))    
      pygame.display.update()  #SET GAME SPEED
      clock.tick(90)
  
     


