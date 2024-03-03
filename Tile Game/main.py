# Inicializa o pygame
import pygame
from pygame.locals import *

# Importa o botão customizado
from levels.scripts.design import pyButton

# Importa o nível 1
from levels.level_1 import Level_1

# Importa todos os scripts dentro de levels.scripts
from levels.scripts import *

# Inicializa o pygame
pygame.init()

# Cria uma tela de 800x600
screen = pygame.display.set_mode((800, 600))

# Cria uma área de 200x150
display = pygame.Surface((200, 150)).convert()

# Posição do display
display_rect = display.get_rect()

# Posiciona o display no canto superior esquerdo da tela
display_rect.topleft = (0, 0)

# Comand para iniciar o Level_1
def Play_Level_1():
    Level_1(display, screen)

# Cria o botão com as seguintes características:
# - display: área de 200x150
# - posição: centro do display
# - cor quando o mouse está sobre o botão: (200, 200, 200)
# - texto: "Play"
# - comando: Play_Level_1
# - tamanho: 100, 50
play_button = pyButton(display, pos=display_rect.center, hover_color=(200, 200, 200), text="Play", command= Play_Level_1, size=(100, 50))

# Loop principal
while True:

    # Define a cor de fundo da tela como (80, 90, 100)
    screen.fill((80, 90, 100))

    # Renderiza o display na tela
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

    # Define a cor de fundo do display como (80, 90, 100)
    display.fill((80, 90, 100))

    # Loop de eventos:
    for event in pygame.event.get():
        # Verifica se o usuário pressionou a tecla Esc ou fechou a janela
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            # Encerra o programa
            quit()

        # Verifica se o usuário clicou no botão
        play_button.check_for_click(event)

    # Renderiza o botão
    play_button.render()

    # Atualiza a tela
    pygame.display.update()
