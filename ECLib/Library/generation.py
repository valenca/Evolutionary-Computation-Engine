from random import choice, sample, random
from string import letters, printable

##### Population Generator #####
class Generation():

	def __init__(self, population_size, individual_size):
		self.population_size = population_size
		self.individual_size = individual_size

	##### Binary genotype #####
	def binary(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen':[choice([0,1]) for j in range(self.individual_size)]})
		return population
	###########################

	##### Integer genotype #####
	def integer(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen': sample(range(self.individual_size),self.individual_size)})
		return population
	############################

	##### Float genotype #####
	def float(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen': [random() for j in range(self.individual_size)]})
		return population
	##########################

	##### Character genotype #####
	def character(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen': [choice(letters[:26]) for j in range(self.individual_size)]})
		return population
	##############################

	##### Methinks #####
	def methinks(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen': [choice(printable) for j in range(self.individual_size)]})
		return population
	####################

	##### Rastrigin #####
	def rastrigin(self):
		population = []
		for i in range(self.population_size):
			population.append({'gen': [random()*10.24-5.12 for j in range(self.individual_size)]})
		return population
	#####################

