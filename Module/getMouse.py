
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
            print("Hey you have clicked the left mouse button")
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
               print("We registered a down click")
               print(firstClick.x)
               print(firstClick.y)
               return firstClick
            elif mouseStatus == 1:
               check = pygame.mouse.get_pos()
               secondClick = clickPos
               secondClick.x = check[0]
               secondClick.y = check[1]
               print("We registered a up click")
               print(secondClick.x)
               print(secondClick.y)
               return secondClick
        case 2:
            print("Hey you have clicked the middle mouse button")
        case 3:
            print("Hey you have clicked the right mouse button") 
    return