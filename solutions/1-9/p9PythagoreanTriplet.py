
# Project Euler - Problem 9

"""
(200,375,425) : 40000 + 140625 = 180625
200 + 375 + 425 = 1000
200 + 375 = 425
200375425
"""

import time
start = time.time()
for a in range(1, 1000):
     if a > 1000:
          break
     for b in range(1, 1000):
          if a+b > 1000:
               break
          for c in range(1, 1000):
               if a+b+c > 1000:
                    break
               if a*a+b*b == c*c:
                    #print "(%d,%d,%d) : %d + %d = %d" % (a,b,c, a*a, b*b, c*c)
                    if a+b+c == 1000:
                        print "===========%d + %d = %d" % (a, b, c)
                        print "%.8f Secs" % (time.time() - start)
                        print a*b*c 
                        print time.asctime()
                        exit()

"""
===========200 + 375 = 425
59.52521420 Secs
31875000
Sat May 28 13:10:49 2011 
"""
