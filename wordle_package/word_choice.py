"""Module for getting all words from words.txt and choosing a random word.

    Functions:
    - read_words_file: Reads all valid 5-letter words from the words.txt file.
    - choose_random_word: Chooses a random word from a list of words.
    
"""
import os
import random

def read_words_file() -> list[str]:
    """Read all valid 5-letter words.
    Return: a list of words strings
    """
    filepath = os.path.join("wordle_package", "assets", "words.txt")
    with open(filepath, "r") as file:
        words = [line.strip() for line in file if len(line.strip()) == 5]
    return words
    pass


def choose_random_word(words: list[str]) -> str:
    """Choose the starting word for the game.
    Return: a random word on the list
    """
    return random.choice(words)
    pass
