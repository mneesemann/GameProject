import Player
import Monster
import Map

class Game(object):
	"""This is the model for our game.  It will contain things like player, monster, map, functions like attack etc, and 
	functions that interact with Controller"""
	def __init__(self, arg):
		super(Game, self).__init__()
		self.arg = arg

	def makeGame(self):
		""" For now this just creates an instance of player to test these funcitons out."""
		player = Player.Player(120,120)
		map = Map.Map(3) #3 is just a dummy argument
		monster = Monster.Monster(120,120)

	def Attack(self, Attacker, Defender):
		Defender.HP = Defender.HP -5 