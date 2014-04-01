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
		variables = ['x'+str(i) for i in list(range(self.values['header'][0]))]
		for i in range(self.population_size):
			population.append({'gen':[choice([0,1]) for j in range(self.individual_size)]})
		return population
	###################################


	numb_vars, function_set = get_header(problem)
	vars_set = generate_vars(numb_vars)
	ephemeral_constant = 'uniform(MIN_RND,MAX_RND)'
	const_set = [ephemeral_constant]
	terminal_set = vars_set + const_set
	statistics = []
	# Define initial population
	chromosomes = ramped_half_and_half(function_set,terminal_set,pop_size, in_max_depth)


# Method ramped half-and-half.	
def ramped_half_and_half(func_set,term_set,size, max_depth):
	depth=list(range(3,max_depth))
	pop=[]
	for i in range(size//2):
		pop.append(gen_rnd_expr(func_set,term_set,choice(depth),'grow'))
	for i in range(size//2):
		pop.append(gen_rnd_expr(func_set,term_set,choice(depth),'full'))
	if (size % 2 ) != 0:
		pop.append(gen_rnd_expr(func_set,term_set,choice(depth),'full'))
	return pop
