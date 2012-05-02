# -*- coding: cp936 -*-

# Project Euler - Problem 24
"""
# 数字
bits = [0,1,2,3,4,5,6,7,8,9]
# 阶乘：9!~1!
factors = [362880,40320,5040,720,120,24,6,2,1]
# 每一个bit的倍数
xxth = []
# 每个bit是否已被用
used = []
"""
"""
# 求阶乘
t = 1
for i in range(1,10):
    t *= i
    factors.append(t)
    print t,",",
print
"""
"""
def initUsed():
        '''初始化为未用'''
        for i in range(10):
            used.append(False)
        #print "used", used

def findBits(num):
        '''确定每一个bit上的数字'''
        initUsed()
        for f in factors:
                xxth.append(num / f)
                num %= f
        print "xxth", xxth

def findNotUsed(th):
    '''找到第th个未被使用的bit下标'''
    i = 0
    t = 0
    print "find", th , "not used",
    while t < th:
        if used[i] == False:
            t+=1
        i+=1
    print ",get", i-1,
    return i-1

def getResult():
        result = ""
        i = 0
        for t in xxth:
            if i == 8 and t == 1:
                    index = findNotUsed(1)
            else:
                    index = findNotUsed(t+1)
            #print index
            used[index] = True
            result += str(bits[index])
            i += 1
            print ",", bits[index]
        print result# + str(bits[findNotUsed(1)])

def show():
        print
        print "xxth", xxth
        #print "bits", bits
        #print "used", used

"""
"""
for i in range(1, 10+1):
        xxth = []
        used = []
        findBits(i)
        print i, ":"
        getResult()
        print
"""

import time

start = time.time()
up = 10
used = [0]*up
count = 0

def permutation(pre):
    next = []
    i = 0
    for u in range(up):
        if used[u] == 0:
            next.append(u)
    p = [pre]*len(next)
    if len(next) == 0:
        #print pre
        global count 
        count += 1
        if count == 100*10000:
            print pre
            print "%.8f Secs" % (time.time() - start)
            print time.asctime()
            exit()
        return
    for n in next:
        p[i] += str(n)
        #print p[i]
        used[n] = 1
        permutation(p[i])
        used[n] = 0
        i += 1

permutation("")

"""
2783915460
13.71989202 Secs
Sun May 29 13:01:46 2011
"""
