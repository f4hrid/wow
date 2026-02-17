import pygame

class Spritesheet:
    def __init__(self,
                 path: str,
                 format_type: tuple[int, int],
                 resize: tuple[int, int],
                 amount: int):
        """
        :param path: directorio del archivo de spritesheet
        :param format_type: formato de pixeles general para cada imagen
        :param resize: tamaño de re-escala para cada imagen
        :param amount: cantidad total de sprites
        """

        sheet = pygame.image.load(path).convert_alpha()
        self.sprite_list = list()

        for image in range(amount):
            sprites = pygame.transform.scale(
                sheet.subsurface((format_type[0] * image, 0, format_type[0], format_type[1])),
                resize
            )
            self.sprite_list.append(sprites)

    def play_animation(self, animation: str=None) -> pygame.Surface:
        if animation == "run":
            print("corriendo")
        elif animation == "jump":
            print("saltando")
        elif animation == "fall":
            print("cayendo")
        else:
            print("inactivo")