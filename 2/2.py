import random

# --- HILL-CLIMBING
def basic_hc(problem_size,fitness, max_iter):
	"""Maximization."""
	candidate = random_candidate_bin(problem_size)
	print(candidate)
	cost_candi = fitness(candidate)
	for i in range(max_iter):
		next_neighbors = [random_neighbor_bin(candidate) for j in range(problem_size)]
		cost_next_neighbors = [fitness(next_neighbors[j]) for j in range(problem_size)]
		cost_next_neighbor=max(cost_next_neighbors)
		next_neighbor = next_neighbors[cost_next_neighbors.index(cost_next_neighbor)]
		if cost_next_neighbor >= cost_candi: 
			candidate = next_neighbor
			cost_candi = cost_next_neighbor
		print(candidate)
	return candidate

# -- Generate individuals
def random_candidate_bin(size):
	return [random.choice([0,1]) for i in range(size)]

# -- Neighborhood
# --- For local search
def random_neighbor_bin(individual):
	"""Flip one position."""
	new_individual = individual[:]
	pos = random.randint(0,len(individual) - 1)
	gene = individual[pos]
	new_gene = (gene + 1) % 2
	new_individual[pos] = new_gene
	return new_individual

# -- Evaluate individuals
def onemax(individual):
	"""Individual = list of zeros and ones."""
	return sum(individual)

print(basic_hc(20,onemax,120))