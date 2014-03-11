import random

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
	  
def local_search(fitness,indiv,repeat=100):
	"""simple hill-climbing."""
	best = indiv
	for i in range(repeat):
		candidate = perturb(best,1)
		if fitness(candidate) < fitness(best): # minimization
			best = candidate	
	return best
	
def acceptance(current, candidate,fitness):
	"""Define new local optimum. Minimizing"""
	cost_current = fitness(current)
	cost_candidate = fitness(candidate)
	if cost_candidate > cost_current: # minimization
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
		pertubed[indice] = (pertubed[indice]+1)%2
	return pertubed
	
# -- Evaluate individuals
def brandao(individual):
	k = 0;
	for i in range(len(individual)):
		if individual[i] == 1:
			for j in range(1,min(i+1, len(individual)-i),1):
				if individual[i-j] == individual[i+j] == 1:
					k+=1
					break
	return 100-sum(individual)+k*2

final = ils(100, brandao, 4000, 5)
print(final)
print(sum(final))
print((brandao(final)-100+sum(final))/2)
