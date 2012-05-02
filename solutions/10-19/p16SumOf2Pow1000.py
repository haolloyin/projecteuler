
"""
num = pow(2, 1000)

sum = 0

while num != 0:
	sum += num % 10
	num /= 10

print sum



sum = 0
for n in str(pow(2, 1000)):
	sum += int(n)
print sum

"""


print sum(int(digit) for digit in str(2**1000))


s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

a = s.split(" ")
for i in a:
	print int(i)
