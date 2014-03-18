from random import sample,choice,randint
from copy import deepcopy

def crossover_cycle(parent1, parent2,individual_size):
    count = 1
    mask = [0]*individual_size
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
    for i in range(individual_size):
	offspring1.append(parents[(mask[i]+1)%2][i])
	offspring2.append(parents[(mask[i]+0)%2][i])
    return offspring1,offspring2


def pmx(size,parent1,parent2):
    cut=[0,0]
    cut[0]= 3#choice(range(size))
    offspring=size*[-1]
    if cut[0]>size/2:
        cut[1]=cut[0]-int(size/2)
        cut.sort()
    else:
        cut[1]=cut[0]+int(size/2)

    for i in range(cut[0],cut[1]):
        offspring[i]=parent1[i]

    slice=range(cut[0],cut[1])
    i = parent1[cut[0]]
    for i in range(cut[0],cut[1]):
        if parent2[i] in offspring:
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
          
def ordered_crossover(size,parent1,parent2):
    cut=[0,0]
    cut[0]=randint(0,int(size/2))
    cut[1]=cut[0]+int(size/2)
    offspring=[-1]*size
    p2=deepcopy(parent2)
    for i in range(cut[0],cut[1]):
        offspring[i]=parent1[i]
        p2.remove(offspring[i])
    for i in range(size):
        if offspring[i]==-1:
            offspring[i]=p2.pop(0)
    print offspring
        
        
#parent1=[8,4,7,3,6,2,5,1,9,0]
#parent2=[0,1,2,3,4,5,6,7,8,9]
Z=range(10)
A=sample(Z,len(Z))
B=sample(Z,len(Z))
print A
print B
print ordered_crossover(len(A),A,B)

