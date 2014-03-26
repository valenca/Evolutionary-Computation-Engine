from sys import stdout
from math import ceil, floor

##### Population Analyzer #####
class Status():

	def __init__(self, n_generations, population_size, print_type):
		self.n_generations = n_generations
		self.population_size = population_size
		self.print_type = print_type
		self.phenotype_function = None
		self.status_function = None

	##### General status function #####
	def status(self, generation, population, best_fitnesses, average_fitnesses):

		best_fitnesses.append(population[0]['fit'])
		average_fitnesses.append(sum([individual['fit'] for individual in population])/self.population_size)

		if 'phen' not in population[0]:
			population[0]['phen'] = self.phenotype_function(population[0]['gen'])
			
		if self.print_type == 'bar':
			length=40
			pcurr=int((length*generation*1.0/self.n_generations)+0.5)
			ptotal=length
			clean='\r'
			bar='['+('#'*pcurr)+('-'*(ptotal-pcurr))+']'
			perc=' ('+str(generation)+'/'+str(self.n_generations)+') '
			bfit='Best: '+str(best_fitnesses[-1])+' '
			afit='Avg: '+str(average_fitnesses[-1])+' '
			stdout.write(clean+bar+perc+bfit+afit)
			stdout.flush()

		if self.print_type == 'iter':
			stdout.write('\rIteration: ('+str(generation)+'/'+str(self.n_generations)+') ')
			stdout.flush()
		
		elif self.print_type == 'fit':
			stdout.write('\rFitness: '+str(best_fitnesses[-1])+' / '+str(average_fitnesses[-1]))
			stdout.flush()

		elif self.print_type == 'all':
			stdout.write('\nIteration: ('+str(generation)+'/'+str(self.n_generations)+')\n')
			stdout.write('     Best: '+str(best_fitnesses[-1])+'\n')
			stdout.write('  Average: '+str(average_fitnesses[-1])+'\n')
			stdout.write('Phenotype: '+str(population[0]['phen'])+'\n')
			self.status_function(population, best_fitnesses, average_fitnesses)
			stdout.flush()

			
	###################################

	##### Joao Brandao Numbers ######
	def jbrandao(self, population, best_fitnesses, average_fitnesses):
		stdout.write('    Value: '+str(sum(population[0]['gen']))+'\n')
	#################################

	##### Knapsack ######
	def knapsack(self, population, best_fitnesses, average_fitnesses):
		pass
	#####################

	##### Traveling Salesman Problem #####
	def tsp(self, population, best_fitnesses, average_fitnesses):
		pass
	######################################

	##### Rastrigin #####
	def rastrigin(self, population, best_fitnesses, average_fitnesses):
		pass
	#####################
