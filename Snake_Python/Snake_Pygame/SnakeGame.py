"""Main program file"""

# & /Imports World\ & #
# ------ General defs ------ #
import pygame
# ------ Game variables ------ #
import variáveis as v
# ------ Window modules ------ #
from módulos import defs
from módulos import text
# ------ Entity modules ------ #
from módulos import player
from módulos import apple
# & \Imports World/ & #


########################
# Configuring my World #
########################

class Mundo:
    """Main program"""
    # Build game &
    pygame.init()
    pygame.display.set_caption('Mundo...')

    # Basic utilities &
    janela = pygame.display.set_mode((v.TELA_CHEIA), depth=16, display=1)
    fps = pygame.time.Clock()

    # World variables &
    FPS: int = None
    FPS_pos = None

    ativo_m: bool = None
    mouse_pos: tuple = None
    clicando: bool = None

    # Entities &
    Entidades: dict = {}

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
    def principais_eventos(cls, eventos):
        # Exit to game &
        cls.ativo_m = cls.fechando_janela(eventos)
        cls.clicando = cls.checando_click(eventos)

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
        self.cena: str = 'None'

        # $ Texts $ #
        self.Textos: dict = {}

        # \Itens World/ #
        #################

    def iniciando(self):
        if self.cena.lower() == 'menu': self.menu()
        elif self.cena.lower() == 'jogar': self.jogar()
        self.processando()

    def set_cena(cc, cena: str = None):
        if cena is None: cc.cena = 'menu'
        else: cc.cena = cena.lower()

    def processando(pcs):
        while 1:
            pcs.mouse_pos = pygame.mouse.get_pos()

            if pcs.cena.lower() == 'menu':
                pcs.menu_com_input(pcs.janela)
            elif pcs.cena.lower() == 'jogar':
                pcs.jogar_update()

            for eventos in pygame.event.get():
                pcs.principais_eventos(eventos)

                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_ESCAPE:
                    pcs.ativo_m = False

                if pcs.cena.lower() == 'jogar':
                    pcs.Entidades['cobra'].input(eventos)

            if not pcs.ativo_m:
                break

            pygame.display.update()
            pcs.fps.tick(pcs.FPS)

    def menu_estatico(init, janela):
        defs.borda(janela, v.TELA_CHEIA[0], 30, (80, 80, 80), 0, 20)

        # % Title %
        título = text.Texto(janela, 'Snake_Pygame', 30,
                            cor=(255, 255, 255),
                            x=v.TELA_CHEIA[0] / 2,
                            y=v.TELA_CHEIA[1] / 2 - 100)
        título.sublinhado(posição='cima', caractere='*')

        # % Play game %
        b_jogar = text.Texto(janela, 'Jogar', 40, 210, 50,
                             rect=True,
                             cor=(255, 255, 255),
                             cor_fundo=(10, 10, 10),
                             x=v.TELA_CHEIA[0] / 2,
                             y=v.TELA_CHEIA[1] / 2 + 50)
        b_jogar.sublinhado(posição='cima_baixo')

        # % Exit %
        b_sair = text.Texto(janela, 'Sair', 35, 150, 50,
                            rect=True,
                            cor=(255, 255, 255),
                            cor_fundo=(10, 10, 10),
                            x=v.TELA_CHEIA[0] / 2,
                            y=v.TELA_CHEIA[1] / 2 + 150)
        b_sair.sublinhado(posição='cima_baixo')

        # * Results *
        init.Textos['b_jogar'] = b_jogar
        init.Textos['b_sair'] = b_sair

    def menu_com_input(update, janela):
        if update.clicando:  # Starting game or Leaving &
            if update.Textos['b_jogar'].mouse_colisão(update.mouse_pos):
                update.set_cena('Jogar')
                update.iniciando()
            elif update.Textos['b_sair'].mouse_colisão(update.mouse_pos):
                update.ativo_m = False

    def menu(action):
        action.menu_estatico(action.janela)

    def jogar(self):
        pygame.display.set_caption('Snake_game')

        self.Textos.clear()

        self.Entidades['cobra'] = player.Snake()
        self.Entidades['maça'] = apple.Maça()

    def jogar_update(gp):
        gp.janela.fill((0, 0, 0))

        gp.Entidades['maça'].update(gp.janela)

        gp.Entidades['cobra'].draw(gp.janela)
        gp.Entidades['cobra'].update(gp.Entidades['maça'].volta())

        defs.grid(gp.janela, v.TELA_CHEIA[0],
                  v.TAMANHO_GRID, v.TAMANHO_GRID,
                  cor=(80, 80, 80))

        text.Texto(gp.janela, f'FPS: {gp.fps.get_fps():.2f}',
                   15, cor=(239, 184, 16),
                   x=100, y=70)
