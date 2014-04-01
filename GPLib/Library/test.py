from random import sample,choice,randint
from copy import deepcopy

        
with open('../Data/data_symb.txt', 'r') as f:
	values = {}
	header = f.readline().split()
	values['header'] = [int(header.pop(0))]
	values['header'] += [[[header[i], int(header[i+1])] for i in range(0,len(header),2)]]
	values['data'] = [[float(j) for j in i.split()] for i in f.readlines()]
	print data

