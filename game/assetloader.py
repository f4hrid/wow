from typing import Any
from pygame.surface import Surface
from pygame.image import load
from pygame.transform import scale
from json import load as cacaroto
from game.config import ASSET_PATH


class AssetLoader:
    """ Carga la imagen un spritesheet y construye frames. """

    def __init__(self, asset_name: str, resize: int | tuple[int, int]):

        self._frames: dict[str, Surface | list[Surface]] = dict() # animaciones separadas y agrupadas

        sheet: Surface = self._load_sheet(asset_name) # carga la hoja de sprites

        size: tuple[int, int] = self._normalize_size(resize) # normaliza la variación de la entrada resize

        data: Any = ParseJSON().decode(asset_name) # decodifica el archivo de recortes .json

        spritesheet: Any = SpriteSheet(sheet, size) # redimensiona y recorta cada lamina

        for key, info in data.items():
            if info["type"] == "image":
                self._frames[key] = spritesheet.frame(info["rect"])

            elif info["type"] == "frame":
                self._frames[key] = spritesheet.frames(info["frames"])

    def get_frames(self):
        return self._frames

    @staticmethod
    def _load_sheet(asset: str) -> Surface:
        return load('{}{}.png'.format(ASSET_PATH, asset))

    @staticmethod
    def _normalize_size(resize: int | tuple[int, int]) -> tuple[int, int]:
        if isinstance(resize, int):
            return (resize,)*2
        return resize


class SpriteSheet:
    """ Redimensiona y recorta los frames. """

    def __init__(self, sheet: Surface, size: tuple[int, int]) -> None:
        self.sheet = sheet
        self.size = size

    def frame(self, rect: tuple[int, int, int, int]) -> Surface:
        x, y, w, h = rect
        return scale(self.sheet.subsurface(x, y, w, h), self.size)

    def frames(self, rects: list[tuple[int, int, int, int]]) -> list[Surface]:
        frames = []
        for rect in rects:
            frames.append(self.frame(rect))

        return frames


class ParseJSON:
    """ Parseo de formato: json a python syntax. """

    @staticmethod
    def decode(asset: str) -> Any:
        with open('{}{}.json'.format(ASSET_PATH, asset)) as f:
            return cacaroto(f)