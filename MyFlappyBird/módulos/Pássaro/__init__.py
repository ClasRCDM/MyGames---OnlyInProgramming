import arcade
from typing import Optional
from os import path  # Get files
# ------ Game variables ------ #
import variáveis as v


class Bird(arcade.Sprite):
    """ Bird Sprite """
    def __init__(self, x, y, diretorio):
        """ Init """
        super().__init__()

        self.x, self.y = x, y

        # Set our scale
        self.scale: float = v.B_SPRITE_TSCALING

        main_path = path.join(diretorio, 'texturas/Animation_bird/Verde/Passaro_verde')

        # Conjunto de texturas/Carregando texturas
        self.voando_texturas = [arcade.load_texture_pair(
            f"{main_path}_voando{texture}.png") for texture in range(8)]
        self.parado_texturas = [arcade.load_texture_pair(
            f"{main_path}_voando{texture}.png") for texture in range(2)]
        self.ciscando_texturas = [arcade.load_texture_pair(
            f"{main_path}_voando{texture}.png") for texture in range(3)]

        # Textura_Inicial
        self.texture = self.parado_texturas[0][0]
        self.hit_box = self.texture.hit_box_points

        self.index_texture: int = 0
        self.y_odometer: int = 0
        self.rotação: int = 0

        self.set_bird_location()

    def pymunk_moved(self, physics_engine, dx, dy, d_angle):
        """ Handle being moved by the pymunk engine """
        is_on_ground = physics_engine.is_on_ground(self)
        self.y_odometer += dy

        # Animação de voar
        if not is_on_ground and dy > 0.1 and abs(self.y_odometer) > 5:
            self.x_odometer = 0
            self.index_texture += 0.35
            if self.index_texture > 7: self.index_texture = 0
            self.texture = self.voando_texturas[int(self.index_texture)][0]
            self.rotação -= 6
        else:
            self.rotação += 5

        self.angle = self.rotação
        if self.angle <= v.B_MAXC_ROTAÇÃO:
            self.rotação = v.B_MAXC_ROTAÇÃO
        elif self.angle >= v.B_MAXB_ROTAÇÃO:
            self.rotação = v.B_MAXB_ROTAÇÃO

    def set_bird_location(self):
        self.center_x = v.B_SPRITE_SIZE * self.x + v.B_SPRITE_SIZE / 2
        self.center_y = v.B_SPRITE_SIZE * self.y + v.B_SPRITE_SIZE / 2

    def created_física(self, damping, gravity):
        return arcade.PymunkPhysicsEngine(damping=damping, gravity=gravity)

    def set_física(self, física):
        física.add_sprite(self,
                          friction=v.B_FRICTION,
                          mass=v.B_MASSA,
                          moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                          max_vertical_velocity=v.B_MAXV_SPEED,
                          max_horizontal_velocity=v.B_MAXH_SPEED,
                          collision_type="player")

    def pular(self, chave, física):
        if chave == arcade.key.UP or chave == arcade.key.SPACE:
            impulse = (0, v.B_JUMP_IMPULSE)
            física.apply_impulse(self, impulse)
