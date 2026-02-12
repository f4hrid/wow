import pygame, sys
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

        self.play = self.player()
        self.spritesheet = Spritesheet("assets/spritesheet.png")

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()
            self.draw()
            self.display.flip()
            self.clock.tick(60)

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.play.image, self.play.rect)


    def player(self):
        spritesheet = Spritesheet("assets/spritesheet.png").getSprite()

        imagen = spritesheet
        rect = spritesheet.get_rect()





if __name__ == "__main__":
    test = test()
    test.loop()
