"""Object class file"""

# & /Imports Background\ & #
# ------ General defs ------ #
from os import path
from typing import Union
from arcade import Sprite
# & \Imports Background/ & #


class Object:
    """ Object """

    def __init__(self,
                 diretorio, arquivo,
                 x: Union[int, float] = None,
                 y: Union[int, float] = None,
                 index: int = None,
                 image: str = None):
        """ Create """

        self.DIRETORIO = diretorio
        self.ARQUIVO = arquivo

        self.x = x if x is not None else 0
        self.y = y if y is not None else 0

        self.index = index if index is not None else 0
        self.image = image if image is not None else 'image'

        self.main_path: str = path.join(self.DIRETORIO, self.ARQUIVO)

    def set_location(self, background: Sprite,
                     sprite_size: int,
                     pos: tuple[int, int] = (0, 0),
                     v_pro: bool = False):
        """ Adding positions """

        if not v_pro:
            background.center_x = sprite_size * pos[0] + sprite_size / 2
            background.center_y = sprite_size * pos[1] + sprite_size / 2
        elif v_pro:
            background.center_x = pos[0]
            background.center_y = pos[1]

    def set_scaling(self, background: Sprite, sprite_scaling: float):
        """ adding scales """

        background.scale = sprite_scaling
