import numpy as np
from utils import *

class Individual(object):

    def __init__(self, evaluation_function, allels_num, st, chromosome=None):
        if chromosome is not None:
            self.chromosome = chromosome
        else:
            self.chromosome = self.get_random_chromosome(allels_num, 0.5)

        self.value_function = evaluation_function
        self.st = st

    def decode_individual(self):
        chromosome = np.array(self.chromosome)
        x = decode_array(chromosome,self.st)
        return x

    def fitness_value(self):
        return self.value_function(self.decode_individual())

    def relative_fitness(self, pop_fitness):
        result = self.fitness_value() / pop_fitness
        return result

    def get_random_chromosome(self,length, prop):
        chromosome = []
        for i in range(0, length):
            rand = random.random()
            allel = 0 if prop > rand else 1
            chromosome.append(allel)
        return chromosome

    def mutate(self):
        prop = 0.01
        num_chrom = len(self.chromosome)
        for c in range(num_chrom):
            rand = random.random()
            if rand <= prop:
                chrom_val =self.chromosome[c]
                chrom_val = 1- chrom_val
                self.chromosome[c] = chrom_val

    def __str__(self):
        return self.chromosome



