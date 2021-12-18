from logic import get_random_word, ask_for_difficulty, handle_input, is_game_over

def menu():
    diff = ask_for_difficulty()
    play(difficulty=diff)


def play(difficulty):
    word, lives = get_random_word(difficulty)

    while True:
        guess, subtract_life = handle_input(word, lives)
        if subtract_life:
            lives -=1
        if is_game_over(guess, word, lives):
            break


if __name__ == "__main__":
    menu()