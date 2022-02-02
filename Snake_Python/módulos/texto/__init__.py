# () /Imports text\ () #
from pygame import font  # Text initialization
from os import path, getcwd  # Get files
from variáveis import ARQUIVO_FONT, NOME_FONT  # source location
# () \Imports text/ () #


class Texto:  # Texts
    # Create/Add texts
    font.init()
    diretorio: str = path.join(getcwd(), ARQUIVO_FONT, NOME_FONT)

    def __init__(self, janela, txt: str,
                 tamanho: int, cor: tuple,
                 x: int = 0, y: int = 0,
                 not_pixel: bool = False):
        # &#########################& #
        self.tamanho: int = tamanho

        self.txt: str = txt
        self.pixel: bool = not_pixel
        self.cor: tuple = cor

        self.x, self.y = x, y

        self.janela = janela
        # &#########################& #

        self.draw()

    def sublinhado(text, posição='baixo',
                   cor=('letra', (0, 0, 0)),
                   caractere='_'):  # $ Leaving underlined $ #
        txrender, txfont = text.font(0), text.font(1)
        sublinhado = txfont.render(caractere * len(text.txt), text.pixel,
                                   text.cor if cor[0] == 'letra' else cor[1])
        posi = None
        if posição == 'baixo': posi = text.y - txrender.get_rect().height
        elif posição == 'cima': posi = text.y - txrender.get_rect().height - 60
        elif posição == 'cima_baixo':
            posi = text.y - txrender.get_rect().height
            text.janela.blit(sublinhado, (text.x - txrender.get_rect().width / 2,
                                          text.y - txrender.get_rect().height - 60))

        text.janela.blit(sublinhado, (text.x - txrender.get_rect().width / 2, posi))

    def render(rd):  # $ To create $ #
        txrender = rd.font(0)
        rd.janela.blit(txrender, (rd.x - txrender.get_rect().width / 2,
                                  rd.y - 50))

    def font(rd, index=0):  # $ Set variables $ #
        txt_font = font.Font(rd.diretorio, rd.tamanho)
        txt_render = txt_font.render(rd.txt, rd.pixel, rd.cor)
        return txt_render if index == 0 else txt_font

    def draw(self):  # $ Render $ #
        self.render()
