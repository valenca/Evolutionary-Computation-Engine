from math import cos, pi
from string import printable
from types import FunctionType, MethodType

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
			error += abs(self.math_reg_node(genotype, case[:-1]) - case[-1])
		return 1.0 / (1.0 + error)

	def math_reg_node(self, genotype, case):
		if isinstance(genotype, list):
			function = eval('self.'+genotype[0])
			if isinstance(function, MethodType) and len(genotype) > 1:
				return function(*[self.math_reg_node(son,case) for son in genotype[1:]])
			else:
				return genotype
		elif isinstance(genotype, (float,int)):
			return genotype
		elif isinstance(genotype, str):
			return case[int(genotype[1:])]
		elif isinstance(eval(genotype), FunctionType):
			return eval(genotype)(*())

	def add_w(self,x,y): return x + y
	def mult_w(self,x,y): return x * y	
	def sub_w(self,x,y): return x - y
	def div_prot_w(self,x,y): return x if abs(y) <= 1e-3 else x / y
	def exp_w(self,x,y): return 0 if int(x) == 0 else int(x)**int(y)
	###################################
