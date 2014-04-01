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
