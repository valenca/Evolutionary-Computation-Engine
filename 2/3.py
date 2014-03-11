import random

sentence = "methinks it is like a weasel"

# --- HILL-CLIMBING
def basic_hc(problem_size,fitness, max_iter):
	"""Minimization."""
	candidate = random_candidate_char(problem_size)
	print(''.join([chr2(candidate[i]) for i in range(len(sentence))]))
	cost_candi = fitness(candidate)
	for i in range(max_iter):
		next_neighbor = random_neighbor_char(candidate)
		cost_next_neighbor = fitness(next_neighbor)
		if cost_next_neighbor < cost_candi: 
			candidate = next_neighbor
			cost_candi = cost_next_neighbor
			if cost_candi == 0: break
		if i%50 == 0:
			print(''.join([chr2(candidate[i]) for i in range(len(sentence))]))
	return ''.join([chr2(candidate[i]) for i in range(len(sentence))])

# -- Generate individuals
def random_candidate_char(size):
	return [ord2(random.choice(" abcdefghijklmnopqrstuvwxyz")) for i in range(size)]

def ord2(sym):
	if sym==' ': return 96
	else: return ord(sym)

def chr2(sym):
	if sym == 96: return ' '
	else: return chr(sym)

# -- Neighborhood
# --- For local search
def random_neighbor_char(individual):
	"""Flip one position."""
	new_individual = individual[:]
	new_gene = 95
	while new_gene < 96 or new_gene > 122:
		pos = random.randint(0,len(individual) - 1)
		gene = individual[pos]
		new_gene = gene + random.choice([1,-1])
	new_individual[pos] = new_gene
	return new_individual

# -- Evaluate individuals
def char_distance(individual):
	return sum([abs(ord2(sentence[i])-individual[i]) for i in range(len(sentence))])

print(sentence)
print(basic_hc(28,char_distance,2000))
