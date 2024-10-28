import random

poblacion = []
requisito_objetivo = 255
porcentajeMutacion = 10 #rango de 1 a 100

def genes() :
    individuo = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), 2]
    return individuo

def funcionObjetivo(candidato) :
    global requisito_objetivo
    contador = 0    
    a = 0
    for x in range(len(candidato) - 2, -1, -1) :
        contador += 2**a * candidato[x]
        a += 1
    
    contador = contador / requisito_objetivo
    if contador > 1 : 
        contador -= contador * 2 + 1
    candidato[len(candidato) - 1] = contador
    

def ordenarPoblacion() :
    global poblacion
    poblacion.sort(key=lambda poblacion : poblacion[len(poblacion) - 1], reverse=True)
    
def poblacionIncial(star_population) :
    global poblacion
    for i in range(star_population) :
        poblacion.append(genes())
        
def seleccion() :
    global poblacion
    i = 0
    while i < len(poblacion):
        candidato = poblacion[i]
        if not (candidato[len(candidato) - 1] != 2) :
            funcionObjetivo(poblacion[i])
        i += 1
    
    ordenarPoblacion()

    x = int(len(poblacion) * 0.75 - 1)
    while x < len(poblacion) -1 and len(poblacion) > 2 :
        poblacion.pop(x)            
    
def cruza() :
    global poblacion
    pointConvert = random.randint(2, 5)
    limite = len(poblacion) - 1
    
    i = 0
    while i < limite  and len(poblacion) > 1:
        hijo = [0, 0, 0, 0, 0, 0, 0, 0, 2]
        nuevoCandidato = []
        padre = poblacion[i]
        madre = poblacion[i + 1]
        
        padreOmadre = random.randint(False, True)
        for x in range(0, len(hijo) - 1) :
            if padreOmadre and x < pointConvert :
                hijo[x] = madre[x]
            elif not padreOmadre and x < pointConvert:
                hijo[x] = padre[x]
            elif x >= pointConvert and not padreOmadre:
                hijo[x] = madre[x]
            else :
                hijo[x] = padre[x]
                
        #print("punto" + str(pointConvert))
        #print("padre: " + str(padre), "madre: " + str(madre), sep="\n")
        #print(hijo)
        mutacion(hijo)
        poblacion.append(hijo)
        i += 2
    ordenarPoblacion()

def mutacion(candidatoNuevo) :
    global porcentajeMutacion
    for i in range(0, len(candidatoNuevo) - 1) :
        p = random.uniform(0 , 1)
        if p < porcentajeMutacion/100 :
            candidatoNuevo[i] = random.randint(0, 1)
        funcionObjetivo(candidatoNuevo)
        
def algoritmoGenetico(star_population, generaciones) :
    global poblacion
    poblacionIncial(star_population)
    
    i = 0
    while i < generaciones :
        seleccion()
        print(poblacion[0])
        cruza()
        print("generacion " + str(i) + ", total P: " + str(len(poblacion)) + ": ", poblacion[0], sep="\n")
        i += 1

if __name__ == '__main__' :
    print("\t\tAlgoritmo Genetico", end="\n")
    algoritmoGenetico(int(input("Ingresa el numero de poblacion total: ")), int(input("Ingresa el numero de generaciones: ")))