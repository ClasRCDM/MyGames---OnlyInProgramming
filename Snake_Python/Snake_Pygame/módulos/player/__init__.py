"""Snake class file"""

# & /Imports Player\ & #
# ------ Player variables ------ #
from variáveis import snake, TAMANHO_GRID
from variáveis import SNAKE_COR, SNAKE_VELOCIDADE, SNAKE_TAMANHO
from variáveis import MINHAS_DIREÇÕES
from variáveis import maças, TELA_CHEIA
# ------ Pygame defs ------ #
from pygame import Surface, event
from pygame import K_w, K_s, K_a, K_d
from pygame import KEYDOWN
# ------ Python operators ------ #
from operator import sub, add, setitem
# ------ Random number function ------ #
from random import randrange
# & \Imports Player/ & #


# Player
class Snake:
    SNAKE_PELE = Surface(SNAKE_TAMANHO)
    SNAKE_PELE.fill(SNAKE_COR)
    SNAKE_rect = SNAKE_PELE.get_rect(topleft=snake[0])

    @classmethod
    def draw(cls, janela):
        cls.SNAKE_rect = [cls.SNAKE_PELE.get_rect(topleft=pos) for pos in snake]
        [janela.blit(cls.SNAKE_PELE, rect) for rect in cls.SNAKE_rect]

    def __init__(self):
        print('Cobra colocada')
        self.velocidade: int = SNAKE_VELOCIDADE
        self.minha_direção = MINHAS_DIREÇÕES['DIREITA']

    def verificando_direção_cb(drc, op, v):
        snake[0] = snake[0][0], op(snake[0][1], v)

    def verificando_direção_ed(drc, op, v):
        snake[0] = op(snake[0][0], v), snake[0][1]

    def update(self, MAÇA_PELE):
        if self.minha_direção == MINHAS_DIREÇÕES['CIMA']:
            self.verificando_direção_cb(sub, self.velocidade)
        elif self.minha_direção == MINHAS_DIREÇÕES['BAIXO']:
            self.verificando_direção_cb(add, self.velocidade)
        if self.minha_direção == MINHAS_DIREÇÕES['ESQUERDA']:
            self.verificando_direção_ed(sub, self.velocidade)
        elif self.minha_direção == MINHAS_DIREÇÕES['DIREITA']:
            self.verificando_direção_ed(add, self.velocidade)

        [setitem(snake, p, (snake[p-1][0], snake[p-1][1])) for p in range(len(snake) - 1, 0, -1)]

        if self.SNAKE_rect[0].colliderect(MAÇA_PELE):
            snake.append((snake[-1][0], snake[-1][1]))
            maças[0] = (randrange(0, TELA_CHEIA[0]) // TAMANHO_GRID*TAMANHO_GRID,
                        randrange(0, TELA_CHEIA[1]) // TAMANHO_GRID*TAMANHO_GRID)

    def input(mv, input):
        def ver_input(tecla, direção, input):
            if input.type == KEYDOWN and input.key == tecla:
                mv.minha_direção = MINHAS_DIREÇÕES[direção]

        ver_input(K_w, 'CIMA', input)
        ver_input(K_s, 'BAIXO', input)
        ver_input(K_a, 'ESQUERDA', input)
        ver_input(K_d, 'DIREITA', input)
