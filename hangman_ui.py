import hangman
import words


def select_game_and_word():
    user_game = input('''
    Which version of the game would you like to play? 
  a) Kitchen utensils 
  b) Random nouns 
  c) Word from file 
  : 
    ''')
    print('You selected', user_game)
    while (user_game != 'a') and (user_game != 'b') and (user_game != 'c'):
        user_game = input('Please enter a, b, or c: ')
    if user_game == 'a':
        return words.get_kitchen_word()
        # hidden_word = words.get_kitchen_word()
        # return hidden_word
    elif user_game == 'b':
        return words.get_special_word()
        # hidden_word = words.get_special_word()
        # return hidden_word
    elif user_game == 'c':
        return words.get_word_from_file()
        # hidden_word = words.get_word_from_file()
        # return hidden_word


def display_game():
    '''
    Prints out the current state of the game, including a stick
    figure drawn under a scaffold.
    '''
    stick_figure = ['/','\\','|','\\','/','o']
    positions = [34,35,26,27,25,18]
    health = max(0, 6 - hangman.get_guesses_left())
    scaffold = list(\
        "  ____ \n"+\
        "  1   |\n"+\
        "      |\n"+\
        "      |\n"+\
        "      |\n"+\
        "=======\n")

    for x in range(health):
        scaffold[positions[x]] = stick_figure[x]
    print("".join(scaffold))
    print("Word so far:    " + " ".join(hangman.get_displayed_word()))
    print("Letters already guessed: " + ", ".join(hangman.get_guessed_letters()))
    print("You have " + str(hangman.get_guesses_left()) + " guesses left")


def play_game():
    '''
    Plays one round of the hangman game.
    '''
    print("Welcome to Com S 127 Hangman")

    hidden = select_game_and_word()
    hangman.start(hidden, 6)
    while hangman.guesses_left != 0:
        display_game()
        letter = input("Enter your guess: ")
        hangman.guessed_letters += letter
        correct = hangman.guess_letter(letter)
        if correct:
            print("Good guess!")
            continue
        else:
            print("Nope.")
            hangman.guesses_left -= 1
            continue
        if hangman.is_won():
            print("You win!")
            break
        elif hangman.is_over():
            display_game()
            print("Sorry, you've lost.")
            break
        return hangman.guessed_letters
    print("The word was " + hangman.hidden_word)

# Execution starts here
# select_game_and_word()
display_game()
play_game()
##select_game_and_word()
# print(select_game_and_word())
