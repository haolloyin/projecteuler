

# Project Euler - Problem 36
# 2011-05-25 19:34:51


def isPalindromic(num):
    half = len(num) / 2
    #print "half = ", half
    for i in range(0, half):
        #print num[i], num[len(num)-1-i]
        if num[i] != num[len(num)-1-i]:
            return False
    return True

"""
print isPalindromic("12321")
print isPalindromic("123321")
print isPalindromic("123456321")
exit()
"""

def decimal2binary(num):
    result = ""
    #print "b", num,
    while num != 0:
        result = str(num % 2) + result
        num /= 2
    #print result
    return result

"""
for n in range(1, 20, 2):
    decimal2binary(n)
exit()
"""

import time
sum = 0
start = time.clock()
for n in range(1, 100*10000+1, 2):
    if isPalindromic(str(n)) and isPalindromic(decimal2binary(n)):
            print n, decimal2binary(n)
            sum += n
print sum
print "%.8f Secs" % (time.clock() - start)

# 2011-05-25 20:15:14
"""
1 1
3 11
5 101
7 111
9 1001
33 100001
99 1100011
313 100111001
585 1001001001
717 1011001101
7447 1110100010111
9009 10001100110001
15351 11101111110111
32223 111110111011111
39993 1001110000111001
53235 1100111111110011
53835 1101001001001011
73737 10010000000001001
585585 10001110111101110001
872187
1.22786000 Secs
"""
