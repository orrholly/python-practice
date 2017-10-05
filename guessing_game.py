# **************************************************************
# Program: Play 'Guess My Number' with Hal
# Author: Holly Orr
# Date: 10/2/2017
# Description: Hal will generate a random number between a range
# and user will guess until opting out or guessing the correct
# number.
# **************************************************************


# **************************************************************
# IMPORT MODULES
# **************************************************************
import random
import time


# **************************************************************
# FUNCTIONS
# **************************************************************


# function to generate a random number between 1 and 10
def generate_number(start, stop):
    random_number = random.randrange(start, stop)
    return random_number


# function to ask user name
def introduction():
    your_name = raw_input("Tell me your name: " + "\n")
    print "Hello " + your_name + ". I am the H.A.L 9000. You may call me Hal." + "\n" + "Let's play a game." + "\n"
    return your_name


# function that takes a name and ask it to guess a number
def guess_number():
    passed = False
    while passed is False:
        entered_guest = raw_input("I\'m thinking of a number between 1 and 10." + "\n" + "Guess what it is: " + "\n")
        int_done = convert_to_number(entered_guest)
        passed = test_range(int_done)
        passed = test_unique(int_done)
    return int_done


def convert_to_number(validate_guess):
    result = None
    int_converted = validate_guess
    while result is None:
        try:
            int_converted = int(int_converted)
            result = int_converted
        except ValueError:
            int_converted = raw_input("You have not entered a numeric value. It can only be attributable to human error. Try again." + "\n" + "\n" + "I\'m thinking of a number between 1 and 10." + "\n" + "Guess what it is: " + "\n")
    return int_converted


def test_range(user_int):
    if user_int not in r:
        print "You have not entered a number between 1 - 10. It can only be attributable to human error. Try again." + "\n"
        return False
    else:
        return True


def test_unique(unique_guess):
    if unique_guess in li:
        print "You have already tried that number. It can only be attributable to human error. Enter a different number this time." + "\n"
        return False
    else:
        li.append(unique_guess)
        return True


# see if guess matches Hal's number
def match_number(guess, answer):
    if guess == answer:
        match = 1
    else:
        match = 0
    return match


def give_answer(is_correct, name, number):
    if is_correct == 1:
        print "You are correct " + name + "! I was thinking of the number " + str(number) + "."
        print "You have obviously hacked my system and I will now begin the self-destruct protocol."
    elif is_correct == 0:
        print "Sorry, you are incorrect. This mission is too important for me to allow you to jeopardize it. Would you like to try again?"


def guess_again():
    while True:
        again = raw_input("Answer y or n: " + "\n")
        if again.lower() not in ('y', 'n'):
            print("Not an appropriate choice. It can only be attributable to human error.")
        else:
            return again


def end_game(s):
    print "Shut down has been initiated. This program will self-destruct in: "
    while s:
        print s
        time.sleep(1)
        s -= 1
    print('********** !!!!!! BOOM !!!!!! ****************\n\n\n\n\n')


# **************************************************************
# GLOBAL VARIABLES
# **************************************************************

# flag for user continuing to guess as y at start
play = 'y'

# set range Hal will create a random number in
begin = 1
end = 11  # number to include in range + 1
r = range(begin, end)

# set the number of seconds in countdown before Hal self-destructs
seconds = 5

# initiate a list object for keeping track on user guesses
li = []

# call function to generate random number in selected range and store in
# global variable
hal_number = generate_number(begin, end)

# call function to run introduction and store user name if global
# variable
user_name = introduction()

# **************************************************************
# MAIN
# **************************************************************

# for testing and printing Hal's number - commented out unless
# needed for testing
# print hal_number

# run this code while the user wants to continue to guess
while play == 'y':
    user_number = guess_number()
    user_test = match_number(user_number, hal_number)
    give_answer(user_test, user_name, hal_number)
    if user_test != 1:
        play = guess_again()
    else:
        break

# end the game with a countdown
end_game(seconds)
