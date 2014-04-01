from copy import deepcopy
from random import random

##### Algorithms #####
class Algorithms():

	def __init__(self,n_generations,generation,fitness,sort,neighborhood,parents_selection,
		crossover,mutation,disturbance,survivors_selection,status,stop,values):
		self.n_generations = n_generations
		self.generation = generation
		self.fitness = fitness
		self.sort = sort
		self.neighborhood = neighborhood
		self.parents_selection = parents_selection
		self.crossover = crossover
		self.mutation = mutation
		self.disturbance = disturbance
		self.survivors_selection = survivors_selection
		self.status = status
		self.stop = stop
		self.values = values

	##### Algorithm call function #####
	def call(self, algorithm):
		if algorithm == 'sea':
			return self.sea(self.generation,self.fitness,self.sort,self.parents_selection,self.crossover,
				self.mutation,self.survivors_selection,self.status,self.stop)
		elif algorithm == 'cmea':
			return self.sea(self.generation,self.fitness,self.sort,self.parents_selection,self.crossover,
				self.mutation,self.survivors_selection,self.status,self.stop)
	###################################
	
	##### Simple Evolutionary Algorithm #####
	def sea(self,generation,fitness,sort,parents_selection,crossover,mutation,survivors_selection,status,stop):
		best_fitnesses = []; average_fitnesses = []
		population = generation()													# Generate initial population
		fitness(population); sort(population)										# Evaluate and sort population
		for i in range(self.n_generations):											# Over the generations
			status(i, population, best_fitnesses, average_fitnesses)				# Collecting data from population
			if stop(i,population,best_fitnesses,average_fitnesses): i -= 1; break	# Stop condition
			parents = parents_selection(population)									# Parents selection
			offspring = crossover(parents)											# Generate offspring
			mutation(offspring)														# Mutate offspring
			fitness(offspring); sort(offspring)										# Evaluate and sort offspring
			population = survivors_selection(population, offspring)					# Survivors selection
			fitness(population); sort(population)									# Evaluate and sort population
		status(i+1, population, best_fitnesses, average_fitnesses)					# Collecting data from population
		return population, best_fitnesses, average_fitnesses						# Return final data
	#########################################

	##### Crossover vs Mutation Evolutionary Algorithm #####
	def cmea(self,generation,fitness,sort,parents_selection,crossover,mutation,survivors_selection,status,stop):
		best_fitnesses = []; average_fitnesses = []
		population = generation()													# Generate initial population
		fitness(population); sort(population)										# Evaluate and sort population
		for i in range(self.n_generations):											# Over the generations
			status(i, population, best_fitnesses, average_fitnesses)				# Collecting data from population
			if stop(i,population,best_fitnesses,average_fitnesses): i -= 1; break	# Stop condition
			parents = parents_selection(population)									# Parents selection
			if random() < self.values['crossover_vs_mutation']:						# Choose crossover over mutation
				offspring = crossover(parents)										# Generate offspring
			else:																	# Choose mutation over crossover
				offspring = deepcopy(parents)										# Generate offspring
				mutation(offspring)													# Mutate offspring
			fitness(offspring); sort(offspring)										# Evaluate and sort offspring
			population = survivors_selection(population, offspring)					# Survivors selection
			fitness(population); sort(population)									# Evaluate and sort population
		status(i+1, population, best_fitnesses, average_fitnesses)					# Collecting data from population
		return population, best_fitnesses, average_fitnesses						# Return final data
	########################################################
