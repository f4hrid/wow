from pygame.rect import Rect


class Hitbox:
    """
    Definición de la caja de impacto.
    :returns devuelve una hitbox.
    """

    def __init__(self, offset_x: int, offset_y: int, width: int, height: int):
        self._offset_x = offset_x
        self._offset_y = offset_y
        self._width = width
        self._height = height
        self.rect = Rect(0, 0, self._width, self._height)


    def update(self, box, opposite_side):
        self.rect.y = box.y + self._offset_y

        if opposite_side:
            self.rect.x = box.x + (box.width - (self._width + self._offset_x))
        else:
            self.rect.x = box.x + self._offset_x

    def __repr__(self):
        return self.rect

    def __str__(self):
        return f"hitbox -> {tuple(e for e in self.rect)}"