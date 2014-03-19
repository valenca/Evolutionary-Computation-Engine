##### Individual Evaluator #####
class Fitness():

	def __init__(self, individual_size, values):
		self.individual_size = individual_size
		self.values = values
		self.fitness_function = None

	##### General fitness function #####
	def fitness(self, population):
		for individual in population:
			if 'fit' not in individual:
				individual['fit'] = self.fitness_function(individual['gen'])
	####################################

	##### Joao Brandao Numbers ######
	def fitness_jbrandao(self, genotype):
		violations = 0;
		for i in range(self.individual_size):
			if genotype[i] == 1:
				for j in range(1,min(i+1, self.individual_size-i)):
					if genotype[i-j] == genotype[i+j] == 1:
						violations += 1;
		return 1.5*sum(genotype) + (-1)*violations
	#################################

	##### Knapsack ######
	def fitness_knapsack(self, genotype):
		total_weight = 0; total_values = 0
		for i in range(self.individual_size):
			if genotype[i] == 1:
				total_weight += self.values['weights'][i]
				total_values += self.values['values'][i]
		if total_weight > self.values['max_weight']:
			return (0, total_weight - self.values['max_weight'])
		else:
			return (total_values, total_weight - self.values['max_weight'])
	#####################

	##### Traveling Salesman Problem #####
	def fitness_tsp(self, genotype):
		total_distance = 0
		for i in range(self.individual_size-1):
			total_distance += self.values['distances'][genotype[i]][genotype[i+1]]
		total_distance += self.values['distances'][genotype[-1]][genotype[0]]
		return total_distance
	######################################
