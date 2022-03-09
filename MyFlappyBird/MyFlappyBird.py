"""Main program file"""

# & /Imports World\ & #
# ------ General defs ------ #
import arcade
from typing import Optional
from os import path, getcwd  # Get files
# ------ Game variables ------ #
from variáveis import ARQUIVO
from variáveis import W_LARGURA, W_ALTURA, W_TÍTULOS
from variáveis import DEFAULT_DAMPING, W_GRAVIDADE
# ------ Window modules ------ #
from módulos.Pássaro import Bird
from módulos.Parallax import Parallax
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

        # Janela
        arcade.set_background_color(arcade.csscolor.BLACK)
        self.center_window()

        # Pássaro
        self.pássaro: Optional[arcade.Sprite] = None
        self.pássaro_lista: Optional[arcade.SpriteList] = None

        # Fundo
        self.fundo = None
        self.fundo_lista: Optional[arcade.SpriteList] = None

        # Physics engine
        self.physics_engine: Optional[arcade.PymunkPhysicsEngine] = None

    def setup(self):
        """Inicia o jogo. E caso seja chamado o reinicia."""

        # Grupo/Sprite do pássaro/Bird
        self.pássaro_lista = arcade.SpriteList()
        self.pássaro = Bird(3.5, 6, self.diretorio)

        # Grupo/Sprite do pássaro/Bird
        self.fundo_lista = arcade.SpriteList()
        self.fundo = Parallax(3.5, 6.2, self.diretorio)

        # Adiciona os sprites nos grupos
        self.pássaro_lista.append(self.pássaro)
        [self.fundo_lista.append(self.fundo._return(index)) for index in range(3)]

        # --- Pymunk Physics Engine Setup ---
        damping = DEFAULT_DAMPING
        gravity = (0, -W_GRAVIDADE)

        self.physics_engine = self.pássaro.created_física(damping, gravity)
        self.pássaro.set_física(self.physics_engine)

    def on_draw(self):
        """Renderisa tudo que a na tela."""

        self.clear()

        self.fundo_lista.draw(pixelated=True)
        self.pássaro_lista.draw(pixelated=True)

    def on_update(self, delta_time):
        """Movimentos e lógicas do jogo."""
        self.physics_engine.step()

    def on_key_press(self, chave, modifiers):
        """Chama sempre que uma tecla é pressionada."""

        self.pássaro.pular(chave, self.physics_engine)
