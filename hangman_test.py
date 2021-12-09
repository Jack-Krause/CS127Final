#
# Examples of some simple test cases for the hangman game.
#

import hangman
import hangman_ui

hangman.start("foo", 6)
# print(hangman.get_displayed_word())  # Expected ['-', '-', '-']
hangman.get_hidden_word()     # Expected 'foo'
# print(hangman.get_guessed_letters()) # Expected []
# print(hangman.get_guesses_left())        # Expected 6
# print(hangman.is_over())             # Expected False
# print(hangman.is_won())              # Expected False
#
# result = hangman.guess_letter('x')
# print(result)                        # Expected False
# print(hangman.get_guessed_letters()) # Expected ['x']
# print(hangman.get_guesses_left())        # Expected 5
#
# result = hangman.guess_letter('o')
# print(result)                        # Expected False
# print(hangman.get_guessed_letters()) # Expected ['x', 'o']
# print(hangman.get_displayed_word())  # Expected ['-', 'o', 'o']
#
#
# print(hangman.get_guesses_left())        # Expected 5



