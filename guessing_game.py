# imports
import random
import time


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
def guess_number(name):
    guess = input("I\'m thinking of a number between 1 and 10." + "\n" + "Guess what it is: " + "\n")
    while guess in li:
        guess = input("You have already tried that number. Enter a different number this time: " + "\n")
    li.append(guess)
    return guess


# see if guess matches Hal's number
def check_number(guess, answer):
    # change this to is in

    if 0 < guess < 11:
        if guess == answer:
            match = 1
        else:
            match = 0
    else:
        match = 2
    return match


def give_answer(is_correct, name, number):
    if is_correct == 1:
        print "You are correct " + name + "!" + "\n" + "I was thinking of the number " + str(number) + "."
        print "You have obviously hacked my system and I will now begin the self-destruct protocal."
    elif is_correct == 0:
        print "Sorry, you are incorrect. " + \
              "This mission is too important for me to allow you to jeopardize it."
    else:
        print "You have not entered a number between 1 - 10. It can only be attributable to human error."


def guess_again(name):
    while True:
        print "Would you like to try again?"
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

# global scope variables
play = 'y'
begin = 1
end = 10
seconds = 5
keep = 0
li = []

# only run these functions once and store outbput in global scope variables
hal_number = generate_number(begin, end)
user_name = introduction()

# run this while the user wants to continue to guess
while play == 'y':
    user_number = guess_number(user_name)
    user_test = check_number(user_number, hal_number)
    give_answer(user_test, user_name, hal_number)
    if user_test != 1:
        play = guess_again(user_name)
    else:
        break

# end the game with a countdown
end_game(seconds)