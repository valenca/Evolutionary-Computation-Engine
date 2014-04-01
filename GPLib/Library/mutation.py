from random import random, gauss, sample, choice, randint, shuffle
from string import printable

##### Individual Mutator #####
class Mutation():

	def __init__(self, individual_size, mutation_probability, values):
		self.individual_size = individual_size
		self.mutation_probability = mutation_probability
		self.values = values

	##### Point #####
	def point(self, population):
		for individual in population:
			for j in range(self.individual_size):
				if random() < self.mutation_probability:

	#################

def point_mutation(par, prob_mut_node, func_set, vars_set,const_set):
	par_mut = deepcopy(par)
	if random() < prob_mut_node:
		if isinstance(par_mut,list):
		# Function
			symbol = par_mut[0]
			return [change_function(symbol, func_set)] + [point_mutation(arg, prob_mut_node, func_set, vars_set,const_set) for arg in par_mut[1:]]
		elif isinstance(par_mut, (float, int)):
		# It's a constant
			return eval(const_set[0])
		elif var_b(par_mut): 
		# It's a variable
			return change_variable(par_mut,vars_set)
		else:
			raise TypeError # should not happen
	return par_mut


def change_function(symbol, function_set):
	new_function = choice(function_set)
	while (new_function[0] == symbol) or (new_function[1] != arity(symbol,function_set)):
		new_function = choice(function_set)
	return new_function[0]

def arity(symbol,function_set):
	for func in function_set:
		if func[0] == symbol:
			return func[1]	
											  

def change_variable(variable,vars_set):
	if len(vars_set) == 1:
		return variable
	new_var = choice(vars_set)
	while new_var == variable:
		new_var = choice(vars_set)
	return new_var
