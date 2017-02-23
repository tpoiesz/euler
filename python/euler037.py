from euler import Primes

p = Primes(1000000)

def isTruncPrime(n):
	if not(p.isprime[n]):
		return False
	strn = str(n)
	for i in range(0, len(strn)):
		if not(p.isprime[int(strn[i:])] and p.isprime[int(strn[:len(strn) - i])]):
			return False
	return True

found = 0
sum = 0
num = 11
while found < 11:
	if isTruncPrime(num):
		sum += num
		found += 1
		print num
	num += 1

print sum
