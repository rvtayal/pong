# Environmental Variables
SCREEN_SIZE = (700, 600)
PLAY_AREA = (700, 400)
BANNER_HEIGHT = SCREEN_SIZE[1] - PLAY_AREA[1]
SCORE_FONT = 'ani'
SCORE_FONT_SIZE = 100

WIN_FONT = 'tlwgtypo'
WIN_FONT_SIZE = 100

# easy colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Game variables
PADDLE_SPEED = 8
PADDLE_SIZE = (10, 100)
BALL_SIZE = (10, 10)
BALL_SPEED_FACTOR = 1.05
BALL_SPEED_START = 5
WINNING_SCORE = 7

# Game Data class to hold relevant game data
class GameData:
    def __init__(self):
        self.screen = None
        self.paddleA = None
        self.paddleB = None
        self.ball = None
        self.l_score = 0
        self.r_score = 0
        self.serve = 'right'

    def isOver(self):
        return (self.l_score == WINNING_SCORE) or (self.r_score == WINNING_SCORE)

if __name__ == "__main__":
    import pygame, sys
    fonts = pygame.font.get_fonts()
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 500))
    pygame.font.init()

    # while (True):
    fCount = -1
    thisFont = None
    carryOn = True

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                    carryOn=False 
                elif event.key==pygame.K_n:
                    fCount+=1
                    thisFont = fonts[fCount]
                    print(thisFont)
                    screen.fill(BLACK)
                elif event.key==pygame.K_p:
                    fCount-=1
                    thisFont = fonts[fCount]
                    print(thisFont)
                    screen.fill(BLACK)

                    
            myfont = pygame.font.SysFont(thisFont, 50)
            img = myfont.render('WINS! 0123456789', True, WHITE)
            screen.blit(img,(0,0))
            pygame.display.flip()
            clock.tick(100)

    pygame.quit()