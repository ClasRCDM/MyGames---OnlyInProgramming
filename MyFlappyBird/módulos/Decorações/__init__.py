"""Classes to decorate"""

# & /Imports decorations\ & #
# ------ General defs ------ #
from os import path
from random import randint, uniform
from arcade import Sprite, load_texture_pair
# ------ Game variables ------ #
from variáveis import B_SPRITE_TSCALING, B_SPRITE_SIZE
from variáveis import D_SPRITE_ROCK, D_SPRITE_LEAVES
# & \Imports decorations/ & #


class Big_rock(Sprite):
    def __init__(self, pos, diretorio):
        super().__init__()

        self.x, self.y = pos
        self.scale: float = B_SPRITE_TSCALING

        self.hit_box_algorithm = 'None'

        # Add texture
        main_path: str = path.join(
            diretorio, D_SPRITE_ROCK)

        self.sprite = load_texture_pair(main_path)

        # Set texture
        self.texture = self.sprite[0]

        self.set_position(self.set_pos()[0], self.set_pos()[1])

    def set_pos(self):
        return B_SPRITE_SIZE * self.x + B_SPRITE_SIZE / 2, B_SPRITE_SIZE * self.y + B_SPRITE_SIZE / 2


class Leave_particle(Sprite):
    def __init__(self, pos, diretorio):
        super().__init__()

        self.x, self.y = pos
        self.scale: float = B_SPRITE_TSCALING + 1

        self.hit_box_algorithm = 'None'
        self.side = randint(0, 1)

        # Add texture
        main_path: str = path.join(
            diretorio, D_SPRITE_LEAVES[randint(0, 4)])

        self.sprite = load_texture_pair(main_path)

        # Set texture
        self.texture = self.sprite[0]

        self.set_position(self.set_pos()[0], self.set_pos()[1])

        # Leaf fall movement
        self.effects()

    def set_pos(self):
        return B_SPRITE_SIZE * self.x + B_SPRITE_SIZE / 2, B_SPRITE_SIZE * self.y + B_SPRITE_SIZE / 2

    def effects(self):
        angle_x = angle_y = 0

        if self.angle >= 360:
            self.angle = 0

        if 90 >= abs(self.angle) <= 180:
            angle_x += 0.4
            angle_y -= 0.2
        elif 90 <= abs(self.angle) >= 180:
            angle_x -= 0.3
            angle_y += 0.15

        self.center_y -= 1 + angle_y
        self.center_x += 0.1 + angle_x

        if self.side == 0:
            self.turn_left(round(uniform(0.5, 2.5), 2))
        elif self.side == 1:
            self.turn_right(round(uniform(0.5, 2.5), 2))
