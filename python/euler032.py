from operator import mul
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def isPandigital(str):
	if len(str) != 9:
		return False
	remNum = list(numbers)
	for char in str:
		if char not in remNum:
			return False
		remNum.remove(char)
	return True

products = []
for a in range(1, 10):
	for b in range(1000, 10000):
		c = a * b
		if c > 9999:
			break
		if isPandigital(str(a) + str(b) + str(c)):
			if c not in products:
				products.append(c)

for a in range(10, 100):
	for b in range(100, 1000):
		c = a * b
		if c > 9999:
			break
		if isPandigital(str(a) + str(b) + str(c)):
			if c not in products:
				products.append(c)

print sum(products)