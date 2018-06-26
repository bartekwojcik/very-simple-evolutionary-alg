import numpy as np
import random
import math
import matplotlib.pyplot as plt


def weird_function(x):
    res = x * np.sin(10 * np.pi * x) + 2.0
    return res


def plotStartFunction(x, y):
    line, = plt.plot(x, y, lw=2)
    plt.xlim(-1, 2)
    plt.show()

def decodeArray(array, st):
    array = np.array(array)
    powers = np.arange(0, array.size,1)
    mult = np.array(array) * 2 ** powers
    sumation = np.sum(mult)
    x = (sumation / 2**array.size) * (st[1] - st[0]) + st[0]
    return x

def getRandomChromosome(length, prop):
    chromosome = []
    for i in range(0,length):
        rand = random.random()
        allel = 0 if prop > rand else 1
        chromosome.append(allel)
    return chromosome


