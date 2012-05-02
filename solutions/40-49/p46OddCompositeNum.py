
# Project Euler - Problem 46
# 2011-06-01 17:13:24

import time
from math import sqrt
from prime import isPrime

start = time.time()
primes = []
n = 2

while True:
    flag = False
    if n % 2 == 1:
        if isPrime(n):
            primes.append(n)
        else:
            for i in range(1, int(sqrt(n / 2)) + 1):
                sub = n - 2 * i**2
                if sub in primes:
                    flag = True
                    break
            if flag == False:
                print n
                print "%.8f Secs" % (time.time() - start)
                print time.asctime()
                exit()
    n += 1

    """
    if isPrime(n):
        primes.append(n)
    elif n % 2 == 1:
        for i in range(1, int(math.sqrt(n / 2)) + 1):
            sub = n - 2 * i**2
            if sub not in primes:
                print n
                print "%.8f Secs" % (time.time() - start)
                exit()
            else:
                break
    """

"""
5777
0.13857818 Secs
Wed Jun  1 17:52:56 2011
"""
