import numpy as np
import random
import math
import matplotlib.pyplot as plt
import time
from utils import *
from individual import *

x = np.arange(-1, 2.0, 0.01)
f = weird_function(x)

# plotStartFunction(x, f)

st = [-1, 2]
allels_num = 12

st = [-1, 2]
# array = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1])[::-1]
# ind = Individual(evaluationFunction=weird_function,allels_num=allels_num)
# print(ind.decodeIndividual(st))
# print(ind.fitnessValue(st))
popsize = 10
maxgen = 10
initialPopulation = []
for i in range(popsize):
    ind = Individual(weird_function,allels_num)
    initialPopulation.append(ind)

lmb = lambda ind: ind.fitnessValue(st)
initialValues = list(map(lmb,initialPopulation))
initialDecodedings = list(map(lambda ind: ind.decodeIndividual(st),initialPopulation))

line, = plt.plot(x, f, lw=2)
plt.plot(initialDecodedings,initialValues,'ro')
plt.xlim(-1, 2)
plt.show()




