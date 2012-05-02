
# Project Euler - Problem 66
# Created at: 2011-06-11 18:00:41


import time
from math import sqrt

sq = []

def isSquare(num):
    global sq
    if num in sq:
        return True

	result = sqrt(num)
    if result - int(result) == 0:
        sq.append(num)
		return True
    else:
	    return False

start = time.time()
m = 0
preX = 0
for d in range(1, 140):
    if not isSquare(d):
        y = 1
        while True:
            s = 1 + d * y**2
            if isSquare(s):
                x = int(sqrt(s))
                m = max(m, x)
                print "%d^2 - %d * %d^2 = 1" % (x, d, y)
                break
            y += 1

print "Answer:", m
print "%.8f Secs" % (time.time() - start)
print time.asctime()
