# & /Imports Apple\ & #
# ------ Apple variables ------ #
from variáveis import maças
from variáveis import MAÇA_COR, MAÇA_TAMANHO
from variáveis import TELA_CHEIA
# ------ Pygame defs ------ #
from pygame import Surface
# ------ Random number function ------ #
from random import randrange
# & \Imports Apple/ & #


class Maça:
    MAÇA_PELE = Surface(MAÇA_TAMANHO)
    MAÇA_PELE.fill(MAÇA_COR)
    MAÇA_rect = MAÇA_PELE.get_rect(topleft=maças[0])

    @classmethod
    def update(cls, janela):
        cls.MAÇA_rect = cls.MAÇA_PELE.get_rect(topleft=maças[0])
        [janela.blit(cls.MAÇA_PELE, pos) for pos in maças]

    def __init__(self):
        print(f'{len(maças)}° maça colocada.')

    def volta(self):
        return self.MAÇA_rect

    @staticmethod
    def adicionando_maça():
        print(f'{len(maças)+1}° maça colocada.')
        maças.append((randrange(0, TELA_CHEIA[0]) // 40*40,
                     randrange(0, TELA_CHEIA[1]) // 40*40))
