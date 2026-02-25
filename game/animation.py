import pygame


class Animation:
    pass

class SpritesheetAnimation(Animation):
    def __init__(self):
        self.asd = True
        self.catch_time = 0

    def animate(self, list):
        if self.asd:
            self.asd = False
            self.catch_time = pygame.time.get_ticks()

        print(pygame.time.get_ticks() - self.catch_time)

        for frame_index in range(len(list)):
            frame = list[frame_index]

    def play_animation(self, animation: str=None):
        if animation == "run":
            print("correr")
        elif animation == "jump":
            print("saltando")
        elif animation == "fall":
            print("cayendo")
        else:
            pass
