
##### Joao Brandao Numbers Problem #####
class JBrandao():

	def __init__(self, population_size, individual_size):
		self.population_size = population_size
		self.individual_size = individual_size

	##### Population Generator #####
	def generation(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen':[choice([0,1]) for j in range(self.individual_size)]})
		return population
	################################

	##### Individual Evaluator #####
	def fitness(self, population):
		for individual in population:
			if 'fit' not in individual:
				individual['fit'] = self._fitness(individual['gen'])

	def _fitness(self, genotype):
		violations = 0;
		for i in range(self.individual_size):
			if genotype[i] == 1:
				for j in range(1,min(i+1, self.individual_size-i)):
					if genotype[i-j] == genotype[i+j] == 1:
						violations += 1;
		return 1.5*sum(genotype) + (-1)*violations
	################################

	##### Population Analyzer #####
	def get_status(self, i, population, best_fitnesses, average_fitnesses):

		best_fitnesses.append(population[0]['fit'])
		average_fitnesses.append(sum([individual['fit'] for individual in population])/self.population_size)

		if 'phen' not in population[0]:
			population[0]['phen'] = self.phenotype(population[0]['gen'])

		print("####### " + str(i) + " #######")
		print("Individual: " + str(population[0]['phen']))
		print("   Fitness: " + str(best_fitnesses[-1]) + " / " + str(average_fitnesses[-1]))
		print("     Value: " + str(sum(population[0]['gen'])))
		#print("Violations: " + str((fitness(individual[0])[1])))
	###############################
