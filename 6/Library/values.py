from random import seed, uniform
from scipy.spatial.distance import euclidean as euclidian

##### Values #####
class Values():

	def __init__(self, problem, individual_size):
		self.individual_size = individual_size
		self.values = {}

		if problem == 'jbrandao':
			pass
		elif problem == 'knapsack':
			self.knapsack()
		elif problem == 'tsp':
			self.tsp()
		elif problem == 'rastrigin':
			self.rastrigin()

	##### Knapsack ######
	def knapsack(self):
		correlation = 'strong'
		seed("knapsack")
		v = 10
		r = 5

		# None Correlation
		if correlation == 'none':
			self.values['weights'] = [int(uniform(0, v)) for i in range(self.individual_size)]
			self.values['values'] = [int(uniform(0, v)) for i in range(self.individual_size)]
		# Weak Correlation
		elif correlation == 'weak':
			self.values['weights'] = [int(uniform(0, v)) for i in range(self.individual_size)]
			self.values['values'] = [self.values['weights'][i] + int(uniform(0, v)) for i in range(self.individual_size)]
		# Strong Correlation
		elif correlation == 'strong':
			self.values['weights'] = [int(uniform(0, v)) for i in range(self.individual_size)]
			self.values['values'] = [self.values['weights'][i] + r for i in range(self.individual_size)]
		#
		self.values['max_weight'] = sum(self.values['weights'])/2
		seed()
	#####################

	##### Traveling Salesman Problem #####
	def tsp(self):
		with open('Data/wi29.tsp') as f:
			while f.readline() != "NODE_COORD_SECTION\n": True
			coord = [[float(string) for string in line.split()[1:]] for line in f]
			coord.pop(-1)
			self.values['distances'] = [[0 for j in range(len(coord))] for i in range(len(coord))]
			for i in range(len(coord)):
				for j in range(i,len(coord)):
					self.values['distances'][i][j] = self.values['distances'][j][i] = euclidian(coord[i],coord[j])
		print '\n'.join(list(map(str,self.values['distances'])))
	######################################

	##### Rastrigin #####
	def rastrigin(self):
		self.values['A'] = 10
		self.values['sigma'] = 0.4
	#####################
