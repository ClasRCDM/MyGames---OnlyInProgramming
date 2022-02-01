# & /Imports World\ & #
import pygame

from variáveis import *
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
    ativo_m = None

    @classmethod
    def iniciando_mundo(cls, ativo_m=True, cor_fundo=(0, 0, 0)):
        cls.ativo_m = ativo_m
        cls.janela.fill(cor_fundo)
        cls.processando_mundo()

    @classmethod
    def processando_mundo(cls):
        while 1:
            cls.eventos_mundo()

            if not cls.ativo_m: break

    @classmethod
    def eventos_mundo(cls):
        for evento in pygame.event.get():
            # Exit to game
            if evento.type == pygame.QUIT and cls.ativo_m:
                cls.ativo_m = False

        try:
            cls.eventos_principais()
        except:
            print('\033[31mO metodó "Eventos principais" não existe, imposibilitando a execução!\033[m')
            cls.ativo_m = False

        pygame.display.flip()
        cls.fps.tick(FPS)

    def __init__(cena):
        print('Mundo iniciado')
