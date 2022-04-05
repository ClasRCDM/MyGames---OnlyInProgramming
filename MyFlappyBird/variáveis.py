"""Global constants file"""

# -----------------------------------#
# /absolute variables of the world\ #
W_ALTURA, W_LARGURA = 700, 400
TELA_CHEIA: tuple[int, int] = W_ALTURA, W_LARGURA
W_TÍTULOS: str = 'FlappyGame: The Forest'

W_GRAVIDADE: int | float = 1500

ARQUIVO: str = 'MyFlappyBird'
TEXTURAS = lambda a: f'texturas/{a}/'

DEFAULT_DAMPING: float = 1.0
# \absolute variables of the world/ #
# -----------------------------------#

# ____________________#
# /global variables\ #

# $ Variáveis do pássaro $ #
# --- B = Bird/Pássaro --- #
B_SPRITE_ISIZE: int | float = 13
B_SPRITE_PSCALING = B_SPRITE_TSCALING = 3.9
B_DAMPING: float | int = 0.4
B_FRICTION: float | int = 1.0
B_MASSA: float | int = 1.96
B_JUMP_IMPULSE: int | float = 1400
B_MAXH_SPEED: int | float = 450
B_MAXV_SPEED: int | float = 1200
B_MAXC_ROTAÇÃO, B_MAXB_ROTAÇÃO = -45, 45
B_ANIMATION_SPEED, B_SET_ANGULO = 0.35, 6
B_SPRITE_SIZE = int(B_SPRITE_ISIZE * B_SPRITE_PSCALING)

# $ Background variables $ #
# --- F = Fundo/Background --- #
F_SPRITE_ISIZE: int | float = 13
F_SPRITE_PSCALING = F_SPRITE_TSCALING = 4.0
F_SPRITE_SIZE = int(F_SPRITE_ISIZE * F_SPRITE_PSCALING)

# $ Forest Background Variables $ #
# --- PF = Parallax Forest --- #
PF_MAX_HORIZONTAL: float | int = 1100
PF_PONTO_DE_VOLTA: float | int = -1459
ARQUIVO_BACKGROUND: str = TEXTURAS('background') + 'background'
PF_SEQUENCIA_SPRITES = 3, 4, 2, 5, 1
PF_SEQUENCIA_SSPEED = 2, 0.8, 0.3, 0.3, 1.2

# $ Obstacles Foreground Variables $ #
# --- O = Obstacles --- #
O_SPRITE_ISIZE: int | float = 1
O_SPRITE_PSCALING = O_SPRITE_TSCALING = 3.5
O_SPRITE_SIZE = int(O_SPRITE_ISIZE * O_SPRITE_PSCALING)
ARQUIVO_OBSTACLES: str = TEXTURAS('obstacles')
O_MAX_HORIZONTAL: int | float = 600

# $ Water Variables $ #
# --- WA = Water --- #
WA_ARQUIVO = TEXTURAS('background') + 'effect_water.png'

# $ Variables decorations $ #
# --- D = Decorations --- #
D_SPRITE_ROCK: str = TEXTURAS('decorations') + 'Pedra_grande.png'
D_SPRITE_LEAVES = [TEXTURAS('decorations') + f'Leaves/Leave_{num}.png' for num in range(5)]
D_LEAVES_POS = [(7, 11), (4, 12), (2, 13.5), (0, 11), (6.5, 13)]
