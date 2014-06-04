import plotly
from pickle import load
from numpy import array, mean, vstack

py = plotly.plotly("Mehlins", "vq0aqwkoz4")

with open('fixed5', 'rb') as f:
	results = load(f)
bests1 = mean(array([result['best_fitnesses'] for result in results]), axis=0)
averages1 = mean(array([result['average_fitnesses'] for result in results]), axis=0)
final_bests1 = [result['best_fitnesses'][-1] for result in results]

with open('adapt', 'rb') as f:
	results = load(f)
#results[-15] = results[-16]
bests2 = mean(array([result['best_fitnesses'] for result in results]), axis=0)
averages2 = mean(array([result['average_fitnesses'] for result in results]), axis=0)
final_bests2 = [result['best_fitnesses'][-1] for result in results]

with open('sigmas', 'rb') as f:
  results = load(f)
sigmas = list(map(abs,mean(array(results), axis=0)))[:-1]

indexes = range(len(bests1)+1)

trace1 = {'x': indexes, 'y': bests1}
trace2 = {'x': indexes, 'y': averages1}
trace3 = {'x': indexes, 'y': bests2}
trace4 = {'x': indexes, 'y': averages2}
trace5 = {'x': indexes, 'y': sigmas}

#py.plot([trace1, trace2, trace3, trace4])

box1 = {'y': final_bests1,
  	'type': 'box',
  	'boxpoints': 'all',
  	'jitter': 0.1,
  	'pointpos': -1.2}
box2 = {'y': final_bests2,
  	'type': 'box',
  	'boxpoints': 'all',
  	'jitter': 0.1,
  	'pointpos': -1.2}

#py.plot([box1,box2])

py.plot([trace5])
