from pygame.image import load
from pygame.rect import Rect
from pygame.transform import scale

class AssetLoader:
    def __init__(self,
                 sheetpath: str,
                 form: tuple[int, int],
                 scaled: int | tuple[int, int]
                 ):
        """
        :param sheetpath: ruta que contiene el archivo de spritesheet
        :param form: formato de pixeles original de cada sprite
        :param scaled: tamaño a re-escala para cada imagen
        """
        self.spritesheet = list()

        self._sheet = load(sheetpath)
        self.width, self.height = form[0], form[1]
        self.count = self._sheet.get_width() // self.width

        match scaled:
            case int():
                self.size = (scaled, scaled)
            case tuple():
                self.size = (scaled[0], scaled[1])

        self.__to_split()

    def __to_split(self):
        for image in range(self.count):
            sprite = scale(self._sheet.subsurface(
                Rect(self.width*image, 0, self.width, self.height)),
                self.size)
            self.spritesheet.append(sprite)