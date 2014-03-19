##### Algorithm Stop Condition #####
class Stop():

	def __init__(self, n_generations, stabilization_percentage):
		self.n_generations = n_generations
		self.stabilization_percentage = stabilization_percentage

	##### Do Nothing #####
	def stop_nothing(self, generation, population, best_fitnesses, average_fitnesses):
		return False
	######################

	##### Best Individual Stabilization #####
	def stop_best_stabilization(self, generation, population, best_fitnesses, average_fitnesses):
		if generation >= self.n_generations * self.stabilization_percentage:
			if len(set(best_fitnesses[int(-self.n_generations*self.stabilization_percentage):])) == 1:
				return True
		return False
	#########################################

