"""View Controller stuff"""

import tkinter as tk


class View(object):
	"""View Controller Screens"""
	def __init__(self, master):
		super(View, self).__init__()
		self.master = master
			
	def makeSplash(self,master):
		print("hello")
		splash = SplashScreen(master)


class BattleView(object):
	"""docstring for BattleView"""
	def __init__(self, master):
		super(BattleView, self).__init__()
		self.master = master

class SplashScreen(object):
	"""docstring for SplashScreen"""
	
	def __init__(self, master):
		self.frame = tk.Frame(master)
		self.frame.pack()
		self.label = tk.Label(master, text = "Hello there!")
		self.label.pack()
		self.button = tk.Button(master, text = "Change", command = self.change)
		self.button.pack()
		

	def change(self):
		self.label["text"]  = "Changed"


		

