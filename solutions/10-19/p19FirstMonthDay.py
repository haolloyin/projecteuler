

# Project Euler - Problem 19
# 2011-05-24 19:44:48

import time

sum = 0
start = time.clock()
for y in range(1901, 2001):
    for m in range(1, 13):
        d = str(y) + "-" + str(m) + "-1"
        if time.strptime(d, "%Y-%m-%d").tm_wday == 1:
            sum += 1
print sum
print "%.8d Secs" % (time.clock() - start)

# 2011-05-24 20:07:37
"""
171
00000000 Secs 
"""
