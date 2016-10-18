"""
Author: Kevin Zhang <kevz@mit.edu>
Date: October 15th, 2016
"""

def normalize(dist):
	"""
	This function takes a dictionary object and normalizes it so that it adds
	up to 1.0, making it a valid probability distribution. It should not 
	mutate the dictionary object - instead, it should create a copy and return
	a new dictionary object with the same keys and new values.
	"""
	raise NotImplementedError()

class SudokuNode:
	def __init__(self, N, dist=None):
		"""
		Create a new SudokuNode. If dist is None, it should be initialized with
		a uniform probability distribution over the integers from [1,N]. The 
		distribution should ALWAYS contain all N values, even if the parameter 
		`dist` that is passed in the constructor does not contain all N values,
		you must explicitly set them to zero.
		"""
		self.dist = dist # you must store the current dist in self.dist
		raise NotImplementedError()

	def add(self, node):
		"""
		Add a node to the internal graph representation. Note that as this is 
		an undirected graph, it should also call the add function on the target 
		node and add self to the target node's outgoing links. It should return
		a reference to self as this will allow us to use some cool syntax for 
		linking multiple nodes this this node: node.add(n1).add(n2)
		"""
		raise NotImplementedError()

	def send(self):
		"""
		Compute the outgoing probability distribution - remember to normalize - 
		by multiplying/summing the internal distribution with the edge weights. 
		The edge distribution should be uniform over all values EXCEPT the 
		active value.

		See the sum-product algorithm in graphical models for more information 
		about this procedure. Basically, loop over all possible numbers for 
		this particular cell, multiply the probability of that number with the
		probability of neighbor cells having a different number, and add it all
		up to get a probability distribution over what they neighboring cell 
		should be conditioned on the current node.

		Iterate over all outgoing links, calling the receive method on the 
		connected nodes to send them this node's outgoing probability.
		"""
		raise NotImplementedError()

	def receive(self, dist):
		"""
		Update your internal believe state with the incoming distribution. In 
		essence, multiply the probability for each number together and remember
		to normalize.
		"""
		raise NotImplementedError()

	def __str__(self):
		return str(self.dist)

# the below code tries to solve a 3x3 sudoku puzzle
def solveSimpleSudoku():
	n = [[None]*3 for _ in range(3)]

	n[0][0] = SudokuNode(3, {1:0.8,2:0.1,3:0.1})
	n[0][1] = SudokuNode(3, {1:0.6,2:0.3,3:0.1})
	n[0][2] = SudokuNode(3)

	n[1][0] = SudokuNode(3)
	n[1][1] = SudokuNode(3)
	n[1][2] = SudokuNode(3)

	n[2][0] = SudokuNode(3)
	n[2][1] = SudokuNode(3)
	n[2][2] = SudokuNode(3)

	n[0][0].add(n[0][1]).add(n[0][2])
	n[0][1].add(n[0][2])
	n[1][0].add(n[1][1]).add(n[1][2])
	n[1][1].add(n[1][2])
	n[2][0].add(n[2][1]).add(n[2][2])
	n[2][1].add(n[2][2])

	n[0][0].add(n[1][0]).add(n[2][0])
	n[1][0].add(n[2][0])
	n[0][1].add(n[1][1]).add(n[2][1])
	n[1][1].add(n[2][1])
	n[0][2].add(n[1][2]).add(n[2][2])
	n[1][2].add(n[2][2])

	import random
	for _ in range(100):
	    i = random.randint(0, 2) 
	    j = random.randint(0, 2) 
	    n[i][j].send()

	def get_max(node):
	    return max([(node.dist[key], key) for key in node.dist.keys()])[1]

	print(get_max(n[0][0]), get_max(n[0][1]), get_max(n[0][2]))
	print(get_max(n[1][0]), get_max(n[1][1]), get_max(n[1][2]))
	print(get_max(n[2][0]), get_max(n[2][1]), get_max(n[2][2]))

if __name__ == "__main__":
	solveSimpleSudoku()