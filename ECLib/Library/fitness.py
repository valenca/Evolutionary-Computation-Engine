from math import cos, pi,sin
from string import printable
from random import gauss

##### Individual Evaluator #####
class Fitness():

	def __init__(self, individual_size, values):
		self.individual_size = individual_size
		self.values = values
		self.fitness_function = None

	##### General fitness function #####
	def fitness(self, population):
		for individual in population:
			if 'fit' not in individual:
				individual['fit'] = self.fitness_function(individual['gen'])
	####################################

	##### Onemax #####
	def onemax(self, genotype):
		return sum(genotype)
	##################

	##### Methinks ######
	def methinks(self, genotype):
		difference = 0
		for i in range(self.individual_size):
			difference += abs(printable.index(self.values['sentence'][i]) - printable.index(genotype[i]))
		return difference
	#####################

	##### Joao Brandao Numbers ######
	def jbrandao(self, genotype):
		violations = 0;
		for i in range(self.individual_size):
			if genotype[i] == 1:
				for j in range(1,min(i+1, self.individual_size-i)):
					if genotype[i-j] == genotype[i+j] == 1:
						violations += 1;
		return 1.5*sum(genotype) + (-1)*violations
	#################################

	##### Knapsack ######
	def knapsack(self, genotype):
		total_weight = 0; total_values = 0
		for i in range(self.individual_size):
			if genotype[i] == 1:
				total_weight += self.values['weights'][i]
				total_values += self.values['values'][i]
		if total_weight > self.values['max_weight']:
			return self.values['max_weight'] - total_weight
		else:
			return total_values
	#####################

	##### Traveling Salesman Problem #####
	def tsp(self, genotype):
		total_distance = 0
		for i in range(self.individual_size-1):
			total_distance += self.values['distances'][genotype[i]][genotype[i+1]]
		total_distance += self.values['distances'][genotype[-1]][genotype[0]]
		return total_distance
	######################################

	##### Rastrigin #####
	def rastrigin(self, genotype):
		value = self.values['A'] * self.individual_size
		for i in range(self.individual_size):
			value += (genotype[i]**2 - self.values['A']*cos(2*pi*genotype[i]))
		return value
	#####################

	##### De Jong #####
	def dejong(self, genotype):
		value = 0
		for i in range(self.individual_size):
			value += (i+1) * genotype[i]**4
		return value + gauss(0,1)
	###################

	##### Griewank #####
	def griewank(self, genotype):
		value1 = 0
		value2 = 1
		for i in range(self.individual_size):
			value1 += genotype[i]**2
			value2 *= cos(genotype[i] / ((i+1)**0.5))
		return value1 / 1000.0 - value2 + 1
	####################

	##### Dispersion Problem #############
	def dispersion(self, genotype):		
		def dist(p1,p2):
			res = 0
			for c1,c2 in zip(p1,p2):
				res += (c1-c2)**2
			return res**0.5

		def closestPair(L,dp):
			best = [dist(L[0],L[1]), (L[0],L[1]),(0,1)]
			dim = len(L[0])
			threshold = (3**dim)-(3**(dim-1))
			# 2, 6, 18, 54, 162, 486, 1458, 4374, 13122

			def testPair(p,q,ip,iq):
				d = dist(p,q)
				if d < best[0]:
					best[0] = d
					best[1] = p,q
					best[2] = ip,iq
			
			def merge(A,B):	   
				i = 0
				j = 0
				while i < len(A) or j < len(B):
					if j >= len(B) or (i < len(A) and A[i][1] <= B[j][1]):
						yield A[i]
						i += 1
					else:
						yield B[j]
						j += 1

			def recur(L,ind):
				if len(L) < 2:
					return L
				split = int(len(L)/2)
				splitx = L[split][0]
				L2 = list(merge(recur(L[:split],ind), recur(L[split:],ind+split)))
	
				E = [p for p in L2 if abs(p[0]-splitx) < best[0]]
				for i in range(len(E)):
					#for j in range(1,len(E)):
					for j in range(1,threshold+1):
						if i+j < len(E):
							testPair(E[i],E[i+j],ind+L.index(E[i]),ind+L.index(E[i+j]))
				return L
			L.sort()
			try:
				pass
				return dp[tuple([tuple(i) for i in L])]
			except KeyError:
				pass
			recur(L,0)
			dp[tuple([tuple(i) for i in L])]=best
			return best

		points=[self.values['coords'][i] for i in range(len(genotype)) if genotype[i]==1]
		return closestPair(points,self.values['dp'])[0]
	######################################
