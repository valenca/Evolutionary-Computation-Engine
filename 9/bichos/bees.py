""" 
Bees Algorithms
Pham et alli version (2006) 'The bees algorithm - a novel tool for complex optimization problems' 
"""

__author__ = 'Ernesto Costa'
__date__ = 'April 2014'

import math
import random
import copy
from operator import itemgetter

def bees(fitness, numb_gener,search_space,numb_bees,numb_sites,elite_sites, patch_size,e_bees, o_bees):
    population = [create_random_bee(search_space) for count in range(numb_bees)]
    population = [[indiv, fitness(indiv)] for indiv in population]
    population.sort(key=itemgetter(1))
    best = population[0]
    for i in range(numb_gener):
        # new  elite
        next_gen = []
        for j,indiv in enumerate(population[:numb_sites]):
            if j < elite_sites:
                neigh_size = e_bees
            else:
                neigh_size = o_bees
            next_gen.append(search_neigh(indiv[0], neigh_size,patch_size,search_space,fitness) )
        # new scouts
        scouts = create_scout_bees(search_space, (numb_bees - numb_sites))
        # new population
        population = next_gen + scouts
        population = [[indiv, fitness(indiv)] for indiv in population]
        population.sort(key=itemgetter(1))
        best = update_best(population[0],best)
        show(best)
        patch_size = patch_size * 0.95
    return best
          
    
def create_random_bee(search_space):
    return [random.uniform(lb,ub) for lb,ub in search_space]

def create_scout_bees(search_space, numb_scouts):
    return [create_random_bee(search_space) for i in range(numb_scouts)]

def create_neigh_bee(cromo,patch_size, search_space):
    new_cromo = []
    for i,val in enumerate(cromo):
        r = random.random()
        if r < 0.5:
            new_val = min(val + random.random()*patch_size, search_space[i][1])          
        else:
            new_val = max(val - random.random()*patch_size, search_space[i][0])
        new_cromo.append(new_val)
    return new_cromo


def update_best(candidate, current_best):
    """Assume population is sorted according to fitness."""
    if candidate[1] < current_best[1]:
        return candidate
    else:
        return current_best
  
    
def search_neigh(cromo,neigh_size,patch_size,search_space,fitness):
    neigh = []
    for i in range(neigh_size):
        neigh.append(create_neigh_bee(cromo,patch_size,search_space))
    neigh = [ [indiv, fitness(indiv)] for indiv in neigh]
    neigh.sort(key=itemgetter(1))
    return neigh[0][0]
                                                              

def show(indiv):
    print('Cromo: %s, Fitness: %10.8f' % (indiv[0], indiv[1]))

def sphere(indiv):
    """
    deJong F1 function. 
    domain = [-5.12, 5.12]
    minimun = 0 at (0,...,0)
    """
    return sum([x**2 for x in indiv])

def rastrigin(indiv):
    """
    rastrigin function
    domain = [-5.12, 5.12]
    minimum at (0,....,0)
    """
    n = len(indiv)
    A = 10
    return A * n + sum([x**2 - A * math.cos(2 * math.pi * x) for x in indiv])

def schwefel(indiv):
    """
    domain = [-500,500]
    minimum = 0 at (1,...,1)
    """
    n = len(indiv)
    return 418.9829 * n - sum([ x * math.sin(math.sqrt(abs(x))) for x in indiv])
    
if __name__ == '__main__':
    # Problem configuration
    # 1
    problem_size = 2
    domain_1 = [-5.12, 5.12]
    search_space_1 = [domain_1] * problem_size
    # 2
    domain_2 = [-500,500]
    search_space_2 = [domain_2] * problem_size
    # algorithm configuration
    numb_gener = 100
    numb_bees = 20
    numb_sites = 5
    elite_sites = 2
    patch_size = 5.0
    e_bees = 10
    o_bees = 3
    # do it
    best = bees(rastrigin,numb_gener,search_space_1,numb_bees,numb_sites,elite_sites, patch_size,e_bees, o_bees)
    show(best)
    #best = bees(schwefel,numb_gener,search_space_2,numb_bees,numb_sites,elite_sites, patch_size,e_bees, o_bees)
    #show(best)    
    
    
