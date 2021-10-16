class Checker:
    """A code template for a checker. The
    responsibility of this class of objects is to receive a word-to-guess from the 
    game director, checks the guess from the jumper, and provide a hint for every 
    guess made by the jumper.

    Stereotype:
        Information Holder, Service Provider

    Attributes:
        word (string): The word that jumper should guess.
        hint (list): The list of character.
        correct (loolean): status of current guess
    """

    def __init__(self, word):
        """Class constructor. Declares and initializes instance attributes.

        Args:
          self (Checker): An instance of Checker.
          word (string): a new word
          """
        self.word = word.lower()
        self.hint = []
        self.correct = True

    def checkAnswer(self, char):
        i = 0
        flag = False

        for c in self.word:
            if (c == char.lower()):
                self.hint[i] = c
                flag = True
            i = i + 1

    def get_hint(self):
        message = ""
        i = 0
        for c in self.word:
            if (c == self.hint[i]):
                message = message + c + " "
            else:
                message = message + "_ "
        return message

    def isCorrect(self):
        return self.correct
