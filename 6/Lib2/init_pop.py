import random

def cromo_bin(size):
	indiv = [random.randint(0,1) for i in range(size)]
	return indiv

def cromo_int(size):
	indiv = list(range(1,size + 1))
	random.shuffle(indiv)
	return indiv

def cromo_reals(size):
	indiv = [random.uniform(-10,10) for i in range(size)]
	return indiv

def init_pop(pop_size, cromo_size, func):
	population = [func(cromo_size) for count in range(pop_size)]
	return population

# For evolution strategies
def init_pop_ee(pop_size, domain):
	pop = []
	for i in range(pop_size):
		indiv = []
		for j in range(len(domain)):
			indiv.append(random.uniform(domain[j][0], domain[j][1]))
		pop.append(indiv)
	return pop

def eval_fitness_ee(pop,func):
	new_pop = [[indiv, func(indiv)] for indiv in pop]
	return new_pop
	
			
if __name__ == '__main__':
	print(init_pop(10,5,cromo_int))