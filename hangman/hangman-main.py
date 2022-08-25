import random
import string
from words import words

alphabet = set(string.ascii_uppercase)


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    #print(word)
    word_letters = set(word)
    #print(word_letters)
    user_letter = input("Type a letter: ").strip().upper()
    global alphabet
    used_letters = set()

    while string_validator(user_letter) is False or user_letter == '':
        user_letter = letter_selector()

    # validation to see which letters have already been used
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter[0])
        if user_letter[0] in word_letters:
            word_letters.remove(user_letter)


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


def selection_validator():
    pass


def letter_selector():
    user_letter = input("Type a letter: ").strip().upper()
    return user_letter


hangman()
