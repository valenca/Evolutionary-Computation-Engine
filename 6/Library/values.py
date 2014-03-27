from random import seed, uniform

##### Values #####
class Values():

	def __init__(self, problem, individual_size):
		self.individual_size = individual_size
		self.values = {}

		if problem == 'methinks':
			self.methinks()
		elif problem == 'jbrandao':
			pass
		elif problem == 'knapsack':
			self.knapsack()
		elif problem == 'tsp':
			self.tsp()
		elif problem == 'rastrigin':
			self.rastrigin()

	##### Methinks ######
	def methinks(self):
		self.values['sentence'] = 'The primary documentation of GNU Emacs is in the GNU Emacs Manual  which you can read using Info  either from Emacs or as a standalone program   Please look there for complete and  up to date documentation   This man page is updated only when someone volunteers to do so'
	#####################

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
					distance = (((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2))**(0.5)
					self.values['distances'][i][j] = self.values['distances'][j][i] = distance
	######################################

	##### Rastrigin #####
	def rastrigin(self):
		self.values['A'] = 10
		self.values['sigma'] = 0.4
	#####################
