

import math

def isPrime(num):
	if num == 1:
		return False
	elif num < 4:
		return True
	elif num % 2 == 0:
		return False
	elif num < 9:
		return True
	elif num % 3 == 0:
		return False
	else:
		r = math.floor(math.sqrt(num))
		f = 5
		while f <= r:
			if num % f == 0: return False
			if num % (f+2) == 0: return False
			f = f + 6
	return True

if __name__ == '__main__':
    print isPrime(30)
    print isPrime(7)
