#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import pygame
from drawing import Drawing
from map import world_map
from player import Player
from ray_casting import ray_casting
from settings import *


pygame.init()
game = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(game)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    game.fill(BLACK)

    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick(FPS)
