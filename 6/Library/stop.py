##### Algorithm Stop Condition #####
class Stop():

	def __init__(self, n_generations, population_size, individual_size, values):
		self.n_generations = n_generations
		self.population_size = population_size
		self.individual_size = individual_size
		self.values = values

	##### Do Nothing #####
	def stop_nothing(self, generation, population, best_fitnesses, average_fitnesses):
		return False
	######################

	##### Best Individual Stabilization #####
	def stop_best_stabilization(self, generation, population, best_fitnesses, average_fitnesses):
		if generation >= self.n_generations * self.values['stab_perc']:
			if len(set(best_fitnesses[int(-self.n_generations*self.values['stab_perc']):])) == 1:
				return True
		return False
	#########################################

