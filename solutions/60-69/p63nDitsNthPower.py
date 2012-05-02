# Project Euler - Problem 63
# Created at: 2011-06-10 12:35:07
# coding=utf-8
import time

start = time.time()


"""
count = 0
digit = 1

while True:
    # digit iterating
    num = 1
    power = 0
    length = 0

    while True:
        power = num ** digit
        length = len(str(power))

        if length == digit:
            count += 1
            print "%4d  %4d^%-3d = %d" % (count, num, digit, power)
        elif length > digit:
            if num == 2:
                print count
                exit()
            break
        #print "%4d^%-3d   %d" % (num, digit, length)
        num += 1
    '''
    if num == 2 and length > digit:
        print "%d^%d = %d" % (num, digit, power)
        break
    '''
    digit += 1
"""


count = 0
digit = 1
for num in range(1, 10):
    digit = 1
    while True:
        power = num ** digit
        length = len(str(power))

        if length == digit:
            count += 1
            print "%4d  %4d^%-3d = %d" % (count, num, digit, power)
        elif length > digit:
            break
        #print num, digit, power
        digit += 1

print "Answer:", count
print "%.8f Secs" % (time.time() - start)
print "Solved at:", time.asctime()
