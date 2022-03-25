"""Classes to decorate"""

# & /Imports decorations\ & #
# ------ General defs ------ #
from os import path
from arcade import Sprite, load_texture_pair
# ------ Game variables ------ #
from variáveis import B_SPRITE_TSCALING, B_SPRITE_SIZE
from variáveis import D_SPRITE_ROCK, D_SPRITE_STEAKHOUSE
# & \Imports decorations/ & #


class Big_rock(Sprite):
    def __init__(self, pos, diretorio):
        super().__init__()

        self.x, self.y = pos
        self.scale: float = B_SPRITE_TSCALING

        main_path: str = path.join(
            diretorio, D_SPRITE_ROCK)

        self.sprite = load_texture_pair(main_path)

        # Textura_Inicial
        self.texture = self.sprite[0]

        self.set_location()

    def set_location(self):
        self.center_x = B_SPRITE_SIZE * self.x + B_SPRITE_SIZE / 2
        self.center_y = B_SPRITE_SIZE * self.y + B_SPRITE_SIZE / 2


class Medieval_steakhouse(Sprite):
    def __init__(self, pos, diretorio):
        super().__init__()

        self.x, self.y = pos
        self.scale: float = B_SPRITE_TSCALING

        main_path: str = path.join(
            diretorio, D_SPRITE_STEAKHOUSE)

        self.sprite = load_texture_pair(main_path)

        # Textura_Inicial
        self.texture = self.sprite[0]

        self.set_location()

    def set_location(self):
        self.center_x = B_SPRITE_SIZE * self.x + B_SPRITE_SIZE / 2
        self.center_y = B_SPRITE_SIZE * self.y + B_SPRITE_SIZE / 2
