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
from os import listdir
from cPickle import dump

def testing(n_generations, population_size, individual_size, crossover_probability, mutation_probability,
	disturbance_probability, values, parents_function, survivors_function, crossover_function, algorithm):

	generation = Generation(population_size, individual_size)
	fitness = Fitness(individual_size,values)
	phenotype = Phenotype(individual_size, values)
	parents = Parents(population_size, individual_size, values)
	survivors = Survivors(population_size, values)
	crossover = Crossover(individual_size,crossover_probability, values)
	mutation = Mutation(individual_size, mutation_probability, values)
	disturbance = Mutation(individual_size, disturbance_probability, values)
	neighbors = Neighbors(individual_size, values)
	sort = Sort()
	status = Status(n_generations, population_size, individual_size, print_type)
	stop = Stop(n_generations, values)

	functions = {
		'generation':	generation.rastrigin,
		'fitness':		fitness.rastrigin,
		'phenotype':	phenotype.rastrigin,
		'parents':		eval('parents.'+parents_function),
		'survivors':	eval('survivors.'+survivors_function),
		'crossover':	eval('crossover.'+crossover_function),
		'mutation':		mutation.rastrigin,
		'disturbance':	disturbance.rastrigin,
		'neighbors':	neighbors.rastrigin,
		'sort':			sort.minimization,
		'status':		status.rastrigin,
		'stop':			stop.nothing
	}

	fitness.fitness_function = functions['fitness']
	crossover.crossover_function = functions['crossover']
	status.status_function = functions['status']
	status.phenotype_function = functions['phenotype']
	survivors.sort_function = functions['sort']

	algorithms = Algorithms(n_generations,functions['generation'],fitness.fitness,functions['sort'],
		functions['neighbors'],functions['parents'],crossover.crossover,functions['mutation'],
		functions['disturbance'],functions['survivors'],status.status,functions['stop'])

	results = {}
	results['population'],results['best_fitnesses'],results['average_fitnesses']=algorithms.call(algorithm)

	print(algorithm+' '+str(n_generations)+' '+str(population_size)+' '+str(individual_size)+' '+\
		str(crossover_probability)+' '+str(mutation_probability)+' '+str(disturbance_probability)+' '+\
		str(values['tournament_size'])+' '+str(values['elite_percentage'])+' '+str(values['n_points_cut'])+\
		' '+parents_function+' '+survivors_function+' '+crossover_function)

	#with open(algorithm+' '+str(n_generations)+' '+str(population_size)+' '+str(individual_size)+' '+\
	#	str(crossover_probability)+' '+str(mutation_probability)+' '+str(disturbance_probability)+' '+\
	#	str(values['tournament_size'])+' '+str(values['elite_percentage'])+' '+str(values['n_points_cut'])+\
	#	' '+parents_function+' '+survivors_function+' '+crossover_function, 'w') as f:
	#	pass

	testing_directory = 'Results/Full/'
	with open(testing_directory+'test_'+str(len(listdir(testing_directory))+1)+'.out', 'w') as f:
		dump(results, f)

if __name__ == '__main__':

	##########################
	algorithms = ['sea']
	n_generations = [500]
	population_size = [500]
	individual_size = [10]
	crossover_probability = [0.9]
	mutation_probability = [0.1,0.2]
	disturbance_probability = [0.5]
	print_type = ''
	##########################
	tournament_size = [3]
	elite_percentage = [0.1]
	n_points_cut = [2]
	##########################
	# Rastrigin #
	values = {}
	values['A'] = 10
	values['sigma'] = 0.4
	##########################
	parents_function = ['tournament']
	survivors_function = ['elitism']
	crossover_function = ['one_point']

	for algorithm in algorithms:
		for generation in n_generations:
			for population in population_size:
				for individual in individual_size:
					for crossover in crossover_probability:
						for mutation in mutation_probability:
							for disturbance in disturbance_probability:
								for tournament in tournament_size:
									for elite in elite_percentage:
										for n_points in n_points_cut:
											for parents_f in parents_function:
												for survivors_f in survivors_function:
													for crossover_f in crossover_function:
														values['tournament_size'] = tournament
														values['elite_percentage'] = elite
														values['n_points_cut'] = n_points
														testing(generation,population,individual,crossover,
															mutation,disturbance,values,parents_f,survivors_f,
															crossover_f,algorithm)
