import random


def guess(x):
    random_number = random.randint(1, x)
    print(f"Guess a number between 1 and {x} \n")
    guess = 0
    closeness = closeness_ratio(x)
    print(closeness)
    while guess != random_number:
        guess = int(input("Guess: "))
        absolute_value = abs(guess - random_number)
        if guess > random_number:
            print("Sorry, dude. Too high, try again")
        elif guess < random_number:
            print("Too low!!! Try again")

        if absolute_value < closeness and absolute_value != 0:
            print("SHIT YOU ARE CLOSE!!!!")

    print(f"That is dude! You are right, the number is {random_number}")


#the closeness_ratio helps with a better guessing system in the guess function
def closeness_ratio(x):
    if x < 50:
        return x * 0.1
    elif 50 <= x <= 100:
        return x * 0.12
    elif x > 100:
        return x * 0.15


guess(1000)
