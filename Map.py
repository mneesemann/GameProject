class Map(object):
	"""This is the class that contains all the things that have to do with the map itself.  Contains an array that is the game board.
	It is the place that contains the information of where all of the characters are and if they are interacting.  This might change :)
	"""
	def __init__(self, grid):
		super(Map, self).__init__()
		self.grid = grid
		