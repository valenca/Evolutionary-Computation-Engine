from copy import deepcopy

def decode_rk(vector):
    """Assume all elements are different."""
    aux = vector[:]
    aux.sort()
    permutation =[ vector.index(elem) for elem in aux]
    return permutation

def decode_rk_b(vector):
    """Work even with repeated elements."""
    copia = deepcopy(vector)
    aux = deepcopy(vector)
    aux.sort()
    permutation = []
    for i,elem in enumerate(aux):
        permutation.append(copia.index(elem))
        copia[copia.index(elem)] = None
    return permutation

vector = [0.3,0.5,0.4,0.3,0.2,0.3,0.4]
print(decode_rk(vector))
print(decode_rk_b(vector))
print(vector)