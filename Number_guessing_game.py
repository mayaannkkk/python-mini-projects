import random

low_num = 1
high_num = 100
number = random.randint(low_num, high_num)  # range for guessing a number by computer
guesses = 0

print("Python Number Guessing Game")
print("Guess a number between 1 to 100")
while True:
    # Take user input
    guess = input("Enter Your guess Number:")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print(f"Invalid Guess!Guess a number between {low_num} to {high_num}")
        elif guess > number:
            print("Guess smaller number")
        elif guess < number:
            print("Guess Larger number")
        else:
            print(f"Your guess correct in {guesses} attempt")
            break
    else:
        print(f"Invalid Guess! Guess a number between {low_num} to {high_num}")
