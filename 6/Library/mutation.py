from random import random, gauss

##### Individual Mutator #####
class Mutation():

	def __init__(self, individual_size, mutation_probability, values):
		self.individual_size = individual_size
		self.mutation_probability = mutation_probability
		self.values = values

	##### Binary genotype #####
	def binary(self, population):
		for individual in population:
			for j in range(self.individual_size):
				if random() < self.mutation_probability:
					individual['gen'][j] ^= 1
	###########################

	##### Float genotype #####
	def float(self, population):
		for individual in population:
			for j in range(self.individual_size):
				if random() < self.mutation_probability:
					individual['gen'][j] += gauss(0, self.values['sigma'])
	##########################

	##### Rastrigin #####
	def rastrigin(self, population):
		for individual in population:
			for j in range(self.individual_size):
				if random() < self.mutation_probability:
					individual['gen'][j] += gauss(0, self.values['sigma'])
					if individual['gen'][j] > 5.12: individual['gen'][j] = 5.12
					elif individual['gen'][j] < -5.12: individual['gen'][j] = -5.12
	#####################
