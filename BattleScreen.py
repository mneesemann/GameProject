import tkinter as tk

class BattleScreen(object):
    """docstring for BattleScreen
    Boilerplate for all Screens:
    The Screen classes are self-contained views that only require their controller to pass the
    appropriate callback functions upon instantiation. They should only be added to and removed 
    from the screen using their addToDisplay() and removeFromDisplay() functions. All of their
    data is created and stored upon instantiation, then hidden until needed. When 
    removeFromDisplay() is called, the view is simply hidden, not destroyed. This takes up more
    memory, but I don't think that's a problem for us at this point.

    Notes: The BattleScreen needs to implement a reset() function of some kind.
    
    @param onClickAttack: the callback for when the player clicks the Attack button. I'll let you
    imagine what its implementation might do...
    @param master: the root window of tkinter

    @Public method update(playerHP, enemyHP) Updates the HP values of the player and the enemy. Only the
    numbers need be passed in as strings--the function formats them.
    """
    def __init__(self, master, onClickAttack):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack()
        #Text Variables to manage the text fields in the playerHP and enemyHP labels
        self.playerHPStringVar = tk.StringVar()
        self.playerHPStringVar.set("HP: 10")
        self.enemyHPStringVar = tk.StringVar()
        self.enemyHPStringVar.set("HP: 14")
        #Setup the widgets
        self.titleLabel = tk.Label(self.frame, text = "BattleScreen")
        self.titleLabel.pack()
        self.playerLabel = tk.Label(self.frame, text = "John Matrix")
        self.playerLabel.pack()
        self.playerHP = tk.Label(self.frame, textvariable = self.playerHPStringVar) 
        self.playerHP.pack()
        self.enemyLabel = tk.Label(self.frame, text = "Bennett")
        self.enemyLabel.pack()
        self.enemyHP = tk.Label(self.frame, textvariable = self.enemyHPStringVar)
        self.enemyHP.pack()
        #hp
        self.attackButton = tk.Button(self.frame, text = "Attack", command = onClickAttack)
        self.attackButton.pack()
        #ensure the screen isn't displayed until we want it to be
        self.frame.pack_forget()

    def addToDisplay(self):
        self.frame.pack()
        self.master.mainloop()

    def removeFromDisplay(self):
        self.frame.pack_forget()

    def reset(self):
        #Clear all the HP fields and reset them. Probably will only be used by the controller.
        pass

    def update(self, playerHP, enemyHP):
        self.playerHPStringVar.set("HP: " + playerHP)
        self.enemyHPStringVar.set("HP: " + enemyHP)


