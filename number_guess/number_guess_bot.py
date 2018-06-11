import random

num = 0
has_guessed_correctly = False

min_num = 1
max_num = 50

def setup():
    global num
    global has_guessed_correctly
    num = random.randint(0,50)
    has_guessed_correctly = False

def start_round():
    global max_num
    global min_num
    global has_guessed_correctly
    guess_counter = 0
    while not has_guessed_correctly:
        guess_counter += 1
        guess = make_guess()
        res = check_guess(guess)
        print("Guess = " + str(guess))
        if res == 1:
            max_num = guess
        elif res == -1:
            min_num = guess
        else:
            print("Game over. The number was " + str(num) + "!")
            print("Got it in " + str(guess_counter) + " guesses.")
            has_guessed_correctly = True

def make_guess():
    return int(((max_num - min_num) / 2) + min_num)

def check_guess(guess):
    if guess > num:
        return 1
    elif guess < num:
        return -1
    else:
        return 0

setup()
start_round()