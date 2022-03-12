"""Parallax program file"""

# & /Imports Parallax\ & #
# ------ General defs ------ #
import arcade
# ------ Game variables ------ #
# -
# ------ Window modules ------ #
# -
# & \Imports Parallax/ & #


class Water:
    def __init__(self, x, y, altura, largura):
        self.x, self.y = x, y

        self.altura, self.largura = altura, largura

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y,
                                     self.largura, self.altura,
                                     arcade.csscolor.AQUA)
        arcade.draw_rectangle_filled(self.x, self.y+30,
                                     self.largura, 5,
                                     arcade.csscolor.LIGHT_CYAN)
