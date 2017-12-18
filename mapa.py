import pygame
import random

pygame.init()


ventana = pygame.display.set_mode((800, 600))
fondo = (50,100,50)
serpiente = (0,20,0)
seleccionado = (20,40,20)
colorcomida = (153, 0, 0)

Fuente = pygame.font.Font("pcsenior.ttf", 40)
Fuente2 = pygame.font.Font("pcsenior.ttf", 25)
Fuente3 = pygame.font.Font("pcsenior.ttf", 15)


titulo = Fuente.render("Snake DG", True, serpiente)
jugar = Fuente2.render("Jugar", True, serpiente)
hechopor = Fuente2.render("Creditos", True, serpiente)
seleccionaropcion = Fuente3.render("Espacio para Seleccionar Opcion", True, serpiente)
salirpantalla1 = Fuente3.render("Espacio para Salir a Seleccion de Opcion", True, serpiente)
creditos = Fuente.render("Hecho por", True, serpiente)
creditos2 = Fuente2.render ("Daniel Gost Ribas", True, serpiente)

posicion = [(80,80), (80,100), (80,120)]
comida = (300, 300)

class mapa(object):
    def __init__(self):
        pass

    def fondo(self):
        ventana.fill(fondo)

    def menu(self, seleccion):

        if seleccion == 0:
            pygame.draw.rect(ventana, seleccionado, (110,190,160,50))
        if seleccion == 1:
            pygame.draw.rect(ventana, seleccionado, (110,240,240,50))

        ventana.blit(titulo,(170,100))
        ventana.blit(jugar,(120,200))
        ventana.blit(hechopor,(120,250))
        ventana.blit(seleccionaropcion,(70,450))
        pass

    def creditos(self):
        ventana.blit(creditos,(140,250))
        ventana.blit(creditos2,(160,300))
        pass

    def snake(self, orientacion, comida):
        for i in posicion:
            pygame.draw.rect(ventana, serpiente, (i[0] +1, i[1] +1, 18, 18))

            if posicion.index(i) == len(posicion)-1:
                if orientacion == 0:
                    posicion.append((i[0]+20 , i[1]))

                elif orientacion == 90:
                    posicion.append((i[0], i[1]-20))

                elif orientacion == 180:
                    posicion.append((i[0]-20 , i[1]))

                elif orientacion == 270:
                    posicion.append((i[0] , i[1]+20))

                ventana.blit(salirpantalla1,(90,570))

                if i != comida:
                    del posicion[0]
                    return comida

                else:
                    return (random.randint(0,39)*20, random.randint(0,29)*20)
                break



    def comida(self, comida):
        pygame.draw.rect(ventana, colorcomida, (comida[0], comida[1], 18, 18))
