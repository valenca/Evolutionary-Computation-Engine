from copy import deepcopy
from random import gauss

##### Neighbors Generator #####
class Neighbors():

	def __init__(self, individual_size, values):
		self.individual_size = individual_size
		self.values = values

	##### Binary genotype #####
	def binary(self, individual):
		neighbors = []
		for i in range(self.individual_size):
			neighbor = {'gen':deepcopy(individual['gen'])}
			neighbor['gen'][i] ^= 1
			neighbors.append(neighbor)
		return neighbors
	###########################

	##### Rastrigin #####
	def rastrigin(self, individual):
		neighbors = []
		for i in range(self.individual_size):
			neighbor = {'gen':deepcopy(individual['gen'])}
			neighbor['gen'][i] += gauss(0, self.values['sigma'])
			if neighbor['gen'][i] > 5.12: neighbor['gen'][i] = 5.12
			elif neighbor['gen'][i] < -5.12: neighbor['gen'][i] = -5.12
			neighbors.append(neighbor)
		return neighbors
	#####################
