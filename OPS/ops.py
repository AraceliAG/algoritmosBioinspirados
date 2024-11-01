import random

# DEFINIR UNA CLASE PARA REPRESENTAR UNA PARTÍCULA
class Particula:
    def __init__(self, limites):
        self.posicion = [random.uniform(lim[0], lim[1]) for lim in limites]
        self.velocidad = [0.0 for _ in limites]
        self.mejor_posicion = list(self.posicion)
        self.mejor_valor = float('inf')

# FUNCIÓN DE OPTIMIZACIÓN
def objetivo(x):
    return sum([xi**2 for xi in x])  # EJEMPLO: FUNCION ESFERICA

# ACTUALIZAR LA VELOCIDAD Y POSICIÓN DE LA PARTÍCULA
def actualizar(particula, mejor_global, w, c1, c2):
    for i in range(len(particula.posicion)):
        r1, r2 = random.random(), random.random()
        particula.velocidad[i] = (w * particula.velocidad[i] +
                                  c1 * r1 * (particula.mejor_posicion[i] - particula.posicion[i]) +
                                  c2 * r2 * (mejor_global[i] - particula.posicion[i]))
        particula.posicion[i] += particula.velocidad[i]

# ALGORITMO PRINCIPAL PSO
def pso(limites, num_particulas=30, iteraciones=100, w=0.5, c1=1.0, c2=2.0):
    particulas = [Particula(limites) for _ in range(num_particulas)]
    mejor_global = list(particulas[0].posicion)
    mejor_valor_global = float('inf')

    for _ in range(iteraciones):
        for particula in particulas:
            valor = objetivo(particula.posicion)
            if valor < particula.mejor_valor:
                particula.mejor_valor = valor
                particula.mejor_posicion = list(particula.posicion)
            if valor < mejor_valor_global:
                mejor_valor_global = valor
                mejor_global = list(particula.posicion)

        for particula in particulas:
            actualizar(particula, mejor_global, w, c1, c2)

    return mejor_global, mejor_valor_global

# EJEMPLO DE USO
limites = [(-10, 10), (-10, 10)]  # LIMITES PARA CADA DIMENSIÓN
mejor_pos, mejor_val = pso(limites)
print(f"MEJOR POSICIÓN: {mejor_pos}, MEJOR VALOR: {mejor_val}")
