import Abilities
class Player(object):
	"""This is the player class.  It contains all the information and functions that a player might have.
	Might extend a higher class like Character, but for now stands alone.  Contains things like HP, MP, etc. """
	def __init__(self, HP, MP, abilityList):
		super(Player, self).__init__()
		self.HP = HP
		self.MP = MP
		self.abilityList = abilityList

