from Library.database import Database
from Library.values import Values
from Library.algorithms import Algorithms
from Library.generation import Generation
from Library.individuals import Individuals
from Library.distance import Distance
from Library.fitness import Fitness
from Library.phenotype import Phenotype
from Library.parents import Parents
from Library.survivors import Survivors
from Library.crossover import Crossover
from Library.mutation import Mutation
from Library.neighbors import Neighbors
from Library.sort import Sort
from Library.status import Status
from Library.stop import Stop

from random import uniform, seed
from cPickle import dump

if __name__ == '__main__':

	##### EDIT ONLY THIS #####
	problem = 'griewank'
	algorithm = 'sea'
	n_generations = 2000
	population_size = 500
	individual_size = 100
	crossover_probability = 0.9
	mutation_probability = 1.0/individual_size
	disturbance_probability = 5.0/individual_size
	print_type = 'bar'
	##########################
	values = Values(problem, individual_size)
	values.values['generation_distance'] = 2000
	values.values['tournament_size'] = 3
	values.values['elite_percentage'] = 0.05
	values.values['worst_percentage'] = 0.5
	values.values['n_points_cut'] = 4
	values.values['stabilize_percentage'] = 1
	values.values['stop_interval'] = 0.001
	values.values['fitness_arrival'] = 0
	##########################

	generation = Generation(population_size, individual_size, values.values)
	individuals = Individuals(population_size, individual_size, values.values)
	distance = Distance(individual_size)
	fitness = Fitness(individual_size,values.values)
	phenotype = Phenotype(individual_size, values.values)
	parents = Parents(population_size, individual_size, values.values)
	survivors = Survivors(population_size, values.values)
	crossover = Crossover(individual_size,crossover_probability, values.values)
	mutation = Mutation(individual_size, mutation_probability, values.values)
	disturbance = Mutation(individual_size, disturbance_probability, values.values)
	neighbors = Neighbors(individual_size, values.values)
	sort = Sort()
	status = Status(n_generations, population_size, individual_size, print_type)
	stop = Stop(n_generations, values.values)

	database = Database(generation, individuals, distance, fitness, phenotype, parents,
		survivors, crossover, mutation, disturbance, neighbors, sort, status, stop)
	
	functions = database.database[problem]

	generation.individuals_function = functions['individuals']
	generation.distance_function = functions['distance']
	fitness.fitness_function = functions['fitness']
	crossover.crossover_function = functions['crossover']
	status.status_function = functions['status']
	status.phenotype_function = functions['phenotype']
	survivors.sort_function = functions['sort']

	algorithms = Algorithms(n_generations,functions['generation'],fitness.fitness,functions['sort'],
		functions['neighbors'],functions['parents'],crossover.crossover,functions['mutation'],
		functions['disturbance'],functions['survivors'],status.status,functions['stop'])

	final = []
	seed('griewank')
	for i in range(50):
		results = {}
		results['population'],results['best_fitnesses'],results['average_fitnesses'] = algorithms.call(algorithm)

		print ''
		final.append(results)
	
	with open('output','a') as f:
		dump(final, f)



	#status.print_type = 'all'
	#status.status('Final',results['population'],results['best_fitnesses'],results['average_fitnesses'])
