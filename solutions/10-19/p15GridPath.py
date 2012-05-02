

# Project Euler - Problem 15
# 2011-05-19 12:25:20

n = 5
grid = []
for i in range(0, n):
	grid.append([])
	for j in range(0, n):
		grid[i].append(1)
"""

n = 5
grid = [[1] * n] * n
"""
print grid



#exit()

for r in range(1, n):
	for c in range(1, n):
		grid[r][c] = grid[r-1][c] + grid[r][c-1]
		print "%-4d" % grid[r][c],
	print


for r in range(0, n):
	for c in range(0, n):
		print "%-4d" % grid[r][c],
	print

print grid[-1][-1]

# 137846528820

# 2011-05-19 12:45:36
