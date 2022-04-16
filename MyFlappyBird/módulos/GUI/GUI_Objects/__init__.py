"""Class to objects for GUI"""

# & /Imports objects for GUI\ & #
# ------ General defs ------ #
from os import path
# ------ Game variables ------ #
from variáveis import GD_SPRITE, GM_RESTART, GP_SCOREBOARD, GP_SCORE
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


class Points_score(Object_sprite):
    def __init__(self, pos, diretorio):
        super().__init__(pos[0], pos[1])

        self.scale: float = B_SPRITE_TSCALING

        # Add texture
        self.set_sprite(self.sprite_loc(diretorio, GP_SCOREBOARD))

        self.set_pos(B_SPRITE_SIZE)


class Score(Object_sprite):
    def __init__(self, pos, diretorio, size=0):
        super().__init__(pos[0], pos[1])

        self.scale: float = B_SPRITE_TSCALING-size

        # -- Numbers
        self.numbers: str = GP_SCORE

        # Add texture
        self.set_sprite(self.sprite_loc(
            diretorio, self.numbers[0]))

        self.set_pos(B_SPRITE_SIZE)

    def set_sprite_number(self, diretorio, index):
        self.set_sprite(self.sprite_loc(
            diretorio, self.numbers[index]))
