"""Class to objects for GUI"""

# & /Imports objects for GUI\ & #
# ------ General defs ------ #
from os import path
from arcade import Sprite, load_texture_pair
# ------ Game variables ------ #
from variáveis import G_SPRITE_TSCALING, G_SPRITE_SIZE
# & \Imports objects for GUI/ & #


class PlayBox(Sprite):
    def __init__(self, pos, diretorio):
        super().__init__()

        self.x, self.y = pos
        self.scale = G_SPRITE_TSCALING

        self.hit_box_algorithm = 'None'

        # Add texture
        main_path: str = path.join(
            diretorio)

        self.sprite = load_texture_pair(main_path)

        # Set texture
        self.texture = self.sprite[0]

        self.set_position(self.set_pos()[0], self.set_pos()[1])

    def set_pos(self) -> int | float:
        """ Set location """

        return G_SPRITE_SIZE * self.x + G_SPRITE_SIZE / 2, G_SPRITE_SIZE * self.y + G_SPRITE_SIZE / 2
