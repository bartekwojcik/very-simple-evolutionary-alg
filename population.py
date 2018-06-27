from collections import OrderedDict
from individual import Individual
import random

class Population(object):
    def whole_pop_fitness(self,population, st):
        pop_fitnesses = list(map(lambda ind: ind.fitnessValue(st), population))
        sum_pop_fitness = sum(pop_fitnesses)
        return sum_pop_fitness

    def get_pop_fitness_density(self,population,st):
        # discovering python's collections, lol

        pop_fitness = self.whole_pop_fitness(population,st)
        d = list((i.relativeFitness(pop_fitness,st), i) for i in population)
        # rel_fitness = OrderedDict(sorted(rel_fitness_dict.items(),key=lambda t:t[0]))
        fit_list = d #list(d.items())
        # lam = lambda x, y: (x.relativeFitness(pop_fitness, st) + y.relativeFitness(pop_fitness, st), y)
        # density_dict = dict(map(lam,fit_list,))
        density = add_rec(fit_list[1:],[(fit_list[0])])
        return density

    def breed_population(self, mating_pool,allels_num, eval_func):
        offspring_list = []
        for i in range(0,len(mating_pool),2):
            one = mating_pool[i]
            two = mating_pool[i+1]
            off_one,off_two = self.cross_them_over(one,two,allels_num)

            off_one = Individual(eval_func,allels_num,off_one)
            off_two = Individual(eval_func,allels_num,off_two)

            offspring_list.append(off_one)
            offspring_list.append(off_two)
        return offspring_list


    def cross_them_over(self, one, two,l):
        point = random.randint(1,l-1)
        all_one = one.chromosome
        all_two = two.chromosome

        half_one = all_one[:point]
        one_half = all_one[point:]

        half_two = all_two[:point]
        two_hald = all_two[point:]

        off_one = half_one+two_hald
        off_two = one_half+half_two

        mutant_one = self.mutate(off_one)
        mutant_two = self.mutate(off_two)

        return off_one,off_two

    def mutate(self,individual):
        prop = 0.01
        num_chrom = len(individual)
        for c in range(num_chrom):
            rand = random.random()
            if rand <= prop:
                chrom_val =individual[c]
                chrom_val = 1- chrom_val
                individual[c] = chrom_val
        return individual


def add_rec(list, tail_list):
    if list:
        second_pair = list[0]
        last_existing = tail_list[-1]
        new_pair = (last_existing[0] + second_pair[0], second_pair[1])
        tail_list.append(new_pair)
        if list[1:]:
            add_rec(list[1:],tail_list)
    return tail_list




