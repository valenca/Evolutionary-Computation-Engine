from random import random

##### Individual Mutator #####
class Mutation():

	def __init__(self, population_size, individual_size, mutation_probability):
		self.population_size = population_size
		self.individual_size = individual_size
		self.mutation_probability = mutation_probability

	##### Binary genotype #####
	def mutation_binary(self, population):
		for individual in population:
			for j in range(individual_size):
				if random() < self.mutation_probability:
					individual['gen'][j] ^= 1
	###########################
