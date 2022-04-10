"""Class to GUI"""

# & /Imports GUI\ & #
# ------ General defs ------ #
from arcade import SpriteList
# ------ Game variables ------ #
# ------ Window modules ------ #
from módulos.GUI.GUI_Objects import Defeat
# & \Imports GUI/ & #


class GUI_world:
    def __init__(self, game_mode):
        """ Init GUI """

        # Sprites
        self.GUI = {}

        self.game_mode = game_mode

        # -- Groups GUI
        # Start Game
        self.GUI_menu, self.GUI_defeat = SpriteList(), SpriteList()

    def set_gui(self, diretorio):
        """ Create all GUI """

        self.GUI['DERROTA'] = Defeat((3.6, 11.5), diretorio)

    def append_tiles(self):
        """ Add GUI for screen """

        self.GUI_defeat.append(self.GUI['DERROTA'])

    def draw(self):
        self.GUI_menu.draw(pixelated=True)

        if self.game_mode == 'Morte':
            self.GUI_defeat.draw(pixelated=True)

    def _game_mode(self, game_mode):
        self.game_mode = game_mode
