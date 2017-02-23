import euler as e

p = e.Primes(100000)
found = 0
for num in range(646, 200000):
	if p.number_of_factors(num) == 4:
		found += 1
		if found == 4:
			print num - 3
			break
	else:
		found = 0
