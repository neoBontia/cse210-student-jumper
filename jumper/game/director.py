import jumper
from .... import checker
from ...... import state


class director:

    """a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype: Coordinator
       
        
        
        """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.jumper = jumper()
        self.checker = checker()
        self.state = state()


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            gets update from jumper
        """
        while jumper.getlives:
            self.get_inputs()
            self.updates()
            self.displayOutputs()


    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play.

        Args:
            self (Director): An instance of Director.
        """
        jumper.guessALetter()

    def updates (self):
        checker.checkAnswer(jumper.getGuess)
        jumper.updateLives(checker.isCorrect)
        state.updateStatus(jumper.getLives, checker.getHint)
    
    def displatOutput(self):
        state.draw()