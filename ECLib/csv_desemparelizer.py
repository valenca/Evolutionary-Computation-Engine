from sys import argv

for path in argv[1:]:
	with open(path,'r') as f:
		data=[]
		for line in f:
			data.append(list(line[:-1].split(',')))

	new=[item for sublist in data for item in sublist]
	cla=['0']*len(data[0])+['1']*len(data[1])

	data=zip(cla,new)
	with open("new_"+path,'w') as f:
		for line in data:
			f.write(",".join(line)+"\n")
		
