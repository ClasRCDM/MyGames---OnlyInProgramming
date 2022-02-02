from pygame import font
from os import path, getcwd  # Get files
from variáveis import ARQUIVO_FONT, NOME_FONT


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

        self.x = self.y = x, y

        self.janela = janela
        # &#########################& #

        self.render()

    def render(rd):  # $ To create $ #
        text_font = font.Font(rd.diretorio, rd.tamanho)
        text_render = text_font.render(rd.txt, rd.pixel, rd.cor)

        rd.janela.blit(text_render, (600 / 2, 600 / 2))

    def draw(self):  # $ Render $ #
        self.render()
