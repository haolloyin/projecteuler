

# filename = p21AmicableNum.py

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math

def divisorsSum(num):
	sum = 1
	i = 1
	count = 1
	for i in range(2, int(math.floor(num/2)+1)):
		if num % i == 0:
			#print i,
			count += 1
			sum += i
	#print
	return sum


a = []
sum = 0
for i in range(2, 10000):
	if i not in a:
		tempSum = divisorsSum(i)
		if tempSum != i and divisorsSum(tempSum) == i:
			a.append(tempSum)
			sum = sum + i + tempSum

print sum

"""
sum = 0
for i in range(2, 10000):
	tempSum = divisorsSum(i)
	if tempSum != i and divisorsSum(tempSum) == i:
		sum += i
"""


#print divisorsSum(220)

## 31626
