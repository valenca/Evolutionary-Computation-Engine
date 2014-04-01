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

	###################


def subtree_crossover(par_1,par_2):
	"""ATENTION:if identical sub_trees replace the first ocorrence..."""
	# Choose crossover point (indepently)
	size_1 = indiv_size(par_1)
	size_2 = indiv_size(par_2)
	cross_point_1 = choice(list(range(size_1)))
	cross_point_2 = choice(list(range(size_2)))
	# identify subtrees to echange
	sub_tree_1 = sub_tree(par_1, cross_point_1)
	sub_tree_2 = sub_tree(par_2, cross_point_2)
	# Exchange
	new_par_1 = deepcopy(par_1)
	offspring = replace_sub_tree(new_par_1, sub_tree_1,sub_tree_2)
	return offspring


def sub_tree(tree,position):
	def sub_tree_aux(tree,position):
		global count
		if position == count:
			count = 0
			return tree
		else:
			count += 1
			if isinstance(tree,list):
				for i,sub in enumerate(tree[1:]):
					res_aux = sub_tree(sub, position)
					if res_aux:
						break
				return res_aux
	return sub_tree_aux(tree,position)

def replace_sub_tree(tree, sub_tree_1, sub_tree_2):
	if tree == sub_tree_1:
		return sub_tree_2
	elif isinstance(tree, list):
		for i,sub in enumerate(tree[1:]):
			res = replace_sub_tree(sub, sub_tree_1, sub_tree_2)
			if res and (res != sub):
				return [tree[0]] + tree[1:i+1] + [res] + tree[i+2:]
		return tree
	else:
		return tree

