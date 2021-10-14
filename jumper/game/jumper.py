import random
from game.word import Word
from game.console import Console

class Jumper:
    """A code template for a the seeker who looks for the seeker. The 
    responsibility of this class of objects is to move from location to 
    location in pursuit of the Seeker.
    
    Stereotype:
        Information Holder

    Attributes:
        


    """
    
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self.word = Word()
        self.console = Console()
        self.console.write("Welcome to Jumper! Are you ready to find the secret word? Let's play!")
        self.chosen_word = Word.chosen_word
        self.hidden_word = self.word.hide_word(self.chosen_word)
        self.console.print_list(self.hidden_word)

        self.parachute = ["  ___  "," /___\ "," \   / ","  \ /  ","   0   ","  /|\  ","  / \  ","         ","^^^^^^^"]
        self.get_jumper()

    def get_jumper(self, guess = True):
        """ Function that creates the parachute and updates it  """
        if guess:
            for i in self.parachute:
                self.console.write(i)
        else:
            if self.parachute[0] == "  \ /  ":
                self.parachute[1] = "   X   "
            self.parachute.pop(0)
            for i in self.parachute:
                self.console.write(i)
    

    def check_keep_playing(self):
        """ 
        Function that returns true or false if the parachute is present or not
        """
        if self.parachute[0] == "   X   ":
            return -1
        
        elif "_ " not in Word.hidden_word:
            return 0

        else:
            return True

    def check_guess(self, guess):
        """
        Function that checks if the guess letter is in the word and returns true or false if the guess is correct or not
        """
        if guess in self.chosen_word:
            return True
        else:
            return False
    
  

