sum = fib = old1 = 0
old2 = 1
while fib < 4000000:
	fib = old1 + old2
	sum += fib if fib % 2 == 0 else 0
	old1 = old2
	old2 = fib
print(sum)