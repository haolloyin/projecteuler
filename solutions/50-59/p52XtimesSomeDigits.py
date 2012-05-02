
# Project Euler - Problem 52
# 2011-06-01 23:36:26

import time

def isSameDits(num):
    for i in range(2, 7):
        for c in str(i * num):
            if c not in str(num):
                return False
    return True

start = time.time()
n = 1
while True:
    if isSameDits(n):
        print n
        for i in range(2, 7):
            print n * i
        print "%.8f Secs" % (time.time() - start)
        print time.asctime()
        exit()
    n += 1


"""
142857

285714
428571
571428
714285
857142
0.49895406 Secs
Wed Jun  1 23:45:15 2011
"""
