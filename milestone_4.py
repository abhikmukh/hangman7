import random


class Hangman:
    """
    Hangman game
    """
    def __init__(self, word_list, num_lives=5):
        """
        Initialise the attributes
        Args:
            word_list: list of words to begin the game
            num_lives: default is 5
        """
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in range(len(self.word))]
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        self.num_letters = 0

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.
        Args:
            guess: str

        Returns: None

        """
        if guess.lower() in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        """
             Iteratively check if the input is a valid guess

        """
        while True:
            guess = input("Enter a single letter ")
            if len(guess) != 1 or guess.isalpha() is False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


# list of words with all same words to check how the program copes with same letters
hangman_begins = Hangman(["banana", "banana", "banana", "banana", "banana"])
hangman_begins.ask_for_input()







