import numpy as np
from utils import *

class Individual(object):

    def __init__(self, evaluationFunction, allels_num,chromosome=None):
        if chromosome is not None:
            self.chromosome = chromosome
        else:
            self.chromosome = getRandomChromosome(allels_num,0.5)

        self.valueFunction = evaluationFunction

    def decodeIndividual(self, st):
        chromosome = np.array(self.chromosome)
        x = decodeArray(chromosome,st)
        return x

    def fitnessValue(self,st):
        return self.valueFunction(self.decodeIndividual(st))

    def relativeFitness(self,pop_fitness,st):
        result = self.fitnessValue(st)/pop_fitness
        return result

    def __str__(self):
        return self.chromosome



