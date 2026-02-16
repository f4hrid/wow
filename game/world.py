import pygame
from game.config import GRAVITY


class World:
    def __init__(self):
        self.floor = 555
        self.gravity = GRAVITY
        self.mass = 3

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        surface.fill(pygame.Color("black"))

    def getGravitational(self):
        y = 0
        y += self.gravity
        if y > self.gravity*5:
            y = self.gravity*5
        return y

