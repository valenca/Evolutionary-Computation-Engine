from operator import itemgetter

##### Individual Sorter #####
class Sort():

	def __init__(self):
		pass

	##### Decreasingly Sorter #####
	def maximization(self, population):
		population.sort(key=itemgetter('fit'), reverse = True)
	###############################

	##### Increasingly Sorter #####
	def minimization(self, population):
		population.sort(key=itemgetter('fit'), reverse = False)
	###############################
