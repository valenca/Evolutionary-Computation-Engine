from Library.database import Database
from Library.values import Values
from Library.algorithms import Algorithms
from Library.generation import Generation
from Library.fitness import Fitness
from Library.phenotype import Phenotype
from Library.parents import Parents
from Library.survivors import Survivors
from Library.crossover import Crossover
from Library.mutation import Mutation
from Library.disturbance import Disturbance
from Library.neighbors import Neighbors
from Library.sort import Sort
from Library.status import Status
from Library.stop import Stop

from random import uniform, seed

if __name__ == '__main__':

	##### EDIT ONLY THIS #####
	problem = 'methinks'
	n_generations = 50000
	population_size = 500
	individual_size = 1386
	crossover_probability = 0.9
	mutation_probability = 1.0/individual_size
	disturbance_probability = 5.0/individual_size
	print_type = 'all'

	values = Values(problem, individual_size)

	values.values['tournament_size'] = 3
	values.values['stabilize_percentage'] = 0.1
	values.values['elite_percentage'] = 0.1
	values.values['stop_interval'] = 0.00001
	values.values['n_points'] = 2
	##########################


	generation = Generation(population_size, individual_size)
	fitness = Fitness(individual_size,values.values)
	phenotype = Phenotype(individual_size, values.values)
	parents = Parents(population_size, individual_size, values.values)
	survivors = Survivors(population_size, values.values)
	crossover = Crossover(individual_size,crossover_probability, values.values)
	mutation = Mutation(individual_size, mutation_probability, values.values)
	disturbance = Disturbance(individual_size, disturbance_probability, values.values)
	neighbors = Neighbors(individual_size, values.values)
	sort = Sort()
	status = Status(n_generations, population_size, print_type)
	stop = Stop(n_generations, values.values)

	database = Database(generation, fitness, phenotype, parents, survivors,
		crossover, mutation, disturbance, neighbors, sort, status, stop)
	
	functions = database.database[problem]

	fitness.fitness_function = functions['fitness']
	crossover.crossover_function = functions['crossover']
	status.status_function = functions['status']
	status.phenotype_function = functions['phenotype']
	survivors.sort_function = functions['sort']


	algorithms = Algorithms(n_generations,functions['generation'],fitness.fitness,functions['sort'],
		functions['neighbors'],functions['parents'],crossover.crossover,functions['mutation'],
		functions['disturbance'],functions['survivors'],status.status,functions['stop'])

	results = {}
	results['population'],results['best_fitnesses'],results['average_fitnesses'] = algorithms.call('sea')

	print''
	#status.print_type = 'all'
	#status.status('Final',results['population'],results['best_fitnesses'],results['average_fitnesses'])
