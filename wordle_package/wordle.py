"""Module for the Wordle game.

    Functions:
    - check_guess_correct: Checks if a guess is correct.
    - find_all_char_positions: Finds all positions of a character in a word.
    - feed_back_word: Provides feedback on a guess compared to the word.

    Constants:
    - MAX_ATTEMPTS: The maximum number of attempts allowed in the game.
"""


from typing import List


# Max attempts of the game

MAX_ATTEMPTS = 6


def check_guess_correct(word: str, guess: str) -> bool:
    """Check the guess against the word
    Return: True if the guess is correct, False otherwise
    """
    return guess == word 
    pass


def find_all_char_positions(word: str, char: str) -> List[int]:
    """Given a word and a character, find all the indices of that character."""
    return [i for i, c in enumerate(word) if c == char]


def feed_back_word(word: str, guess: str) -> List[str]:
    """Check the guess against the word and return the feedback.
    Return: A list with the feedback for each letter in the guess.
    """
    # Initialize feedback as RED for all letters
    feedback = ["RED"] * 5
    word_list = list(word)  # Convert word to a list for mutability
    guess_list = list(guess)
    
    # First pass: Check for correct letters in the correct position (GREEN)
    for i in range(5):
        if guess_list[i] == word_list[i]:
            feedback[i] = "GREEN"
            word_list[i] = None  # Mark the letter as matched

    # Second pass: Check for correct letters in the wrong position (YELLOW)
    for i in range(len(guess)):
        if feedback[i] == "RED":  # Only process letters not already marked GREEN
            char_positions = find_all_char_positions(word, guess[i])
            if char_positions:  # If the letter exists in the remaining word
                feedback[i] = "YELLOW"
                word_list[char_positions[0]] = None  # Mark the first occurrence as used

    return feedback

