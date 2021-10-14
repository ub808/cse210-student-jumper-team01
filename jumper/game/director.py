from game.console import Console
from game.jumper import Jumper
from game.word import Word


class Director:
    """
    A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue. 
    """
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """

        self.console = Console()
        self.word = Word()
        self.jumper = Jumper()
        self.keep_playing = True

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the letter guess from the user.

        Args:
            self (Director): An instance of Director.
        """
        
        self.letter_guess = self.console.read_letter("Guess a letter [a-z]: ").lower()  
        
        

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, update the word and print the new jumper.

        Args:
            self (Director): An instance of Director.
        """
        self.word.hidden(self.letter_guess)
        self.is_letter = self.jumper.check_guess(self.letter_guess)
        self.jumper.get_jumper(self.is_letter)

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the hider provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        
        result = self.jumper.check_keep_playing()
        
        if result == -1:
            self.console.write("\033[31mSorry, you didn't guess the word! Game over.\x1b[0m")
            self.keep_playing = False
        
        elif result == 0:
            self.console.write("You have found the correct word! Congratulations! Game over")
            self.keep_playing = False

        else:
            self.keep_playing = True

        