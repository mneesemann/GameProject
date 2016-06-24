import Player
import Monster
import Map

class Game(object):
	"""This is the main class for running the game.  It controls the game states and is the first thing to run.  It won't contain any
	game logic itself, just manage the various states of the game, loading screen, start screen, different levels, etc"""
	def __init__(self, arg):
		super(Game, self).__init__()
		self.arg = arg

	def makeGame(self):
		print("hello")
		""" For now this just creates an instance of player to test these funcitons out."""
		player = Player.Player(120,120)
		map = Map.Map(3) #3 is just a dummy argument
		monster = Monster.Monster(120,120)
		print ("we're inside makegame alright")
		print(player.HP)

game = Game(3)
print(game.arg)
game.makeGame() 