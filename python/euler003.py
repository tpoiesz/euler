def largestPrimeFactor(num):
	num2 = num/2
	i = 2
	while i < num2:
		while num % i == 0:
			num /= i
			print num
		if num == 1:
			return i
		i += 1

print largestPrimeFactor(600851475143)