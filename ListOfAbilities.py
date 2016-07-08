from Abilities import *

class Punch(Ability):
	def __init__(self):
		super(Punch, self).__init__("punch",10,10)
	def execute(self,user,target):
		if user.mp>10:
			target.hp = target.hp - 10
			user.mp = user.mp - 10
		else:
			print("you're too whimpy")


class Flex(Ability):
	def __init__(self):
		super(Flex, self).__init__("Flex",-10,10)



		
