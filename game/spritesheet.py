from logging import exception

import pygame, ursina
from ursina import SpriteSheetAnimation

class Spritesheet:
    def __init__(self, path: str, format_type: tuple, resize: tuple, amount: int):
        """
        :param path: directorio del archivo de spritesheet
        :param format_type: formato de pixeles general para cada imagen
        :param resize: tamaño de re-escala para cada imagen
        :param amount: cantidad total de sprites
        """
        self.path = path
        self.format = format_type
        self.resize = resize
        self.amount = amount

    @staticmethod
    def to_load(filename: str) -> pygame.Surface:
        return pygame.image.load(filename).convert_alpha()

    @staticmethod
    def to_scale(surface: pygame.Surface, scale: tuple) -> pygame.Surface:
        return pygame.transform.scale(surface, scale)

    @staticmethod
    def to_layer(surface: pygame.Surface, cut: tuple) -> pygame.Surface:
        return surface.subsurface(pygame.Rect(cut))

    def get_sprite(self) -> dict[int, pygame.Surface]:
        spritesheet_group = {}
        sheet = Spritesheet.to_load(self.path)

        try:
            for image in range(self.amount):
                sprite = Spritesheet.to_scale(
                    Spritesheet.to_layer(
                        sheet,
                        (32*image, 0, 32, 32)),
                    self.resize)
                spritesheet_group[image] = sprite

            return spritesheet_group
        except FileNotFoundError:
            return spritesheet_group


    def get_rect(self) -> tuple[int, int, int, int]:
        pass

