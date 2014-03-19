from random import random

##### Individual Mutator #####
class Mutation():

	def __init__(self, individual_size, mutation_probability):
		self.individual_size = individual_size
		self.mutation_probability = mutation_probability

	##### Binary genotype #####
	def binary(self, population):
		for individual in population:
			for j in range(self.individual_size):
				if random() < self.mutation_probability:
					individual['gen'][j] ^= 1
	###########################
