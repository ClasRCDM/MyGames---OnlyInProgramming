"""Global constants file"""

# -----------------------------------#
# /absolute variables of the world\ #
W_ALTURA, W_LARGURA = 700, 400
TELA_CHEIA: tuple[int, int] = W_ALTURA, W_LARGURA
W_TÍTULOS: str = 'FlappyGame...'

W_GRAVIDADE: int = 1500

ARQUIVO: str = 'MyFlappyBird'
ARQUIVO_BACKGROUND: str = 'texturas/background/background'
# \absolute variables of the world/ #
# -----------------------------------#

# ____________________#
# /global variables\ #

# $ Variáveis do pássaro $ #
# --- B = Bird/Pássaro --- #
B_SPRITE_ISIZE: int = 13
B_SPRITE_PSCALING = B_SPRITE_TSCALING = 4.0
B_DAMPING: float = 0.4
B_FRICTION: float = 1.0
B_MASSA: float = 1.9
B_JUMP_IMPULSE: int = 1800
B_MAXH_SPEED: int = 450
B_MAXV_SPEED: int = 1200
B_MAXC_ROTAÇÃO, B_MAXB_ROTAÇÃO = -45, 45
B_ANIMATION_SPEED: float = 0.35
B_SET_ANGULO: int = 6
B_SPRITE_SIZE = int(B_SPRITE_ISIZE * B_SPRITE_PSCALING)

DEFAULT_DAMPING: float = 1.0

# $ Background variables $ #
# --- F = Fundo/Background --- #
F_SPRITE_ISIZE: int = 1
F_SPRITE_PSCALING = F_SPRITE_TSCALING = 3.9
F_SPRITE_SIZE = int(B_SPRITE_ISIZE * B_SPRITE_PSCALING)

# $ Forest Background Variables $ #
# --- PF = Parallax Forest --- #
PF_MAX_HORIZONTAL: int = 1100
PF_PONTO_DE_VOLTA: int = -1395
