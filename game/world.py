import pygame, typing
from game.config import GRAVITY


class World:
    def __init__(self):
        self.floor = 555
        self.gravity = GRAVITY

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        surface.fill(pygame.Color("black"))

    def apply_gravity(self, rect: pygame.Rect):
        dy = 1
        dy += self.gravity
        rect.y += dy
