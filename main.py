import numpy as np
import random
import math
import matplotlib.pyplot as plt
import time
from utils import *
from individual import *
from population import Population


def get_mating_pool(popsize,dens):
    mating_pool =[]
    for i in range(popsize):
        rand = random.random()
        try:
            selected = next(x for x in dens if x[0] > rand)[1]
        except:
            debug =5
        mating_pool.append(selected)
    return mating_pool


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
current_population = []
for i in range(popsize):
    ind = Individual(weird_function,allels_num)
    current_population.append(ind)



lmb = lambda ind: ind.fitnessValue(st)
initialValues = list(map(lmb, current_population))
initialDecodedings = list(map(lambda ind: ind.decodeIndividual(st), current_population))

line, = plt.plot(x, f, lw=2)
plt.plot(initialDecodedings,initialValues,'ro')
plt.xlim(-1, 2)
plt.show()

pop_fitness= Population().whole_pop_fitness(current_population, st)
test = sum(list(map(lambda ind: ind.relativeFitness(pop_fitness, st), current_population)))
print(test)
assert math.fabs(test -1) <= 1e-5, "probability must sum to one!"

for interarorek in range(maxgen):
    if not current_population or len(current_population) <10:
        debug = 5
    dens = Population().get_pop_fitness_density(current_population,st)
    mating_pool = get_mating_pool(popsize,dens)
    random.shuffle(mating_pool)
    current_population = Population().breed_population(mating_pool,allels_num, weird_function)

newDecodings = list(map(lambda ind: ind.decodeIndividual(st), current_population))
newValues = list(map(lmb, current_population))

line, = plt.plot(x, f, lw=2)
plt.plot(newDecodings,newValues,'ro')
plt.xlim(-1, 2)
plt.show()





