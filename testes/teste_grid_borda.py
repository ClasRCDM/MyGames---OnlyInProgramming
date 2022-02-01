from pygame import init, display, time, event, draw, QUIT
from numpy import arange


def grid(janela, comprimento, tamanho_linha, tamanho_quadrado):
    def draw_grid(v):
        draw.line(janela, (255, 255, 255),
                  (v * tamanho_quadrado, 0),
                  (v * tamanho_quadrado, comprimento))
        draw.line(janela, (255, 255, 255),
                  (0, v * tamanho_quadrado),
                  (comprimento, v * tamanho_quadrado))

    # Iniciando o grid
    for x_c in arange(comprimento // tamanho_linha):
        draw_grid(x_c)


def borda(janela, comprimento, tamanho, cor=(0, 0, 0), espaçamento=0, p_borda=12):
    def borda_vertical(lado='esquerdo'):
        for y in arange(comprimento // tamanho):
            draw.line(janela, cor,
                      (y if lado == 'esquerdo' else y+comprimento-p_borda,
                       espaçamento),
                      (y if lado == 'esquerdo' else y+comprimento-p_borda,
                       comprimento))

    def borda_horizontal(lado='cima'):
        for x in arange(comprimento // tamanho):
            draw.line(janela, cor,
                      (espaçamento,
                       x if lado == 'cima' else x+comprimento-p_borda),
                      (comprimento,
                       x if lado == 'cima' else x+comprimento-p_borda))

    # -------------------------- Bordas
    borda_vertical(lado='esquerdo')
    borda_vertical(lado='direita')
    borda_horizontal(lado='cima')
    borda_horizontal(lado='baixo')


# ------------------ Programa
init()

tela_cheia = 600, 600

janela = display.set_mode(tela_cheia)
janela.fill((0, 0, 0))
display.set_caption('Testes de grid')

FPS = 60
Fps = time.Clock()


def teste_grid(game):
    while 1:
        for evento in event.get():
            if evento.type == QUIT:
                game = False

        grid(janela, 400, 42, 50)
        borda(janela, 600, 30, (80, 80, 80), 0, 20)

        display.flip()
        Fps.tick(FPS)

        if not game:
            break
