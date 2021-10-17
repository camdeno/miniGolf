import pygame 
from Ball import Ball

#
# WHITE = (255,255,255)
# BLACK = (0,0,0)
# RED = (255,0,0)

# XPOS = 200
# YPOS = 300


# #set ball's color and size
# playerBall = Ball(XPOS,YPOS,RED)
# #set ball's location on screen
# print(playerBall.pos_x)

# all_sprites_list = pygame.sprite.Group()
# all_sprites_list.add(playerBall)

def drawWindow(display,fillColor,spriteList): 
    display.fill((fillColor))                      # Sets the Window Color

    #all_sprites_list.draw(display)
    spriteList.draw(display)
    pygame.display.update()                    # Updates the window

