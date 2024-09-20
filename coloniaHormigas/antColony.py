import random as rn
import numpy as np
from numpy.random import choice as np_choice

class ColoniaDeHormigas(object):

    def __init__(self, distancias, n_hormigas, n_mejores, n_iteraciones, decaimiento, alfa=1, beta=1):
        """
        Args:
            distancias (2D numpy.array): Matriz cuadrada de distancias. Se asume que la diagonal es np.inf.
            n_hormigas (int): Número de hormigas por iteración
            n_mejores (int): Número de mejores hormigas que depositan feromonas
            n_iteraciones (int): Número de iteraciones
            decaimiento (float): Tasa a la que las feromonas decaen. El valor de feromonas se multiplica por el decaimiento, por lo que 0.95 llevará a un decaimiento lento, y 0.5 a un decaimiento mucho más rápido.
            alfa (int o float): Exponente sobre la feromona, un alfa más alto da más peso a la feromona. Default=1
            beta (int o float): Exponente sobre la distancia, un beta más alto da más peso a la distancia. Default=1

        Ejemplo:
            colonia_hormigas = ColoniaDeHormigas(distancias_alemanas, 100, 20, 2000, 0.95, alfa=1, beta=2)
        """
        self.distancias = distancias
        self.feromona = np.ones(self.distancias.shape) / len(distancias)
        self.todos_indices = range(len(distancias))
        self.n_hormigas = n_hormigas
        self.n_mejores = n_mejores
        self.n_iteraciones = n_iteraciones
        self.decaimiento = decaimiento
        self.alfa = alfa
        self.beta = beta

    def ejecutar(self):
        camino_mas_corto = None
        mejor_camino_de_todos_los_tiempos = ("placeholder", np.inf)
        for i in range(self.n_iteraciones):
            todos_caminos = self.generar_todos_los_caminos()
            self.esparcir_feromonas(todos_caminos, self.n_mejores, camino_mas_corto=camino_mas_corto)
            camino_mas_corto = min(todos_caminos, key=lambda x: x[1])
            print(camino_mas_corto)
            if camino_mas_corto[1] < mejor_camino_de_todos_los_tiempos[1]:
                mejor_camino_de_todos_los_tiempos = camino_mas_corto
            self.feromona = self.feromona * self.decaimiento
        return mejor_camino_de_todos_los_tiempos

    def esparcir_feromonas(self, todos_caminos, n_mejores, camino_mas_corto):
        caminos_ordenados = sorted(todos_caminos, key=lambda x: x[1])
        for camino, dist in caminos_ordenados[:n_mejores]:
            for movimiento in camino:
                self.feromona[movimiento] += 1.0 / self.distancias[movimiento]

    def generar_distancia_de_camino(self, camino):
        distancia_total = 0
        for ele in camino:
            distancia_total += self.distancias[ele]
        return distancia_total

    def generar_todos_los_caminos(self):
        todos_caminos = []
        for i in range(self.n_hormigas):
            camino = self.generar_camino(0)
            todos_caminos.append((camino, self.generar_distancia_de_camino(camino)))
        return todos_caminos

    def generar_camino(self, inicio):
        camino = []
        visitados = set()
        visitados.add(inicio)
        previo = inicio
        for i in range(len(self.distancias) - 1):
            movimiento = self.elegir_movimiento(self.feromona[previo], self.distancias[previo], visitados)
            camino.append((previo, movimiento))
            previo = movimiento
            visitados.add(movimiento)
        camino.append((previo, inicio))  # volver al punto de inicio    
        return camino

    def elegir_movimiento(self, feromona, dist, visitados):
        feromona = np.copy(feromona)
        feromona[list(visitados)] = 0

        fila = feromona ** self.alfa * ((1.0 / dist) ** self.beta)

        fila_normalizada = fila / fila.sum()
        movimiento = np_choice(self.todos_indices, 1, p=fila_normalizada)[0]
        return movimiento
