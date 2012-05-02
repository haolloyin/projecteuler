

# Project Euler-Problem 18
# 2011-05-14 15:52:30

s = """75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split(" ")

a = []
for i in s:
	if i.startswith("0"):
		a.append(int(i[1]))
	else:
		a.append(int(i))
"""
print len(a)
exit()
"""


"""
sum = 75
index = 0
l = 0
for line in range(1, 15):
	l = line * line + l
	index += line
	if a[index] > a[index+1]:
		print "left    line %d: %d > %d" % (line+1, a[index], a[index+1])
		sum += a[index]
		index += line
	else:
		print "right   line %d: %d < %d" % (line+1, a[index], a[index+1])
		sum += a[index+1]
		index += line+1
print sum
"""


#a = [3, 7, 4, 2, 4, 6, 8, 5, 9, 3]

def find(line, index):
	if line < 16:
		print a[index],
		lsum = a[index] + find(line+1, index+line)
		print
		print a[index],
		rsum = a[index] + find(line+1, index+line+1)
		print
		if lsum > rsum:
			print "line %d: l --> %d" % (line, lsum)
			return lsum
		else:
			print "line %d: r --> %d" % (line, rsum)
			return rsum
	return 0
print find(1, 0)

# 2011-05-19 12:24:52

# 1074
