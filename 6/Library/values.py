from random import seed, uniform

##### Values #####
class Values():

	def __init__(self, problem, individual_size):
		self.individual_size = individual_size
		self.values = {}

		if problem == 'methinks':
			self.methinks()
		elif problem == 'jbrandao':
			pass
		elif problem == 'knapsack':
			self.knapsack()
		elif problem == 'tsp':
			self.tsp()
		elif problem == 'rastrigin':
			self.rastrigin()

	##### Methinks ######
	def methinks(self):
		self.values['sentence'] = 'GNU  Emacs  is  a  version of Emacs, written by the author of the original (PDP-10) Emacs, Richard Stallman.  The user functionality of GNU Emacs encompasses\n       everything other editors do, and it is easily extensible since its editing commands are written in Lisp.\n\n       The primary documentation of GNU Emacs is in the GNU Emacs Manual, which you can read using Info, either from Emacs or as a standalone program.  Please  look\n       there for complete and up-to-date documentation.  This man page is updated only when someone volunteers to do so.\n\n       Emacs  has  an  extensive interactive help facility, but the facility assumes that you know how to manipulate Emacs windows and buffers.  CTRL-h or F1 enters\n       the Help facility.  Help Tutorial (CTRL-h t) starts an interactive tutorial to quickly teach beginners the fundamentals of Emacs.  Help  Apropos  (CTRL-h  a)\n       helps  you  find a command with a name matching a given pattern, Help Key (CTRL-h k) describes a given key sequence, and Help Function (CTRL-h f) describes a\n       given Lisp function.\n\n       GNU Emacs\'s many special packages handle mail reading (RMail) and sending (Mail), outline editing (Outline), compiling (Compile),  running  subshells  within\n       Emacs windows (Shell), running a Lisp read-eval-print loop (Lisp-Interaction-Mode), automated psychotherapy (Doctor), and much more.'
	#####################

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
