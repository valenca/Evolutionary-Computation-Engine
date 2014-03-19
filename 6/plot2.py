from matplotlib import pyplot
from cPickle import load

outputs = ['Results/output1','Results/output2','Results/output3']
colours = ['r','g','b']
lines = [0,0,0]
for k in range(3):

	with open(outputs[k], "r") as f:
		n_runs = load(f)
		results = [[],[]]
		for i in range(n_runs):
			best,avg = load(f)
			results[0].append(best)
			results[1].append(avg)

	data = [list(range(n_runs)),[0]*n_runs,[0]*n_runs]

	for j in range(n_runs):
		data[1][j] += results[0][j][-1]
		data[2][j] += results[1][j][-1]

	lines[k], = pyplot.plot(data[0],data[1],colours[k])
	pyplot.plot(data[0],data[2],colours[k]+'--')

pyplot.legend(lines, ['tournament','roulette','sus'],loc=1)
pyplot.axhline(0, color='black')
pyplot.axvline(0, color='black')
pyplot.show()
