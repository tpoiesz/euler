def cycle(n):
	powers = []
	elem = 1
	t = 1
	while elem not in powers:
		powers.append(elem)
		elem = (10**t) % n
		t +=1
	return t - powers.index(elem) - 1	

maxCyc = 0
maxArg = 0
for n in range(2, 1000):
	cyc = cycle(n)
	if cyc > maxCyc:
		maxCyc = cyc
		maxArg = n
print maxCyc
print maxArg
