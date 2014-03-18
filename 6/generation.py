from random import choice, sample, random
from string import letters

##### Population Generator #####
class Generation():

	def __init__(self, population_size, individual_size):
		self.population_size = population_size
		self.individual_size = individual_size

	##### Binary genotype #####
	def generation_binary(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen':[choice([0,1]) for j in range(self.individual_size)]})
		return population
	###########################

	##### Integer genotype #####
	def generation_integer(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen': sample(range(self.individual_size),self.individual_size)})
		return population
	############################

	##### Float genotype #####
	def generation_float(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen': [random() for j in range(self.individual_size)]})
		return population
	##########################

	##### Character genotype #####
	def generation_character(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen': [choice(letters[:26]) for j in range(self.individual_size)]})
		return population
	##############################
