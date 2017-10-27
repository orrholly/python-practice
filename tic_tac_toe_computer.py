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
player1_gamepiece = ""
player2_gamepiece = ""
turn = ""

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
    global player1_gamepiece
    global player2_gamepiece
    global turn
    while not (player_mode == 1 or player_mode == 2):
        player_mode = convert_to_number(raw_input("Welcome. Will you be playing in 1 or 2 player mode?: \n"))
        if player_mode == 1:
            print "You chose to play the computer."
        else:
            print "You chose to play another human."
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


def go_first():
    # 'flip the coin' for who goes first
    if random.randint(0, 1) == 0:
        return 'player_1'
    else:
        return 'player_2'

def play_game_mode_1():
    global go_again
    global turn
    display_game_board()
    while go_again.lower() == "y":
        if turn == 'player_1':
            player1_move()
        else:
            player2_computer_move()

def play_game_mode_2():
    global go_again
    global turn
    display_game_board()
    while go_again.lower() == "y":
        if turn == 'player_1':
            player1_move()
        else:
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
    global player1_gamepiece
    global turn
    while True:
        player1_input = check_number("Player 1", player1_gamepiece)
        if gameboard[player1_input] != 'x' and gameboard[player1_input] != 'o':
            gameboard[player1_input] = player1_gamepiece
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()
    turn = "player_2"


def player2_move():
    global player2_gamepiece
    global turn
    while True:
        player2_input = check_number("Player 2", player2_gamepiece)
        if gameboard[player2_input] != 'x' and gameboard[player2_input] != 'o':
            gameboard[player2_input] = player2_gamepiece
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()
    turn = "player_1"

# TODO add computer move logic
def player2_computer_move():
    global player2_gamepiece
    global turn
    while True:
        player2_input = check_number("Player 2", player2_gamepiece)
        if gameboard[player2_input] != 'x' and gameboard[player2_input] != 'o':
            gameboard[player2_input] = player2_gamepiece
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()
    turn = "player_1"


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
        # TODO add conditional for mode 1 or 2
        play_game_mode_2()
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
    global player_mode
    introduction()
    if player_mode == 1:
        play_game_mode_1()
    else:
        play_game_mode_2()


if __name__ == "__main__":
    main()