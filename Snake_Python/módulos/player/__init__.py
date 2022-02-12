# & /Imports Player\ & #
# ------ Player variables ------ #
from variáveis import snake, TAMANHO_GRID
from variáveis import SNAKE_COR, SNAKE_VELOCIDADE, SNAKE_TAMANHO
from variáveis import MINHAS_DIREÇÕES, minha_direção
from variáveis import maças, TELA_CHEIA
# ------ Pygame defs ------ #
from pygame import Surface
from pygame import K_w, K_s, K_a, K_d
from pygame import key
# ------ Python operators ------ #
from operator import sub, add
# ------ Random number function ------ #
from random import randrange
# & \Imports Player/ & #


# Player
class Snake:
    SNAKE_PELE = Surface(SNAKE_TAMANHO)
    SNAKE_PELE.fill(SNAKE_COR)
    SNAKE_rect = SNAKE_PELE.get_rect(topleft=snake[0])

    crescente_corpo = 2

    @classmethod
    def update(cls, janela, MAÇA_PELE):
        cls.SNAKE_rect = [cls.SNAKE_PELE.get_rect(topleft=pos) for pos in snake]
        [janela.blit(cls.SNAKE_PELE, rect) for rect in cls.SNAKE_rect]

        if cls.verificando_movimento(0) and cls.verificando_movimento(1):
            snake.append((snake[0][0], snake[0][1]))

        if cls.SNAKE_rect[0].colliderect(MAÇA_PELE):
            cls.crescente_corpo += 1
            maças[0] = (randrange(0, TELA_CHEIA[0]) // TAMANHO_GRID*TAMANHO_GRID,
                        randrange(0, TELA_CHEIA[1]) // TAMANHO_GRID*TAMANHO_GRID)
        else: snake.pop(1) if len(snake) >= cls.crescente_corpo else None

    @classmethod
    def verificando_movimento(vr_v, pos, valor=None):
        index = valor if valor is not None else '.0'
        x_y = f'{snake[0][pos] / TAMANHO_GRID:.3f}'
        if index in x_y:  # .025
            return True
        return False

    def __init__(self):
        print('Cobra colocada')
        self.velocidade: int = SNAKE_VELOCIDADE
        self.velocidade_constante: int = 10

        self.proxima_direção_cb = None
        self.proxima_direção_ed = None

    def direção(drc):
        def verificando_direção_cb(op, v, di):
            snake[0] = snake[0][0], op(snake[0][1], v) \
                if minha_direção == MINHAS_DIREÇÕES[di] else snake[0][1]

        def verificando_direção_ed(op, v, di):
            snake[0] = op(snake[0][0], v) \
                if minha_direção == MINHAS_DIREÇÕES[di] else snake[0][0], snake[0][1]

        verificando_direção_cb(sub, drc.velocidade, 'CIMA')
        verificando_direção_cb(add, drc.velocidade, 'BAIXO')
        verificando_direção_ed(sub, drc.velocidade, 'ESQUERDA')
        verificando_direção_ed(add, drc.velocidade, 'DIREITA')

        if drc.proxima_direção_cb is not None or drc.proxima_direção_ed is not None:
            global minha_direção
            if drc.verificando_movimento(0):
                minha_direção = drc.proxima_direção_cb \
                    if drc.proxima_direção_cb is not None else minha_direção
                drc.proxima_direção_cb = None
            if drc.verificando_movimento(1):
                minha_direção = drc.proxima_direção_ed \
                    if drc.proxima_direção_ed is not None else minha_direção
                drc.proxima_direção_ed = None

    def movendo(mv):
        teclas = key.get_pressed()

        def mover(tecla, p_direção, opção):
            if teclas[tecla]:
                if opção == 0: mv.proxima_direção_cb = p_direção
                elif opção == 1: mv.proxima_direção_ed = p_direção

        mover(K_w, MINHAS_DIREÇÕES['BAIXO'], 0)
        mover(K_s, MINHAS_DIREÇÕES['CIMA'], 0)
        mover(K_a, MINHAS_DIREÇÕES['DIREITA'], 1)
        mover(K_d, MINHAS_DIREÇÕES['ESQUERDA'], 1)

    def set_velocidade(speed, velocidade):
        speed.velocidade = velocidade * -speed.velocidade_constante
