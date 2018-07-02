import numpy as np
import random
import math
import matplotlib.pyplot as plt
import time
from utils import *
from individual import Individual
from population import Population_proc

x = np.arange(-1, 2.0, 0.01)
f = weird_function(x)

# plotStartFunction(x, f)

st = [-1, 2]
allels_num = 12

# array = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1])[::-1]
# ind = Individual(evaluationFunction=weird_function,allels_num=allels_num)
# print(ind.decodeIndividual(st))
# print(ind.fitnessValue(st))

popsize = 10
maxgen = 10
current_population = []
for i in range(popsize):
    ind = Individual(weird_function, allels_num, st)
    current_population.append(ind)

initial_values = list(map(lambda ind: ind.fitness_value(), current_population))
initial_decodings = list(map(lambda ind: ind.decode_individual(), current_population))

population_proc = Population_proc(st)
pop_fitness = population_proc.whole_pop_fitness(current_population)
test = sum(list(map(lambda ind: ind.relative_fitness(pop_fitness), current_population)))
print(test)
assert math.fabs(test - 1) <= 1e-7, "probability must sum to one!"

for j in range(maxgen):
    dens = population_proc.get_pop_fitness_density(current_population)
    mating_pool = population_proc.get_mating_pool(popsize, dens)
    random.shuffle(mating_pool)
    current_population = population_proc.breed_population(mating_pool, allels_num, weird_function)

new_decodings = list(map(lambda ind: ind.decode_individual(), current_population))
new_values = list(map(lambda ind: ind.fitness_value(), current_population))

print('final max value:')
print(max(new_values))
print('final max decoding:')
print(max(new_decodings))

line, = plt.plot(x, f, lw=2)
plt.plot(new_decodings, new_values, 'ro', label="final values")
plt.plot(initial_decodings, initial_values, 'bo',label="initial values")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.xlim(-1, 2)
plt.ioff()
plt.show()
