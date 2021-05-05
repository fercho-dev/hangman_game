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
    return chosen_word.strip()


def draw_screen(_word, _guessed_letters):
    """Make the interface of the game.
    This function  receives two parameters:
    _word -> the word the player is guessing (string)
    _guessed_letters -> the letters the player has guessed (dict)"""

    # create wordline
    if _guessed_letters == {}:
        word_line = " __" * len(_word)
    else:
        word_line = " "
        for position in range(0, len(_word)):
            if position in _guessed_letters.keys():
                word_line += _guessed_letters[position]
            else:
                word_line += "__"
            word_line += " "
    # clean the screen
    os.system("clear")
    # print screen
    print("Guess the word!")
    print(word_line)
    print("\n")


def get_input(_word, _guessed_letters):
    """Get the user input. if it is part of the word return it and the position of that letter inside the word.
    Returns the letter input and the position of that letter in the word in a list.
    if the letter is not in the word returns an empty string.
    if the user tries a word and fails returns empty string.
    if the user tries a word and wins returns the word."""

    user_input = input("Try with a letter or a word...\n").lower()
    # is it a word?
    if len(user_input) > 1:
        if user_input == _word:
            return _word, []
        else:
            return "", []
    # is it a letter?
    else:
        if user_input in _word:
            position = []
            current_position = 0
            for letter in _word:
                if user_input == letter:
                    position.append(current_position)
                current_position += 1
            return user_input, position
        else:
            return "", []


def draw_final_screen(_victory):
    if _victory == True:
        # clean the screen
        os.system("clear")
        print("Congrats, you win!")


def main():
    word = get_word()
    game_over = False
    guessed_letters = {}
    victory = False
    while not game_over:
        draw_screen(word, guessed_letters)
        new_letter, letter_position = get_input(word, guessed_letters)
        if new_letter == word:
            victory = True
            game_over = True
        elif new_letter != "":
            for position in letter_position:
                guessed_letters[position] = new_letter
    draw_final_screen(victory)


if __name__ == '__main__':
    main()
