from algorithm import *
from generation import Generation
from fitness import Fitness

if __name__ == '__main__':

	n_runs = 1

	n_generations = 50
	population_size = 2
	individual_size = 3
	parents_selection_group_size = 3
	crossover_probability = 0.9
	mutation_probability = 0.1
	elite_percentage = 0.05

	'''generation = generate_population
	fitness = jbrandao
	order = order
	parents_selection = parents_selection
	crossover = crossover
	mutation = mutation
	survivors_selection = survivors_selection
	phenotype = jbrandao_phenotype
	status = jbrandao_status'''

	generation = Generation(population_size, individual_size)
	fitness = Fitness(population_size, individual_size, Fitness.fitness_jbrandao, None)
	print fitness.fitness
	a = generation.generation_binary()
	print a
