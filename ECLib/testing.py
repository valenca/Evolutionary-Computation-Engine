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
from sys import stdout
from gc import collect

global testing_type; testing_type = 'Compare'
global testing_directory; testing_directory = 'Results/'+testing_type+'/'
global compare; compare = []

##### EDIT ONLY THIS #####
algorithms = ['sea']
n_runs = 50
n_generations = [500]
population_size = [250]
individual_size = [52]
crossover_probability = [0.9]
mutation_probability = [0.052]
disturbance_probability = [0.5]
print_type = ''
##########################
tournament_size = [3]
elite_percentage = [0.1]
n_points_cut = [2]
##########################
parents_function = ['tournament','roulette','sus']
survivors_function = ['elitism']
crossover_function = ['one_point']
##########################
# TSP #
values = {}
with open('Data/berlin52.tsp') as f:
	while f.readline() != "NODE_COORD_SECTION\n": True
	coord = [[float(string) for string in line.split()[1:]] for line in f]
	coord.pop(-1)
	values['distances'] = [[0 for j in range(len(coord))] for i in range(len(coord))]
	for i in range(len(coord)):
		for j in range(i,len(coord)):
			distance = (((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2))**(0.5)
			values['distances'][i][j] = values['distances'][j][i] = distance
##########################

def testing(n_generations, population_size, individual_size, crossover_probability, mutation_probability,
	disturbance_probability, values, parents_function, survivors_function, crossover_function, algorithm):

	generation = Generation(population_size, individual_size, values)
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
		'generation':	generation.integer,
		'fitness':		fitness.tsp,
		'phenotype':	phenotype.tsp,
		'parents':		eval('parents.'+parents_function),
		'survivors':	eval('survivors.'+survivors_function),
		'crossover':	eval('crossover.'+crossover_function),
		'mutation':		mutation.bubble_swap,
		'disturbance':	None,
		'neighbors':	None,
		'sort':			sort.minimization,
		'status':		status.tsp,
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

	seed('testing')
	results = []
	for i in range(n_runs):
		result = {}
		result['population'],result['best_fitnesses'],result['average_fitnesses']=algorithms.call(algorithm)
		results.append(result)
		collect()
		stdout.write('\rRun: ('+str(i+1)+'/'+str(n_runs)+')')
		stdout.flush()

	print('\r'+algorithm+' '+str(n_generations)+' '+str(population_size)+' '+str(individual_size)+' '+\
		str(crossover_probability)+' '+str(mutation_probability)+' '+str(disturbance_probability)+' '+\
		str(values['tournament_size'])+' '+str(values['elite_percentage'])+' '+str(values['n_points_cut'])+\
		' '+parents_function+' '+survivors_function+' '+crossover_function),

	if testing_type == 'Full':
		print('-> '+testing_directory+'test_'+str(len(listdir(testing_directory))+1)+'.out')
		with open(testing_directory+'test_'+str(len(listdir(testing_directory))+1)+'.out', 'w') as f:
			header = {'Algorithm':algorithm,
			'Number of Generations':str(n_generations),
			'Population Size':str(population_size),
			'Individual Size':str(individual_size),
			'Crossover Probability':str(crossover_probability),
			'Mutation Probability':str(mutation_probability),
			'Disturbance Probability':str(disturbance_probability),
			'Tournament Size':str(values['tournament_size']),
			'Elite Percentage':str(values['elite_percentage']),
			'Number of Points Cut':str(values['n_points_cut']),
			'Parents Function':parents_function,
			'Survivors Function':survivors_function,
			'Crossover Function':crossover_function}
			dump(header, f)
			dump(results, f)
	elif testing_type == 'Compare':
		print('\n'),
		results = [result['best_fitnesses'] for result in results]
		means = [0]*(n_generations+1)
		for i in range(n_runs):
			for j in range(n_generations+1):
				means[j] += results[i][j]
		for i in range(n_generations+1):
			means[i] /= float(n_runs)
		compare.append(means)

if __name__ == '__main__':

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

	if testing_type == 'Compare':
		print('-> '+testing_directory+'compare_'+str(len(listdir(testing_directory))+1)+'.csv')
		with open(testing_directory+'compare_'+str(len(listdir(testing_directory))+1)+'.csv', 'w') as f:
			compare = zip(*compare)
			[f.write(','.join(map(str,line))+'\n') for line in compare]
