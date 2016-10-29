"""
Author: Kevin Zhang <kevz@mit.edu>
Date: October 29th, 2016
"""
import numpy as np

class QuadraticFit:
	def __init__(self):
		"""
		Create some instance variables to hold observations.
		"""
		raise NotImplementedError()

	def predict(self, t):
		"""
		Return a (x, y) tuple for the given time.
		"""
		raise NotImplementedError()
		
	def observe(self, t, x, y):
		"""
		Both x and y are scalars. Save these observations and fit a 2nd order 
		polynomial so that we get the parametric equations x(t) and y(t). Even
		though it may seem intuitive to fit a 1st order polynomial to x, we are
		going to use a 2nd order polynomial to try and get a better prediction.

		Hint: Use the numpy API whenever possible.
		https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html
		"""
		raise NotImplementedError()
