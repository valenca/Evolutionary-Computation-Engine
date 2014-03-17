import os
from matplotlib import pyplot as pl

path="output"

vec20=[]
vec50=[]
vec100=[]

fname=""
with open(path+fname) as f:
    n_runs = int(f.readline())
    data = []
    for i in range(n_runs):
        n_generations = int(f.readline())
        data.append([[float(j) for j in f.readline().split()] for k in range(n_generations)])
            
max_generations = max([len(data[i]) for i in range(n_runs)])
final_data = [list(range(max_generations)),[0 for i in range(max_generations)],[0 for i in range(max_generations)]]
   
final_data=[i[-1] for i in data]

final_data=map(list, zip(*final_data))

print final_data

pl.plot(list(range(len(data))),final_data[0])
pl.plot(list(range(len(data))),final_data[1])

pl.axhline(0, color='black')
pl.axvline(0, color='black')
pl.show()
