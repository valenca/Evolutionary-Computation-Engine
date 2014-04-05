from random import sample, random, randint, choice
from copy import deepcopy

##### Parent Crossover #####
class Crossover():

	def __init__(self, individual_size, crossover_probability, values):
		self.individual_size = individual_size
		self.crossover_probability = crossover_probability
		self.values = values
		self.crossover_function = None

	##### General crossover function #####
	def crossover(self, parents):
		offspring = []
		for i in range(0, len(parents)-1, 2):
			if random() < self.crossover_probability:
				offspring1,offspring2 = self.crossover_function(parents[i]['gen'],parents[i+1]['gen'])
				offspring.append({'gen':offspring1})
				offspring.append({'gen':offspring2})
			else:
				offspring.append(deepcopy(parents[i]))
				offspring.append(deepcopy(parents[i+1]))
		return offspring
	######################################

	##### One-Point #####
	def one_point(self, parent1, parent2):
		cut_index = randint(1, self.individual_size-1)
		offspring1 = parent1[:cut_index] + parent2[cut_index:]
		offspring2 = parent2[:cut_index] + parent1[cut_index:]
		return offspring1, offspring2
	#####################

	##### N-Points #####
	def n_points(self, parent1, parent2):
		parents = [parent1, parent2]
		cut_indexes = [0]
		cut_indexes.extend(sorted(sample(list(range(1,self.individual_size)),self.values['n_points_cut'])))
		cut_indexes.append(self.individual_size)
		offspring1 = []
		offspring2 = []
		for i in range(len(cut_indexes)-1):
			offspring1.extend(parents[i%2][cut_indexes[i]:cut_indexes[i+1]])
			offspring2.extend(parents[(i+1)%2][cut_indexes[i]:cut_indexes[i+1]])
		return offspring1, offspring2
	####################

	##### Uniform #####
	def uniform(self, parent1, parent2):
		parents = [parent1, parent2]
		mask = [choice([0,1]) for i in range(self.individual_size)]
		offspring1 = []
		offspring2 = []
		for i in range(self.individual_size):
			offspring1.append(parents[mask[i]][i])
			offspring2.append(parents[mask[(i+1)%2]][i])
		return offspring1, offspring2
	####################

	##### Order #####
	def ordered(self, parent1, parent2):
		parents = [parent1, parent2]
		offspring = [[None]*self.individual_size,[None]*self.individual_size]
		cut_index = sorted(sample(list(range(self.individual_size)),2))
		for i in range(2):
			temp = deepcopy(parents[i^1])
			for j in range(cut_index[0],cut_index[1]):
				offspring[i][j] = parents[i][j]
				temp.remove(offspring[i][j])
			for j in range(self.individual_size):
				if offspring[i][j] == None:
					offspring[i][j] = temp.pop(0)
		return offspring[0],offspring[1]
	#################

	##### Cycle #####
	def cycle(self, parent1, parent2):
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
	#################

	##### PMX #####
	def pmx(self, parent1, parent2):
		parents = [parent1, parent2]
		offspring = [[None]*self.individual_size,[None]*self.individual_size]
		cut_index = sorted(sample(list(range(self.individual_size)),2))
		for i in range(2):
			for j in range(cut_index[0],cut_index[1]):
				offspring[i][j] = parents[i][j]
			indexes = list(range(cut_index[0],cut_index[1]))
			for j in range(cut_index[0],cut_index[1]):
				if parents[i^1][j] in offspring[i]:
					continue
				else:
					index = j
					while True:
						temp = parents[i^1].index(parents[i][index])
						if temp not in indexes:
							offspring[i][temp] = parents[i^1][j]
							indexes.append(temp)
							break
						else:
							index = parents[i^1].index(parents[i][index])
			for j in range(self.individual_size):
				if offspring[i][j] == None:
					offspring[i][j] = parents[i^1][j]
		return offspring[0],offspring[1]
	###############
