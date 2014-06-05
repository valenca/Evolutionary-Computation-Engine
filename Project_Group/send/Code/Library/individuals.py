from random import choice, sample, random
from string import letters, printable

##### Individual Generator #####
class Individuals():

	def __init__(self, population_size, individual_size, values):
		self.population_size = population_size
		self.individual_size = individual_size
		self.values = values

	##### Binary genotype #####
	def binary(self):
		return {'gen':[choice([0,1]) for j in range(self.individual_size)]}
	###########################

	##### Static Binary genotype #####
	def static_binary(self):
		static = self.values["static_binary"]
		return {'gen':sample([1]*static+[0]*(self.individual_size-static),self.individual_size)}
	##################################

	##### Integer genotype #####
	def integer(self):
		return {'gen': sample(range(self.individual_size),self.individual_size)}
	############################

	##### Float genotype #####
	def float(self):
		return {'gen': [random() for j in range(self.individual_size)]}
	##########################

	##### Character genotype #####
	def character(self):
		return {'gen': [choice(letters[:26]) for j in range(self.individual_size)]}
	##############################

	##### Methinks #####
	def methinks(self):
		return {'gen': [choice(printable) for j in range(self.individual_size)]}
	####################

	##### Rastrigin #####
	def rastrigin(self):
		return {'gen': [random()*10.24-5.12 for j in range(self.individual_size)]}
	#####################

	##### De Jong #####
	def dejong(self):
		return {'gen': [random()*2.56-1.28 for j in range(self.individual_size)], 'sigma': random()}
	###################

	##### Griewank #####
	def griewank(self):
		return {'gen': [random()*1200-600 for j in range(self.individual_size)], 'sigma': 5}
	####################
