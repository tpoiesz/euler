from euler import isPerm
from math import ceil

def test(n):
	for pr in range(1, 7):
		if not isPerm(str(n), str(pr*n)):
			return False
	return True

for i in range(1, 20):
	low = int(10**i)
	high = ceil(low*1.66)
	for num in range(low, int(high)):
		if test(num):
			print num

