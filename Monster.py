class Monster(object):
	"""This is the Monster class.  It contains all the information and functions that a Monster might have.
	Might extend a higher class like Character, but for now stands alone.  Contains things like HP, MP, etc. """
	def __init__(self, HP, MP):
		super (Monster, self).__init__()
		self.HP = HP
		self.MP = MP