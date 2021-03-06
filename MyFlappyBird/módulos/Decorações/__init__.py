"""Class to decorate"""

# & /Imports decorations\ & #
# ------ General defs ------ #
# ------ Game variables ------ #
from variáveis import B_SPRITE_TSCALING, B_SPRITE_SIZE
from variáveis import D_SPRITE_ROCK
# ------ Window modules ------ #
from módulos.Objeto import Object_sprite
# & \Imports decorations/ & #


class Big_rock(Object_sprite):
    """ Sprite Big rock """

    def __init__(self, pos, diretorio):
        """ Setup Rock """
        super().__init__(pos[0], pos[1])

        self.scale: float = B_SPRITE_TSCALING

        # Add texture
        self.set_sprite(self.sprite_loc(diretorio, D_SPRITE_ROCK))

        self.set_pos(B_SPRITE_SIZE)

    def move(self, vel):
        if self.center_x <= 500:
            self.center_x += vel
