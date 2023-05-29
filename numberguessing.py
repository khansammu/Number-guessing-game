import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of guesses
guesses = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    # Get user's guess
    guess = int(input("Take a guess: "))

    # Increase the number of guesses
    guesses += 1

    # Compare the guess with the secret number
    if guess < secret_number:
        print("Too low! Guess higher.")
    elif guess > secret_number:
        print("Too high! Guess lower.")
    else:
        print(f"Congratulations! You guessed the number in {guesses} attempts.")
        break

print("Thank you for playing!")

