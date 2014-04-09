from random import random, gauss, sample, choice, randint, shuffle
from string import printable

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

	##### Bubble Swap #####
	def bubble_swap(self, population):
		for individual in population:
			if random() < 0.5:
				iterations = list(range(0,self.individual_size-1,2))
			else:
				iterations = range(1,self.individual_size,2)
			for j in iterations:
				if random() < self.mutation_probability:
					individual['gen'][j],individual['gen'][j+1] = individual['gen'][j+1],individual['gen'][j]
	#######################

	##### Swap Different Values #####
	def swap(self, population):
		for individual in population:
			if random() < self.mutation_probability:
				indexes = [0, 0]
				while individual['gen'][indexes[0]] == individual['gen'][indexes[1]]:
					indexes = sorted(sample(list(range(self.individual_size)),2))
				individual['gen'][indexes[0]],individual['gen'][indexes[1]] =\
				individual['gen'][indexes[1]],individual['gen'][indexes[0]]
	#################################

	##### Swap Different Values Optimized for binaries #####
	def swap_bin(self, population):
		for individual in population:
			if random() < self.mutation_probability:
				tmp=sample(list(range(self.individual_size)),self.individual_size)
				ind1=individual['gen'][tmp[0]]
				ind2=individual['gen'][tmp[1]]
				i=2
				while ind2==ind1:
					ind2=individual['gen'][tmp[i]]
					i+=1

				individual['gen'][ind1],individual['gen'][ind2] =\
				individual['gen'][ind2],individual['gen'][ind1]
	#########################################################

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
				indexes = sorted(sample(list(range(self.individual_size)),2))
				temp = individual['gen'][indexes[0]:indexes[1]]
				shuffle(temp)
				individual['gen'][indexes[0]:indexes[1]] = temp
	####################

	##### Methinks ######
	def methinks(self, population):
		for individual in population:
			for j in range(self.individual_size):
				if random() < self.mutation_probability:
					if individual['gen'][j] == printable[0]:
						individual['gen'][j] = printable[1]
					elif individual['gen'][j] == printable[-1]:
						individual['gen'][j] = printable[-2]
					else:
						individual['gen'][j]=printable[printable.index(individual['gen'][j])+choice([-1,1])]
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
