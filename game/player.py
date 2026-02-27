import pygame
from pygame.color import Color

from game.animation import SpritesheetAnimation
from game.assetloader import AssetLoader
from game.config import HITS, JUMP, MAX_SPEED, SPEED, SLIP, WIDTH


class Player:
    def __init__(self):
        #BÁSICO DE PERSONAJE
        self.hp = HITS
        self.jump = JUMP
        self.max_speed = MAX_SPEED
        self.speed = SPEED
        self.slip = SLIP
        self.dx = 0
        self.dy = 0

        self.assets = AssetLoader("assets/testspritesheet.png", (32, 32), 128)
        self.actions = self.assets.spritesheet
        self.animation = SpritesheetAnimation(self.actions)
        self.image = self.actions[0]
        self.position = self.image.get_rect(center=(WIDTH / 2, 100))

        self.hitbox = None


        #ESTADOS DE COMPORTAMIENTO
        self.sides = ["left", "right"]
        self.current_side = self.sides[1]

        self.is_grounded = False

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

    def draw(self):
        """ Devuelve la surface, datos necesarios para ser dibujada. """
        return self.image, self.position

    def apply_movement(self):
        """ Movimiento del jugador en cuestión. """

        self._remember_current_side()
        self._apply_friction()
        self._apply_acceleration()
        self._max_clamp_speed()
        self._apply_jump()
        self.__test_animation()
        self._update_position()

    def __test_animation(self):
        if self.is_rightward:
            self.image = self.animation.play_animation()

    def _apply_animation(self):
        if self.dy < 0: #esta saltando
            self.animation.play_animation("jump")
        elif self.dx < 0:
            self.animation.play_animation("run")
        elif self.dx > 0:
            self.animation.play_animation("run")
        elif self.dy > 0:
            self.animation.play_animation("fall")
        else:
            self.animation.play_animation("idle")

    def _remember_current_side(self):
        if self.is_leftward:
            self.current_side = self.sides[0]
        elif self.is_rightward:
            self.current_side = self.sides[1]

    def _apply_jump(self):
        # genera fuerza de salto
        if not (self.is_upward and self.is_grounded):
            return

        self.dy = -self.jump
        self.is_grounded = False

    def _apply_acceleration(self):
        # fomenta la aceleración progresiva con delta
        if self.is_leftward:
            self.dx -= self.speed
        elif self.is_rightward:
            self.dx += self.speed

    def _apply_friction(self):
        # aplica fricción para generar un derrape
        if self.dx == 0:
            return

        if self.dx < 0:
            self.dx = min(self.dx + self.slip, 0)
        else:
            self.dx = max(self.dx - self.slip, 0)

    def _max_clamp_speed(self):
        # fija la velocidad limite
        self.dx = max(-self.max_speed, min(self.dx, self.max_speed))

    def _update_position(self):
        self.position.x += self.dx
        self.position.y += self.dy

    def properties(self):
        txt = pygame.font.SysFont("Arial", 20).render(
            "aceleración %s; atración %s; last side %s" %(self.dx, self.dy, self.current_side),
            True,
            Color("white")
        )
        return txt, txt.get_rect(topright=(WIDTH - 150, 200))

    def turn_over(self, b):
        self.image = pygame.transform.flip(self.image, b, False)

    def draw_rect(self):
        return pygame.draw.rect(self.image, Color("white"), (0, 0, 128, 128), 2)
