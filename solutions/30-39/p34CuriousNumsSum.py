
# Project Euler - Problem 34
# 2011-05-21 20:50:59

import time
start = time.time()
factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
total = 0

def upperbound():
    bit = 1
    while 10**bit < factorial[9] * bit:
        bit += 1
    return bit
"""
print upperbound()
exit()
"""

for num in range(3, 10**(upperbound()-1)):
    if sum(factorial[int(c)] for c in str(num)) == num:
        print num
        total += num
    """
    sum = 0
    for i in str(num):
        sum += factorial[int(i)]
        if sum > num:
            break
    if sum == num:
        print num
    """

print "the sum is", total
print "%.8f Secs" % (time.time() - start)
print time.asctime()

"""
145
40585
the sum is 40730
8.38617992 Secs
Wed Jun  1 15:20:03 2011
"""

"""
7
ihao-MacBook:30-39 mb375$ python p34CuriousNumsSum.py 
145
40585
the sum is 40730
93.90939498 Secs
Wed Jun  1 15:14:12 2011
"""

"""
1
2 # 1! = 1 and 2! = 2 are not sums they are not included.

145
40585

the sum of above is 40730

2011-06-01 00:19:38
"""
