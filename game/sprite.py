from collections import defaultdict
from typing import Self
from pygame.surface import Surface
from pygame.image import load as image_load
from pygame.transform import scale
from json import load as json_load

from game.animation import AnimationController, Animation

def load_sprites(image_path: str, data_path: str):
    """ Carga del contenido visual """
    surface = Load.surface(image_path)
    frames, metadata = Load.data(data_path)
    return Sprite(surface).set_frames(frames).set_scale_to(metadata).build()


class MetadataNotFoundError(Exception):
    """ Configuración de datos adicional no encontrada o inexistente. """
    pass

class SpriteProcessingError(Exception):
    """ Procedimiento de spritesheet tuvo error. """
    pass

class Load:
    @staticmethod
    def surface(filename: str, namehint: str= ""):
        try:
            return image_load(filename, namehint)
        except FileNotFoundError:
            raise FileNotFoundError("No se encontró el archivo. ")

    @staticmethod
    def data(filename: str) -> tuple:
        try:
            with open(filename, "r") as file:
                data = json_load(file)

            if "meta" not in data:
                raise MetadataNotFoundError(
                    "No se encontró la llave 'metadata' "
                )

            return data["frames"], data["meta"]
        except FileNotFoundError as e:
            raise FileNotFoundError(
                "Archivo de configuración no encontrado "
            ) from e

class Sprite:
    def __init__(self, surface: Surface) -> None:
        self._surface: Surface = surface
        self._assets: defaultdict[str, list[tuple[Surface, int]]] = defaultdict(list)
        self.more_assets: defaultdict[str, list] = defaultdict(list)

    def set_frames(self, frames: list[dict]) -> Self:
        for frame in frames:
            clip = self._subsurface(frame["frame"])
            self._assets[frame["type"]].append((clip, frame["duration"]))
        return self

    def _get_subsurface(self, coord: dict):
        try:
            return self._surface.subsurface(
                coord["x"], coord["y"], coord["w"], coord["h"]
            )
        except ValueError as e:
            raise SpriteProcessingError(
                f"Rect invalido al recortar frame: {coord}"
            ) from e

    def set_scale_to(self, metadata: dict) -> Self:
        scaled = defaultdict(list)

        for animation, frame in self._assets.items():
            scaled[animation] = [
                (scale(surface, metadata["scale"]), duration) for surface, duration in frame
            ]

        self._assets = scaled

        return self

    def _subsurface(self, coord: dict):
        try:
            return self._surface.subsurface(
                coord["x"], coord["y"], coord["w"], coord["h"]
            )
        except ValueError as e:
            raise SpriteProcessingError(
                f"Rect invalido al recortar frame: {coord}"
            ) from e

    def build(self) -> dict[str, list[tuple[Surface, int]]]:
        return dict(self._assets)