import pygame
from pygame.surface import Surface

from game.sprite import Load, Sprite
from collections import defaultdict
from game.animation import AnimationController, Animation



surface = Load.surface("assets/player.png")
data, meta = Load.data("assets/player.json")

assets = Sprite.spritesheet(surface, data)

for key, value in assets.items():
    print(key, value)



animation = AnimationController(animations={"run": Animation(assets["run"])})
#AnimationController(Animations={key: Animation(value) for key, value in assets})

pygame.init()

while True:
    imagen = animation.update()
    animation.play("run")




# ------------------------------------------------------

# ------------------------------------------------------

"""
animations = 
{
    "idle": <Animation>,
    "run": <Animation>,
    "jump": <Animation>,
    "fall": <Animation>
}
assets =
{
    "animation1": [(<surface>, duration)],
    "animation2": [(<surface>, duration), (<surface>, duration)], # LLAVE Y VALOR
    "animation3": [(<surface>, duration), (<surface>, duration)],
    "animation4": [(<surface>, duration), (<surface>, duration)]
}
data =
{
    "frames": [
        {
            "info": ...
        },
        {
            "info": ...
        },
        {
            "info": ...
        },
        {
            "info": ...
        }
    ]
}
"""


"""
# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
running = True
dt = 0

player_img = pygame.image.load_surface("tassets/sticktest.png")
player_pos = pygame.Vector2(0,0)

spx = 90
spy = 20


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    hitbox = pygame.Rect(
        player_pos[0] + spx, player_pos[1] + spy, player_img.get_width() - spx * 2 , player_img.get_height() - spy
    )
    pygame.draw.rect(screen,"green", hitbox, 1)
    screen.blit(player_img, player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
"""