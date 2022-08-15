import random
from words import words


def get_valid_word(list_of_words):
    word = random.choice(list_of_words)
    while '-' in word or ' ' in word:
        word = random.choice(list_of_words)

    return word


def hangman():
    user_letter = input("Type a letter: ").upper()
    used_letters = set()

    while string_validator(user_letter) is False:
        user_letter = letter_selector()

    used_letters.add(user_letter[0])


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
    user_letter = input("Type a letter: ").upper()
    return user_letter

hangman()