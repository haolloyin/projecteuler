
# Project Euler - Problem 48
# 2011-05-29 16:06:41

num = 1000
sum = 0
for i in range(1, num+1):
	sum = sum + i**i
print sum
s = str(sum)
print s[-10:]

"""
9110846700
"""
