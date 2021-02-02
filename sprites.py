import pygame
from random import random
import math
from util import *

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        self.paddle_size = height

    def moveUp(self, pixels=5):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels=5):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400

    def bounce(self, ball):
        paddleY = self.rect.y + self.paddle_size/2
        ballY = ball.rect.y + ball.height/2
        dY = paddleY - ballY

        dTheta = (dY/(self.paddle_size/2)) * math.pi/3 # radians for 60 degrees
        theta = dTheta + ball.getTheta()
        if theta > math.pi/3:
            theta = math.pi/3
        elif theta <= -math.pi/3:
            theta = -math.pi/3
        x = math.cos(dTheta)
        y = math.sin(dTheta)
        y*=-1

        if ball.dir[0] < 0:
            ball.dir = [x,y]
        else:
            ball.dir = [-x, y]

class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width=10, height=10):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.speed = 5
        self.dir = [1, 0]
        # self.dir[1] = math.sqrt(1 - self.dir[0]**2)
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        self.width = width
        self.height = height
        
    def update(self):
        self.rect.x += self.dir[0] * self.speed
        self.rect.y += self.dir[1] * self.speed
        # print(self.dir)
        # print(self.rect.x, self.rect.y)
        if self.rect.y == 0:
            self.rect.y = 1

    def getTheta(self):
        return math.atan(-1 * self.dir[1]/self.dir[0])
