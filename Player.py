from Character import *
from ListOfAbilities import *
class Player(Character):
	"""This is the player class.  It contains all the information and functions that a player might have.
	Might extend a higher class like Character, but for now stands alone.  Contains things like HP, MP, etc. """
	def __init__(self):
		super(Player, self).__init__(120,120,"You",[Punch(),Flex()])

