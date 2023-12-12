import random

word_list = ["apple", "orange", "mango", "banana", "melon"]

word = random.choice(word_list)


def check_guess(guess):
    """
     Check if the guessed letter is in the word.
    Args:
        guess: str

    Returns:

    """

    if guess.lower() in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    """
     Iteratively check if the input is a valid guess

    """
    while True:
        guess = input("Enter a single letter ")
        if len(guess) == 1 and guess.isalpha():
            break
        print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


ask_for_input()



