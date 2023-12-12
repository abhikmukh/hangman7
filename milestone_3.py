import random

word_list = ["apple", "orange", "mango", "banana", "melon"]

word = random.choice(word_list)

while True:
    guess = input("Enter a single letter ")
    if len(guess) == 1 and guess.isalpha():
        break
    print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")

