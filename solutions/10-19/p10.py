import prime

sum = 0

for i in range(2, 200*10000+1):
	if prime.isPrime(i):
		print i, " ",
		sum += i

print "\nsum = ", sum

