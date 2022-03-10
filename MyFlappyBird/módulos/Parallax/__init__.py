"""Parallax program file"""

# & /Imports Parallax\ & #
# ------ General defs ------ #
from numpy import arange
# ------ Game variables ------ #
from variáveis import P_MAX_HORIZONTAL, P_PONTO_DE_VOLTA
# ------ Window modules ------ #
from módulos.Floresta import Background
# & \Imports Parallax/ & #


class Parallax:
    """ Parallax class file """

    MAX_X = P_MAX_HORIZONTAL
    PONTO_X = P_PONTO_DE_VOLTA

    def __init__(self, x, y, diretorio):
        self.layer_1 = Background((x, x-24), y, diretorio, 2)
        self.layer_2 = Background((x, x-24), y, diretorio, 1)
        self.layer_3 = Background((x, x-24), y, diretorio, 0)

        self.set_psize(self.layer_1)
        self.set_psize(self.layer_2)
        self.set_psize(self.layer_3)

    def set_psize(self, layer):
        return [layer.set_size(
            layer.return_sprite(index), index
            ) for index in arange(2)]

    def _return(self, index, background):
        return background.return_sprite(index)

    def update(s_up, background):
        s_up.movimento(background)

        (s_up.loop_movimento(background, index) for index in arange(2))

    def movimento(self, background):
        [background.movement_aside(
            background.return_sprite(index), 2
            ) for index in arange(2)]

    def loop_movimento(self, background, index):
        if background.return_sprite(index).center_x >= self.MAX_X:
            background.return_sprite(index).center_x = self.PONTO_X
