from random import random, gauss, sample, choice, randint, shuffle
from string import letters

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

	##### Swap Values #####
	def swap(self, population):
		for individual in population:
			for j in range(0,self.individual_size-1,2):
				if random() < self.mutation_probability:
					individual['gen'][j],individual['gen'][j+1] = individual['gen'][j+1],individual['gen'][j]
	#######################

	##### Insert #####
	def insert(self, population):
		for individual in population:
			for j in range(self.individual_size):
				if random() < self.mutation_probability:
					value = individual['gen'].pop(j)
					individual['gen'].insert(randint(0,self.individual_size-2), value)
	##################

	##### Scramble #####
	def scramble(self, population):
		for individual in population:
			if random() < self.mutation_probability:
				indexes = sample(list(range(self.individual_size)),2)
				if indexes[1] < indexes[0]:
					indexes[0],indexes[1] = indexes[1],indexes[0]
				temp = individual['gen'][indexes[0]:indexes[1]]
				shuffle(temp)
				individual['gen'][indexes[0]:indexes[1]] = temp
	####################

	##### Methinks ######
	def methinks(self, population):
		characters = letters + ' '
		for individual in population:
			for j in range(self.individual_size):
				if random() < self.mutation_probability:
					if individual['gen'][j] == characters[0]:
						individual['gen'][j] = characters[1]
					elif individual['gen'][j] == characters[-1]:
						individual['gen'][j] = characters[-2]
					else:
						individual['gen'][j]=characters[characters.index(individual['gen'][j])+choice([-1,1])]
	#####################

	##### Rastrigin #####
	def rastrigin(self, population):
		for individual in population:
			for j in range(self.individual_size):
				if random() < self.mutation_probability:
					individual['gen'][j] += gauss(0, self.values['sigma'])
					if individual['gen'][j] > 5.12: individual['gen'][j] = 5.12
					elif individual['gen'][j] < -5.12: individual['gen'][j] = -5.12
	#####################

	##### ILS Special #####
	def ils(self, population, mutation_probability):
		temp = self.mutation_probability
		self.mutation_probability = mutation_probability
		self.methinks(population)
		self.mutation_probability = temp
	#######################
