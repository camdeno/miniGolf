
import pygame
from Ball import Ball
from drawWindow import drawWindow

class clickPos():
    def __init__(self, x, y):
        x = x
        y = y

def getMouse(button, ballXPos, ballYPos, mouseStatus):
    match button:
        case 1:
            click = clickPos
            firstClick = clickPos
            secondClick = clickPos
            mousePos = pygame.mouse.get_pos()
            click.x = mousePos[0]
            click.y = mousePos[1]
            # if ((click.x > ballXPos) and (click.x < (ballXPos + 80)) and (click.y > ballYPos) and (click.y < (ballYPos + 50))):
            #     return True
            # else:
            #     return False
            if mouseStatus == 0:
               check = pygame.mouse.get_pos()
               firstClick = clickPos
               firstClick.x = check[0]
               firstClick.y = check[1]
               return firstClick
            elif mouseStatus == 1:
               check = pygame.mouse.get_pos()
               secondClick = clickPos
               secondClick.x = check[0]
               secondClick.y = check[1]
               return secondClick
        case 2: # Middle Mouse Button
            # Avoid returning an error by returning 0. No Vector can be created with 0 
            click = clickPos
            click.x = 0
            click.y = 0
            return click
        case 3: # Right Mouse Button
            # Avoid returning an error by returning 0. No Vector can be created with 0 
            click = clickPos
            click.x = 0
            click.y = 0
            return click
    return