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

import sys

# draw the board
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]



def create_game_board():
    print board[0], "|", board[1], "|", board[2]
    print "---------"
    print board[3], "|", board[4], "|", board[5]
    print "---------"
    print board[6], "|", board[7], "|", board[8]


create_game_board()


# **************************************************************
# FUNCTIONS
# **************************************************************

# def create_game_board():
#     while
#
#         for i in frange(0.5, 1.0, 0.1):
#             ...
#             print(i)







# **************************************************************
# MAIN
# **************************************************************
