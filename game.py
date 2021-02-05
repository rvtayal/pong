import sys, pygame
from sprites import Paddle, Ball
import math
from util import *

def game_init() -> GameData:
    gd = GameData()
    gd.l_score = 0
    gd.r_score = 0
    pygame.init()
    pygame.font.init()

    # Open a window
    size = SCREEN_SIZE
    gd.screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")
    return gd


def game_end():
    pygame.quit()


def round_init(gd:GameData):
    gd.paddleA = Paddle(WHITE, PADDLE_SIZE[0], PADDLE_SIZE[1])
    gd.paddleA.x = 20
    gd.paddleA.y = (PLAY_AREA[1]/2 - PADDLE_SIZE[1]/2) + BANNER_HEIGHT
    
    gd.paddleB = Paddle(WHITE, PADDLE_SIZE[0], PADDLE_SIZE[1])
    gd.paddleB.x = PLAY_AREA[0] - 20 - PADDLE_SIZE[0]
    gd.paddleB.y = (PLAY_AREA[1]/2 - PADDLE_SIZE[1]/2) + BANNER_HEIGHT

    gd.ball = Ball(RED, BALL_SIZE[0], BALL_SIZE[1], gd.serve)
    gd.ball.x = PLAY_AREA[0] / 2
    gd.ball.y = (PLAY_AREA[1]/2) + BANNER_HEIGHT

    all_sprites_list = pygame.sprite.Group()

def round(gd:GameData):
    winner = None
    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    
    # Add the paddles to the list of sprites
    all_sprites_list.add(gd.paddleA)
    all_sprites_list.add(gd.paddleB)
    all_sprites_list.add(gd.ball)

    carryOn = True

    clock = pygame.time.Clock()

    all_sprites_list.update()
    # display, then wait a second to start
    gd.screen.fill(BLACK)
    # pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    pygame.draw.line(gd.screen, WHITE, [PLAY_AREA[0]/2, BANNER_HEIGHT], [PLAY_AREA[0]/2, PLAY_AREA[1]+BANNER_HEIGHT], 2)
    pygame.draw.line(gd.screen, WHITE, [0, BANNER_HEIGHT-2], [PLAY_AREA[0], BANNER_HEIGHT-2], 5)

    # display score
    scorefont = pygame.font.SysFont(SCORE_FONT, SCORE_FONT_SIZE)
    lfont = scorefont.render(str(gd.l_score), True, YELLOW)
    gd.screen.blit(lfont,(SCREEN_SIZE[0]/4 - SCORE_FONT_SIZE/2 + 10, BANNER_HEIGHT/2 - SCORE_FONT_SIZE/2))

    rfont = scorefont.render(str(gd.r_score), True, YELLOW)
    gd.screen.blit(rfont,(3*SCREEN_SIZE[0]/4 - SCORE_FONT_SIZE/2 + 10, BANNER_HEIGHT/2 - SCORE_FONT_SIZE/2))

    all_sprites_list.draw(gd.screen)

    pygame.display.flip()
    pygame.time.delay(1000)

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
            gd.paddleA.moveUp(PADDLE_SPEED)
        if keys[pygame.K_s]:
            gd.paddleA.moveDown(PADDLE_SPEED)
        if keys[pygame.K_UP]:
            gd.paddleB.moveUp(PADDLE_SPEED)
        if keys[pygame.K_DOWN]:
            gd.paddleB.moveDown(PADDLE_SPEED)  
        
        # --- Game logic should go here
        all_sprites_list.update()

        #Check if the ball is bouncing against any of the 4 walls:
        if gd.ball.rect.x>=PLAY_AREA[0]-BALL_SIZE[0]: # score
            gd.l_score += 1
            carryOn = False
            winner = 'left'
        if gd.ball.rect.x<0:   #score
            gd.r_score += 1
            carryOn = False
            winner = 'right'
        if gd.ball.rect.y>PLAY_AREA[1]+BANNER_HEIGHT-BALL_SIZE[1]:
            gd.ball.dir[1] = -gd.ball.dir[1]
        if gd.ball.rect.y<=BANNER_HEIGHT:
            gd.ball.dir[1] = abs(gd.ball.dir[1])

        # Detect collisions and bounce ball
        if pygame.sprite.collide_mask(gd.ball, gd.paddleA):
            gd.paddleA.bounce(gd.ball)
        elif pygame.sprite.collide_mask(gd.ball, gd.paddleB):
            gd.paddleB.bounce(gd.ball)

        gd.screen.fill(BLACK)
        # pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        pygame.draw.line(gd.screen, WHITE, [PLAY_AREA[0]/2, BANNER_HEIGHT], [PLAY_AREA[0]/2, PLAY_AREA[1]+BANNER_HEIGHT], 2)
        pygame.draw.line(gd.screen, WHITE, [0, BANNER_HEIGHT-2], [PLAY_AREA[0], BANNER_HEIGHT-2], 5)

        # display score
        scorefont = pygame.font.SysFont(SCORE_FONT, SCORE_FONT_SIZE)
        lfont = scorefont.render(str(gd.l_score), True, YELLOW)
        gd.screen.blit(lfont,(SCREEN_SIZE[0]/4 - SCORE_FONT_SIZE/2 + 10, BANNER_HEIGHT/2 - SCORE_FONT_SIZE/2))

        rfont = scorefont.render(str(gd.r_score), True, YELLOW)
        gd.screen.blit(rfont,(3*SCREEN_SIZE[0]/4 - SCORE_FONT_SIZE/2 + 10, BANNER_HEIGHT/2 - SCORE_FONT_SIZE/2))

        all_sprites_list.draw(gd.screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    gd = game_init()
    round_init(gd)
    round(gd)
    game_end()