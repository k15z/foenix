"""
Author: Kevin Zhang <kevz@mit.edu>
Date: October 14th, 2016
"""

class FloodFill:
	def __init__(self, arr):
		"""
		This creates a new FloodFill object from the given 2D array. For more 
		information, see https://en.wikipedia.org/wiki/Flood_fill. You can 
		think of this as implementing the "paint bucket" tool found in most 
		image editors. When you click on a part of the image, it fills in all
		nearby pixels (of the same color as the pixel you clicked) with a new
		color of your choice.
		"""
		raise NotImplementedError()

	def fill(self, i, j, x):
		"""
		This returns a copy of the 2D array which has been flood-filled with 
		the value of x. Only cells directly north, south, east, or west are 
		considered to be connected/touching - do NOT include diagonals.
		"""
		raise NotImplementedError()
