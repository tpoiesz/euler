total = 1
end = 1

for i in range(2,1001 // 2 + 2):
	diff = (i-1) * 2
	start = end + diff
	end = (2 * i - 1)**2
	total += sum(range(start, end+diff, diff))
print total

