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
from variáveis import PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA
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
        # arcade.enable_timings() habilitar quando for ver o fps

        # Janela
        arcade.set_background_color(arcade.csscolor.BLACK)
        self.center_window()

        # Pássaro
        self.pássaro: Optional[arcade.Sprite] = None
        self.pássaro_lista: Optional[arcade.SpriteList] = None

        # Fundo
        self.fundo = {}
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

        self.fundo['layer_1'] = Parallax(
            3.5, 6.4, self.diretorio, 2, 'floresta',
            PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA)
        self.fundo['layer_2'] = Parallax(
            3.5, 6, self.diretorio, 1, 'floresta',
            PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA)
        self.fundo['layer_3'] = Parallax(
            3.5, 6.7, self.diretorio, 0, 'floresta',
            PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA)
        self.fundo['layer_4'] = Parallax(
            2.5, 15, self.diretorio, 0, 'Lights',
            PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA)
        self.fundo['layer_5'] = Parallax(
            15, 16.5, self.diretorio, 1, 'Lights',
            PF_MAX_HORIZONTAL, PF_PONTO_DE_VOLTA)

        # Adiciona os sprites nos grupos
        #self.pássaro_lista.append(self.pássaro)

        [self.fundo_lista.append(self.fundo['layer_3']._return(
            index, self.fundo['layer_3'].layer)) for index in range(2)]
        [self.fundo_lista.append(self.fundo['layer_4']._return(
            index, self.fundo['layer_4'].layer)) for index in range(2)]
        [self.fundo_lista.append(self.fundo['layer_2']._return(
            index, self.fundo['layer_2'].layer)) for index in range(2)]
        [self.fundo_lista.append(self.fundo['layer_5']._return(
            index, self.fundo['layer_5'].layer)) for index in range(2)]
        [self.fundo_lista.append(self.fundo['layer_1']._return(
            index, self.fundo['layer_1'].layer)) for index in range(2)]

        # --- Pymunk Physics Engine Setup --- #
        damping = DEFAULT_DAMPING
        gravity = (0, -W_GRAVIDADE)

        self.physics_engine = self.pássaro.created_física(damping, gravity)
        self.pássaro.set_física(self.physics_engine)

    def on_draw(self):
        """Renderisa tudo que a na tela."""

        self.clear()

        self.fundo_lista.draw(pixelated=True)
        #self.pássaro_lista.draw(pixelated=True)

    def on_update(self, delta_time):
        """Movimentos e lógicas do jogo."""
        self.physics_engine.step()

        self.fundo['layer_1'].update(self.fundo['layer_1'].layer, 2)
        self.fundo['layer_2'].update(self.fundo['layer_2'].layer, 0.8)
        self.fundo['layer_3'].update(self.fundo['layer_3'].layer, 0.3)
        self.fundo['layer_4'].update(self.fundo['layer_4'].layer, 0.3)
        self.fundo['layer_5'].update(self.fundo['layer_5'].layer, 1.2)

        # print(arcade.get_fps()) Get fps

    def on_key_press(self, chave, modifiers):
        """Chama sempre que uma tecla é pressionada."""

        self.pássaro.pular(chave, self.physics_engine)
