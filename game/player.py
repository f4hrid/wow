from dataclasses import dataclass

from pygame.rect import Rect
from pygame.font import SysFont
from pygame.color import Color
from pygame.transform import flip
from game.animation import Animation, AnimationController
from game.assetloader import AssetLoader
from game.config import HITS, JUMP, MAX_SPEED, SPEED, SLIP, WIDTH, HEIGHT


@dataclass
class PlayerState:
    is_upward: bool = False
    is_grounded: bool = False
    is_leftward: bool = False
    is_rightward: bool = False


class Player(PlayerState):
    """ Objeto jugador. """
    def __init__(self):
        self.hp = HITS
        self.jump = JUMP
        self.max_speed = MAX_SPEED
        self.speed = SPEED
        self.slip = SLIP
        self.dx = 0
        self.dy = 0

        self.assets = AssetLoader('player', 128).get_frames()
        self.animation = AnimationController(
            animations={key: Animation(value) for key, value in self.assets.items()}
        )

        self.image = self.assets["icon"] # con animation
        self.box = Rect(0, 0, 128, 128)
        self.hitbox = self.box

        self.facing_left = False


    def update(self):
        self._apply_movement()
        self._apply_animation()


    def draw(self):
        """ Devuelve la surface, datos necesarios para ser dibujada. """
        return self.image, self.box


    def _apply_movement(self):
        """ Movimiento del jugador en cuestión. """

        self._apply_acceleration()
        self._apply_friction()
        self._max_clamp_speed()
        self._apply_jump()
        self._update_box()

    def _apply_animation(self):
        """ Animación del jugador. """

        self._remember_current_side()
        self._switch_animation()
        self._update_animation()
        self._update_hitbox()
        self._flip_side()

    def _switch_animation(self):
        if self.dy < 0:
            self.animation.play('jump')
        elif self.dy > 0:
            self.animation.play('fall')
        elif self.dx < 0 or self.dx > 0:
            self.animation.play('run')
        elif self.dy == 0 and self.dx == 0:
            self.animation.animations['idle'].delay = 800
            self.animation.play('idle')

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

    def _remember_current_side(self):
        if self.dx < 0:
            self.facing_left = True
        elif self.dx > 0:
            self.facing_left = False

    def _flip_side(self):
        self.image = flip(self.image, self.facing_left, False)

    def _box_alignment(self, width, height):
        if width < 128/2 and height < 128:
            hitbox = Rect(self.box.x + width, self.box.y + height, 128 - width * 2, 128 - height)
            return hitbox
        return self.box

    def _update_hitbox(self):
        self.hitbox = self._box_alignment(48, 64)

    def _update_animation(self):
        self.image = self.animation.update()

    def _update_box(self):
        self.box.x += self.dx
        self.box.y += self.dy

    def properties(self):
        txt = SysFont("Arial", 20).render(
            "aceleración %s; atración %s; last side %s" %(self.dx, self.dy, "left" if self.facing_left else "right"),
            True,
            Color("black")
        )
        return txt, txt.get_rect(topright=(WIDTH - 150, 200))