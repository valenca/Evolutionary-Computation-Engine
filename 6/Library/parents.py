from random import sample

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
