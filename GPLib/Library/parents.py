from random import sample, random

##### Parents Selection #####
class Parents():

	def __init__(self, population_size, individual_size, values):
		self.population_size = population_size
		self.individual_size = individual_size
		self.values = values
