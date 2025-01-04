"""Module for validating input guess.

    Functions:
    - check_guess_valid: Checks if a guess is a valid 5-letter word.
    - get_valid_guess: Gets a valid guess from the user.

"""

from typing import List


def check_guess_valid(guess: str) -> bool:
    """Check if the guess is a valid 5-letter word
    Return: True if the guess is valid, False otherwise
    """
    return (len(guess) == 5)
    pass


def get_valid_guess(all_words: list[str], guesses: list[str]) -> str:
    """Get a valid guess from the user.
    Must be:
    1. 5-letter word (lowercase)
    2. Not previously guessed
    3. Exists in all_words
    """
    while True:
        guess = input("Give me a guess: ").strip()
        
        # Check if the guess is a 5-letter lowercase word
        if len(guess) != 5 or not guess.islower():
            print("The word must be 5 lowercase letters.")
            continue
        
        # Check if the guess has already been made
        if guess in guesses:
            print("You already guessed that word.")
            continue
        
        # Check if the guess exists in the allowed word list
        if guess not in all_words:
            print("The word is not in the valid word list.")
            continue
        
        # If all checks pass, return the guess
        return guess
    pass

