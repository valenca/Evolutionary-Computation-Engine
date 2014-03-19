##### Population Analyzer #####
from sys import stdout as out
from math import ceil,floor
class Status():

	def __init__(self, n_generations, population_size, print_type):
		self.n_generations = n_generations
		self.population_size = population_size
		self.print_type = print_type
		self.phenotype = None
		self.status_function = None

	##### General status function #####
	def status(self, generation, population, best_fitnesses, average_fitnesses):

		best_fitnesses.append(population[0]['fit'])
		average_fitnesses.append(sum([individual['fit'] for individual in population])/self.population_size)

		if 'phen' not in population[0]:
			population[0]['phen'] = self.phenotype(population[0]['gen'])
			
		if self.print_type == 'bar':
			length=40
			pcurr=length*(generation+1)/self.n_generations
			ptotal=length
			subprog=pcurr
			clean="\r"
			bar="["+("#"*int(ceil(pcurr)))+("-"*int(floor(ptotal-pcurr)))+"]"
			perc=" ("+str(generation+1)+"/"+str(self.n_generations)+") "
			bfit="Best: "+str('%.8f'%best_fitnesses[-1])+ " "
			afit="Avg: " +str('%.8f'%average_fitnesses[-1])+ " "

			out.write(clean+bar+perc+bfit+afit)
			out.flush()

		if self.print_type == 'iter':
			print str(generation)
		
		elif self.print_type == 'fit':
			print str(generation) + " "+str('%.8f'%best_fitnesses[-1]) + " " + str('%.8f'%average_fitnesses[-1])

		elif self.print_type == 'all':
			print "\n>>" + str(generation) + ": "+str('%.8f'%best_fitnesses[-1]) + " | " + str('%.8f'%average_fitnesses[-1]+"\n\n")
			print str(population[0]['phen'])
			self.status_function(population, best_fitnesses, average_fitnesses)

			
	###################################

	##### Joao Brandao Numbers ######
	def jbrandao(self, population, best_fitnesses, average_fitnesses):
		print("     Value: " + str(sum(population[0]['gen'])))
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
