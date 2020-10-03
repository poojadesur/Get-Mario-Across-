import pygame
from pygame import mixer
pygame.init()
pygame.font.init()

colorsafe = (139, 71, 38)

screen = pygame.display.set_mode((1000, 1100))

myfont2 = pygame.font.SysFont("freesansbold.ttf", 40)
myfont = pygame.font.SysFont("freesansbold.ttf", 70)
myfont3=pygame.font.SysFont("Britannic Bold", 90)

#class for player icon
class Yoshi(pygame.sprite.Sprite):

    def __init__(self, yoshix, yoshiy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mario.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.yoshix = yoshix
        self.yoshiy = yoshiy
        self.fimage = pygame.transform.flip((self.image), True, False)

    #when either player has collided
    def hit(self):
        text = myfont2.render('You Lose!', False, (0, 0, 0))
        screen.blit(text, (435, 75))
        pygame.display.flip()
        pygame.time.wait(1000)

    #when either player has crossed the entire game
    def success(self):
        text = myfont2.render('You Win!', False, (0, 0, 0))
        screen.blit(text, (435, 75))
        self.yoshix = 950  
        self.yoshiy = 950
        pygame.display.flip()
        pygame.time.wait(1000)

    #redering player2's image
    def render(self, screen):
        screen.blit(self.image, (self.yoshix, self.yoshiy))

    #rendering player1's image
    def render2(self, screen):
        screen.blit(self.fimage, (self.yoshix, self.yoshiy))

#class for moving obstacles
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, movex, movey):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("redshell.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.movex = movex
        self.movey = movey
        self.hitbox = (self.movex + 5, self.movey + 5, 40, 40)

    def render(self, screen):
        screen.blit(self.image, (self.movex, self.movey))

#class for fixed obstacles
class sObstacle(pygame.sprite.Sprite):
    def __init__(self, staticx, staticy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("piranha.png")
        self.image = pygame.transform.scale(self.image, (75, 70))
        self.staticx = staticx
        self.staticy = staticy
        self.hitbox = (self.staticx + 15, self.staticy + 2, 45, 70)

    def render(self, screen):
        screen.blit(self.image, (self.staticx, self.staticy))

#text when player 1 wins a round
def p1roundwinner():
    text = myfont2.render('Player 1 won this round!', False, (0, 0, 0))
    screen.blit(text, (95, 75))

#text when player 2 wins a round
def p2roundwinner():
    text = myfont2.render('Player 2 won this round!', False, (0, 0, 0))
    screen.blit(text, (95, 75))

#text when player1 wins the game
def p1winner():
    text = myfont2.render('Winner:Player 1!!', False, (0, 0, 0))
    screen.blit(text, (170, 25))

#text when player 2 wins the game
def p2winner():
    text = myfont2.render('Winner:Player 2!!', False, (0, 0, 0))
    screen.blit(text, (170, 25))