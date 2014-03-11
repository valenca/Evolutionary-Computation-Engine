""" PL2: single state stochastic algorithms."""

import random
from math import exp, sin, cos, pi


# ---- RANDOM SEARCH
def random_search(domain,fitness,max_iter):
    """
    domain: [...,[xi_min, xi_max]]
    """
    best = random_candidate_float(domain)
    cost_best = fitness(best)
    for i in range(max_iter):
        candidate = random_candidate_float(domain)
        cost_candi = fitness(candidate)
        if cost_candi < cost_best:
            best = candidate
            cost_best = cost_candi
    return best


# --- HILL-CLIMBING
def basic_hc(problem_size,fitness, max_iter):
    """Maximization."""
    candidate = random_candidate_bin(problem_size)
    cost_candi = fitness(candidate)
    for i in range(max_iter):
        next_neighbor = random_neighbor_bin(candidate)
        cost_next_neighbor = fitness(next_neighbor)
        if cost_next_neighbor >= cost_candi: 
            candidate = next_neighbor
            cost_candi = cost_next_neighbor        
    return candidate

def random_restart_hc(problem, fitness, max_iter,restart):
    candidate = random_candidate_bin(problem)
    cost_candidate = fitness(candidate)
    best = candidate
    cost_best = cost_candidate
    for i in range(1,max_iter+1,restart):
        j = 1
        while (j % restart) != 0:
            new_candidate = random_neighbor_bin(candidate)
            cost_new_candidate = fitness(new_candidate)
            if cost_new_candidate >= cost_candidate: 
                candidate = new_candidate
                cost_candidate = cost_new_candidate  
            j += 1
        if cost_candidate >= cost_best:
            best = candidate
            cost_best = cost_candidate 
        candidate = random_candidate_bin(problem)
        cost_candidate = fitness(candidate)
    return best

# -- SIMULATED ANNEALING
def simulated_annealing(domain,fitness, sigma, schedule, max_iter):
    best = random_candidate_float(domain)
    cost_best = fitness(best)
    data_best = [cost_best]
    count = 0
    time = schedule(count)
    while (count < max_iter) and (time > 0):
        candidate = random_neighbor_float(domain,best,sigma)
        cost_candi = fitness(candidate)
        if cost_candi < cost_best: 
            best = candidate
            cost_best = cost_candi
        else:
            p = random.random()
            app = exp((cost_best - cost_candi)/ float(time))
            if p < app:
                best = candidate
                cost_best = cost_candi
        count += 1
        time = schedule(count)
        data_best.append(cost_best)
    return best#, data_best


def exp_schedule(k=20,decay=0.005, limit=5000):
    def compute(t):
        if t >= limit:
            return 0
        else:
            return k * exp(-decay * t)
    return compute

# -- TABU SEARCH
def tabu_search(domain,fitness,sigma,tabu_size, num_tweaks, max_iter):
    best = random_candidate_float(domain)
    cost_best = fitness(best)
    data_best = [cost_best]
    tabu = [best]
    for i in range(max_iter):
        if len(tabu) > tabu_size:
            tabu.pop(0)
        candidate = random_neighbor_float(domain,best, sigma)
        for i in range(num_tweaks):
            new_candidate = random_neighbor_float(domain,best,sigma)
            if (not (similar(new_candidate,tabu, 0.01))) and ((fitness(new_candidate) < fitness(candidate))\
               or (similar(candidate,tabu,0.01))):
                candidate = new_candidate 
        
        cost_candi = fitness(candidate)
        if (not (similar(new_candidate,tabu,0.01))) and cost_candi < cost_best: # minimization
            best = candidate
            cost_best = cost_candi
            tabu.append(candidate)      
        data_best.append(cost_best) 
    return best#, data_best
    
    
def similar(indiv,tabu, delta):
    """ To detect similar individuals in the tabu list."""
    if isinstance(indiv,int):
        return indiv in tabu
    if isinstance(indiv,float):
        for elem in tabu:
            if abs(elem - indiv) < delta:
                return True
        return False


# -- ITERATED LOCAL SEARCH
def ils(domain,fitness, max_iter, size):
    """
    Iterated Local Search: no use of memory!
    domain: [..., [xi_min, xi_max],...]
    fitness: function name
    max_iter: stop condition
    size: number of components to be perturbed
    """
    initial = build_initial(domain)
    best = local_search(domain,fitness,initial)
    for i in range(max_iter):
        candidate = perturb(domain,best,size)
        new_best = local_search(domain,fitness,candidate)
        best = acceptance(best, new_best, fitness)
    return best

# Problem specific: for reals

def build_initial(domain):
    """Generates a N-dimentional vector of floats."""
    return random_candidate_float(domain)
    
def acceptance(current, candidate,fitness):
    """Define new local optimum. Minimizing"""
    cost_current = fitness(current)
    cost_candidate = fitness(candidate)
    if cost_current < cost_candidate: # Minimization
        return current
    else:
        return candidate
    
def perturb(domain,individual,size,  sigma=1):
    """Probabilitic modification of size componentes of a vector."""
    pertubed = individual[:]
    indices = random.sample(range(len(individual)),size)
    for indice in indices:
        delta = random.gauss(0,sigma)
        while not (domain[indice][0] <= pertubed[indice] + delta <= domain[indice][1]):
            delta = random.gauss(0,sigma)
        pertubed[indice] += delta 
    return pertubed
      
def local_search(domain,fitness,indiv,repeat=100):
    """simple hill-climbing."""
    best = indiv
    for i in range(repeat):
        candidate = perturb(domain,best,1)
        if fitness(candidate) < fitness(best): # minimization
            best = candidate    
    return best

# -- Neighborhood
# --- For local search
def random_neighbor_bin(individual):
    """Flip one position."""
    new_individual = individual[:]
    pos = random.randint(0,len(individual) - 1)
    gene = individual[pos]
    new_gene = (gene + 1) % 2
    new_individual[pos] = new_gene
    return new_individual

def random_neighbor_float(domain,individual,sigma=1):
    new_individual = individual[:]
    indice = random.randint(0, len(individual)-1)
    delta = random.gauss(0,sigma)
    while not (domain[indice][0] <= new_individual[indice] + delta <= domain[indice][1]):
        delta = random.gauss(0,sigma)
    new_individual[indice] += delta
    return new_individual

# -- Generate individuals

def random_candidate_bin(size):
    return [random.choice([0,1]) for i in range(size)]

def random_candidate_float(sp):
    return [random.uniform(sp[i][0],sp[i][1]) for i in range(len(sp))]

def random_candidate_permut(size):
    return random.shuffle(range(size))


# -- Evaluate individuals
def onemax(individual):
    """Individual = list of zeros and ones."""
    return sum(individual)

def de_jong_f1(individual):
    """ 
    De Jong F1 or the sphere function
    domain: [-5.12, 5.12] for each dimension.
    min = 0 at x = (0,0,...,0)
    """
    return sum([ x_i ** 2 for x_i in individual])




if __name__ == '__main__':
    dimension = 3
    search_space = [[-5.12, 5.12] for i in range(dimension)]
    #print(random_search(search_space,de_jong_f1,120))
    #print(basic_hc(20,onemax,120))
    #print(random_restart_hc(20,onemax,200,30))
    #print(exp_schedule()(20))
    #print(simulated_annealing(search_space,de_jong_f1, 1, exp_schedule(), 15000))
    #print(tabu_search(search_space,de_jong_f1, 1,10, 5, 150))
    print(ils(search_space,de_jong_f1, 1500, 1))


