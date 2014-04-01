from math import cos, pi
from string import printable

##### Individual Evaluator #####
class Fitness():

	def __init__(self, individual_size, values):
		self.individual_size = individual_size
		self.values = values
		self.fitness_function = None

	##### General fitness function #####
	def fitness(self, population):
		for individual in population:
			if 'fit' not in individual:
				individual['fit'] = self.fitness_function(individual['gen'])
	####################################
