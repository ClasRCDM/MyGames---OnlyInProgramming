import pygame
from numpy import arange


def grid(janela, comprimento, tamanho_linha, tamanho_quadrado):
    """
    :param janela: especifica a janela a ser usada.
    :param comprimento: espaço que vai ocupar na tela.
    :param tamanho_linha: até onde as linhas irão.
    :param tamanho_quadrado: o tamanho do quadrado do grid.
    :return: none
    """

    def draw_grid(v):
        pygame.draw.line(janela, (255, 255, 255),
                         (v * tamanho_quadrado, 0),
                         (v * tamanho_quadrado, comprimento))
        pygame.draw.line(janela, (255, 255, 255),
                         (0, v * tamanho_quadrado),
                         (comprimento, v * tamanho_quadrado))

    # Iniciando o grid
    for x_c in arange(comprimento // tamanho_linha): draw_grid(x_c)


def borda(janela, comprimento, tamanho, espaçamento=0):
    for x_c in arange(comprimento // tamanho):
        pygame.draw.line(janela, (255, 255, 255),
                         (x_c, espaçamento), (x_c, comprimento))
    for y_c in arange(comprimento // tamanho):
        pygame.draw.line(janela, (255, 255, 255),
                         (espaçamento, y_c), (comprimento, y_c))


pygame.init()

tela_cheia = 600, 600

janela = pygame.display.set_mode(tela_cheia)
janela.fill((0, 0, 0))
pygame.display.set_caption('Testes de grid')

FPS = 60
Fps = pygame.time.Clock()

game = True
while 1:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: game = False

    grid(janela, 400, 42, 50)

    pygame.display.flip()
    Fps.tick(FPS)

    if not game: break
