# & /Imports Player\ & #
# ------ Player variables ------ #
from variáveis import snake, TAMANHO_GRID
from variáveis import SNAKE_COR, SNAKE_VELOCIDADE, SNAKE_TAMANHO
from variáveis import MINHAS_DIREÇÕES, minha_direção
from variáveis import maças, TELA_CHEIA
# ------ Pygame defs ------ #
from pygame import Surface
from pygame import K_w, K_s, K_a, K_d, K_c
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

    @classmethod
    def update(cls, janela, MAÇA_PELE):
        cls.SNAKE_rect = [cls.SNAKE_PELE.get_rect(topleft=pos) for pos in snake]
        [janela.blit(cls.SNAKE_PELE, rect) for rect in cls.SNAKE_rect]

        if cls.SNAKE_rect[0].colliderect(MAÇA_PELE):
            snake.append((snake[-1][0], snake[-1][1]))
            maças[0] = (randrange(0, TELA_CHEIA[0]) // TAMANHO_GRID*TAMANHO_GRID,
                        randrange(0, TELA_CHEIA[1]) // TAMANHO_GRID*TAMANHO_GRID)

    @classmethod
    def verificando_movimento(vr_v, pos, parte, valor=None):
        index = valor if valor is not None else '.0'
        x_y = f'{snake[parte][pos] / TAMANHO_GRID:.3f}'
        if index in x_y:  # .025
            return True
        return False

    def __init__(self):
        print('Cobra colocada')
        self.velocidade: int = SNAKE_VELOCIDADE
        self.velocidade_constante: int = 10

        self.proxima_direção_cb = None
        self.proxima_direção_ed = None

        self.direção_snake_ed = 'DIREITA'
        self.direção_snake_cb = 'None'

    def direção(drc):
        def verificando_direção_cb(op, v, di, parte):
            snake[parte] = snake[parte][0], op(snake[parte][1], v) \
                if minha_direção == MINHAS_DIREÇÕES[di] else snake[parte][1]

        def verificando_direção_ed(op, v, di, parte):
            snake[parte] = op(snake[parte][0], v) \
                if minha_direção == MINHAS_DIREÇÕES[di] else snake[parte][0], snake[parte][1]

        def movendo_corpo_cb(direção, op):
            def lado(pos, op):
                if drc.direção_snake_ed == pos:
                    snake[p_corpo] = op(snake[p_corpo][0], drc.velocidade), snake[p_corpo][1]

            get_corpo = (pos for pos in range(len(snake) - 1, 0, -1) if minha_direção == direção)
            for p_corpo in get_corpo:
                if abs(snake[0][1] - snake[p_corpo][1]) < 40*p_corpo:
                    lado('DIREITA', sub)
                    lado('ESQUERDA', add)
                else:
                    snake[p_corpo] = snake[p_corpo][0], op(snake[p_corpo][1], drc.velocidade)

        def movendo_corpo_ed(direção, op):
            def lado(pos, op):
                if drc.direção_snake_cb == pos:
                    snake[p_corpo] = snake[p_corpo][0], op(snake[p_corpo][1], drc.velocidade)

            get_corpo = (pos for pos in range(len(snake) - 1, 0, -1) if minha_direção == direção)
            for p_corpo in get_corpo:
                if abs(snake[0][0] - snake[p_corpo][0]) < 40*p_corpo:
                    lado('BAIXO', sub)
                    lado('CIMA', add)
                else:
                    snake[p_corpo] = op(snake[p_corpo][0], drc.velocidade), snake[p_corpo][1]

        verificando_direção_cb(sub, drc.velocidade, 'BAIXO', 0)
        verificando_direção_cb(add, drc.velocidade, 'CIMA', 0)
        verificando_direção_ed(sub, drc.velocidade, 'ESQUERDA', 0)
        verificando_direção_ed(add, drc.velocidade, 'DIREITA', 0)

        if drc.proxima_direção_cb is not None or drc.proxima_direção_ed is not None:
            global minha_direção
            if drc.verificando_movimento(0, 0):
                minha_direção = drc.proxima_direção_cb \
                    if drc.proxima_direção_cb is not None else minha_direção
                drc.proxima_direção_cb = None
            if drc.verificando_movimento(1, 0):
                minha_direção = drc.proxima_direção_ed \
                    if drc.proxima_direção_ed is not None else minha_direção
                drc.proxima_direção_ed = None

        if len(snake) > 1:
            movendo_corpo_ed(0, add)
            movendo_corpo_ed(1, sub)
            movendo_corpo_cb(2, sub)
            movendo_corpo_cb(3, add)

    def movendo(mv):
        teclas = key.get_pressed()

        def mover(tecla, v_direção, p_direção, opção):
            if teclas[tecla]:
                if opção == 0:
                    mv.direção_snake_cb = p_direção
                    mv.proxima_direção_cb = v_direção
                elif opção == 1:
                    mv.direção_snake_ed = p_direção
                    mv.proxima_direção_ed = v_direção

        mover(K_w, MINHAS_DIREÇÕES['CIMA'], 'CIMA', 0)
        mover(K_s, MINHAS_DIREÇÕES['BAIXO'], 'BAIXO', 0)
        mover(K_a, MINHAS_DIREÇÕES['DIREITA'], 'ESQUERDA', 1)
        mover(K_d, MINHAS_DIREÇÕES['ESQUERDA'], 'DIREITA', 1)

    def set_velocidade(speed, velocidade):
        speed.velocidade = velocidade * -speed.velocidade_constante
