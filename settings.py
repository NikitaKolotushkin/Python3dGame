import math

# GAME SETTINGS
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100

# RAY CASTING SETTINGS
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 900
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# PLAYER SETTINGS
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 3

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (100, 100, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)