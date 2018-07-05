import os
from random_words import RandomWords
# create clear function to clear console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# init variables
game_over = False
# generate a random word using the RandomWords module
word = RandomWords().random_word()
# list containing all correct guesses made by user
guess = ["_"] * len(word)
# list storing all guesses made by user
guesses = []
# amount of guesses remaining for user
lives = 5

# main game loop
while not game_over:
    # clear console window
    clear()

    # print characters player has guessed correctly so far
    print(" ".join(guess))
    # display to user how many guesses they have left
    print("Guesses remaining: " + str(lives))
    # only take first character of input
    letter = input("Guess a letter: ")[0:1].lower()

    # check that user has not guessed this character before
    if letter not in guesses:
        # add guessed character to list of guessed characters
        guesses.append(letter)
        # get all indexes of guessed character in word
        indexes = [pos for pos, char in enumerate(word) if char == letter]

        # check if word contains users guess
        if len(indexes) < 1:
            # decrement lives by one
            lives = lives - 1
            # check if user has any guesses left
            if lives == 0:
                # user is out of guesses
                # end game
                game_over = True
                # print message to user
                print("You ran out of guesses.")

        # loop through each index where word contains guessed character
        for index in indexes:
            # show guessed letter locations in word
            guess[index] = letter

        # check to see if user has guessed all characters
        if "".join(guess) == word:
            # end game
            game_over = True
            # clear console
            clear()
            # print message to user
            print("Congratulations, you won!")

# display word to user
print("The word was '" + word + "'.")