from itertools import permutations

def checkSSDivisibility(perm):
	divs = [1, 2, 3, 5, 7, 11, 13, 17]
	for i in range(1, 8):
		if int(''.join(perm[i:i+3])) % divs[i]:
			return False
	return True

print sum([int(''.join(x)) for x in permutations('1234567890') if checkSSDivisibility(x)])
