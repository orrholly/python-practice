# coding=utf-8
# **************************************************************
# Program: tic_tac_toe.py
# Author: Holly Orr
# Date: 10/24/2017
#
# Description:
# write a program that lets two humans play a game of Tic Tac Toe in a terminal. The program should let the players take
# turns to input their moves. The program should report the outcome of the game.

# For later:  add support for a computer player to your game. You can start with random moves and make the AI smarter if
# you have time.
# **************************************************************

import random

# **************************************************************
# GLOBAL VARIABLES
# **************************************************************

# set player mode to zero initially to be set to 1 or 2 by user
player_mode = 0

# create gameboard list variable with 9 ints
gameboard = range(9)

# for error checking that the chosen spot is in range
r = range(9)

# score keeping
player1_score = 0
player2_score = 0

# set global flag to keep or stop playing
go_again = "y"

# **************************************************************
# FUNCTIONS
# **************************************************************

# TODO: Change all player1 to playerx and all player2 to player0

def introduction():
    print "\n"
    print "Let's play tic-tac-toe!"

    # TODO: if adding logic to give option to play computer
    global player_mode
    while not (player_mode == 1 or player_mode == 2):
        player_mode = convert_to_number(raw_input("Welcome. Will you be playing in 1 or 2 player mode?: \n"))
        player1_gamepiece, player2_gamepiece = input_player_piece()
        turn = go_first()
        if turn == "player_1":
            print('Congrats Player 1. The ' + player1_gamepiece + ' \'s will go first.')
        else:
            print('Congrats Player 2. The ' + player2_gamepiece + ' \'s will go first.')


def input_player_piece():
    piece = ''
    while not (piece == 'x' or piece == 'o'):
        print
        piece = raw_input("Do you want to be x or o?" + "\n")
    # if user chooses x, it will be listed first, if chooses o it will be listed first
    if piece == 'x':
        return ['x', 'o']
    else:
        return ['o', 'x']



# TODO: Add random generator to see who goes first
def go_first():
    # 'flip the coin' for who goes first
    if random.randint(0, 1) == 0:
        return 'player_1'
    else:
        return 'player_2'


def play_game():
    global go_again
    display_game_board()
    while go_again.lower() == "y":
        player1_move()
        player2_move()

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
        player1_input = check_number("Player 1", "x")
        if gameboard[player1_input] != 'x' and gameboard[player1_input] != 'o':
            gameboard[player1_input] = 'x'
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()


def player2_move():
    while True:
        player2_input = check_number("Player 2", "o")
        if gameboard[player2_input] != 'x' and gameboard[player2_input] != 'o':
            gameboard[player2_input] = 'o'
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()

# TODO add computer move logic


def check_winner():
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

    # variables for player1 and player2
    x_win = "x"
    o_win = "o"

    is_tied = all(isinstance(x, str) for x in gameboard)
    if is_tied is True:
        print "It's a tie!"
        play_again()
    else:
        for combo in winning_combos:
            is_winner = all(combo[0] == item for item in combo)
            if is_winner is True:
                if x_win in combo:
                    print "The x's win! Congrats Player 1!"
                    global player1_score
                    player1_score += 1
                    play_again()
                elif o_win in combo:
                    global player2_score
                    player2_score += 1
                    print "The o's win! Congrats Player 2!"
                    play_again()


def play_again():
    # get global variables for scores
    global player1_score
    global player2_score
    global go_again
    str_player1_score = str(player1_score)
    str_player2_score = str(player2_score)
    print "\n"
    print "SCORE:"
    print "-------------------"
    print "PLAYER 1 | PLAYER 2"
    print "   " + str_player1_score + "     |    " + str_player2_score
    print "-------------------"
    print "\n"
    # ask if want to play again
    go_again = raw_input("Would you like to play again? Enter y or n:" + "\n")
    while go_again.lower() != "n" and go_again.lower() != "y":
        go_again = raw_input("You must enter y or n:" + "\n")

    if go_again.lower() == "y":
        global gameboard
        gameboard = range(9)
        print "Great! Let's keep playing!"
        play_game()
    else:
        print "Thanks for playing!"
        exit()


def check_number(player, symbol):
    passed = False
    while passed is False:
        entered_player = raw_input(player + ", it's your turn. Enter the number on the board where you want to place an " + symbol + ": \n")
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


def main():
    introduction()
    play_game()


if __name__ == "__main__":
    main()