

__author__ = 'Ernesto Costa'
__date__ = 'April 2012'


import random
import math
import matplotlib.pyplot as plt

# Random
def random_initial_population(domain, size):
    return [[random.uniform(dom_i[0], dom_i[1]) for dom_i in domain] for count in range(size)]

# Parallel diversification
def latin_hypercube(domain, size):
    """One individual by hypercube."""
    numb_segments = size ** (1.0/len(domain))
    vectors = []
    for dom_i in domain:
        dist = (dom_i[1] - dom_i[0])/ numb_segments
        vectors.append(list(frange(dom_i[0],dom_i[1], dist))) 
    pairs = []
    for vector in vectors:
        pairs_from_vector = [[vector[i], vector[i+1]] for i in range(len(vector)-1)]
        pairs.append(pairs_from_vector)
    hyper_cubes = gen_cross_all(pairs)
    data_points = [generate_one(hc) for hc in hyper_cubes]
    return data_points  


def gen_cross_all(values):
    partial = [[elem] for elem in values[0]]
    remaining = values[1:]
    return gen_cross(partial, remaining)

def gen_cross(partial,remaining):
    """partial = list of points with dimension k.
    remaining = list of n-k dimensions."""
    if remaining == []:
        return partial
    else:
        partial = expand(partial,remaining[0])
        return gen_cross(partial,remaining[1:])
    

def expand(partial, dimension):
    new_partial = []
    for segment in dimension:
        new_partial.extend(cross(partial,segment))
    return new_partial

def cross(partial,segment):
    return [elem + [segment] for elem in partial]
       
def values(vector):
    random.seed(12345)
    return [random.uniform(vector[i],vector[i+1])for i in range(len(vector) - 1)]
  
 

# Sequential Diversification
# Simple Sequential Inhibition
def ssi(domain,size, min_dist):
    """not controlling max trials."""
    pop = [generate_one(domain)]
    for i in range(size-1):
        indiv = generate_one(domain)
        while not accept(indiv,pop,min_dist):
            indiv = generate_one(domain)
        pop.append(indiv)
    return pop

def accept(indiv,population, distance):
    for elem in population:
        if euclidean_distance(indiv,elem) < distance:
            return False
    return True

def ssi_b(domain_size, min_dist, max_reject):
    """Controlling max trials."""
    pop = [generate_one(domain)]
    for i in range(size-1):
        reject = 0
        indiv = generate_one(domain)
        while not accept(indiv,pop,min_dist):
            if reject == max_reject:
                return []
            else:
                reject += 1
                indiv = generate_one(domain)
        pop.append(indiv)
    return pop 


def generate_one(domain):
    return [random.uniform(dom_i[0],dom_i[1]) for dom_i in domain]

def generate_one_discrete(domain,size):
    return [random.choice(domain) for i in range(size)]
            
# auxiliary
def euclidean_distance(vec_1, vec_2):
    pairs = list(zip(vec_1,vec_2))   
    return math.sqrt(sum([(pair[0] - pair[1])**2 for pair in pairs]))

def hamming_distance(vec_1, vec_2):
    return sum([ 1 for i in range(len(vec_1)) if vec_1[i] != vec_2[i]])
    
    
    
def frange(n1,n2=None,n3=1.0):
    """
    Floating point range.
    """
    if n2 == None:
        n2 = float(n1)
        n1 = 0.0
    proximo = n1
    while (n3 >= 0.0 and proximo <= n2) or (n3 < 0.0 and proximo >= n2):
        yield proximo
        proximo = proximo +  n3



if __name__ == '__main__':
    """
    pop_1 = random_initial_population([[0,1],[0,1]],81)
    x_1 = [val[0] for val in pop_1]
    y_1 = [val[1] for val in pop_1]
    plt.title('Random Initialization')
    plt.axis([0.0,1.0,0.0,1.0])
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.plot(x_1,y_1,'ro')
    plt.show() 
  
    pop_3 = latin_hypercube([[0,1],[0,1]],81)
    x_3 = [val[0] for val in pop_3]
    y_3 = [val[1] for val in pop_3]
    plt.title('Latin Hypercube')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x_3,y_3,'ro')
    plt.show()

    pop_4 = ssi([[0,1],[0,1]],81,0.05)
    x_4 = [val[0] for val in pop_4]
    y_4 = [val[1] for val in pop_4]
    plt.title('Simple Sequential Inhibition')
    plt.plot(x_4,y_4,'ro')
    plt.xlabel('X1') 
    plt.ylabel('X2')
    plt.show()  
    """
   
    pop_1 = random_initial_population([[0,1],[0,1]],225)
    x_1 = [val[0] for val in pop_1]
    y_1 = [val[1] for val in pop_1]
    
    pop_3 = latin_hypercube([[0,1],[0,1]],225)
    x_3 = [val[0] for val in pop_3]
    y_3 = [val[1] for val in pop_3] 
    
    pop_4 = ssi([[0,1],[0,1]],225,0.05)
    x_4 = [val[0] for val in pop_4]
    y_4 = [val[1] for val in pop_4] 
    
    plt.figure(1)
    plt.subplot(311)    
    plt.title('Random Initialization')
    plt.gca().axes.get_xaxis().set_ticks([])
    plt.plot(x_1,y_1,'ro')
    plt.ylabel('X2')
    
    plt.subplot(312)
    plt.title('Latin Hypercube')
    plt.gca().axes.get_xaxis().set_ticks([])
    plt.ylabel('X2')
    plt.plot(x_3,y_3,'bo')

    plt.subplot(313)
    plt.title('Simple Sequential Inhibition')
    plt.xlabel('X1')
    plt.ylabel('X2') 
    plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x_4,y_4,'go')
   
    plt.show()  
    """
    # --- distances
    vec_1 = generate_one_discrete(['A','C','T','G'],10)
    vec_2 = generate_one_discrete(['A','C','T','G'],10)
    
    print vec_1
    print vec_2
    print
    print hamming_distance(vec_1,vec_2)

    print latin_hypercube_population([[0,1],[0,1]],9)
    print list(frange(0,1,1.0/3))
    """
    
    