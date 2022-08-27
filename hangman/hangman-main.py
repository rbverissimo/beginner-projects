import random
import string
from words import words

alphabet = set(string.ascii_lowercase)


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word)
    print(word_letters)
    user_letter = input("Type a letter: ").strip().lower()
    global alphabet
    used_letters = set()

    while len(word_letters) > 0:
        full_validation(user_letter, used_letters, word_letters)
        print_word(used_letters, word)


def string_validator(letter):
    if len(letter) > 1:
        print("Full string. Only the first letter will be accounted for")
        print('The first letter is', letter[0])
        print('Is that alright?')
        confirmation = input("Y/N:").lower()
        if confirmation == 'y':
            return True
        else:
            return False
    else:
        return True


def selection_validator(user_letter, used_letters, word_letters):
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter[0])
        if user_letter[0] in word_letters:
            word_letters.remove(user_letter[0])
            print("You guess right!")
    elif user_letter in used_letters:
        print("Please try another one")
        user_letter = letter_selector()
        full_validation(user_letter, used_letters, word_letters)
    else:
        print("You chose an invalid character")
        user_letter = letter_selector()
        full_validation(user_letter, used_letters, word_letters)


def letter_selector():
    user_letter = input("Type a letter: ").strip().lower()
    return user_letter


def full_validation(user_letter, used_letters, word_letters):
    while string_validator(user_letter) is False or user_letter == "":
        user_letter = letter_selector()

    selection_validator(user_letter, used_letters, word_letters)


def show_used_letters(used_letters):
    print("You've already guess these letters: ", " ".join(used_letters))


def print_word(used_letters, word):
    #creates a list while iterating over it in the order
    word_list = [letter if letter in used_letters else '_' for letter in word]
    print("Current word:", ' '.join(word_list))


hangman()
