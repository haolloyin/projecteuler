# Project Euler - Problem 56
# Created at: 2011-06-11 12:54:20

import time
start = time.time()

m = 0
for a in range(1, 100):
    for b in range(1, 100):
        num = a ** b
        sum = 0
        for c in str(num):
            sum += int(c)
        m = max(m, sum)

print
print "%.8f Secs" % (time.time() - start)
print "Answer:", m
print "Solved at:", time.asctime()

"""
0.90069294 Secs
Answer: 972
Solved at: Sat Jun 11 12:58:18 2011

You are the 16293rd person to have solved this problem.
"""
