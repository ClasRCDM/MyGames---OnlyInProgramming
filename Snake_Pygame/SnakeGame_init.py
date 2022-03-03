"""
Name: SnakeGame_Pygame
Description: A simple snake game to test my pygame skills
Author: Clas_RCDM
Email: raphaelcalixto2013@gmail.com
Created from: 01/03/2022
Copyright: (c) Raphael Calixto
"""

###################
#  Init my World  #
###################
from SnakeGame import Mundo


def snake_game():
    Snake = Mundo()
    Snake.variáveis_inicias(fps=10)
    Snake.set_cena('menu')
    Snake.iniciando()


if __name__ == '__main__':
    snake_game()
