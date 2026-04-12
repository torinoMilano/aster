import sys

import pygame

import asteroidfield
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from shot import Shot


def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")
    pygame.mouse.set_visible(True)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers =(updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroidfield = AsteroidField()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            updatable.update(dt)
            for sprite in drawable:
                sprite.draw(screen)

            for sprite in asteroids:
                for shot in shots:
                    if sprite.collides(shot):
                        print("Asteroid hit")
                        log_event("asteroid_shot")
                        sprite.split()
                        shot.kill()
                        break
                if sprite.collides(player):
                    log_event("player_hit")
                    print("Game Over")
                    sys.exit()


            dt = clock.tick(60) / 1000.0
            pygame.display.flip()


if __name__ == "__main__":
    main()
