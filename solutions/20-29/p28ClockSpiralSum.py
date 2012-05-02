
# Project Euler - Problem 28
# 2011-05-21 03:40:05
"""
import time
sum = 1
begin = 3
spiral = 3
start = time.clock()
while spiral <= 1001:
    print "spiral", spiral, ", begin", begin
    for i in range(0, 4):
        sum += begin
        print begin
        if i != 3:
            begin += spiral-1
    spiral += 2
    begin += spiral-1
print sum
print "%.6f Secs" % (time.clock() - start)
"""

# 2011-05-21 20:02:32
"""
669171001
0.015840 Secs
"""

import time
sum = 1
begin = 3
start = time.clock()
for spiral in range(3, 1002, 2):
    #print "spiral", spiral, ", begin", begin
    for i in range(4):
        sum += begin
        #print begin
        begin += spiral-1
    begin += 2
print sum
print "%.6f Secs" % (time.clock() - start)

# 2011-05-21 20:29:06
"""
669171001
0.001691 Secs
"""
