# **************************************************************
# Program: CracklePop
# Author: Holly Orr
# Date: 9/29/2017
#
# Description:
# Write a program that prints out the numbers 1 to 100 (inclusive).
# If the number is divisible by 3, print Crackle instead of the number.
# If it's divisible by 5, print Pop.
# If it's divisible by both 3 and 5, print CracklePop.
# **************************************************************

start = 1;  # range start number
stop = 101; # number to include in range + 1

for i in range(start, stop):
    if (i % 3 == 0) and (i % 5 == 0):
        print 'CracklePop'
    elif i % 3 == 0:
        print 'Crackle'
    elif i % 5 == 0:
        print 'Pop'
    else:
        print i
