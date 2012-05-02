# Project Euler - Problem 23
# created at 2011-05-19 23:14:06

def isAbundantNum(num):
    half = num / 2 + 1
    sum = 0
    for i in range(1, half):
        if num % i == 0:
            sum += i
    return sum > num

import time
abundantNums = []
start = time.clock()
for i in range(12, 28123+1):
    if isAbundantNum(i):
        abundantNums.append(i)

print "%d Secs" % (time.clock() - start)
print "the size of abundantNums is : ", len(abundantNums)

sum = 0
for i in range(1, 28123+1):
    can = False
    for num in abundantNums:
        if i > num:
            if i-num in abundantNums:
                can = True
                #print i, "can written by 2 abundant numbers"
                break
        else:
            break
    if can == False:
        sum += i
print "%d Secs" % (time.clock() - start)
print sum

# 2011-05-20 9:57:45
"""
38 Secs
the size of abundantNums is :  6965
1275 Secs = 22 Mins
4179871
"""


# 2011-05-19 23:58:45
"""
the size of abundantNums is :  6965
30 Secs
395437503
39 Secs
"""

# 2011-05-20 00:21:33
"""
the size of abundantNums is :  6965
0 Secs
459690
16 Secs
"""