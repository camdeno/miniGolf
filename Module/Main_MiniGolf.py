# A simple mini golf game used to learn python


# Launch and Initialize
import pygame
import os 

from pygame.constants import MOUSEBUTTONDOWN                                        
from drawWindow import drawWindow                    
from getMouse import getMouse
from Ball import Ball 

pygame.init()                                        # Initializes pygame

# Declare Constants
WIDTH = 800                                          # CONST that Sets the Width of the Window
HEIGHT = 600                                         # CONST that Sets the Height of the Window
FPS = 60                                             # CONST that Sets the Framerate of the Window
WHITE = (255,255,255)                                # CONST Color White
BLACK = (0,0,0)                                      # CONST Color Black
RED = (255,0,0)                                      # CONST Color Red
XPOS = 200                                           # CONST Starting XPOS for Ball
YPOS = 300                                           # CONST Starting YPOS for Ball


# Create Window and Main Game Loop
display = pygame.display.set_mode ((WIDTH,HEIGHT))   # Sets the display screen size to 800 x 600 -- Fullscreen can be set with 1920,1080
pygame.display.set_caption("Mini Golf")              # Sets the display caption to the game name
pygame.display.update()                              # Pushes the change to the window
open = True                                          # Sets open state

Clock = pygame.time.Clock()                          # Creates a clock to store framerate



#set ball's color, size, and pos
playerBall = Ball(XPOS,YPOS,WHITE)                   # Create playerBall

all_sprites_list = pygame.sprite.Group()             # Create Sprite List
all_sprites_list.add(playerBall)                     # Add playerball to Sprite List

while open:
    Clock.tick(FPS)                                  # Sets the Framerate       
    for event in pygame.event.get():                 # Checking for an event and storing all events in the event box
        if event.type == pygame.QUIT:                # If the X is pressed, Close the game -- This can also be used to handle events such as the close in the UI
           open = False                              # Sets open state to False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
             # Check to see if the ball is under the mouse button
                button = event.button
                isClicked = getMouse(button,playerBall.rect.x,playerBall.rect.y)
             # If True, Draw Vector from where the mouse was to where it gets drug to
                if isClicked == True:
                    playerBall.rect.x += 20         # Move the Ball if it gets touched. 
                # Set the velocity of the ball and the direction using Trig and a Set Velocity --  Call a function?
             # If no, do nothing
    
    #playerBall.rect.x += 1                           # Moves the Rect
    #print(playerBall.rect.x)                         # Prints X POS

    drawWindow(display,BLACK,all_sprites_list)       # Sets the window white
    
pygame.quit()                                        # Quits pygame
quit()                                               # Quits the module


