##### Population Analyzer #####
class Status():

	def __init__(self, population_size, individual_size, status, values):
		self.population_size = population_size
		self.individual_size = individual_size
		self.status = status
		self.values = values

	##### General status function #####
	def status(self, generation, population, best_fitnesses, average_fitnesses):

		best_fitnesses.append(population[0]['fit'])
		average_fitnesses.append(sum([individual['fit'] for individual in population])/self.population_size)

		if 'phen' not in population[0]:
			population[0]['phen'] = self.phenotype(population[0]['gen'])

		print("####### " + str(generation) + " #######")
		print("Individual: " + str(population[0]['phen']))
		print("   Fitness: " + str(best_fitnesses[-1]) + " / " + str(average_fitnesses[-1]))
		self.status(population, best_fitnesses, average_fitnesses)
	###################################

	##### Joao Brandao Numbers ######
	def status_jbrandao(self, population, best_fitnesses, average_fitnesses):
		print("     Value: " + str(sum(population[0]['gen'])))
	#################################

	##### Knapsack ######
	def status_knapsack(self, population, best_fitnesses, average_fitnesses):
		pass
	#####################

	##### Traveling Salesman Problem #####
	def status_tsp(self, population, best_fitnesses, average_fitnesses):
		pass
	######################################
