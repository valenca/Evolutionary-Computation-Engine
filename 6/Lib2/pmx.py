#-*- coding: utf-8 -*-

""" pmx.py
operador de cruzamento para permutações.
Ernesto Costa, Março 2010.
"""


def pmx_cross(cromo_1,cromo_2,prob_cross):
	size = len(cromo_1)
	value = random.random()
	if value < prob_cross:
		pc= random.sample(range(size),2)
		pc.sort()
		pc1,pc2 = pc
		f1 = [None] * size
		f2 = [None] * size
		f1[pc1:pc2+1] = cromo_1[pc1:pc2+1]
		f2[pc1:pc2+1] = cromo_2[pc1:pc2+1]
		# primeiro filho
		# parte do meio
		for j in range(pc1,pc2+1):
			if cromo_2[j] not in f1:
				pos_2 = j
				g_j_2 = cromo_2[pos_2]
				g_f1 = f1[pos_2]
				index_2 = cromo_2.index(g_f1)
				while f1[index_2] != None:
					index_2 = cromo_2.index(f1[index_2])
				f1[index_2] = g_j_2
		# restantes
		for k in range(size):
			if f1[k] == None:
				f1[k] = cromo_2[k]
		# segundo filho	
		# parte do meio
		for j in range(pc1,pc2+1):
			if cromo_1[j] not in f2:
				pos_1 = j
				g_j_1 = cromo_1[pos_1]
				g_f2 = f2[pos_1]
				index_1 = cromo_1.index(g_f2)
				while f2[index_1] != None:
					index_1 = cromo_1.index(f2[index_1])
				f2[index_1] = g_j_1
		# parte restante
		for k in range(size):
			if f2[k] == None:
				f2[k] = cromo_1[k]				
		return [f1,f2]
	else:
		return [cromo_1,cromo_2]