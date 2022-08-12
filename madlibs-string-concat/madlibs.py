
import os

print("Hi! Let's create some insane text \n")
os.system("pause")

adjective = input("Adjective: ")
first_verb = input("Verb: ")
second_verb = input("Another verb: ")
famous_person = input("A famous person: ")

if "to" in first_verb.lower():
    trimmed_first_verb = first_verb.strip()
    first_verb = trimmed_first_verb.removeprefix("to").strip()

if "to" in second_verb.lower():
    trimmed_second_verb = second_verb.strip()
    second_verb = trimmed_second_verb.removeprefix("to").strip()



madlib = f"Computer program is so {adjective}!! I love to {first_verb} \n " \
         f"Stay hidrated and {second_verb}. You are {famous_person}!"

print(madlib)



