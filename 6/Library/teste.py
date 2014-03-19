from random import sample,choice,randint
from copy import deepcopy

def crossover_cycle(size, parent1, parent2):
    count = 1
    mask = [0]*size
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
    for i in range(size):
        offspring1.append(parents[(mask[i]+1)%2][i])
        offspring2.append(parents[(mask[i]+0)%2][i])
    return offspring1,offspring2

def crossover_pmx(size, parent1, parent2):
        parents = [parent1, parent2]
        offspring = [[None]*size,[None]*size]
        cut_index = sample(list(range(size)),2)
        if cut_index[1] < cut_index[0]:
            cut_index[0],cut_index[1] = cut_index[1],cut_index[0]
        print cut_index

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
                
            for j in range(size):
                if offspring[i][j] == None:
                    offspring[i][j] = parents[i^1][j]

        return offspring[0],offspring[1]
          
def ordered_crossover(size, parent1, parent2):
        parents = [parent1, parent2]
        offspring = [[None]*size,[None]*size]
        cut_index = sample(list(range(size)),2)
        if cut_index[1] < cut_index[0]:
            cut_index[0],cut_index[1] = cut_index[1],cut_index[0]
        print cut_index
        for i in range(2):
            temp = deepcopy(parents[i^1])
            for j in range(cut_index[0],cut_index[1]):
                offspring[i][j] = parents[i][j]
                temp.remove(offspring[i][j])
            for j in range(size):
                if offspring[i][j] == None:
                    offspring[i][j] = temp.pop(0)
        return offspring[0],offspring[1]
from math import cos,pi
def rastrigin(genotype):
    value = 10 * 10
    for i in range(10):
        value += (genotype[i]**2 - 10*cos(2*pi*genotype[i]))
    return value

print rastrigin([0,0,0,0,0,0,0,0,0,0])
        
