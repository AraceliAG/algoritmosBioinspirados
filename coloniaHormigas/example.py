import numpy as np

from antColony import ColoniaDeHormigas  

distancias = np.array([[np.inf, 2, 2, 5, 7],
                       [2, np.inf, 4, 8, 2],
                       [2, 4, np.inf, 1, 3],
                       [5, 8, 1, np.inf, 2],
                       [7, 2, 3, 2, np.inf]])

colonia_hormigas = ColoniaDeHormigas(distancias, 1, 1, 100, 0.95, alfa=1, beta=1)
camino_mas_corto = colonia_hormigas.ejecutar()
print("camino_mas_corto: {}".format(camino_mas_corto))
