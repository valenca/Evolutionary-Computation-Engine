from random import sample, random, randint
from copy import deepcopy

##### Parent Crossover #####
class Crossover():

	def __init__(self, population_size, individual_size, crossover, crossover_probability):
		self.population_size = population_size
		self.individual_size = individual_size
		self.crossover = crossover
		self.crossover_probability = crossover_probability

	##### General crossover function #####
	def crossover(self, parents):
		offspring = []
		for i in range(0, len(parents)-1, 2):
			if random < crossover_probability:
				offspring1,offspring2 = self.crossover(parents[i]['gen'],parents[i+1]['gen'])
				offspring.append({'gen':offspring1})
				offspring.append({'gen':offspring2})
			else:
				offspring.append(parents[i])
				offspring.append(parents[i+1])
		return offspring
	######################################

	##### One-Point Crossover #####
	def crossover_one_point(self, parent1, parent2):
		cut_index = randint(1, self.individual_size-1)
		offspring1 = parent1[:cut_index] + parent2[cut_index:]
		offspring2 = parent2[:cut_index] + parent1[cut_index:]
		return offspring1,offspring2
	###############################

	##### Cycle Crossover #####
	def crossover_cycle(self, parent1, parent2):
		count = 1
		mask = [0]*self.individual_size
		toggle = False
		for i in parent1:
			while mask[parent1.index(i)] == 0:
				toggle = True
				mask[parent1.index(i)] = count
				i = parent1[parent2.index(i)]
			if toggle:
				toggle = False
				count += 1
		parents = [parent1,parent2]
		offspring1 = []
		offspring2 = []
		for i in range(self.individual_size):
			offspring1.append(parents[(mask[i]+1)%2][i])
			offspring2.append(parents[(mask[i]+0)%2][i])
		return offspring1,offspring2
	###########################

	##### PMX #####
	def crossover_pmx(self, parent1, parent2):
	    cut=[0,0]
		cut[0]=randint(0,int(size/2))
		cut[1]=cut[0]+int(size/2)
		offspring = size-1

	    for i in range(cut[0],cut[1]):
	        offspring[i]=parent1[i]

	    slice=range(cut[0],cut[1])
	    i = parent1[cut[0]]
	    for i in range(cut[0],cut[1]):
	        if  parent2[i] in offspring:
	            continue
	        else:
	            j=i
	            while True:
	                var=parent2.index(parent1[j])
	                if var not in slice:
	                    offspring[var]=parent2[i]
	                    slice.append(var)
	                    break
	                else:
	                    j=parent2.index(parent1[j])
	        
	    for i in range(size):
	        if offspring[i]==-1:
	            offspring[i]=parent2[i]
	    return offspring
	###############



