from random import seed, uniform

##### Values #####
class Values():

	def __init__(self, problem, individual_size):
		self.individual_size = individual_size
		self.values = {}

		if problem == 'symb_reg':
			self.math_reg('Data/data_symb.txt')
		elif problem == 'sin_reg':
			self.math_reg('Data/data_sin.txt')
		elif problem == 'sphere_reg':
			self.math_reg('Data/data_sphere.txt')

	##### Methematical Regression ######
	def math_reg(self, input_file):
		with open(input_file, 'r') as f:
			header = f.readline().split()
			self.values['header'] = [int(header.pop(0))]
			self.values['header'] += [[[header[i], int(header[i+1])] for i in range(0,len(header),2)]]
			self.values['data'] = [[float(j) for j in i.split()] for i in f.readlines()]
		print self.values
	####################################
