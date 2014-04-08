from random import seed, uniform

##### Values #####
class Values():

	def __init__(self, problem, individual_size):
		self.individual_size = individual_size
		self.values = {}
		eval('self.'+problem)


	##### Onemax #####
	def onemax(self):
		pass
	##################

	##### Methinks ######
	def methinks(self):
		self.values['sentence'] = 'Methinks it is like a weasel'
	#####################

	##### Joao Brandao Numbers ######
	def jbrandao(self):
		pass
	#################################

	##### Knapsack ######
	def knapsack(self):
		correlation = 'strong'
		seed("knapsack")
		v = 10
		r = 5

		# None Correlation
		if correlation == 'none':
			self.values['weights'] = [int(uniform(0, v)) for i in range(self.individual_size)]
			self.values['values'] = [int(uniform(0, v)) for i in range(self.individual_size)]
		# Weak Correlation
		elif correlation == 'weak':
			self.values['weights'] = [int(uniform(0, v)) for i in range(self.individual_size)]
			self.values['values'] = [self.values['weights'][i] + int(uniform(0, v)) for i in range(self.individual_size)]
		# Strong Correlation
		elif correlation == 'strong':
			self.values['weights'] = [int(uniform(0, v)) for i in range(self.individual_size)]
			self.values['values'] = [self.values['weights'][i] + r for i in range(self.individual_size)]
		#
		self.values['max_weight'] = sum(self.values['weights'])/2
		seed()
	#####################

	##### Traveling Salesman Problem #####
	def tsp(self):
		with open('Data/wi29.tsp') as f:
			while f.readline() != "NODE_COORD_SECTION\n": True
			coord = [[float(string) for string in line.split()[1:]] for line in f]
			coord.pop(-1)
			self.values['distances'] = [[0 for j in range(len(coord))] for i in range(len(coord))]
			for i in range(len(coord)):
				for j in range(i,len(coord)):
					distance = (((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2))**(0.5)
					self.values['distances'][i][j] = self.values['distances'][j][i] = distance
	######################################

	##### Rastrigin #####
	def rastrigin(self):
		self.values['A'] = 10
		self.values['sigma'] = 0.4
	#####################

	##### Dispersion Problem #####
	def dispersion(self):
		with open('Data/in100.disp') as f:

			N=int(f.readline())
			D=int(f.readline())
			k=int(f.readline())
			vector=[]
			for i in range(N):
				a=[]
				for j in range(D):
					a.append(float(f.readline()))
				vector.append(a)
			
			self.values['coords']=vector
			self.values['dp']=dict()
			self.values['static_binary']=80
	##############################
