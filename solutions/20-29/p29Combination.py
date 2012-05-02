
# Project Euler - Problem 29
# 2011-05-25 12:52:13

import time
terms = []
start = time.clock()
for a in range(2, 101):
    for b in range(2, 101):
        ab = a ** b
        if ab not in terms:
            terms.append(ab)
print len(terms)
print "%.8f Secs" % (time.clock() - start)

# 2011-05-25 13:01:22
"""
9183
2.15738200 Secs
"""
