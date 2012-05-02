
# Project Euler - Problem 7

import prime
import time

start = time.time()
count = 0
p = 1
while True:
	p = p+1
    if prime.isPrime(p) == True:
		count = count+1
        print "%d : %d " % (count, p)
		if count == 10001:
 	        print "the 10001st prime is %d " % p
    	    break

print "%.8f Secs" % (time.time() - start)
print time.asctime()
print p

#104743
