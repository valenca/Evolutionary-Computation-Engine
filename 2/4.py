import random
from scipy.spatial.distance import euclidean as eucl

with open('wi29.tsp') as f:
	while f.readline() != "NODE_COORD_SECTION\n": True
	coord = [[float(string) for string in line.split()[1:]] for line in f]
	coord.pop(-1)
	dist = [[0 for j in range(len(coord))] for i in range(len(coord))]
	for i in range(len(coord)):
		for j in range(i,len(coord)):
			dist[i][j] = dist[j][i] = eucl(coord[i],coord[j])
	#[[dist[i][j]=eucl(coord[i], coord[j]) for j in range(i,len(coord))] for i in range(len(coord))]

# --- HILL-CLIMBING
def basic_hc_restart(problem_size,fitness, max_iter, restart):
	"""Minimization."""
	best = random_candidate_permut(problem_size)
	cost_best = fitness(best)
	for j in range(restart):
		candidate = random_candidate_permut(problem_size)
		cost_candi = fitness(candidate)
		for i in range(max_iter):
			next_neighbor = random_neighbor_switch(candidate)
			cost_next_neighbor = fitness(next_neighbor)
			if cost_next_neighbor < cost_candi: 
				candidate = next_neighbor
				cost_candi = cost_next_neighbor
				if cost_candi == 0: break
			#if i%500 == 0:
			#	print(candidate, fitness(candidate))
		if cost_candi < cost_best:
			best = candidate
			cost_best = cost_candi
	return best

# -- TABU SEARCH
def tabu_search(problem_size,fitness,tabu_size, num_tweaks, max_iter):
	best = random_candidate_permut(problem_size)
	cost_best = fitness(best)
	print(best, cost_best)
	data_best = [cost_best]
	tabu = [best]
	for i in range(max_iter):
		if len(tabu) > tabu_size:
			tabu.pop(0)
		candidate = random_neighbor_switch(best)
		for j in range(num_tweaks):
			new_candidate = random_neighbor_switch(best)
			if (not (similar(new_candidate,tabu, 0.01))) and ((fitness(new_candidate) < fitness(candidate))\
			   or (similar(candidate,tabu,0.01))):
				candidate = new_candidate 
		
		cost_candi = fitness(candidate)
		if (not (similar(new_candidate,tabu,0.01))) and cost_candi < cost_best: # minimization
			best = candidate
			cost_best = cost_candi
			tabu.append(candidate)	  
		data_best.append(cost_best)
		if i%50 == 0:
			print(best, fitness(best))
	return best#, data_best

def similar(indiv,tabu, delta):
	""" To detect similar individuals in the tabu list."""
	if isinstance(indiv,int):
		return indiv in tabu
	if isinstance(indiv,float):
		for elem in tabu:
			if abs(elem - indiv) < delta:
				return True
		return False

# -- Generate individuals
def random_candidate_permut(size):
	vec = list(range(size))
	random.shuffle(vec)
	return vec

# -- Neighborhood
def random_neighbor_switch(individual):
	new_individual = individual[:]
	vec = list(range(len(individual)))
	pos1 = random.choice(vec)
	vec.pop(pos1)
	pos2 = random.choice(vec)
	new_individual[pos1],new_individual[pos2] = new_individual[pos2],new_individual[pos1]
	return new_individual

# -- Evaluate individuals
def city_distance(individual):
	return sum([dist[individual[i]][individual[(i+1)%len(coord)]] for i in range(len(coord))])

final = basic_hc_restart(len(coord),city_distance, 1000, 100)
#final = tabu_search(len(coord),city_distance,100, 5, 10000)
print(final, city_distance(final))
