import random
from game.word import Word
from game.console import Console

class Jumper:
    """A code template for a the jumper who looks for the word. The 
    responsibility of this class of objects is to create to parachute and 
    keep it updated, decide when game is over and verify if guessed letter is correct. 
    
    Stereotype:
        Information Holder

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue. 
        parachute: create parachute
        get_jumper: updates parachute after guess
        word (Word): random word from list
        chosen_word: word picked from random list of words.
        hidden_word: puts underscores to represent letters of chosen word.
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

        self.parachute = ["\033[44m   ___   \x1b[0m","\033[44m  /___\  \x1b[0m","\033[44m  \   /  \x1b[0m","\033[44m   \ /   \x1b[0m","\033[44m    0    \x1b[0m","\033[44m   /|\   \x1b[0m","\033[44m   / \   \x1b[0m","\033[44m         \x1b[0m","\033[42m ^^^^^^^ \x1b[0m"]
        self.get_jumper()

    def get_jumper(self, guess = True):
        """ Function that creates the parachute and updates it.
        Args:
            self(Jumper): An instance of Jumper.
            guess: Boolean to maintain parachute
        """
        if guess:
            for i in self.parachute:
                self.console.write(i)
        else:
            if self.parachute[0] == "\033[44m   \ /   \x1b[0m":
                self.parachute[1] = "\033[44m    X    \x1b[0m"
            self.parachute.pop(0)
            for i in self.parachute:
                self.console.write(i)
    

    def check_keep_playing(self):
        """ 
        Function that returns true or false if the parachute is present or not.
        Args:
            self(Jumper): An instance of Jumper.
        """
        if self.parachute[0] == "\033[44m    X    \x1b[0m":
            return -1
        
        elif "_ " not in Word.hidden_word:
            return 0

        else:
            return True

    def check_guess(self, guess):
        """
        Function that checks if the guess letter is in the word and returns true or false if the guess is correct or not.
        Args:
            self(Jumper): An instance of Jumper.
            guess: Letter chose by the jumper.
        """
        if guess in self.chosen_word:
            return True
        else:
            return False
    
  

