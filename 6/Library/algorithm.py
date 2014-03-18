
##### Basic Hill Climbing #####
def bhc(n_generations,generation,fitness,sort,neighborhood,
	survivors_selection,phenotype,status,stop):

	best_fitnesses = []; average_fitnesses = []
	population = generation()												# Generate initial population
	fitness(population)														# Evaluate population
	for i in range(n_generations):											# Over the generations
		get_status(i, population, best_fitnesses, average_fitnesses)		# Collecting data from population
		if stop(i, population, best_fitnesses, average_fitnesses): break	# Stop condition
		neighbors = neighborhood(population[0])								# Generate neighbors
		fitness(neighbors); sort(neighbors)									# Evaluate and sort neighbors
		population = survivors_selection(population, neighbors)				# Survivors selection
		fitness(population)													# Evaluate population
	return population, best_fitnesses, average_fitnesses					# Return final data

###############################


##### Parallel Hill Climbing #####
def phc(n_generations,generation,fitness,sort,neighborhood,
	survivors_selection,phenotype,status,stop):

	best_fitnesses = []; average_fitnesses = []
	population = generation()												# Generate initial population
	fitness(population); sort(population)									# Evaluate and sort population
	for i in range(n_generations):											# Over the generations
		get_status(i, population, best_fitnesses, average_fitnesses)		# Collecting data from population
		if stop(i, population, best_fitnesses, average_fitnesses): break	# Stop condition
		for j in range(len(population)):									# Over the population
			neighbors = neighborhood(population[j])							# Generate neighbors
			fitness(neighbors); sort(neighbors)								# Evaluate and sort neighbors
			population[j] = survivors_selection(population[j], neighbors)	# Survivors selection
		fitness(population); sort(population)								# Evaluate and sort population
	return population, best_fitnesses, average_fitnesses					# Return final data

##################################


##### Simple Evolutionary Algorithm #####
def sea(n_generations,generation,fitness,sort,parents_selection,
	crossover,mutation,survivors_selection,phenotype,status,stop):

	best_fitnesses = []; average_fitnesses = []
	population = generation()												# Generate initial population
	fitness(population); sort(population)									# Evaluate and sort population
	for i in range(n_generations):											# Over the generations
		get_status(i, population, best_fitnesses, average_fitnesses)		# Collecting data from population
		if stop(i, population, best_fitnesses, average_fitnesses): break	# Stop condition
		parents = parents_selection(population)								# Parents selection
		offspring = crossover(parents)										# Generate offspring
		mutation(offspring)													# Mutate offspring
		fitness(offspring); sort(offspring)									# Evaluate and sort offspring
		population = survivors_selection(population, offspring)				# Survivors selection
		fitness(population); sort(population)								# Evaluate and sort population
	return population, best_fitnesses, average_fitnesses					# Return final data

#########################################
