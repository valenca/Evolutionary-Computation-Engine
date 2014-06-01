##### Database #####
class Database():

	def __init__(self, generation, individuals, distance, fitness, phenotype, parents,
		survivors, crossover, mutation, disturbance, neighbors, sort, status, stop):

		self.database = {

			'onemax':
				{
					'generation':	generation.rus,
					'individuals':	individuals.binary,
					'distance':		distance.euclidian,
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
					'generation':	generation.rus,
					'individuals':	individuals.methinks,
					'distance':		distance.euclidian,
					'fitness':		fitness.methinks,
					'phenotype':	phenotype.methinks,
					'parents':		parents.tournament,
					'survivors':	survivors.best,
					'crossover':	crossover.uniform,
					'mutation':		mutation.methinks,
					'disturbance':	disturbance.methinks,
					'neighbors':	neighbors.methinks,
					'sort':			sort.minimization,
					'status':		status.methinks,
					'stop':			stop.arrival_x
				},

			'jbrandao':
				{
					'generation':	generation.rus,
					'individuals':	individuals.binary,
					'distance':		distance.euclidian,
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
					'generation':	generation.rus,
					'individuals':	individuals.binary,
					'distance':		distance.euclidian,
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
					'generation':	generation.sd,
					'individuals':	individuals.integer,
					'distance':		distance.hamming,
					'fitness':		fitness.tsp,
					'phenotype':	phenotype.tsp,
					'parents':		parents.tournament,
					'survivors':	survivors.elitism,
					'crossover':	crossover.pmx,
					'mutation':		mutation.revert,
					'disturbance':	disturbance.swap,
					'neighbors':	neighbors.rastrigin,
					'sort':			sort.minimization,
					'status':		status.tsp,
					'stop':			stop.best_stabilization
				},

			'rastrigin':
				{
					'generation':	generation.rus,
					'individuals':	individuals.rastrigin,
					'distance':		distance.euclidian,
					'fitness':		fitness.rastrigin,
					'phenotype':	phenotype.rastrigin,
					'parents':		parents.roulette,
					'survivors':	survivors.elitism,
					'crossover':	crossover.one_point,
					'mutation':		mutation.rastrigin,
					'disturbance':	disturbance.rastrigin,
					'neighbors':	neighbors.rastrigin,
					'sort':			sort.minimization,
					'status':		status.rastrigin,
					'stop':			stop.interval_stabilization
				},

			
			'schewefel':
				{
					'generation':	generation.rus,
					'individuals':	individuals.schewefel,
					'distance':		distance.euclidian,
					'fitness':		fitness.schewefel,
					'phenotype':	phenotype.schewefel,
					'parents':		parents.tournament,
					'survivors':	survivors.elitism,
					'crossover':	crossover.one_point,
					'mutation':		mutation.schewefel,
					'disturbance':	disturbance.rastrigin,
					'neighbors':	neighbors.rastrigin,
					'sort':			sort.minimization,
					'status':		status.rastrigin,
					'stop':			stop.interval_stabilization
				},

			'dispersion':
				{
					'generation':	generation.rus,
					'individuals':	individuals.static_binary,
					'distance':		distance.euclidian,
					'fitness':		fitness.dispersion,
					'phenotype':	phenotype.dispersion,
					'parents':		parents.roulette,
					'survivors':	survivors.elitism,
					'crossover':	crossover.order,
					'mutation':		mutation.swap,
					'disturbance':	disturbance.rastrigin,
					'neighbors':	neighbors.rastrigin,
					'sort':			sort.maximization,
					'status':		status.dispersion,
					'stop':			stop.interval_stabilization
				}
			}
