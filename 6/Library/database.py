##### Database #####
class Database():

	def __init__(self, generation, fitness, phenotype, parents, survivors,
				 crossover, mutation, neighbors, sort, status, stop):

		self.database = {

			'jbrandao':
				{
					'generation':	generation.binary,
					'fitness':		fitness.jbrandao,
					'phenotype':	phenotype.jbrandao,
					'parents':		parents.tournament,
					'survivors':	survivors.elitism,
					'crossover':	crossover.one_point,
					'mutation':		mutation.binary,
					'neighbors':	neighbors.binary,
					'sort':			sort.maximization,
					'status':		status.jbrandao,
					'stop':			stop.best_stabilization
				},

			'knapsack':
				{
					'generation':	generation.binary,
					'fitness':		fitness.knapsack,
					'phenotype':	phenotype.knapsack,
					'parents':		parents.tournament,
					'survivors':	survivors.elitism,
					'crossover':	crossover.one_point,
					'mutation':		mutation.binary,
					'neighbors':	neighbors.binary,
					'sort':			sort.maximization,
					'status':		status.knapsack,
					'stop':			stop.best_stabilization
				},

			'rastrigin':
				{
					'generation':	generation.rastrigin,
					'fitness':		fitness.rastrigin,
					'phenotype':	phenotype.rastrigin,
					'parents':		parents.tournament,
					'survivors':	survivors.elitism,
					'crossover':	crossover.one_point,
					'mutation':		mutation.rastrigin,
					'neighbors':	neighbors.rastrigin,
					'sort':			sort.minimization,
					'status':		status.rastrigin,
					'stop':			stop.interval_stabilization
				}
			}
