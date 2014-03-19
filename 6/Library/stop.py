from math import ceil

##### Algorithm Stop Condition #####
class Stop():

	def __init__(self, n_generations, values):
		self.n_generations = n_generations
		self.values = values

	##### Do Nothing #####
	def nothing(self, generation, population, best_fitnesses, average_fitnesses):
		return False
	######################

	##### Best Individual Stabilization #####
	def best_stabilization(self, generation, population, best_fitnesses, average_fitnesses):
		if generation >= self.n_generations * self.values['stabilize_percentage']:
			index = -int(ceil(self.n_generations*self.values['stabilize_percentage']))
			if len(set(best_fitnesses[index:])) == 1:
				return True
		return False
	#########################################

	##### Interval Stabilization #####
	def interval_stabilization(self, generation, population, best_fitnesses, average_fitnesses):
		print 'qwer', generation, self.n_generations * self.values['stabilize_percentage']
		if generation >= self.n_generations * self.values['stabilize_percentage']:
			print 'asdf'
			index = -int(ceil(self.n_generations*self.values['stabilize_percentage']))
			interval = abs(best_fitnesses[-1] - best_fitnesses[index])
			print interval
			if interval < self.values['stop_interval']:
				return True
		return False
	##################################

