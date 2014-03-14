import matplotlib.pyplot as pl, sys

if __name__ == '__main__':

	if(len(sys.argv)<2):
		print("Missing arguments")
		sys.exit()

	if sys.argv[1] == '1': ofile = "Results/jb.out"
	elif sys.argv[1] == '2': ofile = "Results/ks_nc.out"
	elif sys.argv[1] == '3': ofile = "Results/ks_wc.out"
	else: ofile = "Results/ks_sc.out"

	colours = ['r','g','b']
	lines = [0,0,0]
	data = [[],[],[]]
	with open(ofile) as f:
		n_runs = int(f.readline())
		for i in range(n_runs):
			for j in range(3):
				n_generations = int(f.readline())
				data[j].append([[float(j) for j in f.readline().split()] for k in range(n_generations)])

	[[data[2][i][j].append(0) for j in range(len(data[2][i]))] for i in range(len(data[2]))]

	final_data = [list(range(n_generations))]
	for i in range(3):
		final_data.append([[0 for j in range(n_generations)] for k in range(2)])
		for j in range(len(final_data[0])):
			for k in range(n_runs):
				final_data[i+1][0][j] += data[i][k][j][0];
				final_data[i+1][1][j] += data[i][k][j][1];
			final_data[i+1][0][j] /= n_runs
			final_data[i+1][1][j] /= n_runs

	for i in range(3):
		lines[i], = pl.plot(final_data[0],final_data[i+1][0],colours[i])
		if i < 2: pl.plot(final_data[0],final_data[i+1][1],colours[i]+"--")

	pl.legend(lines, ['sea','phc','bhc'],loc=4)
	pl.axhline(0, color='black')
	pl.axvline(0, color='black')
	pl.show()
