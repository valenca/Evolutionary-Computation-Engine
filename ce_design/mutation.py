
# mutation

import random
import copy

# genérica 

def muta_bin(indiv,prob_muta, muta_func):
    cromo = copy.deepcopy(indiv)
    for i in range(len(indiv)):
        cromo[i] = muta_func(cromo[i],prob_muta)
    return cromo

# binário
def muta_bin_gene(gene, prob_muta):
    g = gene
    value = random.random()
    if value < prob_muta:
        g ^= 1
    return g


# integers


# permutations

def muta_perm_swap(indiv, prob_muta):
    cromo = copy.deepcopy(indiv)
    value = random.random()
    if value < prob_muta:
        index = random.sample(range(len(cromo)),2)
        index.sort()
        i1,i2 = index
        cromo[i1],cromo[i2] = cromo[i2], cromo[i1]
    return cromo

def muta_perm_scramble(indiv,prob_muta):
    cromo = copy.deepcopy(indiv)
    value = random.random()
    if value < prob_muta:
        index = random.sample(range(len(cromo)),2)
        index.sort()
        i1,i2 = index
	scramble = cromo[i1:i2+1]
	random.shuffle(scramble) 
	cromo = cromo[:i1] + scramble + cromo[i2+1:]
    return cromo


def muta_perm_inversion(indiv,prob_muta):
    cromo = copy.deepcopy(indiv)
    value = random.random()
    if value < prob_muta:
        index = random.sample(range(len(cromo)),2)
        index.sort()
        i1,i2 = index
	inverte = []
	for elem in cromo[i1:i2+1]:
	    inverte = [elem] + inverte
        cromo = cromo[:i1] + inverte + cromo[i2+1:]
    return cromo

def muta_perm_insertion(indiv, prob_muta):
    cromo = copy.deepcopy(indiv)
    value = random.random()
    if value < prob_muta:
        index = random.sample(range(len(cromo)),2)
        index.sort()
        i1,i2 = index
	gene = cromo[i2]
	for i in range(i2,i1,-1):
	    cromo[i] = cromo[i-1]
	cromo[i1+1] = gene
    return cromo

# reals

def muta_reals(indiv, prob_muta, domain, sigma):
    cromo = copy.deepcopy(indiv)
    for i in range(len(cromo)):
	cromo[i] = muta_reals_gene(cromo[i],prob_muta, domain[i], sigma[i])
    return cromo

def muta_reals_gene(gene,prob_muta, domain_gene, sigma_gene):
    value = random.random()
	new_gene = gene
    if value < prob_muta:
		muta_value = random.gauss(0,sigma_i)
		new_gene = gene + muta_value
	if new_gene < domain_i[0]:
	    new_gene = domain_i[0]
	elif new_gene > domain_i[1]:
	    new_gene = domain_i[1]
	return new_gene
	

# para testar

def cromo_bin(size):
	indiv = [random.randint(0,1) for i in range(size)]
	return indiv

def cromo_int(size):
	indiv = list(range(1,size+1))
	random.shuffle(indiv)
	return indiv

def cromo_reals(size):
    indiv = [random.uniform(-10,10) for i in range(size)]
    return indiv


if __name__ == '__main__':
    c1 = cromo_bin(10)
    print(c1)
    print(muta_bin(c1,1.0, muta_bin_gene))
    c2 = cromo_int(10)
    print(c2)
    print(muta_perm_insertion(c2,1.0))

        