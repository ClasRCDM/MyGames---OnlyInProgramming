"""Main program file"""

# & /Imports World\ & #
# ------ General defs ------ #
import arcade
# ------ Game variables ------ #
import variáveis as v
# ------ Window modules ------ #
# & \Imports World/ & #


########################
# Configuring my World #
########################

class Jogo(arcade.Window):
    """
    Main application class.
    """

    @classmethod
    def main(cls):
        """ Main function """
        janela = Jogo()
        janela.setup()
        arcade.run()

    def __init__(self):
        super().__init__(v.LARGURA, v.ALTURA, v.TÍTULOS)

        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        self.clear()
