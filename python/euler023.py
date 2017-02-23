import euler as e
class Abundant:
	def __init__(self, n):
		self.abundant = []
		self.isAbundant = (n+1) * [False]
		for num in xrange(1,n+1):
			if sum(e.divisors(num)) > num:
				self.abundant.append(num)
				self.isAbundant[num] = True

def sumOfAbundant(n):
	for num1 in [x for x in ab.abundant if x < n]:
		if ab.isAbundant[n - num1]:
			return True
	return False


def findSmallest():
	ab = Abundant(28123)
	for i in range(28123, 0, -1):
		done = True
		for num1 in [x for x in ab.abundant if x < i]:
			if ab.isAbundant[i - num1]:
				done = False
				break
		if done:
			return i
	return 0

ab = Abundant(28123)
print sum( [x for x in range(1,28000) if not(sumOfAbundant(x))])