# **************************************************************
# Program: tic_tac_toe.py
# Author: Holly Orr
# Date: 10/24/2017
#
# Description:
# write a program that lets two humans play a game of Tic Tac Toe in a terminal. The program should let the players take
#  turns to input their moves. The program should report the outcome of the game.

# For later:  add support for a computer player to your game. You can start with random moves and make the AI smarter if
# you have time.
# **************************************************************

# **************************************************************
# IMPORT MODULES
# **************************************************************

# **************************************************************
# FUNCTIONS
# **************************************************************

def introduction():
    # TODO: if adding logic to give option to play computer
    # print "Welcome. Will you be playing in 1 or 2 player mode?"

    # TODO: put directions here

    display_game_board()

def display_game_board():
    print "\n"
    print gameboard[0], "|", gameboard[1], "|", gameboard[2]
    print "---------"
    print gameboard[3], "|", gameboard[4], "|", gameboard[5]
    print "---------"
    print gameboard[6], "|", gameboard[7], "|", gameboard[8]
    print "\n"

def player1_move():
    while True:
        player1_input = check_number("Player 1")
        if gameboard[player1_input] != 'x' and gameboard[player1_input] != 'o':
            gameboard[player1_input] = 'x'
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()

def player2_move():
    while True:
        player2_input = check_number("Player 2")
        if gameboard[player2_input] != 'x' and gameboard[player2_input] != 'o':
            gameboard[player2_input] = 'o'
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()

def check_winner():
    # is_winner = all(top_row[0] == item for item in top_row)
    # print is_winner
    for combo in winning_combos:
        is_winner = all(combo[0] == item for item in combo)
        if is_winner is True:
            print "You are a winner!"

def check_number(player):
    passed = False
    while passed is False:
        entered_player = raw_input(player + " It's your turn. Enter the number of the spot on the board:  " + "\n")
        int_done = convert_to_number(entered_player)
        passed = test_range(int_done)
    return int_done


def convert_to_number(validate_int):
    result = None
    int_converted = validate_int
    while result is None:
        try:
            int_converted = int(int_converted)
            result = int_converted
        except ValueError:
            int_converted = raw_input("You have not entered a numeric value. Try again:  " + "\n")
    return int_converted


def test_range(user_int):
    if user_int not in r:
        print "You have not entered a spot by it number between 0 - 8. "
        return False
    else:
        return True

# **************************************************************
# GLOBAL VARIABLES
# **************************************************************

# create gameboard list variable with 9 ints
gameboard = range(9)

# for error checking that the chosen spot is in range
r = range(9)

# winning rows
top_row = [gameboard[0], gameboard[1], gameboard[2]]
mid_row = [gameboard[3], gameboard[4], gameboard[5]]
bottom_row = [gameboard[6], gameboard[7], gameboard[8]]
# winning columns
left_col = [gameboard[0], gameboard[3], gameboard[6]]
mid_col = [gameboard[1], gameboard[4], gameboard[7]]
right_col = [gameboard[2], gameboard[5], gameboard[8]]
# winning diagonals
diag_lr = [gameboard[0], gameboard[4], gameboard[8]]
diag_rl = [gameboard[2], gameboard[4], gameboard[6]]

# list of all winning combination lists
winning_combos = [top_row, mid_row, bottom_row, left_col, mid_col, right_col, diag_lr, diag_rl]

# **************************************************************
# MAIN
# **************************************************************

introduction()

while True:
    player1_move()
    player2_move()
    check_winner()



