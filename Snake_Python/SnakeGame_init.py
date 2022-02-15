###################
#  Init my World  #
###################
from SnakeGame import Mundo

if __name__ == '__main__':
    Snake = Mundo()
    Snake.variáveis_inicias(fps=120)
    Snake.set_cena('jogar')
    Snake.iniciando()
