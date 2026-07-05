from json import load
from typing import Any

import pygame.image
from pygame.rect import Rect
from game.config import ASSET_PATH


class Hitbox(Rect):
    """
    Definición de la caja de impacto.
    :return devuelve una hitbox.
    """

    def __init__(self, offset_x: int, offset_y: int, width: int, height: int):
        super().__init__(0, 0, width, height)
        self._offset_x = offset_x
        self._offset_y = offset_y
        self._width = width
        self._height = height

    def __str__(self):
        return f"{repr(self)}"

    def update(self, box, opposite_side, *kwargs):
        self.y = box.y + self._offset_y

        if opposite_side:
            self.x = box.x + (box.width - (self._width + self._offset_x))
        else:
            self.x = box.x + self._offset_x