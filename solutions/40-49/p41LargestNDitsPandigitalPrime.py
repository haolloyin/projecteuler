
# Project Euler - Problem 41
# 2011-05-26 19:41:09

import time
from prime import isPrime

start = time.clock()
largest = 987654321

def isPandigital(num):
    s = str(num)
    for i in range(1, 9+1):
        if str(i) not in s:
            return False
    return True

"""
print isPandigital(largest)
print isPrime(largest)
for i in range(10, 0, -1):
    print i
exit()
"""

up = 0
used = [0]*up
pfile = open('words-p42.txt', 'w')

def permutation(pre):
    next = []
    for u in range(up):
        if used[u] == 0:
            next.append(u)

    p = [pre]*len(next)
    if len(next) == 0:
        pfile.write(pre+"\r\n")
        return

    i = 0
    for n in next:
        p[i] += str(n+1)
        used[n] = 1
        permutation(p[i])
        used[n] = 0
        i += 1

def initPandigitalFile():
    for i in range(2, 10):
        global up, used, pfile
        up = i
        used = [0]*up
        pfile.close()
        pfile = open("permutations1to" + str(i) +"-p41.txt", 'w')
        permutation("")
        pfile.close()

"""
initPandigitalFile()
exit()
"""

"""
permutation("")
exit()
"""
#pandigitalNum = open("permutations1to9-p41.txt", 'r').read().split('\r\n')

for i in range(8, 1, -1):
    pandigitalNum =  open("permutations1to"+str(i)+"-p41.txt", 'r').read().split('\r\n')
    print pandigitalNum.pop()
    print pandigitalNum[-1]
    pandigitalNum.reverse()
    print pandigitalNum[-1]

    for i in pandigitalNum:
        #print i
        if isPrime(int(i)):
            print i
            exit()

print time.asctime()
print "%.8f Secs" % (time.clock() - start)

"""
2011-05-29 15:49:08
7652413
"""
