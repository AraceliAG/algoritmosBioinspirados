import random

# FUNCION PARA CALCULAR LA AFINIDAD
def calcular_afinidad(anticuerpo, antigeno):
    # LA AFINIDAD ES SIMPLEMENTE EL NÚMERO DE CARACTERES COINCIDENTES
    return sum(1 for a, b in zip(anticuerpo, antigeno) if a == b)

# FUNCION PARA MUTAR UN ANTICUERPO
def mutar(anticuerpo, tasa_mutacion=0.1):
    nuevo_anticuerpo = ""
    for gen in anticuerpo:
        if random.random() < tasa_mutacion:
            # CAMBIAR EL GEN POR OTRO CARACTER ALEATORIO
            nuevo_anticuerpo += chr(random.randint(65, 90))  # LETRAS MAYÚSCULAS A-Z
        else:
            nuevo_anticuerpo += gen
    return nuevo_anticuerpo

# GENERAR POBLACIÓN INICIAL DE ANTICUERPOS
def generar_poblacion(tamano_poblacion, tamano_anticuerpo):
    poblacion = []
    for _ in range(tamano_poblacion):
        anticuerpo = ''.join(chr(random.randint(65, 90)) for _ in range(tamano_anticuerpo))
        poblacion.append(anticuerpo)
    return poblacion

# ALGORITMO PRINCIPAL AIS
def ais(antigeno, tamano_poblacion=100, iteraciones=1000, tasa_mutacion=0.1):
    # GENERAR POBLACIÓN INICIAL
    poblacion = generar_poblacion(tamano_poblacion, len(antigeno))
    mejor_afinidad = 0
    mejor_anticuerpo = None

    for _ in range(iteraciones):
        # EVALUAR AFINIDAD
        afinidades = [calcular_afinidad(anticuerpo, antigeno) for anticuerpo in poblacion]

        # SELECCIONAR EL MEJOR ANTICUERPO
        indice_mejor = afinidades.index(max(afinidades))
        if afinidades[indice_mejor] > mejor_afinidad:
            mejor_afinidad = afinidades[indice_mejor]
            mejor_anticuerpo = poblacion[indice_mejor]

        # MUTAR LA POBLACIÓN
        poblacion = [mutar(anticuerpo, tasa_mutacion) for anticuerpo in poblacion]

    return mejor_anticuerpo, mejor_afinidad

# EJEMPLO DE USO
antigeno = "HELLO"
mejor_anticuerpo, mejor_afinidad = ais(antigeno)
print(f"MEJOR ANTICUERPO: {mejor_anticuerpo}, AFINIDAD: {mejor_afinidad}")
