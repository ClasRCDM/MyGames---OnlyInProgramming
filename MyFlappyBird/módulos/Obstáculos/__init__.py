# & /Imports Obstacles\ & #
# ------ General defs ------ #
import arcade
from os import path
from random import randint
# ------ Game variables ------ #
from variáveis import O_SPRITE_SIZE, O_SPRITE_TSCALING
from variáveis import ARQUIVO_OBSTACLES, O_MAX_HORIZONTAL
# & \Imports Obstacles/ & #


class Obstacles:
    def __init__(self, x, y,
                 diretorio, index,
                 image):
        """ Init Background """

        self.x, self.y = x, y

        main_path: str = path.join(diretorio, ARQUIVO_OBSTACLES)

        # Conjunto de texturas/Carregando texturas
        self.tronco_baixo = arcade.Sprite(
            f"{main_path}{image}_{index}.png", hit_box_algorithm='Simple')
        self.tronco_cima = arcade.Sprite(
            f"{main_path}{image}_{index}.png",
            hit_box_algorithm='Simple', flipped_vertically=True)

        self.set_size()

    def set_location(self):
        """ Set position background """
        y_rand = randint(-150, 220)
        self.tronco_baixo.center_x = O_SPRITE_SIZE * self.x + O_SPRITE_SIZE / 2
        self.tronco_baixo.center_y = O_SPRITE_SIZE * self.y+y_rand + O_SPRITE_SIZE / 2
        self.tronco_cima.center_x = O_SPRITE_SIZE * self.x + O_SPRITE_SIZE / 2
        self.tronco_cima.center_y = O_SPRITE_SIZE * self.y+640+y_rand + O_SPRITE_SIZE / 2

    def set_scaling(self):
        """ Set scale background """
        self.tronco_baixo.scale = self.tronco_cima.scale = O_SPRITE_TSCALING

    def set_size(self):
        self.set_location()
        self.set_scaling()

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

    def colisão(self):
        print('a')

    def moving(self, física):
        self.loop_movimento(física)

        física.set_velocity(self.tronco_baixo, (100, 0))
        física.set_velocity(self.tronco_cima, (100, 0))

        self.tronco_baixo.angle = self.tronco_cima.angle = 0
