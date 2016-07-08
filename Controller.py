import Game as GameModule
import tkinter as tk
import SplashScreen
import BattleScreen
import GameOverScreen

""" This is our main file that will actually run the damn program"""


class Controller(object):
    """Controller Class ...
    The Controller manages communication between the Screen classes (Splash, Battle, etc.) 
    as its views and the Game classes as its models. It is driven by the click 
    events in the tkinter framework. To facilliate this, it passes callback functions 
    as parameters to the various screen classes during their instantiation. 

    The various Screens are pre-loaded at instantiation but not displayed
    until their addToDisplay() methods are called by the controller. 

    To begin the game, instantiate a Controller object, then call the startGame() method. 

    Notes: When I started implementing the callbacks, I found that the original View class was 
    adding an unnecessary layer of indirection. I deleted it entirely and put the equivalent  
    view classes in the Controller. We probably should implement the various "Screens" with a 
    superclass, since they share the same add and remove functionality. Eventually we may 
    need to add it back in later iterations, should we be spawning a multitude of Screens and
    need a loving parent for them. 

    I've never found a satisfactory way of implementing AI. After thinking about it over several
    coffees, I think we should put it parallel to the Controller. The AI and the Controller will talk
    to one another, and the AI will have direct access to the game model, but be completely unaware 
    of the View. When the AI is activated, the game will disable all user input and allow the AI to 
    muck about. Once the AI is done, control will return to the player. The only tricky part may be
    keeping the Controller aware of any important changes the AI makes in the game model in order 
    to reflect them in the view. But I may be overthinking everything. 
    """
       
    def __init__(self, arg): #Not sure about this "arg" parameter because I don't know python well.
        super(Controller, self).__init__()
        self.arg = arg

        #Setting up the Game Data
        self.game = GameModule.Game()

        #Loading up the GUI Views
        self.tkRoot = tk.Tk()
        self.splashScreen = SplashScreen.SplashScreen(self.tkRoot, self.onClickPlay)
        self.battleScreen = BattleScreen.BattleScreen(self.tkRoot, self.onClickAttack)
        self.gameOverScreen = GameOverScreen.GameOverScreen(self.tkRoot, self.onClickPlayAgain)
        
    #Function that begins the game. Currently, it only adds the splash screen to the view
    #but later it may perform other setup.
    def startGame(self):
        self.splashScreen.addToDisplay()

    #callback function used by the splash screen when the user clicks on "Play"
    def onClickPlay(self):
        self.splashScreen.removeFromDisplay()
        self.battleScreen.addToDisplay()

    #callback function used by the BattleScreen when the user clicks "Attack"
    def onClickAttack(self):
        print("wer're inside onClickAttack!")
        self.battleScreen.update(str(4),str(2))  #I was just figuring out how to use this thing :)

    #callback function used by the game over screen when the user clicks "Play Again"
    def onClickPlayAgain(self):
        self.gameOverScreen.removeFromDisplay()
        #going to need to implementing resetting the battle screen
        self.battleScreen.addToDisplay()  

gameController = Controller("Dummy")
gameController.startGame()