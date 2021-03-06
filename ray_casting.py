import pygame
from map import world_map
from settings import *


def ray_casting(game, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth * depth * 0.00001)
                color = (c, c // 2, c // 3)
                pygame.draw.rect(
                    game,
                    color,
                    (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height),
                )
                break
        cur_angle += DELTA_ANGLE
