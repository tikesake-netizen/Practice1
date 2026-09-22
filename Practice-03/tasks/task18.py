import random


name = input("Hello! What is your name? ")

number = random.randint(1, 20)
attempts = 0

print("Well,", name + ", I am thinking of a number between 1 and 20.")
print("Take a guess.")

while True:
    guess = int(input())
    attempts += 1

    if guess < number:
        print("Your guess is too low. Take a guess.")
    elif guess > number:
        print("Your guess is too high. Take a guess.")
    else:
        print("Good job,", name + "!", "You guessed my number in", attempts, "guesses!")
        break