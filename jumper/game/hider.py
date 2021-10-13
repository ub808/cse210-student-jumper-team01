import random

class Hider:
    """This class holder the methods for the hider.
    
    Attributes:
        location (integer): The location of the hider.
        distance (list): The distance from the seeker.
    """
    
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Seeker): An instance of Seeker.
        """
        
        self.word = ["car", "truck", "airplane"]
        self.letter_list = []
        
    
    def get_word(self):
        """ The get_hint method returns a hint that depends on whether or not 
        the seeker has moved closer or farther away. This is determined by 
        inspecting the last two distances contained in the distance attribute.

        Args: Different instances of distance from hider

        Returns: Message for seeker

        """
        
        index = random.randint(0, len(self.word)-1)
        chosen_word = self.word[index]
        return chosen_word


    def get_letters(self):
        """ parses out the letters into a list
        """

        for i in range(len(self.get_word.chosen_word)):
            self.letter_list[i] = "_ "


    def eval_seeker_input(self):
        pass

    

