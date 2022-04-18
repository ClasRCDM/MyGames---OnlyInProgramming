"""Class to GUI"""

# & /Imports GUI\ & #
# ------ General defs ------ #
from arcade import SpriteList, Sprite
from arcade import exit as arcade_exit
from arcade.gui import UIFlatButton, UIManager
from arcade.gui import UIBoxLayout, UIAnchorWidget
# ------ Game variables ------ #
# ------ Window modules ------ #
from módulos.GUI.GUI_Objects import *
# & \Imports GUI/ & #


class GUI_world:
    def __init__(self, game_mode, diretorio, window):
        """ Init GUI """

        # --- UI
        self.GUI_manager = UIManager()
        self.GUI_manager.enable()

        self.game_mode = game_mode

        # -- Groups GUI
        # Start Game
        self.GUI_menu, self.GUI_defeat = SpriteList(), SpriteList()
        self.GUI_closets = SpriteList()

        # Create a vertical BoxGroup to align buttons
        self.v_box = UIBoxLayout(vertical=False)

        # -- Sprites, Buttons
        self.GUI_buttons = self.set_buttons()
        self.GUI = self.set_gui(diretorio)

        self.buttons(window)
        # --

    # GUI __ Settings
    def buttons(self, window):
        """ Create buttons Exit/Restart for window """

        self.add_view_buttons(
            window, self.GUI_buttons['exit_buttom'], self.GUI_buttons['restart_button'])

        # Create a widget to hold the v_box widget, that will center the buttons
        self.GUI_manager.add(
            UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="top",
                child=self.v_box)
        )

    def set_buttons(self) -> dict:
        # Create the buttons
        return {'exit_buttom': UIFlatButton(text="Exit", width=70, height=42),
                'restart_button': UIFlatButton(text="Restart", width=120, height=42)}

    def add_view_buttons(self, window, exit, restart):
        """ Add buttions in to viewport lose """

        # Add to viewport buttons
        self.v_box.add(
            exit.with_space_around(right=20, top=241, left=34))
        self.v_box.add(
            restart.with_space_around(right=20, top=241, left=-13.5))

        self.buttons_events(
            exit, restart, window)

    def buttons_events(self, exit, restart, window):
        """ Events and actions to buttons """
        @exit.event("on_click")
        def on_click_exit(event):
            arcade_exit()

        @restart.event("on_click")
        def on_click_restart(event):
            window.setup()

    def set_gui(self, diretorio: str) -> dict:
        """ Create all GUI """

        return {'DERROTA': Defeat((3.6, 11.5), diretorio),
                'MENU_restart': Menu_restart((3.6, 8.26), diretorio),
                'PT_placar': Points_score((0.75, 12.26), diretorio),
                'PT_lose': Scoreboard_menu((7, 9.52), diretorio),
                'PT': Score((1.47, 12.24), diretorio),
                'PT_at1': Score((1.1, 12.45), diretorio, 2.3),
                'PT_at2':  Score((0.92, 12.45), diretorio, 2.3)}

    def append_tiles(self):
        """ Add GUI for screen """

        # -$ Sprite group $-

        # -- Set GUI_loser sprites -- #
        self.GUI_defeat.append(self.GUI['DERROTA'])
        self.GUI_defeat.append(self.GUI['MENU_restart'])
        self.GUI_defeat.append(self.GUI['PT_lose'])

        # -- Set GUI score_points - PT = POINT -- #
        self.GUI_closets.append(self.GUI['PT_placar'])

        self.GUI_closets.append(self.GUI['PT'])
        self.GUI_closets.append(self.GUI['PT_at1'])
        self.GUI_closets.append(self.GUI['PT_at2'])

    def add_score(self, collision: Sprite,
                  bird: Sprite, diretorio: str,
                  add_score: list[int],
                  current_score: bool) -> bool:
        """ Sets and adds the points on the scoreboard """

        if collision.center_x >= bird.center_x and current_score:
            add_score[0] += 1

            if add_score[0] > 9:
                add_score[1] += 1
                self.GUI['PT_at2'].set_sprite_number(
                    diretorio, add_score[1])
                add_score[0] = 0

            self.GUI['PT'].set_sprite_number(
                diretorio, add_score[0])

            return False

        return True if collision.center_x <= bird.center_x else False

    def draw(self):
        """ Draw GUI """
        self.GUI_menu.draw(pixelated=True)

        if self.game_mode == 'Morte':
            self.GUI_manager.draw()
            self.GUI_defeat.draw(pixelated=True)
        elif self.game_mode in 'GameplayTela_Inicial':
            self.GUI_closets.draw(pixelated=True)

    # GUI __ property's
    @property
    def game_mode(self):
        return self._game_mode

    @game_mode.setter
    def game_mode(self, game_mode):
        if isinstance(game_mode, str):
            self._game_mode = game_mode
        else: self._game_mode = 'Tela_Inicial'
