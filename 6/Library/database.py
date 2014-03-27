##### Database #####
class Database():

	def __init__(self, generation, fitness, phenotype, parents, survivors,
		crossover, mutation, disturbance, neighbors, sort, status, stop):

		self.database = {

			'onemax':
				{
					'generation':	generation.binary,
					'fitness':		fitness.onemax,
					'phenotype':	phenotype.onemax,
					'parents':		parents.tournament,
					'survivors':	survivors.elitism,
					'crossover':	crossover.one_point,
					'mutation':		mutation.binary,
					'disturbance':	disturbance.binary,
					'neighbors':	neighbors.binary,
					'sort':			sort.maximization,
					'status':		status.onemax,
					'stop':			stop.best_stabilization
				},

			'methinks':
				{
					'generation':	generation.methinks,
					'fitness':		fitness.methinks,
					'phenotype':	phenotype.methinks,
					'parents':		parents.tournament,
					'survivors':	survivors.elitism,
					'crossover':	crossover.uniform,
					'mutation':		mutation.methinks,
					'disturbance':	disturbance.methinks,
					'neighbors':	neighbors.methinks,
					'sort':			sort.minimization,
					'status':		status.methinks,
					'stop':			stop.best_stabilization
				},

			'jbrandao':
				{
					'generation':	generation.binary,
					'fitness':		fitness.jbrandao,
					'phenotype':	phenotype.jbrandao,
					'parents':		parents.tournament,
					'survivors':	survivors.elitism,
					'crossover':	crossover.one_point,
					'mutation':		mutation.binary,
					'disturbance':	disturbance.binary,
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
					'disturbance':	disturbance.binary,
					'neighbors':	neighbors.binary,
					'sort':			sort.maximization,
					'status':		status.knapsack,
					'stop':			stop.best_stabilization
				},

			'tsp':
				{
					'generation':	generation.integer,
					'fitness':		fitness.tsp,
					'phenotype':	phenotype.tsp,
					'parents':		parents.tournament,
					'survivors':	survivors.elitism,
					'crossover':	crossover.ordered,
					'mutation':		mutation.swap,
					'disturbance':	disturbance.swap,
					'neighbors':	neighbors.rastrigin,
					'sort':			sort.minimization,
					'status':		status.tsp,
					'stop':			stop.interval_stabilization
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
					'disturbance':	disturbance.rastrigin,
					'neighbors':	neighbors.rastrigin,
					'sort':			sort.minimization,
					'status':		status.rastrigin,
					'stop':			stop.interval_stabilization
				}
			}
