import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/scissors or Q to quit: ").lower()
    if user_input == "q":
        quit()

    if user_input not in optins :
       continue

       random_number = random.randint(0,2)


print("Goodbye!")