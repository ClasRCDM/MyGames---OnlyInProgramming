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
    # Build game &
    pygame.init()
    pygame.display.set_caption('Mundo...')

    # Basic utilities &
    janela = pygame.display.set_mode((TELA_CHEIA), depth=32, display=1)
    fps = pygame.time.Clock()

    # World variables &
    FPS = None
    ativo_m = None
    mouse_pos = None
    clicando = None

    # &#########################& #
    @classmethod
    def variáveis_inicias(cls, ativo_m=True, cor_fundo=(0, 0, 0), fps=60):
        # @ Important variables @ #
        cls.ativo_m = ativo_m
        cls.janela.fill(cor_fundo)
        cls.FPS = fps

        if cls.mouse_pos is None:
            cls.mouse_pos = pygame.mouse.get_pos()

    @classmethod
    def principais_eventos(cls):
        for evento in pygame.event.get():
            # Exit to game &
            cls.ativo_m = cls.fechando_janela(evento)
            cls.clicando = cls.checando_click(evento)

        pygame.display.flip()
        cls.fps.tick(cls.FPS)

    @classmethod
    def checando_click(cls, evento):  # @ Checking the click @ #
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            return True
        if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            return False

    @classmethod
    def fechando_janela(cls, evento):  # @ Closing window @ #
        if evento.type == pygame.QUIT and cls.ativo_m:
            return False
        return True
    # &#########################& #

    def __init__(self):
        print('Mundo iniciado')

        #################
        # /Itens World\ #

        # $ Texts $ #
        self.Textos: dict = {}

        # \Itens World/ #
        #################

    def iniciando(self):
        self.menu_estatico(self.janela)
        self.processando()

    def processando(pcs):
        while 1:
            pcs.mouse_pos = pygame.mouse.get_pos()

            pcs.principais_eventos()
            pcs.menu_com_input(pcs.janela)

            if not pcs.ativo_m: break

    def menu_estatico(init, janela):
        defs.borda(janela, TELA_CHEIA[0], 30, (80, 80, 80), 0, 20)

        # % Title %
        título = texto.Texto(janela, 'Snake_Pygame', 30,
                             cor=(255, 255, 255),
                             x=TELA_CHEIA[0] / 2,
                             y=TELA_CHEIA[1] / 2 - 100)
        título.sublinhado(posição='cima', caractere='*')

        # % Play game %
        b_jogar = texto.Texto(janela, 'Jogar', 40, 210, 50,
                              rect=True,
                              cor=(255, 255, 255),
                              cor_fundo=(10, 10, 10),
                              x=TELA_CHEIA[0] / 2,
                              y=TELA_CHEIA[1] / 2 + 50)
        b_jogar.sublinhado(posição='cima_baixo')

        # % Exit %
        b_sair = texto.Texto(janela, 'Sair', 35, 150, 45,
                             rect=True,
                             cor=(255, 255, 255),
                             cor_fundo=(10, 10, 10),
                             x=TELA_CHEIA[0] / 2,
                             y=TELA_CHEIA[1] / 2 + 150)
        b_sair.sublinhado(posição='cima_baixo')

        # * Results *
        init.Textos['b_jogar'] = b_jogar
        init.Textos['b_sair'] = b_sair

    def menu_com_input(update, janela):
        if update.clicando:  # Starting game or Leaving &
            if update.Textos['b_jogar'].mouse_colisão(update.mouse_pos):
                print('jogar')
            elif update.Textos['b_sair'].mouse_colisão(update.mouse_pos):
                print('sair')
