
# Project Euler - Problem 42
# 2011-05-27 13:14:16

import time

start = time.time()
words = open('words-p42.txt').read().replace('"', '').split(',')
values = []

print "%d Words" % len(words)
for w in words:
    sum = 0
    for i in w:
        sum += ord(i) - ord('A') + 1
    values.append(sum)

#print values
values.sort()
#print values

largest = values[-1]
triangles = []

n = 1
i = 2
while True:
    triangles.append(n)
    n += i
    i += 1
    if n > largest:
        break
print triangles

count = 0
for v in values:
    if v in triangles:
        count += 1

print "%.8f Secs" % (time.time() - start)
print count

# 2011-05-27 13:29:10
"""
1786 Words
[1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190]
0.01201797 Secs
162
"""
