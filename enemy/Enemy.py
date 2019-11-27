import pygame
from color.Color import enemy_color
from settings.Settings import enemy_speed


class Enemy:
    def __init__(self, screen, vector, player_position):
        self.__screen = screen
        self.__vector = vector
        self.__player_position = player_position
        self.alive = True

    def update(self):
        if self.alive:
            if self.__vector.x > self.__player_position.x:
                self.__vector.x -= enemy_speed
            elif self.__vector.x < self.__player_position.x:
                self.__vector.x += enemy_speed

            if self.__vector.y > self.__player_position.y:
                self.__vector.y -= enemy_speed
            elif self.__vector.y < self.__player_position.y:
                self.__vector.y += enemy_speed

    def draw(self):
        if self.alive:
            pygame.draw.rect(
                self.__screen,
                enemy_color,
                pygame.Rect(
                    (self.__vector.x, self.__vector.y, 50, 50)
                )
            )

    def get_vector(self):
        return self.__vector

    @staticmethod
    def get_width():
        return 50

    @staticmethod
    def get_height():
        return 50