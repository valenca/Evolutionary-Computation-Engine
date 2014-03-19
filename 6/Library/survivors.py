##### Survivors Selection #####
class Survivors():

	def __init__(self, population_size, values):
		self.population_size = population_size
		self.values = values

	##### Best #####
	def best(self, population, candidates):
		if population[0]['fit'] > candidates[0]['fit']:
			return [population[0]]
		else:
			return [candidates[0]]
	################

	##### Generational #####
	def generational(self, population, candidates):
		return candidates
	#################

	##### Elite #####
	def elitism(self, population, candidates):
		elite_size = int(self.population_size * self.values['elite_percentage'])
		if elite_size > 0:
			return population[:elite_size] + candidates[:-elite_size]
		else:
			return candidates
	#################
