# A simple mini golf game used to learn python


# Launch and Initialize
import pygame                                        # Launches Pygame

from drawWindow import drawWindow                    

pygame.init()                                        # Initializes pygame

# Declare Constants
WIDTH = 800                                          # CONST that Sets the Width of the Window
HEIGHT = 600                                         # CONST that Sets the Height of the Window
FPS = 60                                             # CONST that Sets the Framerate of the Window

# Create Window and Main Game Loop
display = pygame.display.set_mode ((WIDTH,HEIGHT))   # Sets the display screen size to 800 x 600 -- Fullscreen can be set with 1920,1080
pygame.display.update()                              # Pushes the change to the window
open = True                                          # Sets open state
while open:                                             
    for event in pygame.event.get():                 # Checking for an event and storing all events in the event box
        if event.type == pygame.QUIT:                # If the X is pressed, Close the game -- This can also be used to handle events such as the close in the UI
           open = False                              # Sets open state to False

    drawWindow(display)                              # Sets the window white

    
pygame.quit()                                        # Quits pygame
quit()                                               # Quits the module


