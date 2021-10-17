import pygame

WHITE = (255,255,255)
WIDTH = 80
HEIGHT = 50
ballImg = pygame.image.load("Assets/golfball.png")
smallBall = pygame.transform.scale(ballImg, (WIDTH,HEIGHT))
class Ball(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,color):
        super().__init__()
        self.image = smallBall
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.rect.x = pos_x
        self.rect.y = pos_y

   