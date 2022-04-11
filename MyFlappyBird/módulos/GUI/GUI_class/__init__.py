"""Class to GUI"""

# & /Imports GUI\ & #
# ------ General defs ------ #
from arcade import SpriteList
from arcade import exit as arcade_exit
from arcade.gui import UIFlatButton, UIManager
from arcade.gui import UIBoxLayout, UIAnchorWidget
# ------ Game variables ------ #
# ------ Window modules ------ #
from módulos.GUI.GUI_Objects import Defeat, Menu_restart
# & \Imports GUI/ & #


class GUI_world:
    def __init__(self, game_mode):
        """ Init GUI """

        # --- UI
        self.GUI_manager = UIManager()
        self.GUI_manager.enable()

        # Sprites
        self.GUI = {}

        self.game_mode = game_mode

        # -- Groups GUI
        # Start Game
        self.GUI_menu, self.GUI_defeat = SpriteList(), SpriteList()

        # Create a vertical BoxGroup to align buttons
        self.v_box = UIBoxLayout(vertical=False)

    def buttons(self, window):
        # Create the buttons
        exit_buttom = UIFlatButton(text="Exit", width=70, height=42)
        restart_button = UIFlatButton(text="Restart", width=120, height=42)

        # Add to viewport buttons
        self.v_box.add(exit_buttom.with_space_around(right=20, top=241, left=34))
        self.v_box.add(restart_button.with_space_around(right=20, top=241, left=-13.5))

        self.buttons_events(exit_buttom, restart_button, window)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.GUI_manager.add(
            UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="top",
                child=self.v_box)
        )

    def buttons_events(self, exit, restart, window):
        @exit.event("on_click")
        def on_click_exit(event):
            arcade_exit()

        @restart.event("on_click")
        def on_click_restart(event):
            window.setup()

    def set_gui(self, diretorio):
        """ Create all GUI """

        self.GUI['DERROTA'] = Defeat((3.6, 11.5), diretorio)
        self.GUI['MENU_restart'] = Menu_restart((3.6, 8.26), diretorio)

    def append_tiles(self):
        """ Add GUI for screen """

        self.GUI_defeat.append(self.GUI['DERROTA'])
        self.GUI_defeat.append(self.GUI['MENU_restart'])

    def draw(self):
        self.GUI_menu.draw(pixelated=True)

        if self.game_mode == 'Morte':
            self.GUI_manager.draw()
            self.GUI_defeat.draw(pixelated=True)

    def _game_mode(self, game_mode):
        self.game_mode = game_mode
