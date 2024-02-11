import random

x = random.randint(1, 10)
guess = 0

while True:
    print("Guess the number taken by the computer between [1, 10]")
    try:
        num = int(input())
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    guess += 1

    if num == x:
        print("You guessed it right!")
        print("No. of guesses =", guess)
        guess = 0
    elif 1 <= num < x:
        print("You guessed too low. Guess a little higher.")
    elif x < num <= 10:
        print("You guessed too high. Guess a little lower.")
    else:
        print("Invalid input! Please enter a number between 1 and 10.")
