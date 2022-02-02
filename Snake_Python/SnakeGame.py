# & /Imports World\ & #
import pygame

from variáveis import *
from módulos import defs
from módulos import texto
# & \Imports World/ & #


########################
# Configuring my World #
########################

class Mundo:
    # Build game
    pygame.init()
    pygame.display.set_caption('Mundo...')

    # Basic utilities
    janela = pygame.display.set_mode((TELA_CHEIA), depth=32, display=1)
    fps = pygame.time.Clock()

    FPS = None
    ativo_m = None

    @classmethod
    def variáveis_inicias(cls, ativo_m=True, cor_fundo=(0, 0, 0), fps=60):
        cls.ativo_m = ativo_m
        cls.janela.fill(cor_fundo)
        cls.FPS = fps

    @classmethod
    def principais_eventos(cls):
        for evento in pygame.event.get():
            # Exit to game
            if evento.type == pygame.QUIT and cls.ativo_m:
                cls.ativo_m = False

        pygame.display.flip()
        cls.fps.tick(cls.FPS)

    def __init__(self):
        print('Mundo iniciado')

    def iniciando(self):
        self.menu(self.janela)
        self.processando()

    def processando(pcs):
        while 1:
            pcs.principais_eventos()

            if not pcs.ativo_m: break

    def menu(init, janela):
        defs.borda(janela, TELA_CHEIA[0], 30, (80, 80, 80), 0, 20)
        texto.Texto(janela, 'teste', 50, (255, 255, 255))
