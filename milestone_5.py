import random
from typing import List


class Hangman:
    """
    Hangman game
    """
    def __init__(self, word_list: List, num_lives: int = 5) -> None:
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
        self.num_letters = len(set(self.word))

    def _check_guess(self, guess: str) -> None:
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

    def ask_for_input(self) -> None:
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
                self._check_guess(guess)
                self.list_of_guesses.append(guess)


def play_game(word_list: List) -> None:
    """
    function to initiate the game
    Args:
        word_list: list of words

    Returns:
        None

    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if num_lives == 0:
            print("You Lost!")

        elif game.num_letters > 0:
            game.ask_for_input()

        elif num_lives != 0 and game.num_letters <= 0:
            print("Congratulations. You won the game!")


if __name__ == '__main__':

    # list of words with all same words to check how the program copes with same letters
    # list_of_words = ["banana", "banana", "banana", "banana", "banana"]
    list_of_words = ["apple", "banana", "orange", "pears", "mango"]
    play_game(list_of_words)








