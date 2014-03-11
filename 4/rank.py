import os


path="Results/"

vec20=[]
vec50=[]
vec100=[]

for fname in os.listdir(path):
    with open(path+fname) as f:
        n_runs = int(f.readline())
        data = []
        for i in range(n_runs):
            n_generations = int(f.readline())
            data.append([[float(j) for j in f.readline().split()] for k in range(n_generations)])
            
    max_generations = max([len(data[i]) for i in range(n_runs)])
    final_data = [list(range(max_generations)),[0 for i in range(max_generations)],[0 for i in range(max_generations)]]
    
    
    for i in range(len(final_data[0])):
        n = 0
        for j in range(n_runs):
            if len(data[j]) > i:
                n += 1
                final_data[1][i] += data[j][i][0]
                final_data[2][i] += data[j][i][1]
        final_data[1][i] /= n
        final_data[2][i] /= n

        
    if(fname[:2]=='20'):
        vec20.append([final_data[1][-1],fname])
    elif (fname[:2]=='50'):
        vec50.append([final_data[1][-1],fname])
    elif (fname[:2]=='10'):
        vec100.append([final_data[1][-1],fname])
        

    
vec20.sort(reverse=True)
vec50.sort(reverse=True)
vec100.sort(reverse=True)
for i in vec20:
    print(i[0],i[1]) 
