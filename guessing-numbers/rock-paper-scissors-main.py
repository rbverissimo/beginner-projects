import random

username = ''
user_score = 0
pc_score = 0


def play():
    global user_score, pc_score
    user_choice = input("Choose 'r' for rock, 'p' for paper and 's' for scissors").lower()
    computer_choice = random.choice(['r', 'p', 's'])
    print(f'{username} plays {user_choice} \n Computer plays {computer_choice}')

    while choice_validator(user_choice) is False:
        user_choice = input("Choose 'r' for rock, 'p' for paper and 's' for scissors").lower()

    if is_tie(user_choice, computer_choice):
        print("It's a tie")
        pc_score = pc_score + 1
        user_score = user_score + 1
        print_score()
        play()

    if is_win(user_choice, computer_choice):
        user_score = user_score + 3
        print(f'ALRIGHT, {username}, YOU WON!!!\n')

    else:
        pc_score = pc_score + 3
        print(f'COMPUTER SCORES!!!\n')

    print_score()
    input("Press any key to continue:")
    replay = input("Wanna play again? Y / N").lower()

    if replay == 'y':
        play_again()
    else:
        print("Thanks for playing")


def username():
    global username
    username = input("State your name, player:")


def welcome_message():
    print(f'Hi, {username}, your score is {user_score} points.\n\n\n')


def choice_validator(user_choice):
    if user_choice == 'r' or user_choice == 'p' or user_choice == 's':
        return True
    return False


def is_tie(user, computer):
    if user == computer:
        return True
    return False


def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    return False


def print_score():
    print(f'Player score {user_score} points')
    print(f'Meanwhile, computer scores {pc_score} \n')
    score_message()


def score_message():
    if user_score <= pc_score:
        print(f'Focus! You can do it, {username} !!!')
    else:
        print(f'Keep up, {username} !!! You are winning')


def play_again():
    play()


username()
welcome_message()
play()
