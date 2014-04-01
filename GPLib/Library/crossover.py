from random import sample, random, randint, choice
from copy import deepcopy

##### Parent Crossover #####
class Crossover():

	def __init__(self, individual_size, crossover_probability, values):
		self.individual_size = individual_size
		self.crossover_probability = crossover_probability
		self.values = values
		self.crossover_function = None

	##### General crossover function #####
	def crossover(self, parents):
		offspring = []
		for i in range(0, len(parents)-1, 2):
			if random() < self.crossover_probability:
				offspring1,offspring2 = self.crossover_function(parents[i]['gen'],parents[i+1]['gen'])
				offspring.append({'gen':offspring1})
				offspring.append({'gen':offspring2})
			else:
				offspring.append(deepcopy(parents[i]))
				offspring.append(deepcopy(parents[i+1]))
		return offspring
	######################################
