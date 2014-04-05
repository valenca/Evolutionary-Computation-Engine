from copy import deepcopy

##### Algorithms #####
class Algorithms():

	def __init__(self,n_generations,generation,fitness,sort,neighborhood,parents_selection,
		crossover,mutation,disturbance,survivors_selection,status,stop):
		self.n_generations = n_generations
		self.generation = generation
		self.fitness = fitness
		self.sort = sort
		self.neighborhood = neighborhood
		self.parents_selection = parents_selection
		self.crossover = crossover
		self.mutation = mutation
		self.disturbance = disturbance
		self.survivors_selection = survivors_selection
		self.status = status
		self.stop = stop

	##### Algorithm call function #####
	def call(self, algorithm):
		if algorithm == 'bhc':
			return self.bhc(self.generation,self.fitness,self.sort,self.neighborhood,
				self.survivors_selection,self.status,self.stop)
		elif algorithm == 'phc':
			return self.phc(self.generation,self.fitness,self.sort,self.neighborhood,
				self.survivors_selection,self.status,self.stop)
		elif algorithm == 'ils':
			return self.ils(self.generation,self.fitness,self.sort,self.disturbance,self.mutation,
				self.neighborhood,self.survivors_selection,self.status,self.stop)
		elif algorithm == 'sea':
			return self.sea(self.generation,self.fitness,self.sort,self.parents_selection,self.crossover,
				self.mutation,self.survivors_selection,self.status,self.stop)
	###################################

	##### Basic Hill Climbing #####
	def bhc(self,generation,fitness,sort,neighborhood,survivors_selection,status,stop):
		best_fitnesses = []; average_fitnesses = []
		population = generation()													# Generate initial population
		fitness(population)															# Evaluate population
		for i in range(self.n_generations):											# Over the generations
			status(i, population, best_fitnesses, average_fitnesses)				# Collecting data from population
			if stop(i,population,best_fitnesses,average_fitnesses):					# Stop condition
				return population, best_fitnesses, average_fitnesses				# Return final data
			neighbors = neighborhood(population[0])									# Generate neighbors
			fitness(neighbors); sort(neighbors)										# Evaluate and sort neighbors
			population = survivors_selection(population, neighbors)					# Survivors selection
			fitness(population)														# Evaluate population
		status(i+1, population, best_fitnesses, average_fitnesses)					# Collecting data from population
		return population, best_fitnesses, average_fitnesses						# Return final data
	###############################

	##### Parallel Hill Climbing #####
	def phc(self,generation,fitness,sort,neighborhood,survivors_selection,status,stop):
		best_fitnesses = []; average_fitnesses = []
		population = generation()													# Generate initial population
		fitness(population); sort(population)										# Evaluate and sort population
		for i in range(self.n_generations):											# Over the generations
			status(i, population, best_fitnesses, average_fitnesses)				# Collecting data from population
			if stop(i,population,best_fitnesses,average_fitnesses):					# Stop condition
				return population, best_fitnesses, average_fitnesses				# Return final data
			for j in range(len(population)):										# Over the population
				neighbors = neighborhood(population[j])								# Generate neighbors
				fitness(neighbors); sort(neighbors)									# Evaluate and sort neighbors
				population[j] = survivors_selection([population[j]], neighbors)[0]	# Survivors selection
			fitness(population); sort(population)									# Evaluate and sort population
		status(i+1, population, best_fitnesses, average_fitnesses)					# Collecting data from population
		return population, best_fitnesses, average_fitnesses						# Return final data
	##################################

	##### Iterated Local Search #####
	def ils(self,generation,fitness,sort,disturbance,mutation,neighborhood,survivors_selection,status,stop):
		best_fitnesses = []; average_fitnesses = []
		population = generation()													# Generate initial population
		fitness(population)															# Evaluate population
		for i in range(self.n_generations):											# Over the generations
			status(i, population, best_fitnesses, average_fitnesses)				# Collecting data from population
			if stop(i,population,best_fitnesses,average_fitnesses):					# Stop condition
				return population, best_fitnesses, average_fitnesses				# Return final data
			backup = deepcopy(population)											# Save population
			[individual.pop('fit') for individual in population]					# Remove fitness evaluation
			disturbance(population)													# Disturb population
			fitness(population); sort(population)									# Evaluate and sort population
			for j in range(len(population)):										# Over the population
				for k in range(100):												# Over the generations
					neighbors = neighborhood(population[j])							# Generate neighbors
					fitness(neighbors); sort(neighbors)								# Evaluate and sort neighbors
					population[j]=survivors_selection([population[j]],neighbors)[0]	# Survivors selection
				candidates = [backup[j], population[j]]; sort(candidates)			# Sort candidates
				population[j] = candidates[0]										# Maintain best of the candidates
			fitness(population); sort(population)									# Evaluate and sort population
		status(i+1, population, best_fitnesses, average_fitnesses)					# Collecting data from population
		return population, best_fitnesses, average_fitnesses						# Return final data
	#################################

	##### Simple Evolutionary Algorithm #####
	def sea(self,generation,fitness,sort,parents_selection,crossover,mutation,survivors_selection,status,stop):
		best_fitnesses = []; average_fitnesses = []
		population = generation()													# Generate initial population
		fitness(population); sort(population)										# Evaluate and sort population
		for i in range(self.n_generations):											# Over the generations
			status(i, population, best_fitnesses, average_fitnesses)				# Collecting data from population
			if stop(i,population,best_fitnesses,average_fitnesses):					# Stop condition
				return population, best_fitnesses, average_fitnesses				# Return final data
			parents = parents_selection(population)									# Parents selection
			offspring = crossover(parents)											# Generate offspring
			mutation(offspring)														# Mutate offspring
			fitness(offspring); sort(offspring)										# Evaluate and sort offspring
			population = survivors_selection(population, offspring)					# Survivors selection
			fitness(population); sort(population)									# Evaluate and sort population
		status(i+1, population, best_fitnesses, average_fitnesses)					# Collecting data from population
		return population, best_fitnesses, average_fitnesses						# Return final data
	#########################################
