import os
import random
from typing import List

# Custom Modules
from wordle_package.word_choice import read_words_file, choose_random_word
from wordle_package.validate_guess import check_guess_valid, get_valid_guess
from wordle_package.wordle import check_guess_correct, feed_back_word
from wordle_package.display import game_instructions, game_start_display, display_win, display_lost, display_word_feedback


def main():
    # Starting parameters
    attempt = 0
    previous_guesses = []

    # Fetch all the words from words.txt and pick a random word
    words = read_words_file()
    target_word = choose_random_word(words)

    # Display the game instructions and start message
    game_instructions()
    game_start_display()

    while attempt < 6:
        # Get a valid guess from the user
        guess = get_valid_guess(words, previous_guesses)
        previous_guesses.append(guess)

        # Check if the guess is correct
        if check_guess_correct(target_word, guess):
            display_win(target_word, attempt + 1)
            break

        # Provide feedback
        feedback = feed_back_word(target_word, guess)
        display_word_feedback(guess, feedback)

        attempt += 1

    if attempt == 6:
        display_lost(target_word)


if __name__ == "__main__":
    main()
