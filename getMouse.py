
import pygame
from Ball import Ball
from drawWindow import drawWindow

class clickPos():
    def __init__(self, x, y):
        x = x
        y = y

def getMouse(button):
    match button:
        case 1:
            print("Hey you have clicked the left mouse button")
            click = clickPos
            mousePos = pygame.mouse.get_pos()
            click.x = mousePos[0]
            click.y = mousePos[1]
            print(click.x)
            print(click.y)
            # if (x  is > ball pos x && x is < ball pos x + size && y is > ball pos y && y is < ball pos y + size)
            # Return True
            # elif
            # Return False  
        case 2:
            print("Hey you have clicked the middle mouse button")
        case 3:
            print("Hey you have clicked the right mouse button") 
    return button