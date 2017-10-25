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

import sys

# **************************************************************
# GLOBAL VARIABLES
# **************************************************************

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

def introduction():
    # TODO: if adding logic to give option to play computer
    # print "Welcome. Will you be playing in 1 or 2 player mode?"

    # TODO: put directions here
    print "Let's play tic-tac-toe!"


def play_game():
    global go_again
    display_game_board()
    while go_again == "y":
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
        player1_input = check_number("Player 1")
        if gameboard[player1_input] != 'x' and gameboard[player1_input] != 'o':
            gameboard[player1_input] = 'x'
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()


def player2_move():
    while True:
        player2_input = check_number("Player 2")
        if gameboard[player2_input] != 'x' and gameboard[player2_input] != 'o':
            gameboard[player2_input] = 'o'
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()


def check_winner():
    # is_winner = all(top_row[0] == item for item in top_row)
    # print is_winner

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

    for combo in winning_combos:
        is_winner = all(combo[0] == item for item in combo)
        if is_winner is True:
            if x_win in combo:
                print "The x's win! Congrats Player 1!"
                global player1_score
                player1_score += 1
                # print str(player1_score)
                play_again()
            elif o_win in combo:
                global player2_score
                player2_score += 1
                # print str(player2_score)
                print "The o's win! Congrats Player 2!"
                play_again()


def play_again():
    # get global variables for scores
    global player1_score
    global player2_score
    global go_again
    str_player1_score = str(player1_score)
    str_player2_score = str(player2_score)
    # print score
    print "\n"
    print "SCORE:"
    print "-------------------"
    print "PLAYER 1 | PLAYER 2"
    print "       " + str_player1_score + " |   " + str_player2_score
    print "-------------------"
    print "\n"
    # ask if want to play again
    go_again = raw_input("Would you like to play again? Enter y or n:" + "\n")
    # TODO lowercase caste
    # TODO check entered y or n
    if go_again == "y":
        global gameboard
        gameboard = range(9)
        print "Great! Let's keep playing!"
        play_game()
    else:
        exit()
    # elif go_again == "n":
    #     print "Thanks for playing!"
    #     play_game()


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


def main():
    # if go_again == "y":
    introduction()
    play_game()
    # elif go_again == "n":
    #     print "Thanks for playing!"
    #     sys.exitfunc()


if __name__ == "__main__":
    main()