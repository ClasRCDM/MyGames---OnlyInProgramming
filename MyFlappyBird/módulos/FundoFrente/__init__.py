"""Background class file"""

# & /Imports BackgroundForeground\ & #
# ------ General defs ------ #
from arcade import SpriteList
from typing import Optional
# ------ Game variables ------ #
from variáveis import PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA
# ------ Window modules ------ #
from módulos.Parallax import Parallax
from módulos.Água import Water
# & \Imports BackgroundForeground/ & #


class BackgroundForeground:
    """ Background and Foreground Sprites """

    def __init__(self):
        """ Init BackgroundForeground """

        self.fundo = {}
        self.fundo_floresta: Optional[SpriteList] = None
        self.fundo_reflexo: Optional[SpriteList] = None

    def create_spritlist(self):
        self.fundo_floresta = SpriteList()
        self.fundo_reflexo = SpriteList()
        self.fundo_reflexo.alpha_normalized = 0.8

    def set_move(self, layer, vel):
        self.fundo[layer].update(self.fundo[layer].layer, vel)

    def set_tiles(self, diretorio):
        self.create_parallax('layer_1', diretorio, 3.6, 6.4, 2,
                             'Floresta')
        self.create_parallax('layer_2', diretorio, 3.4, 6, 1,
                             'Floresta')
        self.create_parallax('layer_3', diretorio, 3.5, 6.8, 0,
                             'Floresta')

        self.create_parallax('layer_4', diretorio, 2.5, 15, 0,
                             'Lights')
        self.create_parallax('layer_5', diretorio, 15, 16.5, 1,
                             'Lights')

        self.fundo['layer_6'] = Water(201, 22, 60, 402)

        self.create_parallax('layer_7', diretorio, 3.5, -0.89, 0,
                             'Reflexo', True)

    def append_tiles(self):
        self.return_parallax(self.fundo_floresta, 'layer_3')
        self.return_parallax(self.fundo_floresta, 'layer_4')
        self.return_parallax(self.fundo_floresta, 'layer_2')
        self.return_parallax(self.fundo_floresta, 'layer_5')
        self.return_parallax(self.fundo_floresta, 'layer_1')

        self.return_parallax(self.fundo_reflexo, 'layer_7')

    def create_parallax(self, layer,
                        diretorio,
                        x, y, index,
                        modelo, flip=False):
        self.fundo[layer] = Parallax(
            x, y, diretorio, index, modelo,
            PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA, flipp=flip)

    def return_parallax(self, tile, layer):
        [tile.append(self.fundo[layer]._return(
            index, self.fundo[layer].layer)) for index in range(2)]

    def update_movs(self):
        self.set_move('layer_1', 2)
        self.set_move('layer_2', 0.8)
        self.set_move('layer_3', 0.3)
        self.set_move('layer_4', 0.3)
        self.set_move('layer_5', 1.2)
        self.set_move('layer_7', 2)

    def draw(self):
        self.fundo_floresta.draw(pixelated=True)
        self.fundo['layer_6'].draw()
        self.fundo_reflexo.draw(pixelated=False)
