from sys import stdout
from math import ceil, floor
from cPickle import dump
##### Population Analyzer #####
class Status():

	def __init__(self, n_generations, population_size, individual_size, print_type):
		self.n_generations = n_generations
		self.population_size = population_size
		self.individual_size = individual_size
		self.print_type = print_type
		self.phenotype_function = None
		self.status_function = None

	##### General status function #####
	def status(self, generation, population, best_fitnesses, average_fitnesses):

		best_fitnesses.append(population[0]['fit'])
		average_fitnesses.append(sum([individual['fit'] for individual in population])/self.population_size)

		if 'phen' not in population[0]:
			population[0]['phen'] = self.phenotype_function(population[0]['gen'])

		if self.print_type == 'iter':
			stdout.write('\rIteration: ('+str(generation)+'/'+str(self.n_generations)+') ')
			stdout.flush()
		
		elif self.print_type == 'fit':
			stdout.write('\rFitness: '+str(best_fitnesses[-1])+' / '+str(average_fitnesses[-1]))
			stdout.flush()

		elif self.print_type == 'info':			
			stdout.write('\rIteration: ('+str(generation)+'/'+str(self.n_generations)+') ')
			stdout.write('Fitness: '+str(best_fitnesses[-1])+' / '+str(average_fitnesses[-1]))
			stdout.flush()
			
		elif self.print_type == 'bar':
			length=40
			pcurr=int((length*generation*1.0/self.n_generations)+0.5)
			#if pcurr - int((length*(generation-1)*1.0/self.n_generations)+0.5) > 0 or generation == 0:
			ptotal=length
			clean='\r'
			bar='['+('#'*pcurr)+('-'*(ptotal-pcurr))+']'
			perc=' ('+str(generation)+'/'+str(self.n_generations)+') '
			bfit='Best: '+str(best_fitnesses[-1])+' '
			afit='Avg: '+str(average_fitnesses[-1])+' '
			stdout.write(clean+bar+perc+bfit+afit)
			stdout.flush()

		elif self.print_type == 'all':
			stdout.write('\nIteration: ('+str(generation)+'/'+str(self.n_generations)+')\n')
			stdout.write('     Best: '+str(best_fitnesses[-1])+'\n')
			stdout.write('  Average: '+str(average_fitnesses[-1])+'\n')
			stdout.write('Phenotype: '+str(population[0]['phen'])+'\n')
			stdout.flush()

		self.status_function(population, best_fitnesses, average_fitnesses)
			
	###################################

	##### Onemax #####
	def onemax(self, population, best_fitnesses, average_fitnesses):
		pass
	##################

	##### Methinks ######
	def methinks(self, population, best_fitnesses, average_fitnesses):
		pass
	#####################

	##### Joao Brandao Numbers ######
	def jbrandao(self, population, best_fitnesses, average_fitnesses):
		if self.print_type == 'all':
			stdout.write('    Value: '+str(sum(population[0]['gen']))+'\n')
			violations_t = 0;
			violations = 0;
			for i in range(self.individual_size):
				if population[0]['gen'][i] == 1:
					flag = 0
					for j in range(1,min(i+1, self.individual_size-i)):
						if population[0]['gen'][i-j] == population[0]['gen'][i+j] == 1:
							violations_t += 1;
							if flag == 0: violations += 1; flag=1
			stdout.write('Violation: '+str(violations)+' '+str(violations_t)+'\n')
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

	##### Griewank #####
	def griewank(self, population, best_fitnesses, average_fitnesses):
		pass
	####################

	##### Dispersion Problem #####
	def dispersion(self, population, best_fitnesses, average_fitnesses):
		with open('Results/scatter.plt','a') as f:
			dump(population[0]['phen'],f)
	##############################
