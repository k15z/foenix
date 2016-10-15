"""
Author: Kevin Zhang <kevz@mit.edu>
Date: October 14th, 2016
"""

class TimeInterval:

	def __init__(self, ti_string):
		"""
		This creates a new TimeInterval object. It parses the ti_string (time 
		interval string) parameter. The time interval string typically consists
		of comma separated "time items", where each time item consists of an 
		integer and a unit. The unit may be singular or plural, and units may 
		be repeated. Whitespace should be ignored and units should not be case 
		sensitive.

		For example "1 seconds, 1 second" should result in a time interval of 
		2 seconds. Some more examples as well as a formal grammar are shown 
		below.
		
		Examples:
			5 hours, 4 minutes, 3 seconds
			5 hours, 4 minutes, 1 second
			1 minute, 5 hours, 1 seconds, 1 second
			5 hours, 1 minute, 2 seconds

		Grammar:
			ti_string := [<ti_item>, ]*
			ti_item = <hour_str> | <minute_str> | <second_str>
			hour_str := <integer> [hour | hours]
			minute_str := <integer> [minute | minutes]
			second_str := <integer> [second | seconds]
		"""
		raise NotImplementedError()

	def getHours(self):
		"""
		This function returns a real number indicating the length of this time 
		interval in hours. It is expected to return a result within 1e-7 of the
		actual value.
		"""
		raise NotImplementedError()

	def getMinutes(self):
		"""
		This function returns a real number indicating the length of this time 
		interval in minutes. It is expected to return a result within 1e-7 of 
		the actual value.
		"""
		raise NotImplementedError()

	def getSeconds(self):
		"""
		This function returns a real number indicating the length of this time 
		interval in seconds.
		"""
		raise NotImplementedError()
