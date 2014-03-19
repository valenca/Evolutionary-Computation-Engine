from matplotlib import pyplot
from cPickle import load

with open("output", "r") as f:
	n_runs = load(f)
	results = [[],[]]
	for i in range(n_runs):
		best,avg = load(f)
		results[0].append(best)
		results[1].append(avg)

data = [list(range(len(results[0][0]))),[0]*len(results[0][0]),[0]*len(results[0][0])]

for i in range(len(results[0][0])):
	for j in range(n_runs):
		data[1][i] += results[0][j][i]
		data[2][i] += results[1][j][i]
	data[1][i] /= n_runs
	data[2][i] /= n_runs

pyplot.plot(data[0],data[1])
pyplot.plot(data[0],data[2],'--')

pyplot.axhline(0, color='black')
pyplot.axvline(0, color='black')
pyplot.show()
