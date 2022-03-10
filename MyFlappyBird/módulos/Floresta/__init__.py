"""Background class file"""

# & /Imports Background\ & #
# ------ General defs ------ #
import arcade
from os import path
from numpy import arange
# ------ Game variables ------ #
from variáveis import F_SPRITE_SIZE, F_SPRITE_TSCALING
from variáveis import ARQUIVO_BACKGROUND
# & \Imports Background/ & #


class Background():
    """ Background Sprites """
    def __init__(self, x, y, diretorio, index):
        """ Init Background """
        super().__init__()

        self.x, self.y = x, y

        main_path: str = path.join(diretorio, ARQUIVO_BACKGROUND)

        # Conjunto de texturas/Carregando texturas
        self.background_texturas = [arcade.Sprite(
            f"{main_path}_floresta{index}.png", hit_box_algorithm='None'
            ) for _ in arange(2)]

    def set_location(self, background, valor):
        """ Set position background """
        background.center_x = F_SPRITE_SIZE * self.x[valor] + F_SPRITE_SIZE / 2
        background.center_y = F_SPRITE_SIZE * self.y + F_SPRITE_SIZE / 2

    def set_scaling(self, background):
        """ Set scale background """
        background.scale: float = F_SPRITE_TSCALING

    def set_size(self, background, valor):
        self.set_location(background, valor)
        self.set_scaling(background)

    def return_sprite(self, index):
        """ return background sprite """
        return self.background_texturas[index]

    def movement_aside(self, background, vel):
        background.center_x += vel
