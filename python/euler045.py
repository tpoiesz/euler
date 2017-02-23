import euler as e

num = 0
diff = 1
while True:
	num += diff
	if e.isPentagonal(num) and e.isHexagonal(num) and num > 40755:
		print num
		break
	diff += 1
