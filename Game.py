import Player
import Monster
import Map
import Abilities

class Game(object):
	"""This is the model for our game.  It will contain things like player, monster, map, functions like attack etc, and 
	functions that interact with Controller"""

	"""This is the list of abilities.  Not sure how they're going to be implemented when the code is complete but for now they're
	just static variables"""
	
	stickArround = Abilities.Ability("Strick Around",30,20)
	chillOut = Abilities.Ability("Chill Out",15,10)
	youreAllSlutsPunch = Abilities.Ability("You're all SLUTS!",7,5)
	listOfAbilities = [stickArround,chillOut,youreAllSlutsPunch]

	def __init__(self):
		super(Game, self).__init__()


	def makeGame(self):
		pass

	def Attack(self, ability, attacker, defender):
		defender.HP = defender.HP -5 

	def makePlayer(self,HP,MP,abilities):
		return Player.Player(HP,MP,abilities)

	def makeMonster(self,HP,MP,abilities):
		return Monster.Monster(HP,MP,abilities)






	
