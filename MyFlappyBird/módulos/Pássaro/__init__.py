"""Bird class file"""

# & /Imports Bird\ & #
# ------ General defs ------ #
import arcade
from os import path
# ------ Game variables ------ #
from variáveis import B_SPRITE_TSCALING, B_JUMP_IMPULSE
from variáveis import B_SET_ANGULO, B_SPRITE_SIZE
from variáveis import B_MAXC_ROTAÇÃO, B_MAXB_ROTAÇÃO
from variáveis import B_FRICTION, B_MASSA, B_ANIMATION_SPEED
from variáveis import B_MAXV_SPEED, B_MAXH_SPEED
# & \Imports Bird/ & #


class Bird(arcade.Sprite):
    """ Bird Sprite """
    def __init__(self, x, y, diretorio):
        """ Init Bird """
        super().__init__()

        self.x, self.y = x, y
        self.scale: float = B_SPRITE_TSCALING

        main_path_cor = 'verde', 'vermelho', 'azul'
        main_path: str = path.join(diretorio, f'texturas/Animation_bird/{main_path_cor[0]}/Passaro_{main_path_cor[0]}')

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
            self.set_animation_sprites(7, B_ANIMATION_SPEED)
            self.rotação -= B_SET_ANGULO
        else: self.rotação += B_SET_ANGULO-1

        self.angle = self.rotação  # Define o angulo
        # Não deixa ultrapassar do angulo máximo
        if self.angle <= B_MAXC_ROTAÇÃO: self.rotação = B_MAXC_ROTAÇÃO
        elif self.angle >= B_MAXB_ROTAÇÃO: self.rotação = B_MAXB_ROTAÇÃO

    def set_animation_sprites(self, q_sprite, speed_sprite):
        self.x_odometer = 0
        self.index_texture = (self.index_texture + speed_sprite) % q_sprite
        self.texture = self.voando_texturas[int(self.index_texture)][0]

    def set_bird_location(self):
        self.center_x = B_SPRITE_SIZE * self.x + B_SPRITE_SIZE / 2
        self.center_y = B_SPRITE_SIZE * self.y + B_SPRITE_SIZE / 2

    def created_física(self, damping, gravity):
        return arcade.PymunkPhysicsEngine(damping=damping, gravity=gravity)

    def set_física(self, física):
        física.add_sprite(self,
                          friction=B_FRICTION,
                          mass=B_MASSA,
                          moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                          max_vertical_velocity=B_MAXV_SPEED,
                          max_horizontal_velocity=B_MAXH_SPEED,
                          collision_type="player")

    def pular(self, chave, física):
        if chave == arcade.key.UP or chave == arcade.key.SPACE:
            impulse = (0, B_JUMP_IMPULSE)
            física.apply_impulse(self, impulse)
