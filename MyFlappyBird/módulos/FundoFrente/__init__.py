"""Background and Foreground class file"""

# & /Imports BackgroundForeground\ & #
# ------ General defs ------ #
import arcade
from arcade import SpriteList
from typing import Optional
# ------ Game variables ------ #
from variáveis import PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA
from variáveis import PF_SEQUENCIA_SPRITES
# ------ Window modules ------ #
from módulos.Parallax import Parallax, Water
from módulos.Obstáculos import Obstacles
# & \Imports BackgroundForeground/ & #


class BackgroundForeground:
    """ Background and Foreground Sprites """

    def __init__(self):
        """ Init BackgroundForeground """

        self.fundo, self.obstáculos = {}, {}

        self.fundo_floresta, self.fundo_reflexo = SpriteList(), SpriteList()
        self.fundo_reflexo.alpha_normalized = 0.8

        self.fundo_obstacles = SpriteList()

    def set_move(self, layer, vel):
        """ Move parallax sprite """
        self.fundo[layer].update(self.fundo[layer].layer, vel)

    def set_tiles(self, diretorio):
        """ Create all tiles """
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

        self.fundo['layer_8'] = Obstacles(-60, 0, diretorio, 0, 'Tronco')
        self.fundo['layer_9'] = Obstacles(-190, 0, diretorio, 1, 'Tronco')

    def append_tiles(self):
        """ Add all tiles """
        # -- Set Parallax sprites to sprite group
        [self.return_parallax(self.fundo_floresta, f'layer_{index}')
         for index in PF_SEQUENCIA_SPRITES]

        # -- Add reflection sprites to sprite group
        self.return_parallax(self.fundo_reflexo, 'layer_7')

        # -- Set Obstacles sprites to sprite group
        self.return_obstacles(self.fundo_obstacles, 'layer_8')
        self.return_obstacles(self.fundo_obstacles, 'layer_9')

    def create_parallax(self, layer,
                        diretorio,
                        x, y, index,
                        modelo, flip=False):
        """ Create object Parallax """
        self.fundo[layer] = Parallax(
            x, y, diretorio, index, modelo,
            PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA, flipp=flip)

    def return_parallax(self, tile, layer):
        """ Set the parallax to the group sprite """
        [tile.append(self.fundo[layer]._return(
            index, self.fundo[layer].layer)) for index in range(2)]

    def return_obstacles(self, tile, layer):
        """ Set the obstacle to the group sprite """
        tile.append(self.fundo[layer].return_sprite(
            self.fundo[layer].tronco_baixo))
        tile.append(self.fundo[layer].return_sprite(
            self.fundo[layer].tronco_cima))

    def update_movs(self, física):
        """ Moving the sprites  """
        self.set_move('layer_1', 2)
        self.set_move('layer_2', 0.8)
        self.set_move('layer_3', 0.3)
        self.set_move('layer_4', 0.3)
        self.set_move('layer_5', 1.2)
        self.set_move('layer_7', 2)

        self.fundo['layer_8'].moving(física)
        self.fundo['layer_9'].moving(física)

    def set_physics(self, física):
        """ Create physics for the obstacles """
        física.add_sprite_list(self.fundo_obstacles,
                               friction=0.6,
                               collision_type="wall",
                               body_type=arcade.PymunkPhysicsEngine.DYNAMIC)

    def draw(self):
        """ Draw sprites groups """
        self.fundo_floresta.draw(pixelated=True)
        self.fundo['layer_6'].draw()
        self.fundo_reflexo.draw(pixelated=False)
        self.fundo_obstacles.draw(pixelated=True)
