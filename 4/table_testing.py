import random, operator, copy, subprocess, sys

def sea(n_generations,population_size,individual_size,parents_selection_group_size,
        generation,fitness,order,parents_selection,crossover,mutation,survivors_selection,phenotype,status,
	crossover_probability,mutation_probability,elite_percentage,ofile):

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
		#status(population[0], fitness, phenotype, str(i), 0)

		# Get best and average fitness of the population's individuals
		best_fitness.append(fitness(population[0][0])[0])
		average_fitness.append(sum([fitness(population[j][0])[0] for j in range(len(population))])/len(population))

		# If there aren't changes in the best for a while -> END
		#if i > n_generations/5 and len(set(best_fitness[-n_generations/5:])) == 1: break;

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
	with open(ofile, "a") as f:
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

if __name__ == '__main__':

	n_runs = 10
	n_generations = [500]
	population_size = [100,250,500]
	individual_size = [20,50,100]
	parents_selection_group_size = [3,5,7]
	generation = generate_population
	fitness = jbrandao
	order = order
	parents_selection = parents_selection
	crossover = crossover
	mutation = mutation
	survivors_selection = survivors_selection
	phenotype = jbrandao_phenotype
	status = jbrandao_status
	crossover_probability = [0.3,0.6,0.9]
	mutation_probability = [0.01,0.05,0.1,0.3]
	elite_percentage = [0.02,0.05,0.1]

	def execute():
		print i,j,k,l,m,n,o

		ofile = "Results/"+str(i)+"_"+str(j)+"_"+str(k)+"_"+str(l)+"_"+str(m)+"_"+str(n)+"_"+str(o)+".out"

		with open(ofile, "w") as f:
			f.write(str(n_runs)+"\n")

		bests = []

		for p in range(n_runs):
			bests.append(sea(k,j,i,o,
			generation,fitness,order,parents_selection,crossover,mutation,survivors_selection,phenotype,status,
			m,l,n,ofile))

		with open(ofile, "a") as f:
			for p in range(n_runs):
				f.write("\nIndividual: " + str(phenotype(bests[p]))+"\n")
				f.write("   Fitness: " + str(fitness(bests[p][0])[0])+"\n")
				f.write("     Total: " + str(sum(bests[p][0]))+"\n")
				f.write("Violations: " + str((fitness(bests[p][0])[1]))+"\n")

	for i in individual_size:
		for j in population_size:
			for k in n_generations:
				for l in mutation_probability:
					for m in crossover_probability:
						for n in elite_percentage:
							for o in parents_selection_group_size:
								execute()

