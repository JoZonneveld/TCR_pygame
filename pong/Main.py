import pygame
from color.Color import *
from pong.ball.Ball import Ball
from pong.player.Player import Player
from vector.Vector import Vector
from pong.settings.Settings import screen_width, screen_height


class Game:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode([screen_width, screen_height])
        self.__clock = pygame.time.Clock()
        self.__player1 = Player(self.__screen, Vector(20, (screen_height / 2) - 25), False)
        self.__player2 = Player(self.__screen, Vector(screen_width - 30, (screen_height / 2) - 25), True)
        self.__ball = Ball(self.__screen)

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
        self.__player1.update()
        self.__player2.update()
        self.__ball.update()

    def draw(self):
        self.__player1.draw()
        self.__player2.draw()
        self.__ball.draw()

    def run(self):
        run_game = True

        while run_game:
            self.__screen.fill(black)
            self.update()
            self.draw()

            run_game = self.__quit_program()

            pygame.display.update()
            self.__clock.tick(90)
        quit()


game = Game()
game.run()
