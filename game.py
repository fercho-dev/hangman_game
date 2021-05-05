import random
import os


def get_word():
    """Get and return a random word from words.txt file."""
    dict_words = {}
    with open("./words.txt", "r", encoding="utf-8") as f:
        for line, word in enumerate(f):
            dict_words[line] = word
    chosen_line = random.choice(list(dict_words.keys()))
    chosen_word = dict_words.get(chosen_line)
    return chosen_word


def draw_screen(_word, _guessed_letters):
    """Make the interface of the game.
    This function  receives two parameters:
    _word -> the word the player is guessing (string)
    _guessed_letters -> the letters the player has guessed (dict)"""
    # create wordline
    if _guessed_letters == {}:
        word_line = "__ " * len(_word)
    else:
        pass
    # clean the screen
    os.system("clear")
    # print screen
    print("Guess the word!")
    print(word_line)
    print("\n")


def get_input(_word, _guessed_letters):
    """Get the user input. if it is part of the word return it and the position of that letter inside the word."""
    user_input = input("Try with a letter or a word...\n")
    if user_input == _word:
        pass


def draw_final_screen(_victory):
    pass


def main():
    word = get_word()
    game_over = False
    guessed_letters = {}
    victory = False
    while not game_over:
        draw_screen(word, guessed_letters)
        new_letter, letter_position = get_input(word, guessed_letters)
        if new_letter != "":
            guessed_letters[letter_position] = new_letter
    draw_final_screen(victory)


if __name__ == '__main__':
    main()
