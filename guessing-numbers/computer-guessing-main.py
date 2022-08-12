import random
#This is a random generated number controller
#The users provide clues to "train" the computer in a sense

count_controller = 0
x = int(input(print("Define the number which the computer must guess")))
rgn_low = 1
rgn_high = x * 2

def computer_guessing(x):
    global rgn_high, rgn_low
    user_feedback = ""
    rgn = computer_first_guess(x)
    while user_feedback != "c":
        print(f'Is {rgn} too high, low or correct?')
        user_feedback = input(print("Pass 'H', 'L' or 'C'")).lower()
        while user_feedback_analyzer(user_feedback) != 0:
            print("Sorry, mate, you gotta tell me if I'm high, low or correct")
            user_feedback = input(print("Pass 'H', 'L' or 'C'")).lower()

        if user_feedback == "l":
            rgn_low = rgn
            rgn = guess_controller(rgn_low, rgn_high)
        if user_feedback == "h":
            rgn_high = rgn
            rgn = guess_controller(rgn_low, rgn_high)


    print("Correct answer!!!")


def computer_first_guess(x):
    low = 1
    high = x * 2
    return random.randint(low, high)

def guess_controller(rgn_low, rgn_high):
    return random.randint(rgn_low, rgn_high)

def user_feedback_analyzer(arg):
    if arg == 'h' or arg == 'l' or arg == 'c':
        return 0
    else:
        return 1

computer_guessing(x)