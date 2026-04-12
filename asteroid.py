import random

import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        print()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        print("splitting")
        if self.radius > 10:
            log_event("asteroid_split")
            r = random.uniform(20, 50)
            self.velocity.rotate(r)
            self.velocity.rotate(-r)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = pygame.Vector2(self.velocity.x + 1, self.velocity.y + 1)
            new_asteroid2.velocity = pygame.Vector2(self.velocity.x - 1, self.velocity.y - 1)
            return [new_asteroid1, new_asteroid2]
        return []