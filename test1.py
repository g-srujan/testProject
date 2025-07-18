import random

def guess_number():
    number = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number:
            print("Correct! The number was", number)
            break
        else:
            print("Wrong! Try again.")

# Example usage
guess_number()