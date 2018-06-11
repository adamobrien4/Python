import random

moves = ["rock","paper","scissors"]

# ask user for input
p_move = input("1 = rock, 2 = paper, 3 = scissors  :  ")
# computer randomly chooses an option
c_move = random.randint(0,2)

# validate users input
if p_move.isnumeric():
    p_move = int(p_move) - 1

    if p_move >= 0 and p_move < 4:

        print("Player: " + moves[p_move])
        print("Computer: " + moves[c_move])

        # calculate outcome of game
        if p_move == c_move:
            print("draw")    
        elif (p_move == 0 and c_move == 2) or (p_move == 1 and c_move == 0) or (p_move == 2 and c_move == 1):
            print("player wins.")
        else:
           print("computer wins")
else:
    print("invalid input")