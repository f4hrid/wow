import pygame

class Animation:...

class SpritesheetAnimation(Animation):
    def __init__(self, sprites):

        self.animations = sprites

        self.has_time_stopped = False
        self.tiempo_capturado = 0

        self.indice = 0


    def run(self):
        pass
    def stop(self):
        pass

    def play_animation(self):
        if not self.has_time_stopped:
            self.has_time_stopped = True
            self.tiempo_capturado = pygame.time.get_ticks()

        tiempo = pygame.time.get_ticks() - self.tiempo_capturado

        for frame_index in range(len(self.animations)):
            if tiempo > 50:
                if self.indice >= len(self.animations) - 1:
                    self.indice = 0
                self.indice += frame_index + 1
                self.tiempo_capturado = pygame.time.get_ticks()
                break
            break

        return self.animations[self.indice]

