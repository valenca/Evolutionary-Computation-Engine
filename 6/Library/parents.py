from random import sample, random

##### Parents Selection #####
class Parents():

	def __init__(self, population_size, individual_size, values):
		self.population_size = population_size
		self.individual_size = individual_size
		self.values = values

	##### Tournament #####
	def tournament(self, population):
		parents = []
		for i in range(self.population_size):
			t_parents = sample(list(range(self.population_size)), self.values['tournament_size'])
			parents.append(population[min(t_parents)])
		return parents
	################

	##### Roulette Wheel #####
	def roulette(self, population):
		parents = []
		fitnesses = [individual['fit'] for individual in population]
		total_fitness = sum(fitnesses)
		for i in range(self.population_size):
			target = random()*total_fitness
			index = 0
			while target > 0:
				target -= fitnesses[index]
				index += 1
			parents.append(population[index-1])
		return parents
	##########################

	##### Stochastic Universal Sampling #####
	def sus(self, population):
		parents = []
		fitnesses = [individual['fit'] for individual in population]
		total_fitness = sum(fitnesses)
		distance = float(total_fitness) / self.population_size
		start = random() * distance
		values = [start + i*distance for i in range(self.population_size)]
		target = fitnesses[0]
		index = 0
		for value in values:
			while target < value:
				index += 1
				target += fitnesses[index]
			parents.append(population(index))
		return parents
	#########################################
