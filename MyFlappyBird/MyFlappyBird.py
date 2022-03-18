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
from módulos.FundoFrente import BackgroundForeground
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
        """ Main function """
        janela = Jogo()
        janela.setup()
        arcade.run()

    def __init__(self):
        super().__init__(W_LARGURA, W_ALTURA, W_TÍTULOS)
        # arcade.enable_timings()  # habilitar quando for ver o fps

        # Janela
        arcade.set_background_color(arcade.csscolor.BLACK)
        self.center_window()

        # Pássaro
        self.pássaro: Optional[arcade.Sprite] = None
        self.pássaro_lista: Optional[arcade.SpriteList] = None

        # Fundo
        self.backfore = None

        # Physics engine
        self.physics_engine: Optional[arcade.PymunkPhysicsEngine] = None

        self.pulo = True

    def setup(self):
        """Inicia o jogo. E caso seja chamado o reinicia."""

        # Grupo/Sprite do pássaro/Bird
        self.pássaro_lista = arcade.SpriteList()
        self.pássaro = Bird(3.5, 6, self.diretorio)

        # Grupo/Sprite do pássaro/Bird
        self.backfore = BackgroundForeground()
        self.backfore.set_tiles(self.diretorio)

        # Adiciona os sprites nos grupos
        self.pássaro_lista.append(self.pássaro)

        self.backfore.append_tiles()

        # --- Pymunk Physics Engine Setup --- #
        damping = DEFAULT_DAMPING
        gravity = (0, -W_GRAVIDADE)

        self.physics_engine = self.pássaro.created_física(damping, gravity)
        self.pássaro.set_física(self.physics_engine)

        self.backfore.set_physics(self.physics_engine)

        def wall_collid(sprite, _wall_sprite, _arbiter, _space, _data):
            """ Called for Player/Wall collision """
            self.pulo = False

        self.physics_engine.add_collision_handler("player", "wall", post_handler=wall_collid)

    def on_draw(self):
        """Renderisa tudo que a na tela."""

        self.clear()

        self.backfore.draw()
        self.pássaro_lista.draw(pixelated=True)

    def on_update(self, delta_time):
        """Movimentos e lógicas do jogo."""
        self.physics_engine.step()

        self.backfore.update_movs(self.physics_engine)

        # print(arcade.get_fps())  # Get fps

    def on_key_press(self, chave, modifiers):
        """Chama sempre que uma tecla é pressionada."""

        if self.pulo: self.pássaro.pular(chave, self.physics_engine)
