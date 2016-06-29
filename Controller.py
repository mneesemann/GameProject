import Game as GameModule
import View as ViewModule
import tkinter

""" This is our main file that will actually run the damn program"""


class Controller(object):
	"""Controller Class ..."""
	def __init__(self, arg):
		super(Controller, self).__init__()
		self.arg = arg

game = GameModule.Game(3)


root = tkinter.Tk()

view = ViewModule.View(root)
view.makeSplash(root)
root.mainloop()

