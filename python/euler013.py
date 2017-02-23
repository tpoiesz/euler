collatzLengths = []
collatzLengths.append(0)
collatzLengths.append(1)

maxChain = 1 
maxChainStart = 1

for i in xrange(2, 1000000):
	extra = 1
	n = i
	while n >= i:
		if n % 2 == 0: 
			n /= 2
		else:
			n = 3*n + 1
		extra += 1
	chain = extra + collatzLengths[n]
	collatzLengths.append(chain)
	if chain > maxChain:
		maxChain = chain
		maxChainStart = i

print maxChainStart