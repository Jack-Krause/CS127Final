# Module containing the state of a hangman game and

# related functions for playing the game.
#


# Below are some ideas for global variables you might use...
# You can change these as you see fit

# The hidden word
hidden_word = ''

# The displayed word as a list of characters
displayed_word = None

# The letters that have already been guessed, as a list of characters
guessed_letters = []

# The number of guesses the player has left
guesses_left = 6

# All correctly guessed letters
correct_guesses = []
for i in guessed_letters:
    for k in hidden_word:
        if i == k:
            correct_guesses += i


# TODO - all the function definitions as specified in the pdf
#Hidden word is here!
# hidden_word = 'x'

def start(hidden, guesses):
    global hidden_word, max_guesses, displayed_word, guessed_letters, guesses_left
    hidden_word = hidden
    max_guesses = guesses
    guessed_letters = []
    guesses_left = 6


def get_hidden_word():
    hidden_word = hangman_ui.select_game_and_word()
    return hidden_word


def get_displayed_word():
    global hidden_word
    lst1 = list(hidden_word)
    for i in range(len(lst1)):
        lst1[i] = '-'
    return lst1

def get_guesses_left():
    global guesses_left
    return guesses_left


def is_over():
    if guesses_left > 0:
        return False
    else:
        return True

def is_won():
    if is_over() and displayed_word == list(hidden_word):
        return True
    else:
        return False

def guess_letter(letter):
    if (letter in hidden_word) and (letter not in correct_guesses):
        return True
    else:
        return False

def get_guessed_letters():
    global guessed_letters
    return guessed_letters
