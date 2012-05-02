

a = 1
b = 1
num = 1
i = 2

while True:
	s = str(num)
	if len(s) != 1000:
		num = a + b
		a = b
		b = num
		i += 1
	else:
		print num, " contains 1000 dits."
		print i
		break
