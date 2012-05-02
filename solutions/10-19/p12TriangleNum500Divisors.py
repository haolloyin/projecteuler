
#!python/
# filename=p12TriangleNum500Divisors.py


"""
from math import sqrt
import sys
 
# import psyco
# psyco.full()
 
def factors(x):
    ''' return the number of divisors of x
    '''
    num = 2 # itself and 1
    for i in xrange(2, int(sqrt(x)) + 1):
        if ((x % i) == 0):
            if (i != sqrt(x)):
                num += 2
            else:
                num += 1
    return num
 
def triangle():
    ''' generate triangular numbers
    '''
    i = 1
    while True:
        yield int(0.5 * i * (i + 1))
        i += 1
 
 
t = triangle()
 
while True:
    num = t.next()
    if (factors(num) >= 501):
        print num
        sys.exit(0)
"""


"""
import math
def tri(n):
	return ((n+1)*(n)/2);
for i in range(7,1000000):
	l=[]
	l.append(1)
	l.append(tri(i))
	for j in range(2,int(math.sqrt(tri(i)))+1):
		if(not tri(i)%j):
			l.append(j)
			l.append(tri(i)/j)
	if(len(l)>500):
		print i
		print tri(i)
		break
exit()
"""

"""
import math
num = 0
j = 0
j += 1
f = 0
num += j
while f < 500:
	j += 1
	f = 0
	num += j
	for i in range(1, int(round(math.sqrt(num)))):
		if num % i == 0:
			f += 2
print num
exit()
"""




"""
def countDivisors(num):
	count = 0
	i = 1
	while True:
		if num % i == 0:
			#print num, " % ", i, " == 0"
			count += 1
		if i == num:
			break
		i += 1
	return count


def findTriangleNum(num):
	result = 0
	for i in range(1, num+1):
		result += i
	return result
"""

"""
num = 1
divisorCount = 500
while True:
	triangleNum = findTriangleNum(num)
	if countDivisors(triangleNum) == divisorCount:
		print triangleNum, " has ", divisorCount, " divisors."
		break
	num += 1
"""
"""
for i in range(1, 10+1):
	num = findTriangleNum(i)
	print num
	print countDivisors(num)
	print
"""




# 2011.5.14
"""
tNum = [1]
dCount = {1:1,}

def triangleNum(num):
	if num == 1:
		tNum[0] = 1
		return tNum[0]
	else:
		tNum.append(tNum[num-2]+num)
		return tNum[num-1]
"""

"""
def divisorsCount(num):
	count = 2
	i = 2
	half = math.floor(num / 2)
	while i <= half:
		if num % i == 0:
			#print num, " % ", i, " == 0"
			count += 1
		i += 1
	return count
"""
#print divisorsCount(345239452827)
#exit()


def triangleNum(n):
	return n*(n+1)/2

"""
def divisorsCount(num):
	a = [num]
	i = 2
	quotient = num / i
	yushu = num % i
	while quotient != yushu:
		if yushu == 0:
			#print i,
			a.append(quotient)
			a.append(yushu)
		i += 1
		quotient = num / i
		yushu = num % i
	return len(a)
"""

from math import sqrt
def divisorsCount(num):
	count = 2
	for i in range(2, int(round(sqrt(num)))):
		if num % i == 0:
			if i != sqrt(num):
				count += 2
			else:
				count += 1
	return count

"""
print divisorsCount(21)
print divisorsCount(28)
exit()
"""

import time
start = time.clock()
num = 1
COUNT = 500
while True:
	t = triangleNum(num)
	if divisorsCount(t) > COUNT:
		print t, " has over ", COUNT, " divisors."
		print "(%s secs)" % (time.clock() - start)
		exit()
	num += 1


# test

"""
for i in range(10, 1, -1):
	print i,

print dCount
print 1 in dCount
dCount[2] = 2
print dCount[2]

for i in range(1, 11):
	print "%-6d :       %d" % (i,triangleNum(i))
"""




def ndiv(n, prime_factors):
    """Return number of divisors of `n`.

    prime_factors: prime factors of `n`.

    >>> from itertools import starmap
    >>> list(starmap(ndiv, ((1, []), (12, [2, 3]))))
    [1, 6]
    """
    assert n > 0
    phi = 1
    for prime in prime_factors: 
        alpha = 0 # multiplicity of `prime` in `n`
        q, r = divmod(n, prime)
        while r == 0: # `prime` is a factor of `n`
            n = q
            alpha += 1
            q, r = divmod(n, prime)
        phi *= alpha + 1 # see http://en.wikipedia.org/wiki/Divisor_function
    return phi         

def prime_factors_gen():
    """Yield prime factors for each natural number.
    
    Based on 
    http://stackoverflow.com/questions/567222/simple-prime-generator-in-python/568618#568618

    >>> from itertools import islice
    >>> list(islice(prime_factors_gen(), 20)) #doctest:+NORMALIZE_WHITESPACE
    [(1, []), (2, [2]), (3, [3]), (4, [2]), (5, [5]), (6, [3, 2]),
    (7, [7]), (8, [2]), (9, [3]), (10, [5, 2]), (11, [11]), (12, [3, 2]),
    (13, [13]), (14, [7, 2]), (15, [5, 3]), (16, [2]), (17, [17]),
    (18, [3, 2]), (19, [19]), (20, [5, 2])]
    """
    D = {1:[]} # nonprime -> prime factors of `nonprime`
    #NOTE: dictionary could be replaced by priority queue
    q = 1
    while True: # Sieve of Eratosthenes algorithm
        if q not in D: # `q` is a prime number
            D[q + q] = [q]
            yield q, [q] 
        else: # q is a composite
            for p in D[q]: # `p` is a factor of `q`
                # therefore `p` is a factor of `p + q` too
                D.setdefault(p + q, []).append(p)
            yield q, D[q]
            del D[q]
        q += 1

def highly_composite_triangular(max_ndivisors):
    '''
    Return the smallest triangular number that has more than
    max_ndivisors divisors.

    >>> # the first 25 highly compisite triangular numbers
    >>> hcts = (1, 3, 6, 28, 36, 120, 300, 528, 630, 2016,
    ...         3240, 5460, 25200, 73920, 157080, 437580,
    ...         749700, 1385280, 1493856, 2031120, 2162160,
    ...         17907120, 76576500, 103672800, 236215980)
    ...
    >>> # corresponding hct has >= number of divisors
    >>> ndivs = (1, 2, 3, 5, 7, 10, 17, 19, 21, 25, 37, 41,
    ...          49, 91, 113, 129, 145, 163, 169, 193, 241,
    ...          321, 481, 577, 649)
    >>> for maxndiv, t in zip(ndivs, hcts):
    ...     h = highly_composite_triangular(maxndiv - 1)
    ...     if h != t:
    ...        print maxndiv, h, t
    ...        break
    ... else:
    ...     print "ok"
    ...
    ok
    '''
    ndivs = {0: 0} # n -> number of divisors
    for n, pfs in prime_factors_gen():
        # save number of divisor of `n`
        ndivs[n] = ndiv(n, pfs)
        # decompose `(n-1)`th triangular number: `n * (n - 1) // 2`
        half, odd = (n//2, n-1) if n % 2 == 0 else ((n - 1)//2, n)
        # n and (n-1) do not have common factors, therefore
        # ndiv(n * (n - 1)) == ndiv(n) * ndiv(n-1)
        #NOTE: we already cached ndiv therefore there is no need to
        #      to save ndivs[half], ndivs[odd] for further use
        if ndivs[half] * ndivs[odd] > max_ndivisors:
            return half * odd  # `(n-1)`th triangular number

def main():
    import time
    start = time.clock()
    h = highly_composite_triangular(500)
    print "%d (%.2g seconds)" % (h, time.clock() - start)

if __name__=="__main__":
    main()
    import doctest; doctest.testmod()
exit()

