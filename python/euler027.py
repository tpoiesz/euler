import euler as e

maxNPrimes = 0
maxArg = []

p = e.Primes(1000000)
for a in range(-1000, 1000):
	for b in [x for x in p.primes if x < 1000]:
		n = 0
		num = n*n + a*n + b
		while p.isprime[num]:
			n += 1
			num = n*n + a*n + b
		if n > maxNPrimes:
			maxNPrimes = n
			maxArg = [a, b]

print maxNPrimes
print maxArg
