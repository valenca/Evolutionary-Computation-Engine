from cPickle import load
import pylab as plt

data=[]

with open('scatter.plt','r') as f:
	while True:
		data.append(load(f))

pylab.figure()
	ln, = plt.plot([])
	plt.ion()
	plt.show()
	while True:
		plt.pause(1)
		ln.set_ydata(data)
		plt.draw()
	
