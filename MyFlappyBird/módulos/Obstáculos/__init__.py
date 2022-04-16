"""Obstacles class file"""

# & /Imports Obstacles\ & #
# ------ General defs ------ #
import arcade
from random import randint
# ------ Game variables ------ #
from variáveis import O_SPRITE_SIZE, O_SPRITE_TSCALING, O_BOXCOLLISION
from variáveis import ARQUIVO_OBSTACLES, O_MAX_HORIZONTAL
from variáveis import B_SPRITE_TSCALING, B_SPRITE_SIZE
# ------ Window modules ------ #
from módulos.Objeto import Object, Object_sprite
# & \Imports Obstacles/ & #


class Obstacles(Object):
    def __init__(self, x, y,
                 diretorio, index,
                 image):
        """ Init Background """
        super().__init__(diretorio, ARQUIVO_OBSTACLES)

        self.x, self.y = x, y
        self.image, self.index = image, index

        # Conjunto de texturas/Carregando texturas
        self.tronco_baixo = arcade.Sprite(
            f"{self.main_path}{self.image}_{self.index}.png",
            hit_box_algorithm='Simple')
        self.tronco_cima = arcade.Sprite(
            f"{self.main_path}{self.image}_{self.index}.png",
            hit_box_algorithm='Simple', flipped_vertically=True)

        self.set_size()

    def set_size(self):
        y_rand = randint(-150, 220)

        self.set_location(self.tronco_baixo, O_SPRITE_SIZE,
                          (O_SPRITE_SIZE * self.x + O_SPRITE_SIZE / 2,
                           O_SPRITE_SIZE * self.y+y_rand + O_SPRITE_SIZE / 2), v_pro=True)
        self.set_location(self.tronco_cima, O_SPRITE_SIZE,
                          (O_SPRITE_SIZE * self.x + O_SPRITE_SIZE / 2,
                           O_SPRITE_SIZE * self.y+640+y_rand + O_SPRITE_SIZE / 2), v_pro=True)

        self.set_scaling(self.tronco_baixo, O_SPRITE_TSCALING)
        self.set_scaling(self.tronco_cima, O_SPRITE_TSCALING)

    def return_sprite(self, tronco):
        """ return background sprite """
        return tronco

    def loop_movimento(self, física):
        y_rand, x_rand = randint(-150, 220), randint(-200, -100)

        self.set_move(x_rand, 0, y_rand, self.tronco_baixo, física)
        self.set_move(x_rand, 650, y_rand, self.tronco_cima, física)

    def set_move(self, x, y, m, tronco, física):
        if tronco._get_center_x() >= O_MAX_HORIZONTAL:
            física.set_position(
                tronco, (x, int(O_SPRITE_SIZE * self.y+m+y + O_SPRITE_SIZE / 2)))

    def moving(self, física, vel):
        self.loop_movimento(física)

        física.set_velocity(self.tronco_baixo, (vel[0], vel[1]))
        física.set_velocity(self.tronco_cima, (vel[0], vel[1]))

        self.tronco_baixo.angle = self.tronco_cima.angle = 0


class Box_collision(Object_sprite):
    def __init__(self, pos, diretorio):
        super().__init__(pos[0], pos[1])

        self.scale: float = B_SPRITE_TSCALING

        # Add texture
        self.set_sprite(self.sprite_loc(diretorio, O_BOXCOLLISION))

        self.set_pos(B_SPRITE_SIZE)

    def move(self, x, y):
        self.set_position(x, y)
