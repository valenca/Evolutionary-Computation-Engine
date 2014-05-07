#! /usr/bin/env python

"""
pso_tsp.py
Implementation of the standard PSO (Kennedy & Eberhart: Swarm Intelligence. pp 313). 
Global neighborhood. 
For solving the TSP using random keys.
Ernesto Costa, May 2014.
"""

# imports
from pylab import *
from random import random,uniform
from copy import deepcopy
from math import sqrt,sin,cos,pi
from operator import itemgetter

# colect and display
def run(numb_runs,numb_generations,numb_particles,weight_inertia, phi_1,phi_2,vel_max, domain, function, problem,type_problem):
    # Colect Data
    print('Wait, please ')
    statistics_total = [pso(numb_generations,numb_particles,weight_inertia, phi_1,phi_2,vel_max, domain, function,problem,type_problem) for i in range(numb_runs)]
    print("That's it!")
    # Process data: best and average by generation
    results = list(zip(*statistics_total))   
    best = [type_problem([result[0] for result in generation]) for generation in results]
    best_average = [sum([result[0] for result in generation])/numb_runs for generation in results]
    average = [sum([indiv[1] for indiv in genera])/numb_runs for genera in results]
    # Mostra
    ylabel('Fitness')
    xlabel('Generation')
    tit = 'Runs: %d , Phi: %0.2f, Vel: %0.2f' % (numb_runs,phi_1, vel_max)
    title(tit)
    axis= [0,numb_generations,0,len(domain)]
    p1 = plot(best,'r-o',label="Best")
    p2 = plot(average,'g->',label="Average")
    p3 = plot(best_average, 'y-s',label="Average of Best")
    if type_problem == max:
        legend(loc='lower right')
    else:
        legend(loc='upper right')
    show()
    
# main program

def pso(numb_generations,numb_particles,weight_inertia, phi_1,phi_2,vel_max, domain, function,problem,type_problem):
    """
    num_generations = number of generations
    numb_particles = number of particles (10 + 2 * sqrt(dimensions)) or [10,50]
    weight_inertia (w) = to control oscilations (0.721 or [0,1[)
    phi_1, phi_2 = cognitive and social weights (1.193 or less than (12* w* (w-1) / (5*w -7)) or sum equal to 4)
    vel_max = maximum variation for move
    domain = [...,(inf_i,sup_i)...] domain values for each dimension
    function = to compute the fitness of a solution candidate
    type_problem = max or min, for maximization or minimization problems.
    k = size of neighborhood
    
    Structures:
    particles = [...,[[...,p_i_j,...],fit_i],...], current position and fitness of particle i
    velocities = [..., [...,v_i_j,...],...]
    best_past = [...,[[...,p_i_j,...],fit_i],...], previous best position and fitness of particle i
    global_best = [[...,p_k_j,...],fit_k], position and fitness of the global best particle
    statistics_by_generation = [...,[best_fitness_gen_i, average_fitness_gen_i], ...]
    """
    # initialization
    numb_dimensions = len(domain)
    particles = [[generate_particle(domain),0] for count in range(numb_particles)]
    velocities = [generate_velocity(vel_max, numb_dimensions) for count in range(numb_particles)]
    
    # first evaluations
    particles = [[part, function(part,problem)] for [part,fit] in particles]
    best_past = deepcopy(particles)
    global_best = find_global_best(particles,type_problem)
    # statistics
    statistics_by_generation = []
    # Run!
    for gen in range(numb_generations):
        # for each particle
        for part in range(numb_particles): 
            # for each dimension
            for dim in range(numb_dimensions):
                # update velocity
                velocities[part][dim] = weight_inertia * velocities[part][dim] 
                + phi_1 * (best_past[part][0][dim] - particles[part][0][dim])
                + phi_2 * (global_best[0][dim] - particles[part][0][dim])
                # update position
                particles[part][0][dim] = particles[part][0][dim] + velocities[part][dim]
                # clampling
                if particles[part][0][dim] < domain[dim][0]:
                    particles[part][0][dim] = domain[dim][0]
                    #velocities[part][dim] = 0
                elif particles[part][0][dim] > domain[dim][1]:
                    particles[part][0][dim] = domain[dim][1]
                    #velocities[part][dim] = 0
            # update fitness particle
            particles[part][1] = function(particles[part][0],problem)

            # update best past
            if type_problem == max:
                # maximization situation
                if particles[part][1] > best_past[part][1]:
                    best_past[part] = deepcopy(particles[part])
		    		# update global best
                    if particles[part][1] > global_best[1]:
                        global_best = particles[part]	
            else: # minimization problem
                if particles[part][1] < best_past[part][1]:
                    best_past[part] = deepcopy(particles[part])
                    if particles[part][1] < global_best[1]:
                        global_best = particles[part]	
        # update statistics
        generation_average_fitness = sum([particle[1] for particle in best_past])/numb_particles
        generation_best_fitness = global_best[1]
        statistics_by_generation.append([generation_best_fitness,generation_average_fitness])
    # give me the best!
    print('\nBest Solution: %s\nFitness: %0.2f' % (decode_rk(global_best[0]),global_best[1]))
    return statistics_by_generation
    

    
# Utilities
def generate_particle(domain):
    """ randomly construct a particle."""
    particle = [random() for inf,sup in domain]
    return particle

def generate_velocity(vel_max, numb_dimensions):
    """ randomly define the velocity of a particle."""
    velocity = [uniform(-vel_max,vel_max) for count in range(numb_dimensions)]
    return velocity


def find_global_best(particles,type_problem):
    """ Find the overall global best."""
    global_best = deepcopy(particles)
    global_best.sort(key=itemgetter(1))
    if type_problem == max:
        return global_best[-1]
    else:
        return global_best[0]
 
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
  	

#  --------------------------  For TSP ------------------------------------

# Getting gthe coordinates of the cities from a file and store them in a dictionary
def get_coordinates_tsp(filename):
    """ 
    General parser for tsp files.
    Obtain the cities' coordinates from a file in tsp format.
    """ 
    with open(filename) as f_in:
        coordinates = []
        line = f_in.readline()
        while not line.startswith('NODE_COORD_SECTION'):
            line = f_in.readline()
        line = f_in.readline()
        while not line.startswith('EOF'):
            n,x,y = line[:-1].split()
            coordinates.append((float(x),float(y)))
            line = f_in.readline()
        f_in.close()
    return coordinates

def dict_cities(coordinates):
    """ Create a dictionary. Key = city identifier, value = coordinates."""
    my_dict = {}
    for i, (x,y) in enumerate(coordinates):
        my_dict[i] = (x,y)
    return my_dict

#  Fitness calculation
def phenotype_rk(genotype,problem):
	""" Obtaing the phenotype = list of coordinates."""
	genotype_permut = decode_rk(genotype)
	pheno = [problem[city] for city in genotype_permut]
	return pheno

def evaluate(genotype,problem):
	tour = phenotype_rk(genotype,problem)
	numb_cities = len(tour)
	dist = 0
	for i in range(numb_cities):
		j = (i+1) % numb_cities
		dist  += distance(tour[i],tour[j])
	return dist

def distance(cid_i, cid_j):
    """ Euclidian distance."""
    x_i, y_i = cid_i
    x_j, y_j = cid_j
    dx = x_i - x_j
    dy = y_i - y_j
    dist = sqrt(dx**2 + dy**2)
    return dist

# From a vector of reals to a permutation of integers
def decode_rk(vector):
    """Work even with repeated elements."""
    copia = deepcopy(vector)
    aux = deepcopy(vector)
    aux.sort()
    permutation = []
    for i,elem in enumerate(aux):
        permutation.append(copia.index(elem))
        copia[copia.index(elem)] = None
    return permutation


if __name__== '__main__':
	filename = '/Users/ernestojfcosta/tmp/wi29.tsp'
	coordinates = get_coordinates_tsp(filename)
	problem = dict_cities(coordinates)
	size = len(problem)
	run(1,100,100,0.8,1.3,2.7,0.8,[(0,1) for i in range(size)],evaluate,problem,min)
    
