from euler import isPandigital

max = 123456789

for num in xrange(10000, 100000):
	for lim in range(1,10):
		cat = ''
		for n in range(1, lim+1):
			cat += str(num * n)
			if len(cat) > 9:
				break
		if isPandigital(cat) and int(cat) > max:
			max = int(cat)
print max

