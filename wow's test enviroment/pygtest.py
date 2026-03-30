# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
running = True
dt = 0

player_img = pygame.image.load("tassets/sticktest.png")
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