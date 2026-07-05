from pygame.time import get_ticks
from pygame.surface import Surface

class Animation:
    """ Creación de animaciones. """

    def __init__(self, frames: tuple[list]) -> None:
        self.frames = frames

        self.index = 0
        self.timer = 0

    def reset(self):
        self.index = 0
        self.timer = 0

    def update(self) -> Surface:
        now = get_ticks()

        frame = self.frames[self.index]

        if frame[1] == 0:
            return frame[0]

        if now - self.timer >= frame[1]:
            self.timer = now
            self.index += 1

            if self.index >= len(self.frames):
                self.index = 0
            print("CAMBIO DE INDICE: ", self.index)

        return frame[0]

class AnimationController:
    """ Controlador de animaciones. """

    def __init__(self, animations: dict) -> None:
        self.animations = animations
        self.current = None

    def play(self, action):
        if self.current != self.animations[action]:
            self.current = self.animations[action]
            self.current.reset()

    def update(self):
        if self.current:
            return self.current.update()
        return self.current