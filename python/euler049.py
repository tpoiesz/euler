import euler as e
from itertools import permutations

p = e.Primes(10000)

for prime in (x for x in p.primes if x > 1000):
	for i in range(18, (10000 - prime)/2, 18):
		num1 = prime + i
		num2 = prime + 2*i
		if e.isPerm(str(prime), str(num1)) and e.isPerm(str(prime), str(num2)) and p.isprime[num1] and p.isprime[num2]:
			print str(prime) + str(num1) + str(num2)



