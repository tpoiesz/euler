from euler import (Primes, isPandigital)

p = Primes(100000000)
for num in [x for x in p.primes if isPandigital(str(x))]:
	print num