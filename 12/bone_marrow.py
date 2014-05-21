import random

def bone_marrow(library,size):
    antibodies = []
    for index in range(size):
        # generate a receptor
        antibody = []
        for lib in library:
            # generate an element
            ab = random.choice(lib)
            antibody.append(ab)
        antibodies.append(antibody)
    return antibodies


if __name__ == '__main__':
    lib_1 = ['A','B','C','D']
    lib_2 = [1,2,3]
    lib_3 = ['@','&']
    library = [lib_1,lib_2,lib_3]
    print(bone_marrow(library,5))
    