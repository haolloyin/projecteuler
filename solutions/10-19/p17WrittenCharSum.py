
# Project Euler - Problem 17
# 2011-05-14 17:47:00


ty1 = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
ty = [3, 6, 6, 5, 5, 5, 7, 6, 6]

ten1 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ten = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

one1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
one = [3, 3, 5, 4, 4, 3, 5, 5, 4]


# a, ab, abc, abcd

"""
sum = 0
for i in range(1, 1000):
	num = str(i)
	charSum = 0
	size = len(num)
	print i,

	if size == 1:
		charSum += one[i-1]
	elif size == 2:
		a = int(num[0])
		b = int(num[1])
		if b == 0:
			if a == 1: # 10
				charSum += 3
			else: # 20, 30, 40 ...
				charSum += ty[a-1]
		else:
			if a == 1: # 10, 11, 12 ...
				charSum += ten[b]
			else: # 21, 22, 34, 54 ...
				charSum += (ty[a-1] + one[b-1])
			elif size == 3:
		a = int(num[0])
		b = int(num[1])
		c = int(num[2])
		charSum += (one[a-1] + len("hundred"))
		if b == 0:
			if c != 0:
				charSum += (len("and") + one[c-1])
		else:
			charSum += 3
			if c == 0:
				charSum += ten[b-1]
			else:
				if b == 1:
					charSum += ten[c]
				else:
					charSum += (ty[b-1] + one[c-1])
	sum += charSum
	print charSum
print sum+11
"""

# 2011-05-14 19:13:25

bit2 = {}
sum = 0
for i in range(1, 1000):
	num = str(i)
	charSum = 0
	size = len(num)
	print i,

	if size == 1:
		charSum += one[i-1]
		bit2[num] = one1[i-1]
		print one1[i-1],
	elif size == 2:
		a = int(num[0])
		b = int(num[1])
		if b == 0:
			if a == 1: # 10
				charSum += 3
				bit2[num] = ten1[a-1]
				print ten1[a-1],
			else: # 20, 30, 40 ...
				charSum += ty[a-1]
				bit2[num] = ty1[a-1]
				print ty1[a-1],
		else:
			if a == 1: # 10, 11, 12 ...
				charSum += ten[b]
				bit2[num] = ten1[b]
				print ten1[b],
			else: # 21, 22, 34, 54 ...
				charSum += (ty[a-1] + one[b-1])
				bit2[num] = ty1[a-1] + one1[b-1]
				print ty1[a-1], one1[b-1],
	elif size == 3:
		a = int(num[0])
		b = int(num[1])
		c = int(num[2])
		charSum = one[a-1] + len("hunderd") + 3
		if b != 0:
			charSum += len(bit2[num[1:]])
		else:
			if c == 0:
				charSum -= 3
			else:
				charSum += one[c-1]
	sum += charSum
	print charSum
print sum+11

# answer: 21124

"""
for i in bit2:
	print bit2[i]
"""
