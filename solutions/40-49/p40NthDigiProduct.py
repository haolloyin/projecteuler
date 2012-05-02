
# Project Euler - Problem 40
# 2011-05-26 19:24:47

import time

start = time.clock()
s = ''
dits = 0
n = 1
while dits < 10**6:
    s += str(n)
    dits += len(str(n))
    n += 1

#print s
#p = int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999])

p = 1
b = [0, 9, 99, 999, 9999, 99999]
for i in b:
    p *= int(s[i])
print
print "%.8f Secs" % (time.clock() - start)
print p

# 2011-05-26 19:35:28
"""
0.31763400 Secs
210
"""
