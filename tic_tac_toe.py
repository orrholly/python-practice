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
    print "Welcome. Will you be playing in 1 or 2 player mode?"
    # capture if they will be playing machine
    display_game_board()

def display_game_board():
    print gameboard[0], "|", gameboard[1], "|", gameboard[2]
    print "---------"
    print gameboard[3], "|", gameboard[4], "|", gameboard[5]
    print "---------"
    print gameboard[6], "|", gameboard[7], "|", gameboard[8]

def player1_move():
    player1_input = check_number()
    while True:
        if player1_input != 'x' and player1_input != 'o':
            player1_input == 'x'
            display_game_board()
            break;
        else:
            print "That spot is already taken! Try again!"
            display_game_board()

def player2_move():
    player2_input = check_number()
    while True:
        if player2_input != 'x' and player2_input != 'o':
            player2_input == 'o'
            display_game_board()
            break;
        else:
            print "That spot is already taken! Try again!"
            display_game_board()

def check_number():
    passed = False
    while passed is False:
        entered_number = raw_input("Select a spot by it's number.")
        int_done = convert_to_number(entered_number)
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
            int_converted = raw_input("You have not entered a numeric value. Try again." )
    return int_converted


def test_range(user_int):
    if user_int not in r:
        print "You have not entered a spot by it number between 1 - 9. "
        return False
    else:
        return True

# **************************************************************
# GLOBAL VARIABLES
# **************************************************************


# create gameboard list variable with 9 ints
r = range(9)
gameboard = [(i + 1) for i in r]


# **************************************************************
# MAIN
# **************************************************************

introduction()

while True:
    player1_move()
    player2_move()



