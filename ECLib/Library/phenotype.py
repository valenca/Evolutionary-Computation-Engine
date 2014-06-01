from math import cos, pi

##### Individual Phenotype #####
class Phenotype():

	def __init__(self, individual_size, values):
		self.individual_size = individual_size
		self.values = values

	##### Onemax #####
	def onemax(self, genotype):
		return [i+1 for i in range(self.individual_size) if genotype[i] == 1]
	##################

	##### Methinks ######
	def methinks(self, genotype):
		return ''.join(genotype)
	#####################

	##### Joao Brandao Numbers ######
	def jbrandao(self, genotype):
		return [i+1 for i in range(self.individual_size) if genotype[i] == 1]
	#################################

	##### Knapsack ######
	def knapsack(self, genotype):
		return [i+1 for i in range(self.individual_size) if genotype[i] == 1]
	#####################

	##### Traveling Salesman Problem #####
	def tsp(self, genotype):
		return genotype
	######################################

	##### Rastrigin ######
	def rastrigin(self, genotype):
		return genotype
	######################

	##### Griewank ######
	def griewank(self, genotype):
		return genotype
	#####################

	##### Dispersion Problem #####
	def dispersion(self,genotype):
		return [self.values['coords'][i] for i in range(len(genotype)) if genotype[i]==1]
	##############################
