"""
File: config.py
Author: f4hridev
Email: ricueroruiz@outlook.com
Github: https://github.com/f4hrid
"""


# Configuración del juego
MAX_HITS = 3

MAX_JUMP = 5
JUMP = 1
MAX_SPEED = 5
SPEED = 1 #
WEIGHT = 1
REBOUND = 1
DELTA_X = 1
DELTA_Y = 1
SLIP = 0.25 # SLIP < MAX_SPEED (mientras más igualado este a SPEED, más seco sera el derrape)
GRAVITY = 1

POWER = None

FPS = 60

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 720

# Tamaños generales de los objetos (no afectan la hitbox, son exclusivamente visuales)

ENTITY_RESIZES = {
    "player": (128, 128)
}
