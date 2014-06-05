##### Survivors Selection #####
class Survivors():

	def __init__(self, population_size, values):
		self.population_size = population_size
		self.values = values
		self.sort_function = None

	##### Best #####
	def best(self, population, candidates):
		temp = [population[0]] + [candidates[0]]
		self.sort_function(temp)
		return [temp[0]]
	################

	##### Generational #####
	def generational(self, population, candidates):
		return candidates
	########################

	##### Elite #####
	def elitism(self, population, candidates):
		elite_size = int(self.population_size * self.values['elite_percentage'])
		if elite_size > 0:
			return population[:elite_size] + candidates[:-elite_size]
		else:
			return candidates
	#################

	##### Worst Out #####
	def worst_out(self, population, candidates):
		worst_size = int(self.population_size * self.values['worst_percentage'])
		if worst_size > 0:
			return population[:-worst_size] + candidates[:worst_size]
		else:
			return population
	#####################

	##### Steady-State #####
	def steady_state(self, population, candidates):
		temp = population + candidates
		self.sort_function(temp)
		return temp[:self.population_size]
	########################
