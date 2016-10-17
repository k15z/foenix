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
		a uniform probability distribution over the integers from [1,N].
		"""
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
