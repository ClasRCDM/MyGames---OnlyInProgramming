from random import randrange

#####################################
# /absolute variables of the world\ #
TELA_CHEIA = 680, 680
TAMANHO_GRID = 40

# \absolute variables of the world/ #
#####################################

######################
# /global variables\ #

# $ Variáveis do player $ #
MINHAS_DIREÇÕES: dict = {'ESQUERDA': 0,
                         'DIREITA': 1,
                         'CIMA': 2,
                         'BAIXO': 3}

SNAKE_COR: tuple = (255, 255, 255)
SNAKE_TAMANHO: tuple = (40, 40)
SNAKE_VELOCIDADE: int = 20

snake: list = [(400, 200)]

minha_direção = MINHAS_DIREÇÕES['ESQUERDA']

# $ Variáveis da maça $ #
MAÇA_COR: tuple = (255, 17, 0)
MAÇA_TAMANHO: tuple = (40, 40)

maças: list = [(randrange(0, TELA_CHEIA[0]) // 40*40,
                randrange(0, TELA_CHEIA[1]) // 40*40)]

# $ Variáveis do para texto $ #
ARQUIVO_FONT: str = 'fonts'
NOME_FONT: str = 'PressStart2P.ttf'

# \global variables/ #
######################
