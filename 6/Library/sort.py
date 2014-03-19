from operator import itemgetter

##### Individual Sorter #####
class Sort():

	def __init__(self):
		pass

	##### Decreasingly Sorter #####
	def decrease(self, population):
		population.sort(key=itemgetter('fit'), reverse = True)
	###############################

	##### Increasingly Sorter #####
	def increase(self, population):
		population.sort(key=itemgetter('fit'), reverse = False)
	###############################
