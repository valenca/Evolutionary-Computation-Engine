from random import choice, sample, random
from string import letters, printable

##### Population Generator #####
class Generation():

	def __init__(self, population_size, individual_size, values):
		self.population_size = population_size
		self.individual_size = individual_size
		self.values = values

	##### Mathematical Regression #####
	def math_reg(self):
		population = []
		for i in range(0,self.population_size//2):
			population.append({'gen':self.math_reg_node('grow', self.values['max_depth'])})
		for i in range(self.population_size//2,self.population_size):
			population.append({'gen':self.math_reg_node('full', self.values['max_depth'])})
		return population

	def math_reg_node(self, method, depth):
		if depth == 0 or (method == 'grow' and random() < float(len(self.values['terminal_set']))/\
			(len(self.values['terminal_set'])+len(self.values['function_set']))):
			terminal = choice(self.values['terminal_set'])
			if callable(terminal): return terminal(-5,5)
			else: return terminal
		else:
			function = choice(self.values['function_set'])
			return [function[0]] + [self.math_reg_node(method,depth-1) for i in range(function[1])]
	###################################
