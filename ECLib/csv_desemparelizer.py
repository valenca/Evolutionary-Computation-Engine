from sys import argv

for path in argv[1:]:
	with open(path,'r') as f:
		data=[]
		for line in f:
			data.append(list(line[:-1].split(',')))

	print data

	with open(path,'w') as f:
		for line in data[]:
			print 
			#f.write(",".join(line)+"\n")
