import pygame

from color.Color import white
from pong.settings.Settings import player_speed, screen_height


class Player:
    def __init__(self, screen, vector, controls):
        self.__screen = screen
        self.__height = 50
        self.__width = 10
        self.__vector = vector
        self.__controls = controls

    def update(self):
        keys = pygame.key.get_pressed()

        if (self.__controls and keys[pygame.K_UP]) or (not self.__controls and keys[pygame.K_w]):
            self.__vector.y -= player_speed
            if self.__vector.y < 0:
                self.__vector.y = 0

        if (self.__controls and keys[pygame.K_DOWN]) or (not self.__controls and keys[pygame.K_s]):
            self.__vector.y += player_speed
            if self.__vector.y > screen_height - self.__height:
                self.__vector.y = (screen_height - self.__height)

    def draw(self):
        pygame.draw.rect(
            self.__screen,
            white,
            pygame.Rect(
                (self.__vector.x, self.__vector.y, self.__width, self.__height)
            )
        )
