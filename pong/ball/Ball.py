import pygame

from color.Color import white
from pong.settings.Settings import screen_height, screen_width


class Ball:
    def __init__(self, screen):
        self.__screen = screen

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.__screen, white, [int(screen_width / 2 - 5), int(screen_height / 2 - 5)], 5, 5)
