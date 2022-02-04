# & /Imports Player\ & #
from variáveis import snake, SNAKE_COR, MINHAS_DIREÇÕES, minha_direção

from pygame import Surface
from pygame import K_w, K_s, K_a, K_d
from pygame import KEYDOWN

from operator import sub, add
# & \Imports Player/ & #


# Player
class Snake:
    SNAKE_PELE = Surface((10, 10))
    SNAKE_PELE.fill(SNAKE_COR)

    @classmethod
    def update(cls, janela):
        [janela.blit(cls.SNAKE_PELE, pos) for pos in snake]

    def __init__(self):
        print('Cobra colocada')

    def direção(drc):
        def verificando_direção_cb(op, v, di):
            if minha_direção == MINHAS_DIREÇÕES[di]:
                snake[0] = snake[0][0], op(snake[0][1], v)

        def verificando_direção_ed(op, v, di):
            if minha_direção == MINHAS_DIREÇÕES[di]:
                snake[0] = op(snake[0][0], v), snake[0][1]

        verificando_direção_cb(sub, 10, 'CIMA')
        verificando_direção_cb(add, 10, 'BAIXO')
        verificando_direção_ed(sub, 10, 'ESQUERDA')
        verificando_direção_ed(add, 10, 'DIREITA')

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

    def movendo(mv, evento):
        def mover(tecla, p_direção):
            if evento.type == KEYDOWN and evento.key == tecla:
                global minha_direção
                minha_direção = p_direção

        mover(K_a, MINHAS_DIREÇÕES['ESQUERDA'])
        mover(K_d, MINHAS_DIREÇÕES['DIREITA'])
        mover(K_w, MINHAS_DIREÇÕES['CIMA'])
        mover(K_s, MINHAS_DIREÇÕES['BAIXO'])
