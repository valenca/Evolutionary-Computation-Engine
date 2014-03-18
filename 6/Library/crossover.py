from random import sample
from copy import deepcopy

def cycle_crossover(A,B):
    count=1
    length=len(A)
    mask=[0]*length
    tog=False
    for i in A:
        while(mask[A.index(i)]==0):
            tog=True
            mask[A.index(i)]=count
            i=A[B.index(i)]
        if tog:
            tog=False
            count+=1
    ab=[A,B]
    C=[]
    D=[]
    for i in range(length):
        C.append(ab[(mask[i]+1)%2][i])
        D.append(ab[(mask[i])%2][i])
    return C,D
    
Z=range(10)
A=sample(Z,len(Z))
B=sample(Z,len(Z))
cycle_crossover(A,B)    



