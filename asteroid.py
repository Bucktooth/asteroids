import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_vector = self.velocity.rotate(angle)
        second_vector = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        smaller_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid_one.velocity = first_vector * 1.2
        smaller_asteroid_two.velocity = second_vector * 1.2