import pygame

class AssetLoader:
    def __init__(self,
                 sheetpath: str,
                 format: int | tuple[int, int],
                 resize: int | tuple[int, int],
                 amount: int):
        """
        :param sheetpath: ruta que contiene el archivo de spritesheet
        :param format: formato de pixeles original de cada sprite
        :param resize: tamaño a re-escala para cada imagen
        :param amount: cantidad total de sprites
        """

        # prepara la imagen
        sheet = pygame.image.load(sheetpath).convert_alpha()
        self.spritesheet = list()

        for image in range(amount):
            sprites = pygame.transform.scale(
                sheet.subsurface((format[0] * image, 0, format[0], format[1])),
                resize
            )
            self.spritesheet.append(sprites)