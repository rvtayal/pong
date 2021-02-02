import sys, pygame
from sprites import Paddle, Ball
import math
from util import *
pygame.init()

# Open a window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

carryOn = True

clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False  

    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)  
    
    # --- Game logic should go here
    all_sprites_list.update()

    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        ball.dir[0] = -ball.dir[0]
    if ball.rect.x<0:
        ball.dir[0] = -ball.dir[0]
    if ball.rect.y>490:
        ball.dir[1] = -ball.dir[1]
    if ball.rect.y<0:
        ball.dir[1] = abs(ball.dir[1]) 

    # Detect collisions and bounce ball
    if pygame.sprite.collide_mask(ball, paddleA):
        paddleA.bounce(ball)
    elif pygame.sprite.collide_mask(ball, paddleB):
        paddleB.bounce(ball)

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()