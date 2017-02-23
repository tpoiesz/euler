from math import sqrt
from bitarray import bitarray


class Primes:

	def __init__(self, size):
		self.primes = []
		self.isprime = bitarray(size)
		self.isprime = size * [True]
		self.isprime[1] = False
		for i in xrange(2, size):
			if self.isprime[i]:
				self.primes.append(i)
				for j in range(i*i, size, i):
					self.isprime[j] = False

	def number_of_factors(self, num):
		return len(self.prime_factors(num))

	def prime_factors(self, num):
		found = set()
		for prime in [p for p in self.primes if p <= sqrt(num)]:
			while num % prime == 0:
				p2 = num/prime
				num /= prime
				found.add(prime)
				if self.isprime[p2]:
					found.add(p2)
					return found
		return found

	def isRelativePrime(self, a, b):
		return self.prime_factors(a).isdisjoint(self.prime_factors(b))


def divisors(n):
	result = [1]
	for num in range(2, int(sqrt(n)) + 1):
		if n % num == 0:
			result.append(num)
			if n/num != num:
				result.append(n / num)
	return result


def isPalindrome(str):
	return str == str[::-1]


def isPandigital(str):
	l = len(str)
	if l > 9:
		return False
	remNum = [chr(c) for c in range(ord('1'), ord('1') + l)]
	for char in str:
		if char not in remNum:
			return False
		remNum.remove(char)
	return True


def char_range(c1, c2):
	for c in xrange(ord(c1), ord(c2) + 1):
		yield chr(c)


class Figure:

	def __init__(self, n, dim):
		self.nums = []
		self.contains = bitarray(n)
		self.contains = n*[False]

		diff = 1
		num = 0
		dim = dim - 2

		while num + diff < n:
			num += diff
			self.nums.append(num)
			self.contains[num] = True
			diff += dim


def figure_numbers(n, dim):
	diff = 1
	num = 0
	result = []
	dim = dim - 2
	for i in xrange(1, n+1):
		num += diff
		result.append(num)
		diff += dim
	return result


def triangle(n):
	return figure_numbers(n, 3)


def pentagonal(n):
	return figure_numbers(n, 5)


def hexagonal(n):
	return figure_numbers(n, 6)


def isPentagonal(num):
	return ((sqrt(24*num + 1) + 1)/6).is_integer()


def isHexagonal(num):
	return ((sqrt(8*num + 1) + 1)/4).is_integer()


def isPerm(a, b):
	return sorted(a) == sorted(b)


def gcd(a, b):
	while b != 0:
		t = a
		a = b
		b = t%b
	return a


def isRelPrime(a, b):
	return gcd(a, b) == 1


def isCube(num):
	c = int(num**(1 / 3.))
	return (c**3 == num) or ((c + 1)**3 == num)
