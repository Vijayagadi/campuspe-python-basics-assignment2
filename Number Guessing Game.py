import random

number = random.randint(1, 100)
attempts = 7

print("Guess the number between 1 and 100")

for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct! You guessed it.")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")

    print("Attempts left:", attempts - i - 1)

else:
    print("Sorry! The number was", number)