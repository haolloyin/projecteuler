
# Project Euler - Problem 38
# 2011-05-26 23:56:22


def isPandigital(num):
    s = str(num)
    for i in range(1, 9+1):
        if str(i) not in s:
            return False
    return True

import time

n = 1
pandigital = 0
flag = True
start = time.clock()
while flag:
    for i in range(2, 10):
        s = ''
        for j in range(1, i+1):
            s += str(n*j)
        print n, j, s
        if len(s) > 9:
            if i == 2:
                flag = False
            break
        else:
            if isPandigital(s):
                pandigital = max(int(s), pandigital)
    n += 1

print "%.8f Secs" % (time.clock() - start)
print pandigital

# 2011-05-27 01:09:07
"""
1 2 12
1 3 123
1 4 1234
1 5 12345
1 6 123456
1 7 1234567
1 8 12345678
1 9 123456789
2 2 24
2 3 246
2 4 2468
2 5 246810
2 6 24681012
2 7 2468101214
...
9998 3 99981999629994
9999 2 999919998
9999 3 99991999829997
10000 2 1000020000

0.29738100 Secs
932718654
"""
