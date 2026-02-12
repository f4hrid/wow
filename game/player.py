import pygame
from game.spritesheet import Spritesheet
from game.config import MAX_HITS, MAX_JUMP, JUMP, MAX_SPEED, SPEED, DELTA_X, DELTA_Y, SLIP, POWER, SCREEN_WIDTH, SCREEN_HEIGHT
from game.world import World


class Player:
    def __init__(self, world: World):
        #BÁSICO DE PERSONAJE
        self.hp = MAX_HITS
        self.max_jump = MAX_JUMP
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
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, self.world.floor))


        self.hitbox = None

        #ESTADOS DE COMPORTAMIENTO
        self.current_side = ("left", "right")

        self.is_standing = False
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_jumping = False

    def handle_input(self):
        key = pygame.key.get_pressed()
        self.is_moving_left = key[pygame.K_a] and not key[pygame.K_d]
        self.is_moving_right = key[pygame.K_d] and not key[pygame.K_a]
        self.is_jumping = key[pygame.K_w]

    def update(self):
        #self.world.apply_gravity(self.rect)
        self.apply_movement()

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)
        self.draw_rect(self.image)

    def apply_movement(self):
        self.apply_friction()
        self.apply_acceleration()
        self.max_clamp_speed()
        self.apply_jump()
        self.max_clamp_jump()

        self.update_position()

    def apply_acceleration(self):
        # fomenta la aceleración progresiva con delta
        if self.is_moving_left:
            self.dx -= self.speed
        elif self.is_moving_right:
            self.dx += self.speed

    def apply_jump(self):
        if self.is_jumping:
            self.dy += -self.jump

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

    def max_clamp_jump(self):
        # fija la velocidad de salto al limite
        self.dy = max(-self.max_jump, min(self.dy, self.max_jump))

    def update_position(self):
        #print("aceleración %s; impulsión %s; \nizq %s; der %s; jump %s" %(self.dx, self.dy, self.is_moving_left, self.is_moving_right, self.is_jumping))
        self.rect.x += self.dx
        self.rect.y += self.dy


    """
    def turn_over(self) -> pygame.Surface: #HELP
        return pygame.transform.flip(self.image, True, False)
    """

    @staticmethod
    def draw_rect(image: pygame.Surface) -> None:
        pygame.draw.rect(image, (0, 255, 0), (0, 0, 128, 128), 2)