"""Main program file"""

# & /Imports World\ & #
# ------ General defs ------ #
import arcade
from typing import Optional
from os import path, getcwd  # Get files
# ------ Game variables ------ #
import variáveis as v
# ------ Window modules ------ #
from módulos.Pássaro import Bird
# & \Imports World/ & #


########################
# Configuring my World #
########################

class Jogo(arcade.Window):
    """
    Main application class.
    """

    diretorio: str = path.join(getcwd(), v.ARQUIVO)

    @classmethod
    def main(cls):
        """ Main function """
        janela = Jogo()
        janela.setup()
        arcade.run()

    def __init__(self):
        super().__init__(v.W_LARGURA, v.W_ALTURA, v.W_TÍTULOS)

        # Janela
        arcade.set_background_color(arcade.csscolor.BLACK)
        self.center_window()

        # Pássaro
        self.pássaro: Optional[arcade.Sprite] = None

        # Physics engine
        self.physics_engine: Optional[arcade.PymunkPhysicsEngine] = None

    def setup(self):
        """Inicia o jogo. E caso seja chamado o reinicia."""

        # Grupo do pássaro
        self.pássaro_lista = arcade.SpriteList()

        # Bird/Pássaro
        self.pássaro = Bird(3.5, 6, self.diretorio)

        # Adiciona o sprite do pássaro no grupo
        self.pássaro_lista.append(self.pássaro)

        # --- Pymunk Physics Engine Setup ---
        damping = v.DEFAULT_DAMPING
        gravity = (0, -v.W_GRAVIDADE)

        self.physics_engine = self.pássaro.created_física(damping, gravity)
        self.pássaro.set_física(self.physics_engine)

    def on_draw(self):
        """Renderisa tudo que a na tela."""

        self.clear()

        self.pássaro_lista.draw(pixelated=True)

    def on_update(self, delta_time):
        """Movimentos e lógicas do jogo."""
        self.physics_engine.step()

    def on_key_press(self, chave, modifiers):
        """Chama sempre que uma tecla é pressionada."""

        self.pássaro.pular(chave, self.physics_engine)
