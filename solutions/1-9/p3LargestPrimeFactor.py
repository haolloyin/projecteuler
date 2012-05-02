
# Project Euler - Problem 3

import prime,math,time

"""
def isPrime(num):
    mid = int(math.sqrt(num))+1
    for i in range(2, mid):
        if num%i == 0:
            return 0
    return 1
"""

#print(isPrime(2))
start = time.time()
num = 600851475143
maxFacotr = 0
i = 2
while(i < math.floor(math.sqrt(num))):
    if prime.isPrime(i) and num % i==0:
         print "%s is a prime factor\n" % i
         maxFactor = i
    i = i+1

print "%.8f Secs" % (time.time() - start)
print maxFactor
print time.asctime()

#6857


"""
71 is a prime factor

839 is a prime factor

1471 is a prime factor

6857 is a prime factor

5.03163290 Secs
6857
Fri May 27 13:14:03 2011
"""
