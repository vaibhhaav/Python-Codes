import random

def guess_number():
    target = random.randint(0,100)
    guess = -1

    print("Guess the number between 0 and 100")

    while guess != target:
        try:
            guess = int(input("Enter your guess: "))

            if guess < target:
                print("Too low! Try again.")
            elif guess > target:
                print("Too high! Try again.")
            else:
                print("Congratulations you've guessed the number:", target)
        except ValueError:
            print("Please enter a valid integer.")

guess_number()