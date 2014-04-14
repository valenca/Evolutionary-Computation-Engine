from math import sqrt

##### Individuals Distance #####
class Distance():

	def __init__(self, individual_size):
		self.individual_size = individual_size

	##### Euclidian Distance #####
	def euclidian(self, genotype1, genotype2):
		return sqrt(sum([(pair[0] - pair[1])**2 for pair in list(zip(genotype1,genotype2))]))
	##############################

	##### Hamming Distance #####
	def hamming(self, genotype1, genotype2):
		return sum([1 for index in range(self.individual_size) if genotype1[index] != genotype2[index]])
	############################

	##### Manhattan Distance #####
	def manhattan(self, genotype1, genotype2):
		return sum([abs(pair[0] - pair[1]) for pair in list(zip(genotype1,genotype2))])
	##############################
