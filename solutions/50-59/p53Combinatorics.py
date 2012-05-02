# Project Euler - Problem 53
# Created at: 2011-06-11 13:03:50


def factorial(num):
    if num > 0:
        return reduce(lambda x, y: x * y, [i for i in range(1, num + 1)])
    else:
        return 1
    """
    f = 1
    for i in range(2, num + 1):
        f *= i
    return f
    """

import time
start = time.time()

count = 0
for n in range(1, 101):
    for r in range(1, 101):
        C_nr = factorial(n) / (factorial(r) * factorial(n - r))
        if C_nr > 100 * 10000:
            count += 1

print
print "%.8f Secs" % (time.time() - start)
print "Answer:", count
print "Solved at:", time.asctime()

"""
0.34392691 Secs
Answer: 4075
Solved at: Sat Jun 11 13:14:14 2011

You are the 17338th person to have solved this problem.
"""
