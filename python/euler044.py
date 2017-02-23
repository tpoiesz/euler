import euler as e

pen = e.Figure(10000000, 5)

for num1 in pen.nums:
	i = 0
	num2 = 0
	while num2 < num1 and num1 + pen.nums[i] < 10000000:
		num2 = pen.nums[i]
		if pen.contains[num1 + num2] and pen.contains[num1 - num2]:
			print num1 - num2
		i += 1
