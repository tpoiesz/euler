import euler as e

def isCircPrime(n):
	nstr = str(n)
	for i in range(1, len(str(n))):
		nstr = nstr[1:] + nstr[0]
		if not(p.isprime[int(nstr)]):
			return False
	return True

p = e.Primes(1000000)
circprimes = [x for x in p.primes if isCircPrime(x)]