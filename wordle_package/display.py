"""Module for displaying colored text in the terminal for the Wordle game.

    Functions:
        - header: Prints a header in the terminal.
        - game_instructions: Prints the game instructions in the terminal.
        - game_start_display: Prints the starting message for the game.
        - display_word_feedback: Displays the colored feedback for a guess.
        - display_win: Prints the winning message.
        - display_lost: Prints the losing message.

    Constants:
        - COLORS: A dictionary containing ANSI color codes for GREEN, YELLOW, RED, and RESET.
"""

from typing import List

# ANSI color formatting
COLORS = {
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "RED": "\033[31m",
    "RESET": "\033[0m"
}

def header(text: str) -> None:
    """Print a header in the terminal."""
    print(f"{COLORS['GREEN']}========== {text} =========={COLORS['RESET']}")


def game_instructions():
    """Print the game instructions in the terminal."""
    header("Welcome to Wordle")
    print(
        f"{COLORS['YELLOW']}Rules:{COLORS['RESET']}\n"
        "- Guess the 5-letter word within 6 attempts.\n"
        "- Feedback will indicate if letters are correct:\n"
        f"  {COLORS['GREEN']}GREEN{COLORS['RESET']}: Correct letter in the correct position.\n"
        f"  {COLORS['YELLOW']}YELLOW{COLORS['RESET']}: Correct letter in the wrong position.\n"
        f"  {COLORS['RED']}RED{COLORS['RESET']}: Incorrect letter.\n"
    )


def game_start_display():
    """Print the starting message for the game."""
    header("Game Start")
    print("You have 6 attempts to guess the word. Good luck!")


def display_word_feedback(guess: str, feedback: List[str]) -> str:
    """Display the coloured feedback for a guess."""
    colored_feedback = ""
    for char, color in zip(guess, feedback):
        colored_feedback += f"{COLORS[color]}{char}{COLORS['RESET']} "
    print(colored_feedback.strip())


def display_win(word: str, attempt: int) -> None:
    """Display the winning message."""
    header("You Win!")
    print(f"Congratulations! You guessed the word '{word}' in {attempt} attempt(s). Well done!")


def display_lost(word: str) -> None:
    """Display the losing message."""
    header("Game Over")
    print(f"Sorry, you couldn't guess the word. The correct word was '{word}'. Better luck next time!")
