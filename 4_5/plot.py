import matplotlib.pyplot as pl

with open("output") as f:
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

pl.plot(final_data[0],final_data[1])
pl.plot(final_data[0],final_data[2])

pl.axhline(0, color='black')
pl.axvline(0, color='black')
pl.show()
