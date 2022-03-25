"""Background and Foreground class file"""

# & /Imports Background Foreground\ & #
# ------ General defs ------ #
import arcade
from arcade import SpriteList
# ------ Game variables ------ #
from variáveis import PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA
from variáveis import PF_SEQUENCIA_SPRITES, PF_SEQUENCIA_SSPEED
# ------ Window modules ------ #
from módulos.Obstáculos import Obstacles
from módulos.Parallax import Parallax, Water
from módulos.Decorações import Big_rock, Medieval_steakhouse
# & \Imports Background Foreground/ & #


class BackgroundForeground:
    """ Background and Foreground Sprites """

    def __init__(self):
        """ Init BackgroundForeground """

        # Sprites
        self.tile, self.obstáculos = {}, {}

        # Group sprites/Forest, Forest reflection
        self.tile_floresta, self.tile_reflexo = SpriteList(), SpriteList()
        self.tile_reflexo.alpha_normalized = 0.8

        # Group sprite obstacles
        self.tile_obstacles, self.tile_objects = SpriteList(), SpriteList()

    def set_move(self, layer, vel):
        """ Move parallax sprite """
        self.tile[layer].update(self.tile[layer].layer, vel)

    def set_tiles(self, diretorio):
        """ Create all tiles """

        # -- Objects Parallax
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

        # -- Object water/Reflection
        self.tile['layer_6'] = Water(201, 22, 60, 402)
        self.create_parallax('layer_7', diretorio, 3.5, -0.89, 0,
                             'Reflexo', True)

        # -- collision obstacles
        self.tile['layer_8'] = Obstacles(-60, 0, diretorio, 0, 'Tronco')
        self.tile['layer_9'] = Obstacles(-190, 0, diretorio, 1, 'Tronco')

        self.tile['layer_10'] = Big_rock((3.4, -1), diretorio)

    def append_tiles(self):
        """ Add all tiles """
        # -- Set Parallax sprites to sprite group
        [self.return_parallax(self.tile_floresta, f'layer_{index}')
         for index in PF_SEQUENCIA_SPRITES]

        # -- Add reflection sprites to sprite group
        self.return_parallax(self.tile_reflexo, 'layer_7')

        # -- Set Obstacles sprites to sprite group
        self.return_obstacles(self.tile_obstacles, 'layer_8')
        self.return_obstacles(self.tile_obstacles, 'layer_9')

        # -- Add Objects sprites to sprite group
        self.tile_objects.append(self.tile['layer_10'])

    def create_parallax(self, layer,
                        diretorio,
                        x, y, index,
                        modelo, flip=False):
        """ Create object Parallax """
        self.tile[layer] = Parallax(
            x, y, diretorio, index, modelo,
            PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA, flipp=flip)

    def return_parallax(self, tiles, layer):
        """ Set the parallax to the group sprite """
        [tiles.append(self.tile[layer]._return(
            index, self.tile[layer].layer)) for index in range(2)]

    def return_obstacles(self, tiles, layer):
        """ Set the obstacle to the group sprite """
        tiles.append(self.tile[layer].return_sprite(
            self.tile[layer].tronco_baixo))
        tiles.append(self.tile[layer].return_sprite(
            self.tile[layer].tronco_cima))

    def update_movs(self, física):
        """ Moving the sprites  """
        [self.set_move(f'layer_{index+1}', speed)
         for index, speed in enumerate(PF_SEQUENCIA_SSPEED)]
        self.set_move('layer_7', 2)

        self.tile['layer_8'].moving(física)
        self.tile['layer_9'].moving(física)

    def set_physics(self, física):
        """ Create physics for the obstacles """
        física.add_sprite_list(self.tile_obstacles,
                               friction=0.6,
                               collision_type="wall",
                               body_type=arcade.PymunkPhysicsEngine.DYNAMIC)

    def draw(self):
        """ Draw sprites groups """
        self.tile_floresta.draw(pixelated=True)
        self.tile['layer_6'].draw()
        self.tile_objects.draw(pixelated=True)
        self.tile_reflexo.draw(pixelated=False)
        self.tile_obstacles.draw(pixelated=True)
