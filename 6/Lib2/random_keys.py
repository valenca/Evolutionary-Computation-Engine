from copy import deepcopy
from random import random

def decode_rk(vector):
    aux = deepcopy(vector)
    aux.sort()
    permutation =[ vector.index(elem) + 1 for elem in aux]
    return permutation


def generate_vector(size):
    return [random() for count in range(size)]

if __name__ == '__main__':
    vec = generate_vector(5)
    print(vec)
    print(decode_rk(vec))
    
