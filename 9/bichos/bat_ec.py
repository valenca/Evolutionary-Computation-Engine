""" 
Bat Algorithm:  adapted from  Xin-She Yang in 'Nature-Inspired Metaheuristics Algorithms'
bat_ec.py
"""

__author__ = 'Ernesto Costa'
__date__ = 'May 2014'

from random import random, uniform, gauss
from operator import itemgetter
from math import exp,cos,pi
from copy import deepcopy
#import matplotlib.pyplot as plt

def bat(numb_bats, numb_gener, frequency, loudness_0, alpha, pulse_rate_0, gamma, domain, fitness):
    """
    loudness: initial value
    frequencies = [f_min, f_max]: typical values [0, 2]
    domain = [..., [inf,sup],...]
    fitness = function whose optimum we are looking for
    """
    dim = len(domain)
    # initialize bat population: positions (x_i)  and velocities (v_i), ....
    pulse_rate = [pulse_rate_0 for j in range(numb_bats)]
    loudness = [loudness_0 for i in range(numb_bats)]    
    velocity = [ [0] * dim for j in range(numb_bats)]
    cromos = [ [uniform(domain[j][0], domain[j][1]) for j in range(dim)] for k in range(numb_bats)]
    pop = [ [cromo, fitness(cromo)] for cromo in cromos]
    # best so far
    best = best_individual(pop)
    for index in range(numb_gener):
        # for each bat
        for i in range(numb_bats):
            # generate new solutions (f, v, x)
            beta = random()
            freq = frequency[0] + (frequency[1] - frequency[0]) * beta
            velocity[i] = [ velocity[i][j] + (pop[i][0][j] - best[0][j]) * freq for j in range(dim)]
            x = [pop[i][0][j] + velocity[i][j] for j in range(dim)] 
            if random() > pulse_rate[i]:
                #print('variant of best...')
                # construct a local variant of the best by a random walk
                x =  [ best[0][j] + 0.01 * gauss(0,1) for j in range(dim)]
            # evaluate new  solution 
            x = [x, fitness(x)]
            if (random() < loudness[i]) and (x[1] < pop[i][1]):
                #print('accept...')
                # accept new solution
                pop[i] = x
                # increase r_i and decrease A_i
                pulse_rate[i] = update_pulse_rate(index, pulse_rate_0)
                loudness[i] = update_loudness(loudness,i)                
                # update best
                if pop[i][1] < best[1]:
                    best = pop[i]
        # mostra best
        show(index,best)
    return best


def run(numb_runs, numb_bats, numb_gener, frequency, loudness,alpha, pulse_rate, gamma, domain, fitness):
    best_ate = []
    for r in range(numb_runs):
        print r,
        best_ate.append(bat(numb_bats, numb_gener, frequency, loudness, alpha, pulse_rate, gamma, domain, fitness)[1])   
        print best_ate[-1]
    # Show
    '''plt.ylabel(' Best Fitness')
    plt.xlabel('Run')
    my_title = 'BAT %d Runs, Fitness: %s' % (numb_runs, fitness)
    plt.title(my_title)
    #plt.axis= [0,numb_runs,0,bests[0]]
    plt.plot(best_ate,'r-o',label="Best")
    #p2 = plt.plot(average_bests,'g-s',label="Average")
    plt.legend(loc='upper right')
    plt.show()'''
    with open('data.csv','a') as f:
        f.write(','.join(list(map(str,best_ate)))+'\n')  


def best_individual(population):
    aux = deepcopy(population)
    aux.sort(key=itemgetter(1))
    return aux[0]

def show(gener, best):
    #print('Generation: %d \nCromo: %s\nFitness: %10.8f\n' % (gener,best[0], best[1]))
    pass


def update_loudness(a, bat,alpha=0.98):
    """ alpha in [0,1]"""
    return alpha * a[bat]

def update_pulse_rate(t,r_0 = 0.2,gamma=0.05):
    """ r_0 and gamma in [0,1]"""
    return r_0 * (1 - exp(-gamma*t))


# --------------- Functions -------------------

def rastrigin_nd(indiv):
    """ Rastrigin. Dominio [(-5.12,5.12),(-5.12,5.12),(-5.12,5.12)]."""
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
    # parameters for the  algorithm
    numb_bats = 250
    numb_gener = 500
    frequency = [0,2]
    loudness = 0.5
    alpha = 0.99
    pulse_rate = 0.1
    gamma = 0.05
    # problem
    dim = 10
    domain = [(-5.12, 5.12) for i in range(dim)]
    fitness = rastrigin_nd
    # do it
    #best = bat(numb_bats, numb_gener, frequency, loudness, alpha, pulse_rate, gamma, domain, fitness)
    #print('Best at the end: ')
    #show(numb_gener,best)
    
    # runs
    numb_runs = 30
    run(numb_runs,numb_bats, numb_gener, frequency, loudness, alpha, pulse_rate,gamma, domain, fitness)

   

            
            
                
