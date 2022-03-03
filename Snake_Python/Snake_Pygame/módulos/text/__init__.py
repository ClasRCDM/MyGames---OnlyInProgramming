"""Text class file"""

# () /Imports text\ () #
from pygame import font, draw  # Text initialization
from os import path, getcwd  # Get files
from variáveis import ARQUIVO_FONT, NOME_FONT  # source location
# () \Imports text/ () #


class Texto:  # Texts
    # Create/Add texts
    font.init()
    diretorio: str = path.join(getcwd(), ARQUIVO_FONT, NOME_FONT)

    def __init__(self, janela, txt: str, tamanho: int,
                 largura: int = 0, altura: int = 0,
                 cor: tuple = (0, 0, 0),
                 cor_fundo: tuple = (0, 0, 0),
                 x: int = 0, y: int = 0,
                 not_pixel: bool = False,
                 rect: bool = False):
        # &#########################& #
        self.tamanho: int = tamanho

        self.txt: str = txt
        self.pixel: bool = not_pixel
        self.rect: bool = rect

        self.cor: tuple = cor
        self.cor_fundo: tuple = cor_fundo

        self.x, self.y = x, y
        self.altura, self.largura = altura, largura

        self.janela = janela
        # &#########################& #

        # Text Variables
        self.colisão_mouse = None

        self.draw()

    def sublinhado(text, posição='baixo',
                   cor=('letra', (0, 0, 0)),
                   caractere='_'):  # $ Leaving underlined $ #
        txrender, txfont = text.fonts(0), text.fonts(1)
        sublinhado = txfont.render(caractere * len(text.txt), text.pixel,
                                   text.cor if cor[0] == 'letra' else cor[1])
        posi = None
        if posição == 'baixo': posi = text.y - txrender.get_rect().height
        elif posição == 'cima': posi = text.y - txrender.get_rect().height - 60
        if posição == 'cima_baixo':
            posi = text.y - txrender.get_rect().height
            text.janela.blit(sublinhado, (text.x - txrender.get_rect().width / 2,
                                          text.y - txrender.get_rect().height - 60))

        text.janela.blit(sublinhado, (text.x - txrender.get_rect().width / 2, posi))

    def render(rd):  # $ To create $ #
        txrender = rd.fonts(0)

        if rd.rect:
            draw.rect(rd.janela, rd.cor_fundo,
                      ((rd.x - txrender.get_rect().width / 2)-10, (rd.y - 50)-10,
                       rd.largura+4, rd.altura+8), 0)
        rd.janela.blit(txrender, (rd.x - txrender.get_rect().width / 2,
                                  rd.y - 50))

    def fonts(rd, index=0):  # $ Set variables $ #
        txt_font = font.Font(rd.diretorio, rd.tamanho)
        txt_render = txt_font.render(rd.txt, rd.pixel, rd.cor)
        return txt_render if index == 0 else txt_font

    def draw(self):  # $ Render $ #
        self.render()

    def mouse_colisão(self, posição):
        txrender = self.fonts(0)
        x_txt = (self.x - txrender.get_rect().width / 2)-10
        y_txt = self.y - 50

        if posição[0] > x_txt and posição[0] < x_txt + self.largura+4:
            if posição[1] > y_txt and posição[1] < y_txt + self.altura+8:
                return True
        return False
