"""Global constants file"""
from arcade import csscolor

# -----------------------------------#
# /absolute variables of the world\ #
W_ALTURA, W_LARGURA = 700, 400
TELA_CHEIA: tuple[int, int] = W_ALTURA, W_LARGURA
W_TÍTULOS: str = 'FlappyGame...'

W_GRAVIDADE: int = 1500

ARQUIVO: str = 'MyFlappyBird'
# \absolute variables of the world/ #
# -----------------------------------#

# ____________________#
# /global variables\ #

# $ Variáveis do pássaro $ #
# --- B = Bird/Pássaro --- #
B_SPRITE_ISIZE = 13
B_SPRITE_PSCALING = B_SPRITE_TSCALING = 4.0
B_DAMPING = 0.4
B_FRICTION = 1.0
B_MASSA = 1.9
B_JUMP_IMPULSE = 1800
B_MAXH_SPEED = 450
B_MAXV_SPEED = 1200
B_MAXC_ROTAÇÃO, B_MAXB_ROTAÇÃO = -45, 55
B_SPRITE_SIZE = int(B_SPRITE_ISIZE * B_SPRITE_PSCALING)

DEFAULT_DAMPING = 1.0
