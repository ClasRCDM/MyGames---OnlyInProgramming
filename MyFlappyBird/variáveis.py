"""Global constants file"""

# -----------------------------------#
# /absolute variables of the world\ #
W_ALTURA, W_LARGURA = 700, 400
TELA_CHEIA: tuple[int, int] = W_ALTURA, W_LARGURA
W_TÍTULOS: str = 'FlappyGame: The Forest'

W_GRAVIDADE: int = 1500

ARQUIVO: str = 'MyFlappyBird'
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
B_MASSA: float = 1.96
B_JUMP_IMPULSE: int = 1800
B_MAXH_SPEED: int = 450
B_MAXV_SPEED: int = 1200
B_MAXC_ROTAÇÃO, B_MAXB_ROTAÇÃO = -45, 45
B_ANIMATION_SPEED, B_SET_ANGULO = 0.35, 6
B_SPRITE_SIZE = int(B_SPRITE_ISIZE * B_SPRITE_PSCALING)

DEFAULT_DAMPING: float = 1.0

# $ Background variables $ #
# --- F = Fundo/Background --- #
F_SPRITE_ISIZE: int = 13
F_SPRITE_PSCALING = F_SPRITE_TSCALING = 4.0
F_SPRITE_SIZE = int(F_SPRITE_ISIZE * F_SPRITE_PSCALING)

# $ Forest Background Variables $ #
# --- PF = Parallax Forest --- #
PF_MAX_HORIZONTAL: float = 1100
PF_PONTO_DE_VOLTA: float = -1459
ARQUIVO_BACKGROUND: str = 'texturas/background/background'
PF_SEQUENCIA_SPRITES = 3, 4, 2, 5, 1
PF_SEQUENCIA_SSPEED = 2, 0.8, 0.3, 0.3, 1.2

# $ Obstacles Foreground Variables $ #
# --- O = Obstacles --- #
O_SPRITE_ISIZE: int = 1
O_SPRITE_PSCALING = O_SPRITE_TSCALING = 3.5
O_SPRITE_SIZE = int(O_SPRITE_ISIZE * O_SPRITE_PSCALING)
ARQUIVO_OBSTACLES: str = 'texturas/obstacles/'
O_MAX_HORIZONTAL: int = 600
