class Ability(object):
	"""docstring for Ability"""
	def __init__(self,name, damage, mpCost):
		super(Ability, self).__init__()
		self.name = name
		self.damage = damage
		self.mpCost = mpCost

	def execute(user,target):
		print("This funciton isn't implemented!")
		