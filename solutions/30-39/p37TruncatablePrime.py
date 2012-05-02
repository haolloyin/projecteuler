
# Project Euler - Problem 37
# 2011-05-26 13:37:18


import time
from prime import isPrime

start = time.clock()
count = 0
n = 22 
sum = 0
while count < 11:
    if isPrime(n):
        flag = True
        l = r = str(n)
        bits = len(l) - 1
        for i in range(0, bits):
            l = l[1: ]
            r = r[:-1]
            #print n, l, r
            if not isPrime(int(l)) or not isPrime(int(r)):
                flag = False
                break
        if flag:
            print n
            sum += n
            count += 1
    n += 1

print sum
print "%.8f Secs" % (time.clock() - start)

# 2011-05-26 15:26:13
"""
23
37
53
73
313
317
373
797
3137
3797
739397
748317
5.11207100 Secs
"""
