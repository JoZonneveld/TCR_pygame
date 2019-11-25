import pygame
from color.Color import *
from player.Player import Player
from enemy.Enemy import Enemy
from vector.Vector import Vector
from settings.Settings import screen_height, screen_width


class Game:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode([screen_width, screen_height])
        self.__clock = pygame.time.Clock()
        self.__player = Player(self.__screen, Vector(screen_width / 2 - 25, screen_height / 2 - 25), 50, 50)
        self.__enemies = [
            Enemy(self.__screen, Vector(0, 0), self.__player.get_player_center()),
            Enemy(self.__screen, Vector(screen_width - 50, screen_height - 50), self.__player.get_player_center()),
            Enemy(self.__screen, Vector(screen_width - 50, 0), self.__player.get_player_center()),
            Enemy(self.__screen, Vector(0, screen_height - 50), self.__player.get_player_center())
        ]

    @staticmethod
    def __quit_program():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True

    def update(self):
        self.__player.update()
        for enemy in self.__enemies:
            enemy.update()

    def draw(self):
        self.__player.draw()
        for enemy in self.__enemies:
            enemy.draw()

    def run(self):
        run_game = True
        while run_game:
            self.__screen.fill(white)
            run_game = self.__quit_program()

            self.update()
            self.draw()

            pygame.display.update()
            self.__clock.tick(90)
        quit()


game = Game()
game.run()
