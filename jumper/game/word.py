import random

class Word:
    """ A code template for a class that handles the word in the game. The responsibility of 
    this class of objects to choose a random word from a list, hide it with under scores 
    and update it throughout the game. 
    
    Stereotype:
        Holder

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue. 
        chosen_word: word picked from random list of words.
        hidden_word: puts underscores to represent letters of chosen word.
        """

    chosen_word = ""
    hidden_word = []
    
    def __init__(self):
        """
            The class constructor.
        
            Args:
                self (Word): an instance of Word.  
        """
        Word.chosen_word = self.select_word()
        Word.hidden_word = self.hide_word(Word.chosen_word) 


    def select_word(self):
        """
            Gets a word random word from a list
            
            return: The chosen word
        """
        words = []
        with open("jumper/game/wordlist.txt") as text:
            for row in text:
                clean_row = row.strip()
                words.append(clean_row)
        
        words_len = len(words) - 1

        index = random.randint(0, words_len)
        #print(words[index])
        return words[index]

    def hidden(self, guess = ""):
        """ 
            Gets the word as input and outputs the list of underscores for the hidden word 

            Update the word to show more letters if guess is correct or show the same word if it is false
            
            return: list of underscores and spaces
        """
        word = Word.chosen_word
        word_len = len(word)

        for i in range(word_len):
            if guess == word[i]:
                Word.hidden_word[i] = word[i]
            
        for i in Word.hidden_word:
            print(i + " ", end = "")
        
        print()
        print()

    def hide_word(self, word):
        """
            Method that receives the word as input and creates a list of "_" to hide the word. It outputs a list with all "_"
        """
        word_len = len(word)
        hidden_w = []

        for i in range(word_len):
            hidden_w.append("_ ")

        return hidden_w

        
            




