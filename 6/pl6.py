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

from random import uniform, seed

if __name__ == '__main__':

	n_runs = 1
	n_generations = 5000
	population_size = 1000
	individual_size = 10
	crossover_probability = 0.9
	mutation_probability = 0.1
	print_type = 'machine'

	values = {}

	values['tournament_size'] = 3
	values['stabilise_percentage'] = 1
	values['elite_percentage'] = 0.1

	#seed("knapsack")
	v = 10
	r = 5
	#NC
	#values['weights'] = [int(uniform(0, v)) for i in range(individual_size)]
	#values['values'] = [int(uniform(0, v)) for i in range(individual_size)]
	#WC
	#values['weights'] = [int(uniform(0, v)) for i in range(individual_size)]
	#values['values'] = [values['weights'][i] + int(uniform(0, v)) for i in range(individual_size)]
	#SC
	values['weights'] = [int(uniform(0, v)) for i in range(individual_size)]
	values['values'] = [values['weights'][i] + r for i in range(individual_size)]
	#
	values['max_weight'] = sum(values['weights'])/2
	#seed()

	values['A'] = 10
	values['sigma'] = 0.4

	algorithms = Algorithms(n_generations)
	generation = Generation(population_size, individual_size)
	fitness = Fitness(individual_size,values)
	phenotype = Phenotype(individual_size, values)
	parents = Parents(population_size, individual_size, values)
	survivors = Survivors(population_size, values)
	crossover = Crossover(individual_size,crossover_probability)
	mutation = Mutation(individual_size, mutation_probability, values)
	neighbors = Neighbors(individual_size)
	sort = Sort()
	status = Status(population_size,print_type)
	stop = Stop(n_generations, values)

	database = {
		'jbrandao':
			{
				'generation':	generation.binary,
				'fitness':		fitness.jbrandao,
				'phenotype':	phenotype.jbrandao,
				'parents':		parents.tournament,
				'survivors':	survivors.elitism,
				'crossover':	crossover.one_point,
				'mutation':		mutation.binary,
				'neighbors':	None,
				'sort':			sort.decrease,
				'status':		status.jbrandao,
				'stop':			stop.best_stabilisation
			},

		'knapsack':
			{
				'generation':	generation.binary,
				'fitness':		fitness.knapsack,
				'phenotype':	phenotype.knapsack,
				'parents':		parents.tournament,
				'survivors':	survivors.elitism,
				'crossover':	crossover.one_point,
				'mutation':		mutation.binary,
				'neighbors':	None,
				'sort':			sort.decrease,
				'status':		status.knapsack,
				'stop':			stop.best_stabilisation
			},
		'rastrigin':
			{
				'generation':	generation.rastrigin,
				'fitness':		fitness.rastrigin,
				'phenotype':	phenotype.rastrigin,
				'parents':		parents.tournament,
				'survivors':	survivors.elitism,
				'crossover':	crossover.one_point,
				'mutation':		mutation.float,
				'neighbors':	None,
				'sort':			sort.increase,
				'status':		status.rastrigin,
				'stop':			stop.best_stabilisation
			}#,
		#'tsp':
		#	{
		#		'generation':	generation.integer,
		#		'fitness':		fitness.tsp,
		#		'phenotype':	phenotype.tsp,
		#		'parents':		parents.tournament,
		#		'survivors':	survivors.elitism,
		#		'crossover':	crossover.pmx,
		#		'mutation':		mutation.switch,
		#		'neighbors':	None,
		#		'sort':			sort.decrease,
		#		'status':		status.tsp,
		#		'stop':			stop.best_stabilisation
		#	}
		}

	problem = database['rastrigin']

	fitness.fitness_function = problem['fitness']
	crossover.crossover_function = problem['crossover']
	status.status_function = problem['status']
	status.phenotype = problem['phenotype']

	results = {}
	results['population'],results['best_fitnesses'],results['average_fitnesses'] = \
	algorithms.sea(problem['generation'],fitness.fitness,problem['sort'],problem['parents'],
		crossover.crossover,problem['mutation'],problem['survivors'],status.status,problem['stop'])
	
	status.print_type = 'all'
	status.status('Final', results['population'],results['best_fitnesses'],results['average_fitnesses'])
	print "Generations:", len(results['best_fitnesses'])
	#with open("outfile")
