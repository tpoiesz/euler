import euler as e
from math import sqrt

p = e.Primes(10000)

def test(n):
	for prime in [x for x in p.primes if x < n]:
		if (sqrt((n - prime)/2.)).is_integer():
			return True
	return False

for num in [x for x in range(9, 10000, 2) if not p.isprime[x] ]:
	if not test(num):
		print num
		break
