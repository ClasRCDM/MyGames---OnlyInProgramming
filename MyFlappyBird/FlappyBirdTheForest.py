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
        self.Modo_jogo: str

        # Scoreboard
        self.Score: list[int, int]
        self.Score_can: bool

        # Pássaro/Bird
        self.pássaro: Optional[arcade.Sprite] = None
        self.pássaro_lista: Optional[arcade.SpriteList] = None
        self.pássaro_pulo: bool

        # Tiled/GUI
        self.backfore = self.GUI = None

        # Physics engine
        self.physics_engine: Optional[arcade.PymunkPhysicsEngine] = None

    # World __ Settings
    def setup(self):
        """ Inicia o jogo. E caso seja chamado o reinicia. """
        self.Modo_jogo: str = 'Tela_Inicial'
        self.pássaro_pulo: bool = True

        # Points score
        self.Score_points: list = [0, 0]
        self.Score_can: bool = True

        # Tile
        self.backfore = Tiled_world(self.diretorio)

        # GUI
        self.GUI = GUI_world(self.Modo_jogo, self.diretorio, self)

        # Grupo/Sprite do pássaro/Bird
        self.pássaro_lista = arcade.SpriteList()
        self.pássaro = Bird((3.5, 6.1), self.diretorio, self.Modo_jogo)

        # --- Pymunk Physics Engine Setup --- #
        damping = DEFAULT_DAMPING
        gravity = (0, -W_GRAVIDADE)

        self.physics_world = arcade.PymunkPhysicsEngine(
            damping=damping, gravity=gravity)
        self.physics_leave = arcade.PymunkPhysicsEngine(
            damping=damping, gravity=(0, -100))

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
            if self.pássaro_pulo and self.Modo_jogo != 'Morte':
                self.pássaro_pulo = False
                self.Modo_jogo = 'Morte'
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
        self.GUI.game_mode = self.Modo_jogo

        if self.pássaro.check_windowpos():
            self.Modo_jogo = 'Morte'
        if self.pássaro.check_windowpos(est=2):
            self.pássaro.kill()

        if self.Modo_jogo == 'Gameplay':
            self.physics_world.step()
            self.backfore.update_movs(self.physics_world)

            self.Score_can = \
                self.GUI.add_score(self.backfore.tile['Obstacles']['layer_collision'],
                                   self.pássaro, self.diretorio,
                                   self.Score_points, self.Score_can)

        elif self.Modo_jogo == 'Morte':
            self.physics_world.step()

            self.backfore.tile['Obstacles']['layer_8'].moving(self.physics_world, (1, 0))
            self.backfore.tile['Obstacles']['layer_9'].moving(self.physics_world, (1, 0))

        self.physics_leave.step()
        # print(arcade.get_fps())  # Get fps

    def on_key_press(self, chave, modifiers):
        """ Chama sempre que uma tecla é pressionada. """

        if self.pássaro_pulo and not self.Modo_jogo == 'Morte':
            self.pássaro.pular(chave, self.physics_world)

        if chave == arcade.key.SPACE and self.Modo_jogo not in 'GameplayMorte':
            self.Modo_jogo = 'Gameplay'

            self.pássaro.game_mode = self.Modo_jogo
            self.pássaro.frames_texture = 7

            self.backfore.append_after_jump()
            self.pássaro_lista.append(self.pássaro.dash_jump)

    # World __ property's
    @property
    def Modo_jogo(self):
        return self._Modo_jogo

    @Modo_jogo.setter
    def Modo_jogo(self, game_mode):
        if isinstance(game_mode, str):
            self._Modo_jogo = game_mode
        else: self._Modo_jogo = 'Tela_Inicial'
