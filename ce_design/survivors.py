
""" Selection of survivors. 
As duas populações são supostas estarem ordenadas por mérito."""


from operator import itemgetter
from random import randint

def survivors_generational(parents,offspring):
    return offspring

def survivors_elitism(parents,offspring,elite):
    """ Sorted. """
    size = len(parents)
    comp_elite = int(size* elite)
    new_population = parents[:comp_elite] + offspring[:size - comp_elite]
    return new_population

def survivors_worst_out(parents,offspring, worst):
    return survivors_elitism(parents,offspring, 1 - worst)

def survivors_mu_plus_lambda(parents,offspring):
    """Minimizing."""
    size = len(parents)
    new_population = parents + offspring
    new_population.sort(key=itemgetter(1)) 
    return new_population[:size]

def survivors_mu_lambda(parents,offspring):
    return offspring[:len(parents)]

def survivors_one_plus_lambda(parent,offspring):
    new_pop = [parent] + offspring
    new_pop.sort(key=itemgetter(1))
    return new_pop[0]

if __name__ == '__main__':
    tam_pop = 5
    tam_cromo = 5
    
    one_parent = [[randint(0,1) for i in range(tam_cromo)],randint(1,100)] 
    parents = [ [[randint(0,1) for i in range(tam_cromo)],randint(1,100)] for j in range(tam_pop)]
    offspring = [ [[randint(0,1) for i in range(tam_cromo)],randint(1,100)] for j in range(tam_pop)]
    offspring2 = [ [[randint(0,1) for i in range(tam_cromo)],randint(1,100)] for j in range(3*tam_pop)]
    parents.sort(key=itemgetter(1))
    offspring.sort(key=itemgetter(1))
    offspring2.sort(key=itemgetter(1))
    print(one_parent)
    print(parents)
    print(offspring)
    print(offspring2)
    print(10 * "-")
    print(survivors_generational(parents,offspring))
    print(survivors_elitism(parents,offspring, 0.6))
    print(survivors_worst_out(parents,offspring,0.4))
    print(survivors_mu_plus_lambda(parents,offspring))
    print(survivors_mu_lambda(parents,offspring2))
    print(survivors_one_plus_lambda(one_parent,offspring))
    
    
