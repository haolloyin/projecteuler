
# Project Euler - Problem 45
# 2011-05-27 19:40:06

import time
start = time.time()
p = 166
h = 144
t = 285

def isPentagonal(num):
    global p
    while True:
        pen = (p*p*3-p)/2
        if pen == num:
            return True
        elif pen > num:
            return False
        p += 1

def isHexagonal(num):
    global h
    while True:
        hexa = (h*h*2-h)
        if hexa == num:
            return True
        elif hexa > num:
            return False
        h += 1


while True:
    tn = (t*t+t)/2
    if isPentagonal(tn) and isHexagonal(tn):
        print tn
        break
    t += 1

print "%.8f Secs" % (time.time() - start)
print time.asctime()


"""
1284953670
1295674380
1427385960
"""

"""
1533776805
0.11855507 Secs
Sun May 29 16:02:47 2011
"""
