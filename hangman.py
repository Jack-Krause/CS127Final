import hangman_ui
# Module containing the state of a hangman game and
# related functions for playing the game.
#


# Below are some ideas for global variables you might use...
# You can change these as you see fit

# The hidden word
hidden_word = None

# The displayed word as a list of characters
displayed_word = None

# The letters that have already been guessed, as a list of characters
guessed_letters = None

# The number of guesses the player has left
guesses_left = None


# TODO - all the function definitions as specified in the pdf
def start(arg1, guesses_left):
    get_hidden_word()


def get_hidden_word():
    hidden_word = hangman_ui.select_game_and_word()
    # return hidden_word
    print(hidden_word)
