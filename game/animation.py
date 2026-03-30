from pygame.time import get_ticks

class Animation:
    """ Representa una animación individual. """

    def __init__(self, frames, delay=60, loop=True):
        self.frames = frames
        self.delay = delay
        self.loop = loop

        self.index = 0
        self.timer = 0
        self.stop = False

    def reset(self):
        self.index = 0
        self.timer = 0
        self.stop = False

    def update(self):
        if self.stop:
            return self.frames[self.index]

        if len(self.frames) == 1:
            return self.frames[0]

        now = get_ticks()

        if now - self.timer >= self.delay:
            self.timer = now
            self.index += 1

            if self.index >= len(self.frames):
                if self.loop:
                    self.index = 0
                else:
                    self.index = len(self.frames) - 1
                    self.stop = True
        return self.frames[self.index]

class AnimationController:
    def __init__(self, animations: object) -> None:
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