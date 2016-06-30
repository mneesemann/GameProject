import tkinter as tk

class GameOverScreen(object):
    """docstring for the GameOverScreen 
    Boilerplate for all Screens:
    The Screen classes are self-contained views that only require their controller to pass the
    appropriate callback functions upon instantiation. They should only be added to and removed 
    from the screen using their addToDisplay() and removeFromDisplay() functions. All of their
    data is created and stored upon instantiation, then hidden until needed. When 
    removeFromDisplay() is called, the view is simply hidden, not destroyed. This takes up more
    memory, but I don't think that's a problem for us at this point.
    
    @param onClickPlayAgain: the callback for, you guessed it, when the player clicks the "Play 
    Again" button. Should take the player back to the BattleScreen
    @param master: the root window of tkinter
    """
    def __init__(self, master, onClickPlayAgain):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack()
        #Setup the widgets
        self.title = tk.Label(self.frame, text = "Let off some steam, Bennett.")
        self.title.pack()
        self.playAgainButton = tk.Button(self.frame, text = "Play Again", command = onClickPlayAgain)
        self.playAgainButton.pack()
        self.quitButton = tk.Button(self.frame, text = "Quit", command= self.frame.quit)
        self.quitButton.pack()
        #Hide until ready to display
        self.frame.pack_forget()

    def addToDisplay(self):
        self.frame.pack()
        self.master.mainloop()

    def removeFromDisplay(self):
        self.frame.pack_forget()