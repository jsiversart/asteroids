import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from player import Player

pygame.init()

clock = pygame.time.Clock()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

def main():
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   print (f"Starting Asteroids! with pygame version: {pygame.version.ver}")
   print (f"Screen width: {SCREEN_WIDTH}")
   print (f"Screen height: {SCREEN_HEIGHT}")
   
   x = SCREEN_WIDTH / 2
   y = SCREEN_HEIGHT / 2
   radius = PLAYER_RADIUS
   player= Player(x, y, radius)
   dt = 0



   while True:
        log_state()
        screen.fill("black")  
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()  
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return




if __name__ == "__main__":
    main()
