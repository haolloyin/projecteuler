
# Project Euler - Problem 43
# 2011-05-27 19:27:32


import time

start = time.time()
primes = [2, 3, 5, 7, 11, 13, 17]
up = 10
used = [0]*up
pandigitalNum = open("permutations0to9-p43.txt", 'r').read().split('\n')


def permutation(pre):
    next = []
    for u in range(up):
        if used[u] == 0:
            next.append(u)

    p = [pre]*len(next)
    if len(next) == 0:
        #print pre
        permutationFile.write(pre+"\n")
        pandigitalNum.append(int(pre))
        return

    i = 0
    for n in next:
        p[i] += str(n)
        #print p[i]
        used[n] = 1
        permutation(p[i])
        used[n] = 0
        i += 1

def isDivisibleByPrimes(num):
    s = str(num)
    for i in range(1, 8):
        if int(s[i:i+3]) % primes[i-1] != 0:
            return False
    return True

def isPandigitalNum(num):
    for i in range(10):
        if str(i) not in num:
            return False
    return True

sum = 0
"""
permutation("")
print len(pandigitalNum)
permutationFile.close()
"""
print len(pandigitalNum)
print pandigitalNum[3628799]
print
#exit()

for n in pandigitalNum:
    if isPandigitalNum(n):
        if isDivisibleByPrimes(int(n)):
            print n
            sum += int(n)

print time.asctime()
print "%.8f Secs" % (time.time() - start)
print "sum =", sum

"""
3628801
9876543210

1406357289
1430952867
1460357289
4106357289
4130952867
4160357289
Sun May 29 14:59:38 2011
40.17463088 Secs
sum = 16695334890
"""
