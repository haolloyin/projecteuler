
# coding=utf-8

# Project Euler - Problem 27
# Created at: 2011-06-13 20:36:15

from prime import isPrime
import time
import math

start = time.time()
m = 0 # 最多的 prime 数
p = 0 # prime 最多的二次方程系数之积

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        mid = int(math.ceil(-(b / 2 * a * 1.0)))
        if mid > 0 and mid == (-(b / 2 * a * 1.0)):
            for i in range(mid + 1):
                if isPrime(n**2 + a * n + b):
                    n += 1
                else:
                    break
        else:
            while isPrime(n**2 + a * n + b):
                #print a, b, n
                n += 1
        print a, b, m
        if n > m:
            p = a * b

print "%.8f Secs" % (time.time() - start)
print "Answer:", p
print "Solved at:", time.asctime()
