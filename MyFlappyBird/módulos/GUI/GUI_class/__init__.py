"""Class to GUI"""

# & /Imports GUI\ & #
# ------ General defs ------ #
from arcade import SpriteList
from arcade import exit as arcade_exit
from arcade.gui import UIFlatButton, UIManager
from arcade.gui import UIBoxLayout, UIAnchorWidget
# ------ Game variables ------ #
# ------ Window modules ------ #
from módulos.GUI.GUI_Objects import *
# & \Imports GUI/ & #


class GUI_world:
    def __init__(self, game_mode):
        """ Init GUI """

        # --- UI
        self.GUI_manager = UIManager()
        self.GUI_manager.enable()

        # -- Sprites, Buttons
        self.GUI, self.GUI_buttons = {}, {}

        self.game_mode = game_mode

        # -- Groups GUI
        # Start Game
        self.GUI_menu, self.GUI_defeat = SpriteList(), SpriteList()
        self.GUI_closets = SpriteList()

        # Create a vertical BoxGroup to align buttons
        self.v_box = UIBoxLayout(vertical=False)

    def buttons(self, window):
        # Create the buttons
        self.GUI_buttons['exit_buttom'] = UIFlatButton(text="Exit", width=70, height=42)
        self.GUI_buttons['restart_button'] = UIFlatButton(text="Restart", width=120, height=42)

        self.add_view_buttons(window, self.GUI_buttons['exit_buttom'], self.GUI_buttons['restart_button'])

        # Create a widget to hold the v_box widget, that will center the buttons
        self.GUI_manager.add(
            UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="top",
                child=self.v_box)
        )

    def add_view_buttons(self, window, exit, restart):
        # Add to viewport buttons
        self.v_box.add(
            exit.with_space_around(right=20, top=241, left=34))
        self.v_box.add(
            restart.with_space_around(right=20, top=241, left=-13.5))

        self.buttons_events(
            exit, restart, window)

    def buttons_events(self, exit, restart, window):
        @exit.event("on_click")
        def on_click_exit(event):
            arcade_exit()

        @restart.event("on_click")
        def on_click_restart(event):
            window.setup()

    def set_gui(self, diretorio, window):
        """ Create all GUI """

        self.GUI['DERROTA'] = Defeat((3.6, 11.5), diretorio)
        self.GUI['MENU_restart'] = Menu_restart((3.6, 8.26), diretorio)

        self.GUI['PT_placar'] = Points_score((0.75, 12.26), diretorio)
        self.GUI['PT'] = Score((1.47, 12.24), diretorio)
        self.GUI['PT_at1'] = Score((1.1, 12.45), diretorio, 2.3)
        self.GUI['PT_at2'] = Score((0.92, 12.45), diretorio, 2.3)

        self.buttons(window)

    def append_tiles(self):
        """ Add GUI for screen """

        self.GUI_defeat.append(self.GUI['DERROTA'])
        self.GUI_defeat.append(self.GUI['MENU_restart'])

        self.GUI_closets.append(self.GUI['PT_placar'])
        self.GUI_closets.append(self.GUI['PT'])
        self.GUI_closets.append(self.GUI['PT_at1'])
        self.GUI_closets.append(self.GUI['PT_at2'])

    def draw(self):
        self.GUI_menu.draw(pixelated=True)
        self.GUI_closets.draw(pixelated=True)

        if self.game_mode == 'Morte':
            self.GUI_manager.draw()
            self.GUI_defeat.draw(pixelated=True)

    def _game_mode(self, game_mode):
        self.game_mode = game_mode
