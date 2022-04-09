"""Main program file"""

# & /Imports World\ & #
# ------ General defs ------ #
import arcade
from typing import Optional
from os import path, getcwd
# ------ Game variables ------ #
from variáveis import ARQUIVO
from variáveis import W_LARGURA, W_ALTURA, W_TÍTULOS
from variáveis import DEFAULT_DAMPING, W_GRAVIDADE
# ------ Window modules ------ #
from módulos.Pássaro import Bird
from módulos.FundoFrente import Tiled_world
from módulos.GUI.GUI_class import GUI_world
# & \Imports World/ & #


########################
# Configuring my World #
########################

class Jogo(arcade.Window):
    """
    Main application class.
    """

    diretorio: str = path.join(getcwd(), ARQUIVO)

    @classmethod
    def main(cls):
        """ Create window """
        janela = Jogo()
        janela.setup()
        arcade.run()

    def __init__(self):
        """ Main function """
        super().__init__(W_LARGURA, W_ALTURA, W_TÍTULOS)
        # arcade.enable_timings()  # habilitar quando for ver o fps

        # Janela/Windows
        arcade.set_background_color(arcade.csscolor.BLACK)
        self.center_window()

        # Game
        self.Modo_jogo: str = 'Tela_Inicial'

        # Pássaro/Bird
        self.pássaro: Optional[arcade.Sprite] = None
        self.pássaro_lista: Optional[arcade.SpriteList] = None
        self.pássaro_pulo: bool = True

        # Tiled/GUI
        self.backfore = self.GUI = None

        # Physics engine
        self.physics_engine: Optional[arcade.PymunkPhysicsEngine] = None

    def setup(self):
        """ Inicia o jogo. E caso seja chamado o reinicia. """

        # Tile
        self.backfore = Tiled_world()
        self.backfore.set_tiles(self.diretorio)

        # GUi
        self.GUI = GUI_world()
        self.GUI.set_gui(self.diretorio)

        # Grupo/Sprite do pássaro/Bird
        self.pássaro_lista = arcade.SpriteList()
        self.pássaro = Bird((3.5, 6.1), self.diretorio, self.Modo_jogo)

        # --- Pymunk Physics Engine Setup --- #
        damping = DEFAULT_DAMPING
        gravity = (0, -W_GRAVIDADE)

        self.physics_world = arcade.PymunkPhysicsEngine(damping=damping, gravity=gravity)
        self.physics_leave = arcade.PymunkPhysicsEngine(damping=damping, gravity=(0, -100))

        # == Add Sprites
        # - Backgrounds_
        self.backfore.append_tiles(self.diretorio, self.physics_leave)
        # -- Bird_
        self.pássaro_lista.append(self.pássaro)
        # --- GUI_
        self.GUI.append_tiles()

        # %__ Physics __$ #
        self.pássaro.set_física(self.physics_world)  # For Bird
        self.backfore.set_física(self.physics_world)  # For Obstacles

        # %__ Physics/Collision response to obstacle __$ #
        def wall_collid(sprite, _wall_sprite, _arbiter, _space, _data):
            """ Called for Player/Wall collision """
            self.pássaro_pulo = False
        # Add response physics
        self.physics_world.add_collision_handler(
            "player", "wall", post_handler=wall_collid)

    def on_draw(self):
        """Renderisa tudo que a na tela."""

        self.clear()

        self.backfore.draw()
        self.GUI.draw()

        self.pássaro_lista.draw(pixelated=True)

    def on_update(self, delta_time):
        """ Movimentos e lógicas do jogo. """

        self.pássaro.update()

        if self.Modo_jogo == 'Gameplay':
            self.physics_world.step()
            self.backfore.update_movs(self.physics_world)

        self.physics_leave.step()
        # print(arcade.get_fps())  # Get fps

    def on_key_press(self, chave, modifiers):
        """ Chama sempre que uma tecla é pressionada. """

        if self.pássaro_pulo: self.pássaro.pular(chave, self.physics_world)

        if chave == arcade.key.SPACE and self.Modo_jogo != 'Gameplay':
            self.Modo_jogo = 'Gameplay'

            self.pássaro._update_setmode(self.Modo_jogo)
            self.pássaro.frames_texture = 7

            self.pássaro_lista.append(self.pássaro.dash_jump)
