import tkinter as tk

class SplashScreen(object):
    """docstring for SplashScreen
    Boilerplate for all Screens:
    The Screen classes are self-contained view that only require their controller to pass the
    appropriate callback functions upon instantiation. They should only added to and removed 
    from the screen using their addToDisplay() and removeFromDisplay() functions. All of their
    data is created and stored upon instantiation, then hidden until needed. When 
    removeFromDisplay(), the view is simply hidden, not destroyed. If we run into memory problems
    one day, we may need to revisit this.
    
    @param onClickPlay: the callback for, you guessed it, when the player clicks the play button. It's
    implementation should take the player to the BattleScreen
    @param master: the root window of tkinter
    """
    def __init__(self, master, onClickPlay):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.onClickPlay = onClickPlay
        #Setup the widgets
        self.title = tk.Label(self.frame, text = "Epic Schwarzenegger Battles")
        self.title.pack()
        self.subtitle = tk.Label(self.frame, text = "Be the Legend")
        self.subtitle.pack()
        self.playButton = tk.Button(self.frame, text = "Play Game!", command = self.onClickPlay)
        self.playButton.pack()
        self.quitButton = tk.Button(self.frame, text = "Quit", command = self.frame.quit)
        self.quitButton.pack()
        #ensure the screen is hidden
        self.frame.pack_forget()

    def addToDisplay(self):
        self.frame.pack()
        self.master.mainloop()

    def removeFromDisplay(self):
        self.frame.pack_forget()
