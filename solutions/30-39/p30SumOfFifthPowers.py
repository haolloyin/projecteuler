
# Project Euler - Problem 30
# 2011-05-31 23:45:26
"""
import time

start = time.time()
powers = [i**5 for i in range(0, 10)]

for num in range(1, 10000*10000):
    s = str(num)
    sum = 0
    for c in s:
        sum += powers[int(c)]
        if sum > num:
            break
    if sum == num:
        print num

print "%.8f Secs" % (time.time() - start)
print time.asctime()
"""

"""
1 # 1**5 is not included.
4150
4151
54748
92727
93084
194979

the sum of above is 443839

>>> 4150 + 4151 + 54748 + 92727 + 93084 + 194979
443839

2011-06-01 00:03:03
"""



# 2011-06-01 14:19:15 

import time

start = time.time()
pow5 = []
total = 0

def upperbound(n):
    global pow5
    pow5 = [i**n for i in range(0, 10)]
    bit = 1
    while 10**bit < pow5[9] * bit:
        bit += 1
    return bit

for num in range(2, 10**upperbound(5) + 1):
    if sum(pow5[int(c)] for c in str(num)) == num:
            print num
            total += num
    """
    s = str(num)
    sum = 0
    for c in s:
        sum += powers[int(c)]
        if sum > num:
            break
    if sum == num:
        print num
    """
print "the sum is", total
print "%.8f Secs" % (time.time() - start)
print time.asctime()

"""
4150
4151
54748
92727
93084
194979
the sum is 443839
8.17817712 Secs
Wed Jun  1 14:55:01 2011
"""


