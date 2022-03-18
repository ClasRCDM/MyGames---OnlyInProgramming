"""Parallax program file"""

# & /Imports Parallax\ & #
# ------ General defs ------ #
from numpy import arange
from arcade import Sprite
from arcade import draw_rectangle_filled, csscolor
# ------ Game variables ------ #
from variáveis import F_SPRITE_SIZE, F_SPRITE_TSCALING
from variáveis import ARQUIVO_BACKGROUND
# ------ Window modules ------ #
from módulos.Objeto import Object
# & \Imports Parallax/ & #


class Parallax:
    """ Parallax class file """

    def __init__(self, x, y,
                 diretorio,
                 index, image,
                 max_x, ponto_max,
                 flipp=False):
        """ Init Parallax """

        self.MAX_X = max_x
        self.PONTO_X = ponto_max

        self.layer = Background((x, x-24.61), y,
                                diretorio, index,
                                image, flipp)

        self.set_psize(self.layer)

    def set_psize(self, layer) -> Object:
        return [layer.set_size(
            layer.return_sprite(index), index
            ) for index in arange(2)]

    def _return(self, index, background: Object) -> Sprite:
        return background.return_sprite(index)

    def update(s_up, background, vel):
        s_up.movimento(background, vel)

        s_up.loop_movimento(background, 0)
        s_up.loop_movimento(background, 1)

    def movimento(self, background, vel):
        [background.movement_aside(
            background.return_sprite(index), vel
            ) for index in arange(2)]

    def loop_movimento(self, background, index):
        if background.return_sprite(index).center_x >= self.MAX_X:
            background.return_sprite(index).center_x = self.PONTO_X


class Background(Object):
    """ Background Sprites """

    def __init__(self, x, y,
                 diretorio, index,
                 image, flip_vertical=False):
        """ Init Background """
        super().__init__(diretorio, ARQUIVO_BACKGROUND)

        self.x, self.y = x, y
        self.image, self.index = image, index

        # Conjunto de texturas/Carregando texturas
        self.background_texturas = [Sprite(
            f"{self.main_path}_{self.image}{self.index}.png",
            hit_box_algorithm='None',
            flipped_vertically=flip_vertical
            ) for _ in arange(2)]

    def set_size(self, background, valor):
        self.set_location(background, F_SPRITE_SIZE,
                          (self.x[valor], self.y))
        self.set_scaling(background, F_SPRITE_TSCALING)

    def return_sprite(self, index):
        """ return background sprite """
        return self.background_texturas[index]

    def movement_aside(self, background, vel):
        background.center_x += vel


class Water:
    def __init__(self, x, y, altura, largura):
        self.x, self.y = x, y

        self.altura, self.largura = altura, largura

    def draw(self):
        draw_rectangle_filled(self.x, self.y,
                              self.largura, self.altura,
                              csscolor.AQUA)
        draw_rectangle_filled(self.x, self.y+30,
                              self.largura, 5,
                              csscolor.LIGHT_CYAN)
