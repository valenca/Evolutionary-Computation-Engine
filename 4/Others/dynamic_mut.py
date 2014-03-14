import random, operator, copy, math

def sea(n_generations,population_size,individual_size,parents_selection_group_size,
	generation,fitness,order,parents_selection,crossover,mutation,survivors_selection,phenotype,
	crossover_probability,lowest_mutation_probability,n_mutation_peaks,elite_percentage):

	# GENERATE initial population
	population = generation(population_size, individual_size)

	best_fitness = []

	# Over the generations
	for i in range(n_generations):

		# Evaluate population by FITNESS; ORDER decreasingly
		for j in range(len(population)): population[j][1] = fitness(population[j][0])[0]
		order(population)

		print("####### " + str(i) + " #######")
		print("   Fitness: " + str(fitness(population[0][0])[0]))
		print("     Total: " + str(len(phenotype(population[0]))))
		print("Violations: " + str((fitness(population[0][0])[1])))

		best_fitness.append(fitness(population[0][0])[0])
		if i > n_generations/5 and len(set(best_fitness[-n_generations/5:])) == 1:
			break;

		# SELECT PARENTS that will reproduce
		parents = parents_selection(copy.deepcopy(population), parents_selection_group_size)

		# Generate offspring by CROSSOVER
		offspring = crossover(parents, crossover_probability)

		# Alter offspring by MUTATION
		mutation(offspring, lowest_mutation_probability, n_mutation_peaks, n_generations, i)

		# Evaluate population by FITNESS; ORDER decreasingly
		for j in range(len(offspring)): offspring[j][1] = fitness(offspring[j][0])[0]
		order(offspring)

		# SELECT SURVIVORS to pass to the next generation
		population = survivors_selection(population, offspring, elite_percentage)

	# Evaluate resulting population by FITNESS; ORDER decreasingly
	for j in range(len(population)): population[j][1] = fitness(population[j][0])[0]
	order(population)

	return population[0]

# Generate population
def generate_population(population_size, individual_size):
	return [[[random.choice([0,1]) for i in range(individual_size)], 0] for j in range(population_size)]

# Evaluate individual by fitness
def jbrandao(individual):
	alfa = 1.5
	beta = -1
	k = 0;
	k2 = 0;

	for i in range(len(individual)):
		if individual[i] == 1:
			flag = 0
			for j in range(1,min(i+1, len(individual)-i),1):
				if individual[i-j] == individual[i+j] == 1:
					k+=1;
					if flag == 0: k2+=1; flag=1

	return (alfa * sum(individual) + beta * k, str(k) + " " + str(k2))

# Order population 
def order(population):
	population.sort(key=operator.itemgetter(1), reverse = True)

# Select parents that will reproduce
def parents_selection(population, parents_selection_group_size):
	parents_selected = []

	for i in range(len(population)):
		tournament_parents = random.sample(population, parents_selection_group_size)
		tournament_parents_fitness = [j[1] for j in tournament_parents]
		tournament_best = tournament_parents[tournament_parents_fitness.index(max(tournament_parents_fitness))]
		parents_selected.append(tournament_best)

	return parents_selected

# Generate offspring by Crossover between parents
def crossover(parents, crossover_probability):
	offspring = []

	for i in range(0, len(parents)-1, 2):
		if random.random() < crossover_probability:
			cut_index = random.choice(list(range(1,len(parents[i][0]))))
			offspring.append([parents[i][0][:cut_index] + parents[i+1][0][cut_index:], 0])
			offspring.append([parents[i+1][0][:cut_index] + parents[i][0][cut_index:], 0])
		else:
			offspring.append(parents[i])
			offspring.append(parents[i+1])

	return offspring

# Mutate offspring 
def mutation(offspring, lowest_mutation_probability, n_mutation_peaks, n_generations, generation):
	m_p = mutation_probability(lowest_mutation_probability, n_mutation_peaks, n_generations, generation)
	for i in offspring:
		for j in range(len(i[0])):
			if random.random() < m_p:
				i[0][j] ^= 1
		#if random.random() < lowest_mutation_probability:
		#	random.shuffle(i[0])

# Get mutation probability for an certain generation
def mutation_probability(lowest_mutation_probability, n_mutation_peaks, n_generations, generation):
	return lowest_mutation_probability * (1 + 4.5*(math.cos(generation * ((2*n_mutation_peaks-1)/(n_generations/math.pi))) + 1))

# Select survivors over a population
def survivors_selection(population, offspring, elite_percentage):
	elite_size = int(len(population) * elite_percentage)
	if elite_size > 0:
		return population[:elite_size] + offspring[:-elite_size]
	else:
		return offspring

# Get phenotype of a individual 
def phenotype(individual):
	return [i+1 for i in range(len(individual[0])) if individual[0][i] == 1]

if __name__ == '__main__':
	n_generations = 500
	population_size = 1000
	individual_size = 100
	parents_selection_group_size = 3
	generation = generate_population
	fitness = jbrandao
	order = order
	parents_selection = parents_selection
	crossover = crossover
	mutation = mutation
	survivors_selection = survivors_selection
	phenotype = phenotype
	crossover_probability = 0.7
	lowest_mutation_probability = 1.0/individual_size
	n_mutation_peaks = 25
	elite_percentage = 1.0/population_size

	best = sea(n_generations,population_size,individual_size,parents_selection_group_size,
	generation,fitness,order,parents_selection,crossover,mutation,survivors_selection,phenotype,
	crossover_probability,lowest_mutation_probability,n_mutation_peaks,elite_percentage)

	print("\n\n####### Best #######")
	print("Individual: " + str(phenotype(best)))
	print("   Fitness: " + str(fitness(best[0])[0]))
	print("     Total: " + str(len(phenotype(best))))
	print("Violations: " + str((fitness(best[0])[1])))
