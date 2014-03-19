import random, operator, copy, subprocess, sys, os

global weight
global value
global max_w


def basic_hc(problem_size,fitness, max_iter):
	"""Maximization."""
	candidate = generate_population(1,problem_size)[0]
	cost_candi = candidate[1]
        arr=[]
	for i in range(max_iter):
		next_neighbors = [[random_neighbor_bin(candidate[0]),0] for j in range(problem_size)]
		cost_next_neighbors = [fitness(next_neighbors[j])[0] for j in range(problem_size)]
                for i in range(problem_size):
                        next_neighbors[i][1]=cost_next_neighbors[i]
		cost_next_neighbor=max(cost_next_neighbors)
		next_neighbor = next_neighbors[cost_next_neighbors.index(cost_next_neighbor)]
		if cost_next_neighbor >= cost_candi: 
			candidate = next_neighbor
			cost_candi = cost_next_neighbor
                arr.append(cost_candi)
                
        print arr
	with open("output", "a") as f:
		f.write(str(len(arr)) + "\n")
		[f.write(str(arr[i])+" "+str(arr[i])+"\n") for i in range(len(arr))]
        print candidate
	return [candidate,0]

def random_neighbor_bin(individual):
	"""Flip one position."""
	new_individual = individual[:]
	pos = random.randint(0,len(individual) - 1)
	gene = individual[pos]
	new_gene = (gene + 1) % 2
	new_individual[pos] = new_gene
	return new_individual

def sea(n_generations,population_size,individual_size,parents_selection_group_size,
        generation,fitness,order,parents_selection,crossover,mutation,survivors_selection,phenotype,status,
        crossover_probability,mutation_probability,elite_percentage):

	best_fitness = []
	average_fitness = []

	# GENERATE initial population
	population = generation(population_size, individual_size)

	# Evaluate initial population by FITNESS; ORDER decreasingly
	for j in range(len(population)): population[j][1] = fitness(population[j][0])[0]
	order(population)

	# Over the generations
	for i in range(n_generations):

		# Print population status
		status(population[0], fitness, phenotype, str(i), 0)

		# Get best and average fitness of the population's individuals
		best_fitness.append(fitness(population[0][0])[0])
		average_fitness.append(sum([fitness(population[j][0])[0] for j in range(len(population))])/len(population))

		# If there aren't changes in the best for a while -> END
		if i > n_generations/5 and len(set(best_fitness[-n_generations/5:])) == 1: break;

		# SELECT PARENTS that will reproduce
		parents = parents_selection(copy.deepcopy(population), parents_selection_group_size)

		# Generate offspring by CROSSOVER
		offspring = crossover(parents, crossover_probability)

		# Alter offspring by MUTATION
		mutation(offspring, mutation_probability)

		# Evaluate population by FITNESS; ORDER decreasingly
		for j in range(len(offspring)): offspring[j][1] = fitness(offspring[j][0])[0]
		order(offspring)

		# SELECT SURVIVORS to pass to the next generation
		population = survivors_selection(population, offspring, elite_percentage)

		# Evaluate population by FITNESS; ORDER decreasingly
		for j in range(len(population)): population[j][1] = fitness(population[j][0])[0]
		order(population)

	# Write best and average values of fitness to file
	with open("output", "a") as f:
		f.write(str(len(best_fitness)) + "\n")
		[f.write(str(best_fitness[i])+" "+str(average_fitness[i])+"\n") for i in range(len(best_fitness))]

	# Return best individual ever
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

# Evaluate individual by fitness
def knapsack(individual):
	total_w = sum([weight[i] for i in range(len(individual)) if individual[i] == 1])
	total_v = sum([value[i] for i in range(len(individual)) if individual[i] == 1])
	
	if total_w > max_w: return (0, total_w-max_w)
	else:               return (total_v, total_w-max_w)

# Order population 
def order(population):
	population.sort(key=operator.itemgetter(1), reverse = True)

# Print population status
def jbrandao_status(individual, fitness, phenotype, header, final):
	if final == 1:
		print("")
	if int(sys.argv[3]) > 0 or final == 1:
		print("####### " + header + " #######")
		if int(sys.argv[3]) > 1 or final == 1:
			if final == 1:
				print("Individual: " + str(phenotype(individual)))
			print("   Fitness: " + str(fitness(individual[0])[0]))
			print("     Total: " + str(sum(individual[0])))
			print("Violations: " + str((fitness(individual[0])[1])))
	if final == 1:
		print("\n")

# Print population status
def knapsack_status(individual, fitness, phenotype, header, final):
	if final == 1:
		print("")
	if int(sys.argv[3]) > 0 or final == 1:
		print("####### " + header + " #######")
		if int(sys.argv[3]) > 1 or final == 1:
			if final == 1:
				print("Individual: " + str(phenotype(individual)))
			print("   Fitness: " + str(fitness(individual[0])[0]))
			print("     Total: " + str(sum([weight[i] for i in range(len(individual[0])) if individual[0][i] == 1])) + " / " + str(max_w))
	if final == 1:
		print("\n")
			
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
def mutation(offspring, mutation_probability):
	for i in offspring:
		for j in range(len(i[0])):
			if random.random() < mutation_probability:
				i[0][j] ^= 1

# Select survivors over a population
def survivors_selection(population, offspring, elite_percentage):
	elite_size = int(len(population) * elite_percentage)
	if elite_size > 0: return population[:elite_size] + offspring[:-elite_size]
	else:              return offspring

# Get phenotype of a individual 
def jbrandao_phenotype(individual):
	return [i+1 for i in range(len(individual[0])) if individual[0][i] == 1]

# Get phenotype of a individual 
def knapsack_phenotype(individual):
	return [i+1 for i in range(len(individual[0])) if individual[0][i] == 1]

if __name__ == '__main__':

	if(len(sys.argv) < 4):
		print("Missing arguments")
		sys.exit(0)

	n_runs = int(sys.argv[2])
	n_generations = 500
	population_size = 100
	individual_size = 100
	parents_selection_group_size = 3
	generation = generate_population
	if sys.argv[1] == '1': fitness = jbrandao
	else:                  fitness = knapsack
	order = order
	parents_selection = parents_selection
	crossover = crossover
	mutation = mutation
	survivors_selection = survivors_selection
	if sys.argv[1] == '1': phenotype = jbrandao_phenotype
	else:                  phenotype = knapsack_phenotype
	if sys.argv[1] == '1': status = jbrandao_status
	else:                  status = knapsack_status
	crossover_probability = 0.9
	mutation_probability = 0.05
	elite_percentage = 0.05

	if fitness == knapsack:
		random.seed("knapsack")
		v = 10
		r = 5
		#NC
		#weight = [int(random.uniform(0, v)) for i in range(individual_size)]
		#value = [int(random.uniform(0, v)) for i in range(individual_size)]
		#WC
		#weight = [int(random.uniform(0, v)) for i in range(individual_size)]
		#value = [weight[i] + int(random.uniform(0, v)) for i in range(individual_size)]
		#SC
		weight = [int(random.uniform(0, v)) for i in range(individual_size)]
		value = [weight[i] + r for i in range(individual_size)]
		#
		max_w = sum(weight)/2
		random.seed()

	with open("output", "w") as f:
		f.write(str(n_runs)+"\n")

	for i in range(n_runs):
                
		best = sea(n_generations,population_size,individual_size,parents_selection_group_size,
                generation,fitness,order,parents_selection,crossover,mutation,survivors_selection,phenotype,status,
		crossover_probability,mutation_probability,elite_percentage)

		status(best, fitness, phenotype, "Run " + str(i+1) + ": Best", 1)	

	#subprocess.call("python2 plot.py", shell=True)
	#os.remove("output")
