# Clonal Selection (II) - Leandro Castro
# Pattern Recognition

from random import randint, choice,sample, uniform, random, gauss
from operator import itemgetter
from copy import deepcopy
from math import cos,pi

def clonalg_pat(patterns, pop_size, mem_size, cromo_size, fitness, max_iter, numb_clones, beta, numb_new):
    """ To keep the size of the population constant numb_clones + numb_new = pop_size."""
    # initialize population
    population = create_population(pop_size, cromo_size)
    print('wait please...')
    for i in range(max_iter):
        print('Generation %d' % i)
        for index,pat in enumerate(patterns):
            # evaluate population
            population = [[cromo, fitness(cromo,pat)] for cromo, fit in population]
            # select best to clone
            aux_pop = deepcopy(population)
            aux_pop.sort(key=itemgetter(1), reverse=True)
            aux_pop = aux_pop[:numb_clones]
            # clone proportional to fitness
            clones = clone(aux_pop,beta)
            # mutate clones inversely proportional to fitness
            clones = mutate(clones)
            # evaluate clones
            clones = [ [cromo, fitness(cromo,pat)] for cromo, fit in clones]
            # choose new best and include it eventually in the memory
            clones.sort(key=itemgetter(1), reverse=True)
            best_clone = clones[0]
            if best_clone[1] > population[index][1]:
                population[index] = deepcopy(best_clone)
            # replace worst elements by randon ones
            if numb_new > 0:
                population[-numb_new:] = create_population(numb_new, cromo_size)
    print("That's it!")
    return population[:mem_size]

        
        
 
def create_population(pop_size, cromo_size):
    population = [[create_cromo(cromo_size),0] for number in range(pop_size)]
    return population 

def create_cromo(cromo_size):
    """Create a random pattern."""
    cromo = [[randint(0,1) for i in range(cromo_size[1])] for i in range(cromo_size[0])]
    return cromo

def affinity(indiv, pat):
    size = len(indiv) * len(indiv[0])
    hamming = sum([ 1 for i in range(len(indiv)) for j in range(len(indiv[0])) if indiv[i][j] != pat[i][j]])
    return size - hamming


def clone(pop, beta):
    """ create clones acording to affinity."""
    size = len(pop)
    clones = []
    for i in range(size):
        copies = [pop[i]] * (beta*size//(i+1))
        clones.extend(copies)
    return clones

def mutate(pop):
    """Maximization"""
    total_fit = sum([fit for cromo,fit in pop])
    new_pop = []
    for i in range(len(pop)):
        new_pop.append(muta_indiv(pop[i],total_fit) )                     
    return new_pop

def muta_indiv(indiv, total_fit):
    """Maximization"""
    new_indiv = deepcopy(indiv)
    cromo, fit = new_indiv
    threshold = random()
    if threshold < (1 /(1 + fit)):
        index_1 = choice(list(range(len(cromo))))
        index_2 = choice(list(range(len(cromo[0]))))
        cromo[index_1][index_2] ^= 1
    return [cromo,0]
                                  
def best(population):
    population = [[cromo, fitness(cromo)] for cromo, fit in population]
    population.sort(key=itemgetter(1),reverse=True)
    return population[0]

# -------------    to see or not to see that is the question.... ----------

import turtle


def white_quad(pos_x, pos_y, side):
    turtle.pu()
    turtle.goto(pos_x, pos_y)
    turtle.pd()
    for i in range(4):
        turtle.fd(side)
        turtle.rt(90)
    turtle.ht()
             
def black_quad(pos_x, pos_y, side):
    turtle.pu()
    turtle.goto(pos_x, pos_y)
    turtle.pd()
    turtle.fillcolor('black')
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(side)
        turtle.rt(90) 
    turtle.end_fill()
    turtle.ht()
    
def draw_pattern(pattern):
    turtle.speed(0)
    side = 10
    size_x = len(pattern[0])
    size_y = len(pattern)
    pos_y = 0
    for i in range(size_y):
        pos_x = 0
        for j in range(size_x):
            if pattern[i][j] == 1:
                black_quad(pos_x, pos_y,side)
            else:
                white_quad(pos_x, pos_y,side)
            pos_x += side
        pos_y -= side

if __name__ == '__main__':

    # --------------------------  Patterns  -------------------------------
    
    zero = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    
    one = [[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0]]
    
    square = [[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]
    
    three = [[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,1,0,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,1,1,1,1,0,0],[0,0,0,0,1,1,1,1,0,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,1,1,0], [0,0,0,0,0,0,0,1,1,0],[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,1,0,0]] 
    
    
    patterns = [three, square,zero,one]
    
    # ----------------------- End Patterns ---------------------------------
    
    
    pop_size = 10
    mem_size = len(patterns)
    cromo_size = [12,10]
    fitness = affinity
    max_iter = 600
    numb_clones = int(1.0 * pop_size)
    numb_new = int(0.0 * pop_size)
    beta = 10
    
    mem = clonalg_pat(patterns,pop_size, mem_size, cromo_size, fitness, max_iter, numb_clones, beta, numb_new)
    #print(mem)
    draw_pattern(mem[0][0])
    turtle.exitonclick()
    
    


