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
from módulos.Parallax import Parallax, Water, Iterator
from módulos.Decorações import Big_rock, Leave_particle
# & \Imports Background Foreground/ & #


class BackgroundForeground:
    """ Background and Foreground Sprites """

    def __init__(self):
        """ Init BackgroundForeground """

        # Sprites
        self.tile = {}

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
        self.tile['layer_1'] = self.set_pllx(diretorio, 3.6, 6.4, 2, 'Floresta')
        self.tile['layer_2'] = self.set_pllx(diretorio, 3.4, 6, 1, 'Floresta')
        self.tile['layer_3'] = self.set_pllx(diretorio, 3.5, 6.8, 0, 'Floresta')
        self.tile['layer_4'] = self.set_pllx(diretorio, 2.5, 15, 0, 'Lights')
        self.tile['layer_5'] = self.set_pllx(diretorio, 15, 16.5, 1, 'Lights')

        # -- Object water/Reflection
        self.tile['layer_6'] = Water(201, 22, 60, 402, diretorio)
        self.tile['layer_7'] = self.set_pllx(diretorio, 3.5, -0.89, 0, 'Reflexo', True)
        self.tile['layer_11'] = self.set_pllx(diretorio, 3.5, -0.89, 0, 'Effect_water', True)

        # -- collision obstacles
        self.tile['layer_8'] = Obstacles(-60, 0, diretorio, 0, 'Tronco')
        self.tile['layer_9'] = Obstacles(-190, 0, diretorio, 1, 'Tronco')

        self.tile['layer_10'] = Big_rock((3.4, -1), diretorio)
        self.tile['layer_12'] = Leave_particle((3, 6), diretorio)

    def append_tiles(self):
        """ Add all tiles """
        # -- Set Parallax sprites to sprite group
        nuns = Iterator(PF_SEQUENCIA_SPRITES, op=1)
        for index in nuns:
            self.return_parallax(self.tile_floresta, f'layer_{index}')

        # -- Add reflection sprites to sprite group
        self.return_sprites(self.tile_reflexo,
                            self.tile['layer_7']._return,
                            (self.tile['layer_7'].layer,
                             self.tile['layer_7'].layer),
                            (0, 1))

        self.return_sprites(self.tile_reflexo,
                            self.tile['layer_11']._return,
                            (self.tile['layer_11'].layer,
                             self.tile['layer_11'].layer),
                            (0, 1))

        # -- Set Obstacles sprites to sprite group
        self.return_sprites(self.tile_obstacles,
                            self.tile['layer_8'].return_sprite,
                            (self.tile['layer_8'].tronco_baixo,
                             self.tile['layer_8'].tronco_cima))

        self.return_sprites(self.tile_obstacles,
                            self.tile['layer_9'].return_sprite,
                            (self.tile['layer_9'].tronco_baixo,
                             self.tile['layer_9'].tronco_cima))

        # -- Add Objects sprites to sprite group
        self.tile_objects.append(self.tile['layer_10'])
        self.tile_objects.append(self.tile['layer_12'])

    def update_movs(self, física):
        """ Moving the sprites  """

        nuns = Iterator(PF_SEQUENCIA_SSPEED, op=2)
        for index, speed in nuns:
            self.set_move(f'layer_{index+1}', speed)

        self.set_move('layer_7', 2)
        self.set_move('layer_11', 2)

        self.tile['layer_8'].moving(física)
        self.tile['layer_9'].moving(física)

        if not self.tile['layer_10'].center_x >= 500:
            self.tile_objects.move(2, 0)

    def return_parallax(self, tiles, layer):
        """ Set the parallax to the group sprite """
        tiles.append(self.tile[layer]._return(
            0, self.tile[layer].layer))
        tiles.append(self.tile[layer]._return(
            1, self.tile[layer].layer))

    def return_sprites(self, tiles, object1, object2, v=None):
        if v is None:
            tiles.append(object1(object2[0]))
            tiles.append(object1(object2[1]))
        elif v is not None:
            tiles.append(object1(v[0], object2[0]))
            tiles.append(object1(v[1], object2[1]))

    def set_pllx(self,
                 diretorio,
                 x, y, index,
                 modelo, flip=False):
        """ Create object Parallax """

        return Parallax(x, y, diretorio, index, modelo,
                        PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA, flipp=flip)

    def set_física(self, física):
        """ Create physics for the obstacles """
        física.add_sprite_list(self.tile_obstacles,
                               friction=0.6,
                               collision_type="wall",
                               body_type=arcade.PymunkPhysicsEngine.DYNAMIC)

    def draw(self):
        """ Draw sprites groups """
        self.tile_floresta.draw(pixelated=True)
        self.tile['layer_6'].draw()

        if not self.tile['layer_10'].center_x >= 500:
            self.tile_objects.draw(pixelated=True)

        self.tile_reflexo.draw(pixelated=True)
        self.tile_obstacles.draw(pixelated=True)
