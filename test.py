import pygame, sys

from game.config import SCREEN_WIDTH, SCREEN_HEIGHT
from game.spritesheet import Spritesheet
from typing import Any, Type, Union


valor: Any = 2

valor = False

nombre: str = "cassandra"

nombre = "johanna fadul"

union: Union[str, int, bool] = True

union = 100

class test:
    def __init__(self):
        pygame.init()

        self.display = pygame.display
        self.screen = self.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.spritesheet = Spritesheet("assets/spritesheet.png", (32, 32), (1,1), 5)
        self.direction = "idle"

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.input()
            self.update()
            self.draw()
            self.display.flip()
            self.clock.tick(60)

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.direction = "run"
        elif key[pygame.K_RIGHT]:
            self.direction = "run"
        elif key[pygame.K_UP]:
            self.direction = "jump"
        elif key[pygame.K_DOWN]:
            self.direction = "down"
        else:
            self.direction = "idle"



    def update(self):
        self.play()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_states()

    def draw_states(self):
        font = pygame.font.SysFont("arial", 20, True)
        txt = font.render("dirección actual: "+self.direction, True, (255, 255, 255))
        self.screen.blit(txt, txt.get_rect(center=(SCREEN_WIDTH//2, 100)))

    def play(self):
        if self.direction == "run":
            self.spritesheet.play_animation("run")
        elif self.direction == "jump":
            self.spritesheet.play_animation("jump")
        elif self.direction == "down":
            self.spritesheet.play_animation("fall")
        else:
            self.spritesheet.play_animation()
if __name__ == "__main__":
    test = test()
    test.loop()
