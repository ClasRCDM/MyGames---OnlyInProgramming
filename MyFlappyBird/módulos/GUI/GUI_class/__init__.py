"""Class to GUI"""

# & /Imports GUI\ & #
# ------ General defs ------ #
from arcade import SpriteList
# ------ Game variables ------ #
# ------ Window modules ------ #
# & \Imports GUI/ & #


class GUI_world:
    def __init__(self):
        """ Init GUI """

        # Sprites
        self.GUI = {}

        # -- Groups GUI
        # Start Game
        self.GUI_menu = SpriteList()

    def set_gui(self, diretorio):
        """ Create all GUI """

        pass

    def append_tiles(self):
        """ Add GUI for screen """

        pass

    def draw(self):
        self.GUI_menu.draw(pixelated=True)
