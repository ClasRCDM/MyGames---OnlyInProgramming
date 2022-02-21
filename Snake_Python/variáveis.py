"""Global constants file"""
from random import randrange

#####################################
# /absolute variables of the world\ #
TELA_CHEIA: tuple[int, int] = 680, 680
TAMANHO_GRID: int = 20

# \absolute variables of the world/ #
#####################################

######################
# /global variables\ #

# $ Variáveis do player $ #
MINHAS_DIREÇÕES: dict = {'CIMA': 0,
                         'ESQUERDA': 1,
                         'BAIXO': 2,
                         'DIREITA': 3}

SNAKE_COR: tuple[int, int, int] = (255, 255, 255)
SNAKE_TAMANHO: tuple[int, int] = (20, 20)
SNAKE_VELOCIDADE: int = 20

snake: list = [(100, 200), (60, 200), (20, 200), (-20, 200)]

# $ Variáveis da maça $ #
MAÇA_COR: tuple[int, int, int] = (255, 17, 0)
MAÇA_TAMANHO: tuple[int, int] = (20, 20)

maças: list = [(randrange(0, TELA_CHEIA[0]) // 40*40,
                randrange(0, TELA_CHEIA[1]) // 40*40)]

# $ Variáveis do para texto $ #
ARQUIVO_FONT: str = 'fonts'
NOME_FONT: str = 'PressStart2P.ttf'

# \global variables/ #
######################
