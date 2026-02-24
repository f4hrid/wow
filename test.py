import pygame, sys

from game.config import WIDTH, HEIGHT
from game.assetloader import AssetLoader, Animation

class test:
    def __init__(self):
        pygame.init()

        self.display = pygame.display
        self.screen = self.display.set_mode((800, 600))

        self.animation = Animation()
        self.spritesheet = AssetLoader("assets/spritesheet.png", (32, 32), (128 * 2, 2 * 128), 5)
        self.image = self.spritesheet.spritesheet[0]
        self.direction = "idle"

        self.list = [0,1,2,3] # lista de ejemplo

    def loop(self):
        """ Game Loop """
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.input()
            self.update()
            self.draw()
            self.display.flip()
            clock.tick(1)

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
        self.draw_player()
        self.draw_states()

    @staticmethod
    def drawing(screen, surface):
        screen.blit(surface, surface.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    def draw_states(self):
        font = pygame.font.SysFont("arial", 20, True)
        txt = font.render("dirección actual: "+self.direction, True, (255, 255, 255))
        self.screen.blit(txt, txt.get_rect(x=WIDTH // 2, y=100))

    def draw_player(self):
        test.drawing(self.screen, self.image)

    def play(self):
        if self.direction == "run":
            self.animation.play_animation(self.spritesheet.spritesheet, "run")
        elif self.direction == "jump":
            self.animation.play_animation("jump")
        elif self.direction == "down":
            self.animation.play_animation("fall")
        else:
            self.animation.play_animation(self.spritesheet.spritesheet)

if __name__ == "__main__":
    test = test()
    test.loop()
