import pygame
from ray_casting import ray_casting
from settings import *


class Drawing:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont("Arial", 36, bold=True)

    def background(self):
        pygame.draw.rect(self.game, SKYBLUE, (0, 0, WIDTH, HEIGHT))
        pygame.draw.rect(self.game, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.game, player_pos, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, BLACK)
        self.game.blit(render, (WIDTH - 65, 5))
