from random import seed, uniform

##### Values #####
class Values():

	def __init__(self, problem, individual_size):
		self.individual_size = individual_size
		self.values = {}

		if problem == 'jbrandao':
			pass
		elif problem == 'knapsack':
			self.knapsack()
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

	##### Rastrigin #####
	def rastrigin(self):
		self.values['A'] = 10
		self.values['sigma'] = 0.4
	#####################
