

# Project Euler - Problem 35
# 2011-05-26 15:31:40

import time
from prime import isPrime

start = time.clock()
count = 0

for n in range(2, 100*10000+1):
    if isPrime(n):
        flag = True
        s = str(n)
        size = len(s)-1
        for i in range(0, size):
            s = s[1:] + s[0]
            if not isPrime(int(s)):
                flag = False
                break
        if flag:
            print n,
            count += 1
print
print "%.8f Secs" % (time.clock() - start)
print "%d circular primes below one million" % count

# 2011-05-26 15:44:39
"""
2 3 5 7 11 13 17 31 37 71 73 79 97 113 131 197 199 311 337 373 719 733 919 971 991 1193 1931 3119 3779 7793 7937 9311 9377 11939 19391 19937 37199 39119 71993 91193 93719 93911 99371 193939 199933 319993 331999 391939 393919 919393 933199 939193 939391 993319 999331
8.05360100 Secs
55 circular primes below one million
"""
