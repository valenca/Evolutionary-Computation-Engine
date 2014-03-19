from Library.algorithms import Algorithms
from Library.generation import Generation
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

algorithms = Algorithms(None)
generation = Generation(None,None)
fitness = Fitness(None,None)
phenotype = Phenotype(None)
parents = Parents(None,None,None)
survivors = Survivors(None,None)
crossover = Crossover(None,None)
mutation = Mutation(None,None)
neighbors = Neighbors(None)
sort = Sort()
status = Status(None,None,None)
stop = Stop(None,None)

database = {
			'jbrandao':
				{
					'generation':	generation.generation_binary,
					'fitness':		fitness.fitness_jbrandao,
					'phenotype':	phenotype.phenotype_jbrandao,
					'parents':		parents.parents_tournament,
					'survivors':	survivors.survivors_elitism,
					'crossover':	crossover.crossover_one_point,
					'mutation':		mutation.mutation_binary,
					'neighbors':	None,
					'sort':			sort.sort_decrease,
					'status':		status.status_jbrandao,
					'stop':			stop.stop_best_stabilization
				}
		   }

if __name__ == '__main__':

	problem = database['jbrandao']
	n_runs = 1
	n_generations = 500
	population_size = 250
	individual_size = 100
	tournament_size = 3
	crossover_probability = 0.9
	mutation_probability = 0.1
	elite_percentage = 0.05
	stabilization_percentage = 1
	print_type = ''

	algorithms = Algorithms(n_generations)
	generation = Generation(population_size, individual_size)
	fitness = Fitness(individual_size,None)
	fitness.fitness_function = fitness.fitness_jbrandao
	phenotype = Phenotype(individual_size)
	parents = Parents(population_size, individual_size, tournament_size)
	survivors = Survivors(population_size, elite_percentage)
	crossover = Crossover(individual_size,crossover_probability)
	crossover.crossover_function = crossover.crossover_one_point
	mutation = Mutation(individual_size, mutation_probability)
	neighbors = Neighbors(individual_size)
	sort = Sort()
	status = Status(population_size,phenotype.phenotype_jbrandao,print_type)
	status.status_function = status.status_jbrandao
	stop = Stop(n_generations, stabilization_percentage)

	population,best_fitnesses,average_fitnesses = algorithms.sea(generation.generation_binary,
		fitness.fitness,sort.sort_decrease,parents.parents_tournament,crossover.crossover,
		mutation.mutation_binary,survivors.survivors_elitism,status.status,stop.stop_best_stabilization)
	
	status.print_type = 'all'
	status.status('Final', population, best_fitnesses, average_fitnesses)
