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
