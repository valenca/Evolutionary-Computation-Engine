from random import sample,choice,randint
from copy import deepcopy
from pprint import pprint



def subtree( parent1, parent2):
		size_1 = indiv_size(parent1)
		size_2 = indiv_size(parent2)
		cross_point_1 = choice(range(size_1))
		cross_point_2 = choice(range(size_2))
		sub_tree_1 = sub_tree(parent1, cross_point_1,0)
		sub_tree_2 = sub_tree(parent2, cross_point_2,0)
		new_par_1 = deepcopy(parent1)
		offspring = replace_sub_tree(new_par_1,sub_tree_1,sub_tree_2)
		return offspring
	###################

def indiv_size( indiv):
	""" Number of nodes of an individual."""
	if not isinstance(indiv, list):
		return 1
	else:
		pprint(indiv)
		print ""
		return 1 + sum(map(indiv_size, indiv[1:]))

def sub_tree( tree, position, count):
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


L=[{'gen': ['mult_w', ['sub_w', ['div_prot_w', 'x0', 'x0'], ['div_prot_w', 4.6275349411101185, 'x0']], ['div_prot_w', ['div_prot_w', 2.922818185622247, 'x0'], ['mult_w', 'x0', 'x0']]]}, {'gen': ['div_prot_w', ['div_prot_w', ['add_w', 'x0', 'x0'], ['add_w', 'x0', 2.440119537695997]], ['mult_w', ['div_prot_w', 4.871296878916581, 0.18883870429373673], ['add_w', 'x0', 0.49514898717472366]]]}]

p1=L[0]["gen"]
p2=L[1]["gen"]
print(subtree(p1,p2))
