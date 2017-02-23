def isPalindrome(num):
	numstr = str(num)
	for i in range(0, len(numstr)/2):
		if numstr[i] != numstr[-i - 1]: return False
	return True

max = 0
for i in range(999, 100, -1):
	for j in range(i, 100, -1):
		prod = i*j
		if prod < max:
			break
		if isPalindrome(prod):
			max = prod

print max
