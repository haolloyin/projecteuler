# Project Euler - Problem 32
# Created at: 2011-06-11 12:04:48

def isPandigitalNum(num):
    for i in range(1, 10):
        if str(i) not in num:
            return False
    return True

'''
print isPandigitalNum("123456789")
'''

import time
start = time.time()

b = 1
num = ''
products = []

for a in xrange(1, 99 + 1):
    b = 1
    if str(0) not in str(a):
        while True:
            if str(0) in str(b):
                b += 1
                continue
            p = a * b
            if str(0) in str(p):
                b += 1
                continue
            num = str(a) + str(b) + str(p)
            if len(num) == 9:
                if isPandigitalNum(num):
                    if p not in products:
                        products.append(p)
                        print "%3d * %4d = %d" % (a, b, p)
            elif len(num) > 9:
                break
            b += 1
print
print "%.8f Secs" % (time.time() - start)
print "Answer:", sum(products), products
print "Solved at:", time.asctime()

"""
  4 * 1738 = 6952
  4 * 1963 = 7852
 12 *  483 = 5796
 18 *  297 = 5346
 28 *  157 = 4396
 39 *  186 = 7254
 48 *  159 = 7632

0.41064405 Secs
Answer: 45228 [6952, 7852, 5796, 5346, 4396, 7254, 7632]
Solved at: Sat Jun 11 12:39:30 2011

  4 * 1738 = 6952
  4 * 1963 = 7852
 12 *  483 = 5796
 18 *  297 = 5346
 28 *  157 = 4396
 39 *  186 = 7254
 48 *  159 = 7632

0.20485616 Secs
Answer: 45228 [6952, 7852, 5796, 5346, 4396, 7254, 7632]


You are the 16198th person to have solved this problem.
"""
