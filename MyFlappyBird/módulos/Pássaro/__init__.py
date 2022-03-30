"""Bird class file"""

# & /Imports Bird\ & #
# ------ General defs ------ #
from os import path
from numpy import arange
from arcade import Sprite, load_texture_pair
from arcade import PymunkPhysicsEngine, key
# ------ Game variables ------ #
from variáveis import B_SPRITE_TSCALING, B_JUMP_IMPULSE
from variáveis import B_SET_ANGULO, B_SPRITE_SIZE
from variáveis import B_MAXC_ROTAÇÃO, B_MAXB_ROTAÇÃO
from variáveis import B_FRICTION, B_MASSA, B_ANIMATION_SPEED
from variáveis import B_MAXV_SPEED, B_MAXH_SPEED
# & \Imports Bird/ & #


class Bird(Sprite):
    """ Bird Sprite """

    @classmethod
    def load_text(cls, name: str, main_path: str, amount: int):
        return [load_texture_pair(
            f"{main_path}_{name}{texture}.png") for texture in arange(amount)]

    def __init__(self, pos: tuple[int, int],
                 diretorio: str, game_mode: str):

        """ Init Bird """
        super().__init__()

        self.x, self.y = pos
        self.center_x, self.center_y = self.set_location()

        self.game_mode: str = game_mode
        self.scale = B_SPRITE_TSCALING

        main_path_cor = 'verde', 'vermelho', 'azul'
        main_path: str = path.join(
            diretorio, f'texturas/Animation_bird/{main_path_cor[0]}/Passaro_{main_path_cor[0]}')

        # Conjunto de texturas/Carregando texturas
        self.voando_texturas = self.load_text("voando", main_path, 8)
        self.parado_texturas = self.load_text("parado", main_path, 2)
        # self.ciscando_texturas = self.load_text("ciscando", main_path, 3)

        # Textura_Inicial
        self.texture = self.parado_texturas[0][0]
        self.hit_box = self.texture.hit_box_points

        self.index_texture: int = 0
        self.y_odometer: int = 0
        self.rotação: int = 0
        self.frames_texture: int = 7

        self.jump_init = 0

    def pymunk_moved(self, physics_engine, dx, dy, d_angle):
        """ Handle being moved by the pymunk engine """
        is_on_ground = physics_engine.is_on_ground(self)
        self.y_odometer += dy

        if self.game_mode == 'Tela_Inicial':
            if not is_on_ground and dy > 0.1 and abs(self.y_odometer) > 5:
                self.set_animation_sprites(
                    self.frames_texture, B_ANIMATION_SPEED, self.parado_texturas)
        elif self.game_mode == 'Gameplay':
            if self.jump_init < 1:
                impulse = (0, B_JUMP_IMPULSE)
                physics_engine.apply_impulse(self, impulse)
                self.jump_init += 1

            # Animação de voar
            if not is_on_ground and dy > 0.1 and abs(self.y_odometer) > 5:
                self.set_animation_sprites(
                    self.frames_texture, B_ANIMATION_SPEED, self.voando_texturas)
                self.rotação -= B_SET_ANGULO
            else: self.rotação += B_SET_ANGULO-1

            self.angle = self.rotação  # Define o angulo
            # Não deixa ultrapassar do angulo máximo
            if self.angle <= B_MAXC_ROTAÇÃO: self.rotação = B_MAXC_ROTAÇÃO
            elif self.angle >= B_MAXB_ROTAÇÃO: self.rotação = B_MAXB_ROTAÇÃO

    def set_animation_sprites(self, q_sprite, speed_sprite, sprites):
        self.x_odometer = 0
        self.index_texture = (self.index_texture + speed_sprite) % q_sprite
        self.texture = sprites[int(self.index_texture)][0]

    def set_location(self):
        return B_SPRITE_SIZE * self.x + B_SPRITE_SIZE / 2, B_SPRITE_SIZE * self.y-245 + B_SPRITE_SIZE / 2

    def _update_setmode(self, game_mode):
        self.game_mode: str = game_mode

    def pular(self, chave, física):
        if chave == key.UP or chave == key.SPACE:
            impulse = (0, B_JUMP_IMPULSE)
            física.apply_impulse(self, impulse)

    def set_física(self, física):
        física.add_sprite(self,
                          friction=B_FRICTION,
                          mass=B_MASSA,
                          moment=PymunkPhysicsEngine.MOMENT_INF,
                          max_vertical_velocity=B_MAXV_SPEED,
                          max_horizontal_velocity=B_MAXH_SPEED,
                          collision_type="player")
