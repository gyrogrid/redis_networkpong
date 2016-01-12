import redis
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        #initialise the sprite
        pygame.sprite.Sprite.__init__(self)
        
        #create the image using the surface function, color it blue
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLUE)

        #assign a rectangle, which is what we will use to move the image
        self.rect = self.image.get_rect()


class Pad(pygame.sprite.Sprite):
    def __init__(self):
        
        #initialise the sprite that represents the pad.
        pygame.sprite.Sprite.__init__(self)
        
        #create the image using the surface function, color it
        self.image = pygame.Surface([10, 200])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

def main():
    pygame.init()
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong Yourself")
    pygame.mouse.set_visible(0)
    background = pygame.Surface(screen.get_size())
    font = pygame.font.Font(None, 30)

    ball = Ball()
    pad1 = Pad()
    pad2 = Pad()

    balls = pygame.sprite.Group()
    balls.add(ball)

    allsprites = pygame.sprite.RenderPlain((balls, pad1, pad2))
    clock = pygame.time.Clock()

    r = redis.Redis(host = '172.20.10.2')

    while 1:
        background.fill(BLACK)
        text = font.render("Player 1: "+str(r.get('score1')), True, WHITE)
        background.blit(text, (150,0))
        text = font.render("Player 2: "+str(r.get('score2')), True, WHITE)
        background.blit(text, (450,0))

        #Event/Input handler.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_UP:
                r.incrby('pad1_y', -10)
            elif event.type == KEYDOWN and event.key == K_DOWN:
                r.incrby('pad1_y', 10)

        ball.rect.x = int(r.get('ball_x'))
        ball.rect.y = int(r.get('ball_y'))
        pad1.rect.x = int(r.get('pad1_x'))
        pad1.rect.y = int(r.get('pad1_y'))
        pad2.rect.x = int(r.get('pad2_x'))
        pad2.rect.y = int(r.get('pad2_y'))

        #print(ball.rect.x)
        #print(ball.rect.y)
        clock.tick(10)
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
