from copy import deepcopy

##### Neighbors Generator #####
class Neighbors():

	def __init__(self, population_size, individual_size):
		self.population_size = population_size
		self.individual_size = individual_size

	##### Binary genotype #####
	def neighbors_binary(self, individual):
		neighbors = []
		for i in range(self.individual_size):
			neighbor = {'gen':deepcopy(individual['gen'])}
			neighbor['gen'][i] ^= 1
			neighbors.append(neighbor)
		return neighbors
	###########################
