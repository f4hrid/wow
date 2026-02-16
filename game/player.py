from operator import truediv

import pygame
from pygame.color import Color
from game.spritesheet import Spritesheet
from game.config import HITS, JUMP, MAX_SPEED, SPEED, SLIP, POWER, SCREEN_WIDTH
from game.world import World


class Player:
    def __init__(self, world: World):
        #BÁSICO DE PERSONAJE
        self.hp = HITS
        self.jump = JUMP
        self.max_speed = MAX_SPEED
        self.speed = SPEED
        self.slip = SLIP
        self.dx = 0
        self.dy = 0

        self.world = world


        self.path = "assets/spritesheet.png"
        self.format = (32, 32)
        self.resize = (256, 256)
        self.amount = 5
        self.sprite_sheet = Spritesheet("assets/spritesheet.png", (32, 32), (128, 128), 5)
        self.image = self.sprite_sheet.get_sprite()[0]
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, 100))


        self.hitbox = None

        #ESTADOS DE COMPORTAMIENTO
        self.current_side = "right"

        self.on_ground = False


        self.is_leftward = False
        self.is_rightward = False
        self.is_upward = False

    def handle_input(self):
        key = pygame.key.get_pressed()
        self.is_leftward = key[pygame.K_a] and not key[pygame.K_d]
        self.is_rightward = key[pygame.K_d] and not key[pygame.K_a]
        self.is_upward = key[pygame.K_w]

    def update(self):
        self.apply_movement()

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)
        self.draw_rect(self.image)

    def apply_movement(self):
        self.remember_current_side()
        self.stay_on_floor()
        self.apply_friction()
        self.apply_acceleration()
        self.max_clamp_speed()
        self.apply_jump()
        self.apply_gravity()
        self.apply_animation()
        self._update_position()

    def apply_animation(self):
        if self.dx < 0:
            pass
        elif self.dx > 0:
            pass
        elif self.dy < 0: #esta saltando
            pass
        elif self.dy > 0:
            pass
        else:
            pass

    def remember_current_side(self):
        if self.is_leftward:
            self.current_side = "left"
            self.turn_over(True)
        elif self.is_rightward:
            self.current_side = "right"
            self.turn_over(False)

    def apply_gravity(self):
        if self.on_ground:
            return

        self.dy += self.world.getGravitational()

    def stay_on_floor(self):
        if self.rect.bottom < self.world.floor:
            return

        self.rect.bottom = self.world.floor
        self.dy = 0
        self.on_ground = True

    def apply_acceleration(self):
        # fomenta la aceleración progresiva con delta
        if self.is_leftward:
            self.dx -= self.speed
        elif self.is_rightward:
            self.dx += self.speed

    def apply_jump(self):
        if not (self.is_upward and self.on_ground):
            return

        self.dy = -self.jump
        self.on_ground = False

    def apply_friction(self):
        # aplica fricción para generar un derrape
        if self.dx == 0:
            return

        if self.dx < 0:
            self.dx = min(self.dx + self.slip, 0)
        else:
            self.dx = max(self.dx - self.slip, 0)

    def max_clamp_speed(self):
        # fija la velocidad limite
        self.dx = max(-self.max_speed, min(self.dx, self.max_speed))

    def _update_position(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def properties(self, screen: pygame.Surface):
        txt = pygame.font.SysFont("Arial", 20).render(
            "aceleración %s; impulsión %s; izq %s; der %s" %(self.dx, self.dy, self.is_leftward, self.is_rightward),
            True,
            Color("white")
        )
        screen.blit(txt, txt.get_rect(center=(SCREEN_WIDTH//2, 200)))

    def turn_over(self, b: bool) -> pygame.Surface: #HELP
        return pygame.transform.flip(self.image, b, False)

    @staticmethod
    def draw_rect(image: pygame.Surface) -> None:
        pygame.draw.rect(image, Color("white"), (0, 0, 128, 128), 2)