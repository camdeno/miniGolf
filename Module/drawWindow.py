import pygame 
from Ball import Ball


def drawWindow(display,fillColor,spriteList): 
    display.fill((fillColor))                      # Sets the Window Color

    #all_sprites_list.draw(display)
    spriteList.draw(display)
    pygame.display.update()                    # Updates the window

