import random
import sys
from utility import clearConsole, read_file
ALL_UNIQUE_LETTERS = [] # contains all letters of the word to be guessed, without duplicates
GUESSED_LETTERS = [] # contains the letters that already have been correctly guessed, without duplicates
TRIED_INVALID_LETTERS = [] # contains the valid, but unsuccesful guesses, without duplicates


def get_random_word(difficulty): # selects a random line from the list of words, depending on the difficulty of the game, chooses the harder or the easier word from the line
    word_pair_collection = read_file("countries-and-capitals", "txt")
    word_pair = random.choice(word_pair_collection)

    word_col = None
    match difficulty:
        case "normal":
            word_col = 0
            lives = 8
        case "hard":
            word_col = 1
            lives = 4

    word = word_pair.split(" | ")[word_col].strip()

    for letter in word:
        if letter not in ALL_UNIQUE_LETTERS and letter != " ":
            ALL_UNIQUE_LETTERS.append(letter.lower())
    return word, lives


def ask_for_difficulty():
    clearConsole()
    while True:
        print("(1) Normal")
        print("(2) Hard")
        user_input = input("Choose your difficulty: ")
        clearConsole()

        match user_input:
            case "1":
                return "normal"
            case "2":
                return "hard"
        print("Invalid input")


def handle_input(word, lives):   
    while True:
        render_visuals(word, lives)
        guess = input("Enter a letter: ")
        clearConsole()
        
        low_guess = guess.lower()  
        low_word = word.lower()
        subtract_life = False

        if guess == "quit":
            print("Bye!")
            sys.exit() 

        elif ( len(low_guess) == 1 
               and guess.isalpha() 
               and low_guess not in ALL_UNIQUE_LETTERS 
               and low_guess not in TRIED_INVALID_LETTERS):
            print("Wrong guess")
            TRIED_INVALID_LETTERS.append(low_guess)
            subtract_life -=1
            return guess, subtract_life

        elif low_guess in TRIED_INVALID_LETTERS:
             print("You've already tried this letter")

        elif low_guess in GUESSED_LETTERS:
            print("This letter is already guessed")

        elif low_guess in ALL_UNIQUE_LETTERS:
            GUESSED_LETTERS.append(low_guess)
            return guess, subtract_life

        elif low_guess == low_word:
            return guess, subtract_life

        else:
            print("Invalid input")


def is_game_over(guess, word, lives):    
    if guess.lower() == word.lower():
        print("You've guessed the whole word!")
        return True
    elif len(GUESSED_LETTERS) == len(ALL_UNIQUE_LETTERS):
        print("You won!")
        return True
    elif lives < 1:
        print("You ran out of lives!")
        print(f"The wird was: {word}")
        return True


def print_table(word, lives): # prints the lines for the word to be guessed 
    print(word)
    print(lives)
    for letter in word:
        if letter.lower() in GUESSED_LETTERS:
            print(letter, end=' ')
        elif letter == " ":
            print(" ", end=' ')
        else:
            print("_", end=' ')


def render_visuals(word, lives):
    print_table(word, lives)