from math import cos, pi

##### Individual Phenotype #####
class Phenotype():

	def __init__(self, individual_size, values):
		self.individual_size = individual_size
		self.values = values

	##### Joao Brandao Numbers ######
	def jbrandao(self, genotype):
		return [i+1 for i in range(self.individual_size) if genotype[i] == 1]
	#################################

	##### Knapsack ######
	def knapsack(self, genotype):
		return [i+1 for i in range(self.individual_size) if genotype[i] == 1]
	#####################

	##### Rastrigin ######
	def rastrigin(self, genotype):
		value = self.values['A'] * self.individual_size
		for i in range(self.individual_size):
			value += (genotype[i]**2 - self.values['A']*cos(2*pi*genotype[i]))
		return value
	######################

	##### Rastrigin ######
	def tsp(self, genotype):
		pass
	######################
