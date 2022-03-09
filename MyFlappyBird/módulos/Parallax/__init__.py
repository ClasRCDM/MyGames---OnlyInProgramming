"""Parallax program file"""

# & /Imports Parallax\ & #
# ------ General defs ------ #
import arcade
# ------ Game variables ------ #
import variáveis as v
# ------ Window modules ------ #
from módulos.Floresta import Background
# & \Imports Parallax/ & #


class Parallax:
    """ Parallax class file """

    def __init__(self, x, y, diretorio):
        self.background = Background(x, y, diretorio)

        [self.background.set_size(self.background.return_sprite(index)
                                  ) for index in range(3)]

    def _return(self, index):
        return self.background.return_sprite(index)

    def movimento(self):
        pass
