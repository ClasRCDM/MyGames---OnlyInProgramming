"""Parallax program file"""

# & /Imports Parallax\ & #
# ------ General defs ------ #
from numpy import arange
# ------ Game variables ------ #
# ------ Window modules ------ #
from módulos.Floresta import Background
# & \Imports Parallax/ & #


class Parallax:
    """ Parallax class file """

    def __init__(self, x, y,
                 diretorio,
                 index_image, image,
                 max_x, ponto_max,
                 flipp=False):
        """ Init Parallax """

        self.MAX_X = max_x
        self.PONTO_X = ponto_max

        self.layer = Background((x, x-24.61), y,
                                diretorio, index_image,
                                image, flipp)

        self.set_psize(self.layer)

    def set_psize(self, layer):
        return [layer.set_size(
            layer.return_sprite(index), index
            ) for index in arange(2)]

    def _return(self, index, background):
        return background.return_sprite(index)

    def update(s_up, background, vel):
        s_up.movimento(background, vel)

        [s_up.loop_movimento(background, index) for index in arange(2)]

    def movimento(self, background, vel):
        [background.movement_aside(
            background.return_sprite(index), vel
            ) for index in arange(2)]

    def loop_movimento(self, background, index):
        if background.return_sprite(index).center_x >= self.MAX_X:
            background.return_sprite(index).center_x = self.PONTO_X
