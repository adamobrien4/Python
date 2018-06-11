import random

# initialise variables
has_guessed_correctly = False
num = random.randint(0,50)
guess_counter = 0

# loop until user guesses the number
while not has_guessed_correctly:
    # ask user for guess
    guess = input("Guess the number:  ")

    # validate the users input
    if guess.isnumeric():
        guess = int(guess)
    else:
        continue

    # increment guess counter
    guess_counter += 1

    # compare the users guess to the number
    if guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")
    else:
        # user correctly guessed the number
        print("You got it in " + str(guess_counter) + " guesses!")
        # stop while loop
        has_guessed_correctly = True
        print("Thanks for playing")