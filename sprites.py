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

        self.x = 0
        self.y = 0

    def moveUp(self, pixels=PADDLE_SPEED):
        self.y -= pixels
        if self.y < BANNER_HEIGHT:
            self.y = BANNER_HEIGHT
        self.update()

    def moveDown(self, pixels=PADDLE_SPEED):
        self.y += pixels
        if self.y > PLAY_AREA[1]+BANNER_HEIGHT-PADDLE_SIZE[1]:
            self.y = PLAY_AREA[1]+BANNER_HEIGHT-PADDLE_SIZE[1]
        self.update()

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def bounce(self, ball):
        paddleY = self.y + self.paddle_size/2
        ballY = ball.y + ball.height/2
        dY = paddleY - ballY

        dTheta = (dY/(self.paddle_size/2)) * math.pi/4 # radians for 45 degrees
        theta = dTheta + ball.getTheta()
        if theta > math.pi/4:
            theta = math.pi/4
        elif theta <= -math.pi/4:
            theta = -math.pi/4
        x = math.cos(dTheta)
        y = math.sin(dTheta)
        y*=-1

        if ball.dir[0] < 0:
            ball.dir = [x,y]
        else:
            ball.dir = [-x, y]

        ball.speed *= BALL_SPEED_FACTOR

class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width=BALL_SIZE[0], height=BALL_SIZE[1], serve='right'):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.speed = BALL_SPEED_START
        if serve == 'right':
            self.dir = [1, 0]
        else:
            self.dir = [-1, 0]
        # self.dir[1] = math.sqrt(1 - self.dir[0]**2)
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        self.width = width
        self.height = height

        self.x = 0.0
        self.y = 0.0
        
    def update(self):
        self.x += self.dir[0] * self.speed
        self.y += self.dir[1] * self.speed
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        # if self.rect.y == 0:
        #     self.rect.y = 1

    def getTheta(self):
        return math.atan(-1 * self.dir[1]/self.dir[0])
