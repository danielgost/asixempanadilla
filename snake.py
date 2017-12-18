import pygame
from pygame.locals import*
import sys
import mapa
import time

pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake DaniG")
mapa = mapa.mapa()

selecciondemenu = 0
pantalla = 0
orientacion = 0
comida = (200, 200)



while True:
    if pantalla == 0:
        mapa.fondo()
        mapa.menu(selecciondemenu)

    elif pantalla == 1:
        mapa.fondo()
        comida = mapa.snake(orientacion, comida)
        mapa.comida(comida)
        pass

    elif pantalla == 2:
        mapa.fondo()
        mapa.creditos()
        pass

    for evento in pygame.event.get():

        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            pass

        elif evento.type == KEYDOWN:
            if pantalla == 0:
                if evento.key == pygame.K_DOWN:
                    if selecciondemenu < 1:
                        selecciondemenu = selecciondemenu + 1
                    else:
                        selecciondemenu = 0

                elif evento.key == pygame.K_UP:
                    if selecciondemenu > 0:
                        selecciondemenu = selecciondemenu - 1
                    else:
                        selecciondemenu = 1

                elif evento.key == pygame.K_SPACE:
                    if selecciondemenu == 0:
                        pantalla = 1

                    elif selecciondemenu == 1:
                        pantalla = 2

            elif pantalla == 1:
                if evento.key == pygame.K_DOWN and orientacion != 90:
                    orientacion = 270

                elif evento.key == pygame.K_UP and orientacion != 270:
                    orientacion = 90

                elif evento.key == pygame.K_LEFT and orientacion != 0:
                    orientacion = 180

                elif evento.key == pygame.K_RIGHT and orientacion != 180:
                    orientacion = 0

                elif evento.key == pygame.K_SPACE:
                    pantalla = 0

            elif pantalla == 2:
                if evento.key == pygame.K_SPACE:
                    pantalla = 0

    pygame.display.update()
    time.sleep(0.05)



