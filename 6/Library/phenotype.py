##### Individual Phenotype #####
class Phenotype():

	def __init__(self, population_size, individual_size):
		self.population_size = population_size
		self.individual_size = individual_size

	##### Joao Brandao Numbers ######
	def phenotype_jbrandao(self, genotype):
		return [i+1 for i in range(self.individual_size) if genotype[i] == 1]
	#################################

	##### Knapsack ######
	def phenotype_jbrandao(self, genotype):
		return [i+1 for i in range(self.individual_size) if genotype[i] == 1]
	#####################
