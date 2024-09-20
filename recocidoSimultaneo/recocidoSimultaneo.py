import numpy as np
import csv
import random
import math
import time
import matplotlib.pyplot as plt

startTime = time.time()
dataset = csv.reader(open('recocidoSimultaneo/berlin52.csv', 'r'),delimiter='\t')
x=list(dataset)
size = len(x)
matriz=np.array(x).astype('float')
initialTemp = 8
finalTemp = 0.1
factor = 0.999
iterations = 5

initialRoute = []
for i in range(len(matriz)+1):
	if i == 0: continue
	initialRoute.append(i)

np.random.seed(666)
np.random.shuffle(initialRoute)

def dist(route):
    cost =  matriz[route[0]-1][route[len(route)-1]-1]
    iterator=1
    while iterator < size:
        cost += matriz[route[iterator-1]-1][route[iterator]-1]
        iterator += 1
    return cost

betterRoute = initialRoute[:]
optimalDist = dist(betterRoute)

currentDists = []
optimalDists = []

x = []
y = []
step = 0
for iteracion in range(iterations):
	temp = initialTemp
	currentRoute = betterRoute[:]
	currentDist = optimalDist
	newDist = optimalDist
	newRoute = betterRoute[:]
	

	while temp > finalTemp:
		index = np.random.random_integers(len(newRoute)-2, size=(1,2))
		#index = random.sample(range(len(newRoute) - 1), 2)
		index = [index.item(0), index.item(1)]
		index[0] += 1
		index[1] += 1		
		beforeExchange = dist(newRoute)
		newRoute[index[0]], newRoute[index[1]] = newRoute[index[1]], newRoute[index[0]]
		afterExchange = dist(newRoute)			
					
		newDist = newDist - beforeExchange + afterExchange
		
		e = newDist - currentDist
		
		if e < 0 or  math.exp( -e / temp ) > np.random.rand():
			currentRoute = newRoute[:]
			currentDist = newDist
		else:
			newDist = currentDist
			newRoute = currentRoute[:]
			
		if currentDist < optimalDist:
			betterRoute = currentRoute[:]
			optimalDist = currentDist
			
		if True:
			currentDists.append(currentDist)
			optimalDists.append(optimalDist)
		
		temp = temp * factor
		step = step + 1
		x.append(step)
		y.append(dist(currentRoute))
	
initialDist = dist(initialRoute)
finalDist = dist(currentRoute)
endTime = time.time()


print ("\t\t\tRoute: ")
print(currentRoute)
print ("\n")
print ("Initial distance: {0}".format(initialDist))
print ("Final distance: {0}".format(finalDist))
mr = 100 * (initialDist - finalDist) / initialDist
print ("Performance improvement: {0} %".format(mr))
print ("Time: {0} seg".format(endTime-startTime))
print ("Number of iterations: {0}".format(step)) 
plt.figure("Simulated annealing algorithm")
plt.plot(x,y)
plt.xlabel("Iterations")
plt.ylabel("Costs")
plt.show()