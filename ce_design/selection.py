
"""
Selection mechanisms.
selection.py
Ernesto Costa March, 2014
"""

import math
import random 
from operator import itemgetter
from copy import deepcopy

def roulette_wheel(population, numb):
    """ Select numb individuals from the population
    according with their relative fitness. MAX. """
    pop = deepcopy(population)
    pop.sort(key=itemgetter(1))
    total_fitness = sum([indiv[1] for indiv in pop])
    mate_pool = []
    for i in range(numb):
        value = random.uniform(0,1)
        index = 0
        total = pop[index][1]/ total_fitness
        while total < value:
            index += 1
            total += pop[index][1]/total_fitness
        mate_pool.append(pop[index])
    return mate_pool


def sus(population,numb):
    """ Stochastic Universal Sampling."""
    pop = deepcopy(population)
    pop.sort(key=itemgetter(1))
    total_fitness = sum([indiv[1] for indiv in pop])
    value = random.uniform(0,1.0/numb)
    pointers = [ value + i * (1.0/numb) for i in range(numb)]
    mate_pool = []
    for j in range(numb):
        val = pointers[j]
        index = 0
        total =pop[index][1]/float(total_fitness)
        while total < val:
            index += 1
            total += pop[index][1]/float(total_fitness)
        mate_pool.append(pop[index])
    return mate_pool

        
def tournament_sel(population, numb,size):
    mate_pool=[]
    for i in range(numb):
        indiv = tournament(population,size)
        mate_pool.append(indiv)
    return indiv

def tournament(population, numb_offspring, t_size):
    return [one_tournament(population,t_size) for count in range(numb_offspring)]

def one_tournament(population,size):
    """Maximization. Problem.Deterministic"""
    pool = random.sample(population, size)
    pool.sort(key=itemgetter(1),reverse = True)
    return pool[0]


def rank_base(population, numb,s):
    """linear version.The greater the better. Choose 1.0 < s <= 2.0."""
    pop_size = len(population)
    pop = deepcopy(population)
    pop.sort(key=itemgetter(1))
    probabilities = [(2*i)/(pop_size * (pop_size + 1))for i in range(1,pop_size+1)]
    mate_pool = []
    for i in range(numb):
        value = random.uniform(0,1)
        index = 0
        total = probabilities[index]
        while total < value:
            index += 1
            total += probabilities[index]
        mate_pool.append(population[index])
    return mate_pool

def rank(population, numb,s):
    """linear version.The greater the better. Choose 1.0 < s <= 2.0."""
    pop_size = len(population)
    pop = deepcopy(population)
    pop.sort(key=itemgetter(1))
    probabilities = [((2 - s)/pop_size) + ((2*i*(s -1))/float((pop_size * (pop_size - 1))))
                     for i in range(pop_size)]
    mate_pool = []
    for i in range(numb):
        value = random.uniform(0,1)
        index = 0
        total = probabilities[index]
        while total < value:
            index += 1
            total += probabilities[index]
        mate_pool.append(population[index])
    return mate_pool

def rank_exp(population, numb):
    """ exponential version.The greater the better."""
    pop_size = len(population)
    normalise = pop_size - ((1 - math.e**(-pop_size)) / (1 - math.e**(-1)))
    pop = deepcopy(population)
    pop.sort(key=itemgetter(1))
    probabilities = [(1 - math.e**(-i)) / normalise for i in range(pop_size)]
    mate_pool = []
    for i in range(numb):
        value = random.uniform(0,1)
        index = 0
        total = probabilities[index]
        while total < value:
            index += 1
            total += probabilities[index]
        mate_pool.append(population[index])
    return mate_pool

# to test

def cromo(size):
    indiv = [random.randint(0,1) for i in range(size)]
    return indiv

def population(size_pop,size_cromo):
    pop = [[cromo(size_cromo),0] for j in range(size_pop)]
    return pop

def one_max(indiv):
    return sum(indiv)

def eval_pop(pop):
    new_pop = [[pop[j][0],one_max(pop[j][0])] for j in range(len(pop))]
    return new_pop

               


if __name__ == '__main__':
    tam_pop = 10
    tam_cromo = 5
    pop = population(tam_pop,tam_cromo)
    pop = eval_pop(pop)
    print('População:\n',pop)
    print(50 * '*')
    print('roulette')
    print(roulette_wheel(pop,tam_pop))
    print('tournament')
    print(tournament(pop,tam_pop,2))
    print('sus')
    print(sus(pop,tam_pop))
    print('rank base')
    print(rank_base(pop,tam_pop,2.0))    
    print('rank')
    print(rank(pop,tam_pop,2.0))
    print('rank exp')
    print(rank_exp(pop,tam_pop))    
    


    
    
    
    