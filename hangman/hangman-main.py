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

    full_validation(user_letter, used_letters, word_letters)

    print(word_letters)



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
    elif user_letter in used_letters:
        print("You already chose this letter. Please try another one")
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



hangman()
