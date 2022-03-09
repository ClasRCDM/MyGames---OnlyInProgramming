"""Background class file"""

# & /Imports Background\ & #
# ------ General defs ------ #
import arcade
from os import path
# ------ Game variables ------ #
from variáveis import F_SPRITE_SIZE, F_SPRITE_TSCALING
from variáveis import ARQUIVO_BACKGROUND
# & \Imports Background/ & #


class Background():
    """ Background Sprites """
    def __init__(self, x, y, diretorio):
        """ Init Background """
        super().__init__()

        self.x, self.y = x, y

        main_path: str = path.join(diretorio, ARQUIVO_BACKGROUND)

        # Conjunto de texturas/Carregando texturas
        self.background_texturas = [arcade.Sprite(
            f"{main_path}_floresta{texture}.png", hit_box_algorithm='None'
            ) for texture in range(3)]

    def set_location(self, background):
        """ Set position background """
        background.center_x = F_SPRITE_SIZE * self.x + F_SPRITE_SIZE / 2
        background.center_y = F_SPRITE_SIZE * self.y + F_SPRITE_SIZE / 2

    def set_scaling(self, background):
        """ Set scale background """
        background.scale: float = F_SPRITE_TSCALING

    def set_size(self, background):
        self.set_location(background)
        self.set_scaling(background)

    def return_sprite(self, index):
        """ return background sprite """
        return self.background_texturas[index]
