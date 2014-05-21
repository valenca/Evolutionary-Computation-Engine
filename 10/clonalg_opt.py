# Clonal Selection - Leandro Castro

from random import randint, choice,sample, uniform, random, gauss
from operator import itemgetter
from copy import deepcopy
from math import cos,pi

def clonalg_opt(pop_size, cromo_size, domain,fitness, max_iter, numb_clones, beta, numb_new):
    """ To keep the size of the population constant numb_clones + numb_new = pop_size."""
    # initialize population
    population = create_population(pop_size, cromo_size, domain)
    print('Wait please....')
    for i in range(max_iter):
        print('Generation:%d ' % i)
        # evaluate population
        population = [[cromo, fitness(cromo)] for cromo, fit in population]
        # select best to clone
        aux_pop = deepcopy(population)
        aux_pop.sort(key=itemgetter(1))
        aux_pop = aux_pop[:numb_clones]
        # clone proportional to fitness
        clones = clone(aux_pop,beta)
        # mutate clones inversely proportional to fitness
        clones = mutate(clones)
        # evaluate clones
        clones = [ [cromo, fitness(cromo)] for cromo, fit in clones]
        # choose new best and include them in the population choosing the overall best ones
        population.extend(clones)
        population.sort(key=itemgetter(1))
        population = population[:numb_clones] 
        # replace worst elements by randon ones
        population.extend(create_population(numb_new, cromo_size,domain))
    return best(population)
        
        
 
def create_population(pop_size, cromo_size,domain):
    population = [[[uniform(domain[index][0],domain[index][1]) for index in range(cromo_size)],0] for number in range(pop_size)]
    return population    

def clone(pop, beta):
    """ create clones acording to affinity."""
    size = len(pop)
    clones = []
    for i in range(size):
        copies = [pop[i]] * (beta*size//(i+1))
        clones.extend(copies)
    return clones

def mutate(pop):
    """Minimization"""
    total_fit = sum([fit for cromo,fit in pop])
    new_pop = []
    for i in range(len(pop)):
        new_pop.append(muta_indiv(pop[i],total_fit) )                     
    return new_pop

def muta_indiv(indiv, total_fit):
    """Minimization"""
    cromo, fit = indiv
    threshold = random()
    if threshold < (fit/total_fit):
        index = choice(list(range(len(cromo))))
        cromo[index] += gauss(0,0.05)
    return [cromo,0]
                                  
def best(population):
    population = [ [cromo, fitness(cromo)] for cromo, fit in population]
    population.sort(key=itemgetter(1))
    return population[0]

# --------------------------  Functions  -------------------------------

def rastrigin(indiv):
    """ Rastrigin. Domínio [(-5.12,5.12),(-5.12,5.12),(-5.12,5.12)]."""
    n = len(indiv)
    # keep values inside the domain
    domain = [[-5.12,5.12] for i in range(n)]
    new_indiv = clamping(indiv,domain)
    f = n * 10.0 + sum([(x**2 - 10.0 * cos(2*pi*x)) for x in new_indiv])
    return f 


def clamping(indiv, domain):
    """keep individual's values inside the domain."""
    new_indiv = [verify(indiv[i],domain[i]) for i in range(len(indiv))]
    return new_indiv

def verify(value,domain_value):
    if value < domain_value[0]:
        return domain_value[0]
    elif value > domain_value[1]:
        return domain_value[1]
    else:
        return value


if __name__ == '__main__':
    """
    pop_1 = create_population(10,5)
    print('IN:\n',pop_1)
    print('OUT:\n',clone(pop_1,2))
    """
    pop_size = 100
    cromo_size = 3
    domain = [[-5.12,5.12]] * cromo_size
    fitness = rastrigin
    max_iter = 1000
    numb_clones = int(0.9 * pop_size)
    numb_new = int(0.1 * pop_size)
    beta = 5
    print(clonalg_opt(pop_size, cromo_size, domain,fitness, max_iter, numb_clones, beta, numb_new))
    
    


