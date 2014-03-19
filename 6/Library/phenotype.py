##### Individual Phenotype #####
class Phenotype():

	def __init__(self, individual_size):
		self.individual_size = individual_size

	##### Joao Brandao Numbers ######
	def jbrandao(self, genotype):
		return [i+1 for i in range(self.individual_size) if genotype[i] == 1]
	#################################

	##### Knapsack ######
	def knapsack(self, genotype):
		return [i+1 for i in range(self.individual_size) if genotype[i] == 1]
	#####################
