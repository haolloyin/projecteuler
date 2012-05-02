

# p14

largest = 0
num = 0
for i in range(2, 100*10000+1):
	n = i
	len = 1
	while n != 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3 * n + 1
		len += 1
	if len > largest:
		largest = len
		num = i

print num, " has ", largest, " chain."
		
