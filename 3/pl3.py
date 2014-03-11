import random

global weight
global value
global max_w

# -- ITERATED LOCAL SEARCH
def ils(problem_size,fitness, max_iter,size):
	"""
	Iterated Local Search: no use of memory!
	domain: [..., [xi_min, xi_max],...]
	fitness: function name
	max_iter: stop condition
	size: number of components to be perturbed
	"""
	initial = random_candidate_bin(problem_size)
	best = local_search(fitness,initial)
	for i in range(max_iter):
		candidate = perturb(best,size)
		new_best = local_search(fitness,candidate)
		best = acceptance(best, new_best, fitness)
	return best
	  
def local_search(fitness,indiv,repeat=1000):
	"""simple hill-climbing."""
	best = indiv
	for i in range(repeat):
		candidate = perturb(best,1)
		if fitness(candidate) > fitness(best): # maximization
			best = candidate	
	return best
	
def acceptance(current, candidate,fitness):
	"""Define new local optimum. Minimizing"""
	cost_current = fitness(current)
	cost_candidate = fitness(candidate)
	if cost_candidate > cost_current: # maximization
		return candidate
	else:
		return current

# -- Generate individuals
def random_candidate_bin(size):
	return [random.choice([0,1]) for i in range(size)]
	
# -- Neighborhood
def perturb(individual,size):
	"""Probabilitic modification of size componentes of a vector."""
	pertubed = individual[:]
	indices = random.sample(range(len(individual)),size)
	for indice in indices:
		pertubed[indice] ^= 1
	return pertubed
	
# -- Evaluate individuals
def knapsack(individual):
	total_w = sum([weight[i] for i in range(len(individual)) if individual[i] == 1])
	total_v = sum([value[i] for i in range(len(individual)) if individual[i] == 1])
	if total_w > max_w:
		return 0
	else:
		return total_v

n = 100
v = 10
r = 5

random.seed("knapsack")

#NC
weight = [int(random.uniform(0, v)) for i in range(n)]
value = [int(random.uniform(0, v)) for i in range(n)]
#WC
#weight = [int(random.uniform(0, v)) for i in range(n)]
#value = [weigth[i] + int(random.uniform(0, v)) for i in range(n)]
#SC
#weight = [int(random.uniform(0, v)) for i in range(n)]
#value = [weigth[i] + r for i in range(n)]

max_w = sum(weight)/2

random.seed()

final = ils(n, knapsack, 1000, 3)
print(str(sum([weight[i] for i in range(len(final)) if final[i] == 1])) + " / " + str(max_w))
print(sum([value[i] for i in range(len(final)) if final[i] == 1]))
