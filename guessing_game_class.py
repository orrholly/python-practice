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
    entered_guess = raw_input("I\'m thinking of a number between 1 and 10." + "\n" + "Guess what it is: " + "\n")
    validated_number = validate_number(entered_guess)
    range_number = in_range_number(validated_number)
    tested_number = unique_number(range_number)
    return tested_number


def validate_number(validate_guess):
    while True:
        try:
            validate_guess = int(validate_guess)
        except ValueError:
            print "Only numeric values are valid. It can only be attributable to human error. Try again." + "\n"
            guess_number()
        return validate_guess


def in_range_number(in_range_guess):
    while in_range_guess not in r:
        print "You have not entered a number between 1 - 10. It can only be attributable to human error. Try again:" + "\n"
        guess_number()
    return in_range_guess


def unique_number(unique_guess):
    while unique_guess in li:
        print "You have already tried that number. It can only be attributable to human error. Enter a different number this time:" + "\n"
        guess_number()
    return unique_guess


# see if guess matches Hal's number
def match_number(guess, answer):
    # change this to is in
    # if guess in r:
    if guess == answer:
        match = 1
    else:
        match = 0
    # else:
    #     match = 99
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
# GLOBAL SCOPE VARIABLES
# **************************************************************

# flag for user continuing to guess
play = 'y'

begin = 1
end = 11  # number to include in range + 1
seconds = 5
keep = 0
li = []
r = range(begin, end)

# only run these functions once and store outbput in global scope variables
hal_number = generate_number(begin, end)
user_name = introduction()

# **************************************************************
# MAIN
# **************************************************************

# run this while the user wants to continue to guess
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
