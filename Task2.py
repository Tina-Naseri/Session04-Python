import random

print("---Welcome to the Random List Generator---")
print("This program generates a list of random numbers within a range.")

while True:
    n = int(input("Please enter your number of elements: "))
    lower_bound = int(input("Please enter the lower bound of the range: "))
    upper_bound = int(input("Please enter the upper bound of the range: "))

    if lower_bound > upper_bound:
        print("Error: The lower bound cannot be greater than the upper bound.")

    if lower_bound == upper_bound:
        print("Error: The lower bound cannot be equal to the upper bound.")

    if n > (upper_bound - lower_bound):
        print(
            f"Error: The number of elements cannot be more than {upper_bound - lower_bound}.")

    else:
        random_list = random.sample(range(lower_bound, upper_bound), n)
        print(random_list)
