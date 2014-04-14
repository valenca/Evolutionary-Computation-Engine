from sys import stdout

##### Population Generator #####
class Generation():

	def __init__(self, population_size, individual_size, values):
		self.population_size = population_size
		self.individual_size = individual_size
		self.values = values
		self.individuals_function = None
		self.distance_function = None

	##### Random Uniform Sampling #####
	def rus(self):
		return [self.individuals_function() for i in range(self.population_size)]
	###################################

	##### Sequencial Diversification #####
	def sd(self):
		population = []
		for i in range(self.population_size):
			stdout.write('\rSD Generation: ('+str(i)+'/'+str(self.population_size)+')')
			stdout.flush()
			while True:
				candidate = self.individuals_function()
				if self.acceptance(population, candidate): break
			population.append(candidate)
		return population

	def acceptance(self, population, candidate):
		for individual in population:
			if self.distance_function(individual['gen'],candidate['gen']) < self.values['generation_distance']:
				return False
		return True
	######################################

	##### Parallel Diversification #####
	def pd(self):
		pass
	####################################
