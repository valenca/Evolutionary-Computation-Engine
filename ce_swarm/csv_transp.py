from sys import argv

for path in argv[1:]:
	with open(path,'r') as f:
		data=[]
		for line in f:
			data.append(list(line[:-1].split(',')))

	data=list(zip(*data))

	with open(path,'w') as f:
		for line in data:
			f.write(",".join(line)+"\n")
