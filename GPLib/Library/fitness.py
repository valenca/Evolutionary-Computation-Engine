from math import cos, pi
from string import printable

##### Individual Evaluator #####
class Fitness():

	def __init__(self, individual_size, values):
		self.individual_size = individual_size
		self.values = values
		self.fitness_function = None

	##### General fitness function #####
	def fitness(self, population):
		for individual in population:
			if 'fit' not in individual:
				individual['fit'] = self.fitness_function(individual['gen'])
	####################################

	##### Mathematical Regression #####
	def math_reg(self, genotype):
		error = 0
		for case in self.values['math_reg_data']:
			error += abs(math_reg_node(genotype, case[:-1]))
		return 1.0 / (1.0 + error)

	def math_reg_node(self, genotype, case):
		if isinstance(genotype, list):
			function = eval(genotype[0])
			if isinstance(function, FunctionType) and len(genotype) > 1:
				return function(*[math_reg_node(son,case) for son in genotype[1:]])
			else:
				return genotype
		elif isinstance(genotype, (float,int)):
			return genotype
		elif isinstance(genotype, str):
			return case[int(genotype[1:])]
		elif isinstance(eval(genotype), FunctionType):
			return eval(genotype)(*())

	def add_w(x,y): return x + y
	def mult_w(x,y): return x * y	
	def sub_w(x,y): return x - y
	def div_prot_w(x,y): if abs(y) <= 1e-3: return x else: return x / y
	def exp_w(x,y):	if int(x) == 0: return 0 else: return int(x)**int(y)
	###################################
