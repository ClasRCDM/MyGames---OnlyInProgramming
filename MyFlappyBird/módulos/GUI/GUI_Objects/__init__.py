"""Class to objects for GUI"""

# & /Imports objects for GUI\ & #
# ------ General defs ------ #
# ------ Game variables ------ #
from variáveis import GD_SPRITE, GM_RESTART
from variáveis import B_SPRITE_TSCALING, B_SPRITE_SIZE
# ------ Window modules ------ #
from módulos.Objeto import Object_sprite
# & \Imports objects for GUI/ & #


class Defeat(Object_sprite):
    def __init__(self, pos, diretorio):
        super().__init__(pos[0], pos[1])

        self.scale: float = B_SPRITE_TSCALING

        # Add texture
        self.set_sprite(self.sprite_loc(diretorio, GD_SPRITE))

        self.set_pos(B_SPRITE_SIZE)


class Menu_restart(Object_sprite):
    def __init__(self, pos, diretorio):
        super().__init__(pos[0], pos[1])

        self.scale: float = B_SPRITE_TSCALING

        # Add texture
        self.set_sprite(self.sprite_loc(diretorio, GM_RESTART))

        self.set_pos(B_SPRITE_SIZE)
