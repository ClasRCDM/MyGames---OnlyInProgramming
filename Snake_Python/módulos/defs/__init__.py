from pygame import draw
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


def borda(janela, comprimento, tamanho,
          cor=(0, 0, 0), espaçamento=0, p_borda=12):
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
