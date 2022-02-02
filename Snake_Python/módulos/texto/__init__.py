from pygame import font


class Texto:  # Texts
    def __init__(self, janela, diretorio: str,
                 txt: str, tamanho: int, cor: tuple,
                 x: int = 0, y: int = 0,
                 pixel: bool = False):

        # Create/Add texts
        font.init()

        # &#########################& #
        self.tamanho = tamanho

        self.txt: str = txt
        self.pixel: bool = pixel
        self.cor: tuple = cor

        self.x, self.y = x, y

        self.janela = janela
        self.diretorio: str = diretorio
        # &#########################& #

        self.render()

    def render(rd):  # $ To create $ #
        text_font = font.SysFont('Times New Roman, Arial', rd.tamanho)
        text_render = text_font.render(rd.txt, rd.pixel, rd.cor)

        rd.janela.blit(text_render, (600 / 2, 600 / 2))

    def draw(self):  # $ Render $ #
        self.render()
