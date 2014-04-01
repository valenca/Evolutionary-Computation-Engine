
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

	##### Subtree #####
	def subtree(self, parent1, parent2):
		size_1 = indiv_size(parent1)
		size_2 = indiv_size(parent2)
		cross_point_1 = choice(range(size_1))
		cross_point_2 = choice(range(size_2))
		sub_tree_1 = sub_tree(par_1, cross_point_1,0)
		sub_tree_2 = sub_tree(par_2, cross_point_2,0)
		new_par_1 = deepcopy(parent1)
		offspring = replace_sub_tree(new_par_1,sub_tree_1,sub_tree_2)
		return offspring
	###################


	def indiv_size(indiv):
		""" Number of nodes of an individual."""
		if not isinstance(indiv, list):
			return 1
		else:
			return 1 + sum(map(indiv_size, indiv[1:]))

	def sub_tree(tree,position,count):
		if position == count:
			return tree
		else:
			count += 1
			if isinstance(tree,list):
				for i,sub in enumerate(tree[1:]):
					res_aux = sub_tree(sub, position,count)
					if res_aux:
						break
				return res_aux

	def replace_sub_tree(tree, sub_tree_1, sub_tree_2):
		if tree == sub_tree_1: return sub_tree_2
		elif isinstance(tree, list):
			for i,sub in enumerate(tree[1:]):
				res = replace_sub_tree(sub, sub_tree_1, sub_tree_2)
				if res and (res != sub):
					return [tree[0]] + tree[1:i+1] + [res] + tree[i+2:]
			return tree
		else:
			return tree

