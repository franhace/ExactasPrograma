import pygame
import time

import numpy as np

# pred_presa = __import__('05-solucion-predador_presa')
pred_presa = __import__('predpresa')
# para instalar pygame:
# python3 -m pip install -U pygame --user

# visual = __import__('05-solucion_visual')

SCREEN_RES = (600, 600)
margin = 25
# pygame.init()
# pygame.display.set_mode(SCREEN_RES)

sprites_group = pygame.sprite.LayeredDirty()
celdas = {}

vacia = pygame.image.load("img/pasto.png")
antilope = pygame.image.load("img/antilope.png")
leon = pygame.image.load("img/leon.png")


class Cell(pygame.sprite.DirtySprite):

    def __init__(self, row=2, col=2, board_size=(3, 3)):
        pygame.sprite.DirtySprite.__init__(self)

        self.row = row - 1
        self.col = col - 1
        self.board_size = board_size

        w = (SCREEN_RES[0] - margin * 2) // board_size[0]
        h = (SCREEN_RES[1] - margin * 2) // board_size[1]

        side = min(w, h)
        x = int(margin + self.col * side + side * 0.5)
        y = int(margin + self.row * side + side * 0.5)
        side_cell = int(side * 0.9)

        self.vacia = pygame.transform.smoothscale(
            vacia, (side_cell, side_cell))
        self.antilope = pygame.transform.smoothscale(
            antilope, (side_cell, side_cell))
        self.leon = pygame.transform.smoothscale(
            leon, (side_cell, side_cell))

        self.image = self.vacia
        self.rect = self.image.get_rect()

        self.rect.center = (x, y)
        # print("Adding cell in ({},{}) for ".format(x,y))
        self.dirty = 1

    def change_to(self, target=" "):
        if target == " ":
            self.image = self.vacia
        elif target == "A":
            self.image = self.antilope
        elif target == "L":
            self.image = self.leon
        self.dirty = 1


def actualizar_tablero(tablero, celdas):
    for i in range(tablero.shape[0]-2):
        for j in range(tablero.shape[1]-2):
            celdas[(i+1, j+1)].change_to(tablero[(i+1, j+1)])

    screen = pygame.display.get_surface()
    sprites_group.draw(screen)
    pygame.display.flip()


def crear_mundo(x, y, antilopes, leones):
    t = pred_presa.generar_tablero_azar(x, y, antilopes, leones)
    sprites_group.remove_sprites_of_layer(1)
    for c in list(celdas.keys()):
        del celdas[c]

    for i in range(t.shape[0]-2):
        for j in range(t.shape[1]-2):
            celdas[(i+1, j+1)] = Cell(i+1, j+1, (x, y))
            sprites_group.add(celdas[(i+1, j+1)], layer=1)

    return t

# screen = pygame.display.get_surface()
#
# sprites_group.draw(screen)
# pygame.display.flip()


i = 0
def evolucionar(tablero):

    global i
    if i % 3 == 0:
        print("== Turno", i // 3, "==")
        print("   Fase alimentacion")
        pred_presa.fase_alimentacion(tablero)
    elif i % 3 == 1:
        print("   Fase reproduccion")
        pred_presa.fase_reproduccion(tablero)
    else:
        print("   Fase mover")
        pred_presa.fase_mover(tablero)

    # actualizar_tablero(tablero, celdas)
    # print(i)
    i = i + 1


def simular(x, y, antilopes, leones, tiempos):
    global i
    pygame.init()
    i = 0
    if pygame.display.get_surface() is None:
        pygame.display.set_mode(SCREEN_RES)

    _t = crear_mundo(x, y, antilopes, leones)
    actualizar_tablero(_t, celdas)

    time.sleep(2)
    for _ in range(tiempos * 3):
        evolucionar(_t)
        actualizar_tablero(_t, celdas)
        time.sleep(0.5)

    input("Press Enter to continue...")
    # screen = pygame.display.get_surface()
    # sprites_group.remove_sprites_of_layer(1)
    # sprites_group.draw(screen)
    # pygame.display.flip()
    pygame.quit()
