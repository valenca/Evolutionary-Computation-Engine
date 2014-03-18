from random import sample, random

##### Parents Selection #####
class Parents():

	def __init__(self, population_size, individual_size, tournament_size):
		self.population_size = population_size
		self.individual_size = individual_size
		self.tournament_size = tournament_size

	##### Tournament #####
	def parents_tournament(self, population):
		parents = []
		for i in range(self.population_size):
			t_parents = sample(list(range(self.population_size)), self.tournament_size)
			parents.append(population[min(t_parents)])
		return parents
	################

	##### Roulette Wheel #####
	def parents_roulette(self, population):
		parents = []
		fitnesses = [individual['fit'] for individual in population]
		total_fitness = sum(fitnesses)
		for i in range(self.population_size):
			target = random()*total_fitness
			index = 0
			while target > 0:
				target -= fitnesses[i]
				index += 1
			parents.append(population[index])
		return parents
	##########################
