

def factorial(num):
	temp = 1
	for i in range(1, num+1):
		temp *= i
	return temp

num = factorial(100)
#print num
sum = 0
while num != 0:
	sum += num % 10
	num /= 10
print sum
