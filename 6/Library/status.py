##### Population Analyzer #####
class Status():

	def __init__(self, population_size, print_type):
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
			
		if(self.print_type == 'iter'):
			print("####### " + str(generation) + " #######")
		elif(self.print_type == 'all'):
			print("####### " + str(generation) + " #######")
			print("Individual: " + str(population[0]['phen']))
			print("   Fitness: " + str(best_fitnesses[-1]) + " / " + str(average_fitnesses[-1]))
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
