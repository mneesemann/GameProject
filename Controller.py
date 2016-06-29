import Game as GameModule
import View as ViewModule

""" This is our main file that will actually run the damn program"""


class Controller(object):
	"""Controller Class ..."""
	def __init__(self, arg):
		super(Controller, self).__init__()
		self.arg = arg

game = GameModule.Game(3)
view = ViewModule.View(2)
