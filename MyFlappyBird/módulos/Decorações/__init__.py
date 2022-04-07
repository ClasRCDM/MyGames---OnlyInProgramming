"""Class to decorate"""

# & /Imports decorations\ & #
# ------ General defs ------ #
from os import path
from random import randint, uniform
from arcade import Sprite, load_texture_pair
# ------ Game variables ------ #
from variáveis import B_SPRITE_TSCALING, B_SPRITE_SIZE
from variáveis import D_SPRITE_ROCK, EL_SPRITE_LEAVES
# & \Imports decorations/ & #


class Big_rock(Sprite):
    """ Sprite Big rock """

    def __init__(self, pos, diretorio):
        """ Setup Rock """
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

    def set_pos(self) -> int | float:
        """ Set location """

        return B_SPRITE_SIZE * self.x + B_SPRITE_SIZE / 2, B_SPRITE_SIZE * self.y + B_SPRITE_SIZE / 2

    def move(self, vel):
        if self.center_x <= 500:
            self.center_x += vel


class Leave_particle(Sprite):
    """ Leaves """

    def __init__(self, pos, diretorio, física):
        """ Starting sheets """
        super().__init__()

        self.x, self.y = pos
        self.scale: float = B_SPRITE_TSCALING + 1
        self.result_angle = 0

        self.hit_box_algorithm = 'None'
        self.side = randint(0, 1)

        self.speed_x = self.speed_y = randint(0, 2)
        self.play_speed = 0

        # Add texture
        main_path: str = path.join(
            diretorio, EL_SPRITE_LEAVES[randint(0, 4)])

        self.sprite = load_texture_pair(main_path)

        # Set texture
        self.texture = self.sprite[0]

        self.set_position(self.set_pos()[0], self.set_pos()[1])
        self.set_física(física)

    def random_pos(self):
        self.speed_x = self.speed_y = randint(0, 2)
        self.set_position(self.set_pos()[0], self.set_pos()[1])

    def pymunk_moved(self, physics_engine, dx, dy, d_angle):
        """ Handle being moved by the pymunk engine """

        # Leaf fall movement
        self.effects(physics_engine, d_angle)

        if self.center_x >= 400 or self.center_y <= 0:
            self.kill()

    def set_física(self, física):
        física.add_sprite(self,
                          mass=2,
                          max_vertical_velocity=450,
                          max_horizontal_velocity=450,
                          collision_type='item')

    def set_pos(self) -> int | float:
        """ Set location """

        return B_SPRITE_SIZE * self.x + B_SPRITE_SIZE / 2, B_SPRITE_SIZE * self.y + B_SPRITE_SIZE / 2

    def effects(self, phy, angle):
        """ Leaf fall movements """

        if self.side == 0:
            self.result_angle += round(uniform(0.5, 2.5), 2)
        elif self.side == 1:
            self.result_angle -= round(uniform(0.5, 2.5), 2)

        self.angle = self.result_angle

        phy.apply_impulse(self, (self.speed_x + self.play_speed,
                                 self.speed_y))
