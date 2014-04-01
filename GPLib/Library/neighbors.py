from copy import deepcopy
from random import gauss, choice
from string import printable

##### Neighbors Generator #####
class Neighbors():

	def __init__(self, individual_size, values):
		self.individual_size = individual_size
		self.values = values
