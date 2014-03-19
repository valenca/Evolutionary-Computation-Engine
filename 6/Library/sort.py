from operator import itemgetter

##### Individual Sorter #####
class Sort():

	def __init__(self):
		pass

	##### Decreasingly Sorter #####
	def sort_decrease(self, population):
		population.sort(key=itemgetter('fit'), reverse = True)
	###############################

	##### Increasingly Sorter #####
	def sort_increase(self, population):
		population.sort(key=itemgetter('fit'), reverse = False)
	###############################
