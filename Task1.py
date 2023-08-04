import random

pc_number = random. randint(0, 20)

print("----Welcome to the Number Guessing Game----")
print("Here are the rules:")
print("--> The computer will generate a random number between 0 and 20.")
print("--> You will have 10 attempts to guess the number correctly.")
print("--> After each guess, the computer will provide feedback to help You.")
print("Have fun and good luck!")

for i in range(10):
    user_number = int(input("What's your guess: "))

    if user_number == pc_number:
        if i == 0:
            print("Congratulations, You won the game on your *FIRST* guess!!!")
            break
        if i == 1:
            print("Congratulations, You won the game on your *SECOND* guess!!!")
            break
        if i == 2:
            print("Congratulations, You won the game on your *THIRD* guess!!!")
            break
        if i > 2:
            print(
                f"Congratulations, You won the game on your *{i+1}th* guess!!!")
            break

    if user_number < pc_number:
        print("Go Upper!")

    if user_number > pc_number:
        if user_number > 20:
            print(
                "Sorry, that number is out of range. Please choose a number between 0 and 20")

        else:
            print("Go Lower!")

    if user_number != pc_number and i == 9:
        print(
            f"Sorry, you didn't guess the number in time. The number was {pc_number}. Better luck next time!")
