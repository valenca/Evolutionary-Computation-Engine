import matplotlib.pyplot as pl, sys

if __name__ == '__main__':

	if(len(sys.argv)<8):
		print("Missing arguments")
		sys.exit()

	n_generations = ['50','100','500']
	population_size = ['100','250','500']
	individual_size = ['20','50','100']
	parents_selection_group_size = ['3','5','7']
	crossover_probability = ['0.3','0.6','0.9']
	mutation_probability = ['0.01','0.05','0.1','0.3']
	elite_percentage = ['0.02','0.05','0.1']

	all_data = [individual_size, population_size, n_generations, mutation_probability,
	crossover_probability, elite_percentage, parents_selection_group_size]

	index = int(sys.argv[1])-1
	indexes = list(range(7))
	indexes.pop(index)

	for i, j in zip(indexes, range(2,9)):
		all_data[i] = [sys.argv[j] for k in range(len(all_data[index]))]

	#print(all_data)

	colours = ['r','g','b','y']
	lines = [0 for i in range(len(all_data[index]))]
	for l in range(len(all_data[index])):
		with open("Results/"+all_data[0][l]+"_"+all_data[1][l]+"_"+all_data[2][l]+"_"+all_data[3][l]+\
			"_"+all_data[4][l]+"_"+all_data[5][l]+"_"+all_data[6][l]+".out") as f:
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
					final_data[1][i] += data[j][i][0];
					final_data[2][i] += data[j][i][1];
			final_data[1][i] /= n
			final_data[2][i] /= n

		lines[l], = pl.plot(final_data[0],final_data[1],colours[l])
		pl.plot(final_data[0],final_data[2],colours[l]+'--')

	pl.legend(lines, [all_data[index][i] for i in range(len(all_data[index]))],loc=4)
	pl.axhline(0, color='black')
	pl.axvline(0, color='black')
	pl.show()

