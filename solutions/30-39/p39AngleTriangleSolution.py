
# Project Euler - Problem 39
# 2011-06-02 00:09:50

import time

start = time.time()

m = 0
num = 0
for i in range(10, 1001):
    #print i
    ok = []
    solutions = 0

    for a in range(1, i):
        for b in range(1, i):
            c = i - a - b
            if c <= 0:
                break
            a2 = a * a
            b2 = b * b
            c2 = c * c
            if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
                if a not in ok and b not in ok and c not in ok:
                    ok.append(a)
                    solutions += 1
                    #print a,b,c

    if solutions > m:
        m = solutions
        num = i
print 
print m, num
print "%.8f Secs" % (time.time() - start)
print time.asctime()


"""
8 840
294.17342210 Secs
"""
