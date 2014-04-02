from random import random, gauss, sample, choice, randint, shuffle
from string import printable
from copy import deepcopy

##### Individual Mutator #####
class Mutation():

	def __init__(self, individual_size, mutation_probability, values):
		self.individual_size = individual_size
		self.mutation_probability = mutation_probability
		self.values = values

	##### Point #####
	def point(self, population):
		for individual in population:
			individual['gen'] = self.point_node(individual['gen'])
	
	def point_node(self, genotype):
		if random() < self.mutation_probability:
			if isinstance(genotype, list):
				function_set = [i for i in self.values['function_set'] if i[0] != genotype[0] and i[1] == len(genotype[1:])]
				if not function_set: function = [genotype[0], len(genotype[1:])]
				else: function = choice(function_set)
				return [function[0]] + [self.point_node(son) for son in genotype[1:]]
			elif isinstance(genotype, (float,int,str)):
				terminal = genotype
				while terminal == genotype:
					terminal = choice(self.values['terminal_set'])
				if callable(terminal): return terminal(-5,5)
				else: return terminal
		else:
			return genotype
	#################
