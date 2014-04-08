##### Database #####
class Database():

	def __init__(self, generation, fitness, phenotype, parents, survivors,
		crossover, mutation, disturbance, neighbors, sort, status, stop):

		self.database = {

			'symb_reg':
				{
					'generation':	generation.math_reg,
					'fitness':		fitness.math_reg,
					'phenotype':	phenotype.math_reg,
					'parents':		parents.tournament,
					'survivors':	survivors.generational,
					'crossover':	crossover.subtree,
					'mutation':		mutation.point,
					'disturbance':	None,
					'neighbors':	None,
					'sort':			sort.maximization,
					'status':		status.math_reg,
					'stop':			stop.arrival_x
				}

			}
