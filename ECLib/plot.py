from matplotlib import pyplot
from pickle import load
from sys import exit
from os import listdir
from numpy import array, mean, vstack

if __name__ == '__main__':

	colours = ['b','g','r','c','m','y','k','w']

	parameters = {0:'Algorithm',
	1:'Number of Generations',
	2:'Population Size',
	3:'Individual Size',
	4:'Crossover Probability',
	5:'Mutation Probability',
	6:'Disturbance Probability',
	7:'Tournament Size',
	8:'Elite Percentage',
	9:'Number of Points Cut',
	10:'Parents Function',
	11:'Survivors Function',
	12:'Crossover Function'}
	print('\n## Which parameter would you like to compare? ##\n')
	for key,value in parameters.items():
		print('  '+str(key)+':\t'+value)
	print('\nOption: ')
	option = int(input())
	if not 0 <= option <= 12:
		exit()

	data_g = []
	data_r = []
	for j in range(1,len(listdir('Results/Full/'))+1):
		with open('Results/Full/test_'+str(j)+'.out', 'rb') as f:
			header = load(f)
			results = load(f)

			parameter = header[parameters[option]]
			bests = mean(array([result['best_fitnesses'] for result in results]), axis=0)
			averages = mean(array([result['average_fitnesses'] for result in results]), axis=0)
			final_bests = [result['best_fitnesses'][-1] for result in results]

			if parameter in [i[0] for i in data_g]:
				index = [i[0] for i in data_g].index(parameter)
				data_g[index][1] = vstack((data_g[index][1], bests))
				data_g[index][2] = vstack((data_g[index][2], averages))
				data_r[index][1].extend(final_bests)
			else:
				data_g.append([parameter, array(bests), array(averages)])
				data_r.append([parameter, final_bests])

	if len(data_g[0][1].shape) > 1:
		for i in data_g:
			i[1] = mean(i[1], axis=0)
			i[2] = mean(i[2], axis=0)

	figure1 = pyplot.figure(1)
	axis1 = figure1.add_axes([0.1, 0.175, 0.825, 0.75])
	x = list(range(len(data_g[0][1])))
	for i in range(len(data_g)):
		axis1.plot(x, data_g[i][1],colours[i],label=data_g[i][0])
		axis1.plot(x, data_g[i][2],colours[i]+'--')
	handles, labels = axis1.get_legend_handles_labels()
	axis1.legend(handles, labels, loc=9, ncol=4, bbox_to_anchor=(.5,-.075), borderaxespad=0.)
	axis1.grid('on')
	axis1.set_title(parameters[option],fontsize=20)

	figure2 = pyplot.figure(2)
	axis2 = figure2.add_axes([0.1, 0.1, 0.825, 0.825])
	bp = axis2.boxplot([i[1] for i in data_r], sym='x')
	#handles, labels = axis2.get_legend_handles_labels()
	#axis2.legend(handles, labels, loc=9, ncol=4, bbox_to_anchor=(.5,-.075), borderaxespad=0.)
	#axis2.grid('on')
	axis2.set_title(parameters[option],fontsize=20)

	pyplot.setp(bp['boxes'], color='black')
	pyplot.setp(bp['whiskers'], color='black')
	pyplot.setp(bp['fliers'], color='black', marker='x')

	axis2.yaxis.grid(True, linestyle='-', which='major', color='lightgrey')
	pyplot.setp(axis2, xticklabels=[i[0] for i in data_r])

	pyplot.show()
