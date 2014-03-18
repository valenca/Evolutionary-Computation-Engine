from random import sample, random
from copy import deepcopy

##### Parent Crossover #####
class Crossover():

	def __init__(self, population_size, individual_size, crossover, crossover_probability):
		self.population_size = population_size
		self.individual_size = individual_size
		self.crossover = crossover
		self.crossover_probability = crossover_probability

	##### General crossover function #####
	def crossover(self, parents):
		offspring = []
		for i in range(0, len(parents)-1, 2):
			if random < crossover_probability:
				offspring1,offspring2 = self.crossover(parents[i]['gen'],parents[i+1]['gen'])
				offspring.append({'gen':offspring1})
				offspring.append({'gen':offspring2})
			else:
				offspring.append(parents[i])
				offspring.append(parents[i+1])
		return offspring
	######################################

	##### Cycle Crossover #####
	def crossover_cycle(self, parent1, parent2):
		count = 1
		mask = [0]*self.individual_size
		toggle = False
		for i in parent1:
			while mask[parent1.index(i)] == 0:
				toggle = True
				mask[parent1.index(i)] = count
				i = parent1[parent2.index(i)]
			if toggle:
				toggle = False
				count += 1
		parents = [parent1,parent2]
		offspring1 = []
		offspring2 = []
		for i in range(self.individual_size):
			offspring1.append(parents[(mask[i]+1)%2][i])
			offspring2.append(parents[(mask[i]+0)%2][i])
		return offspring1,offspring2
	###########################



