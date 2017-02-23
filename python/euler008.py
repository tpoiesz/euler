import time

def strProd(str):
	product = 1
	for char in str:
		product *= int(char)
	return product

max = 0

start = time.time()

file = open("../fixtures/euler008")
filestr = file.read().replace("\n", "")
for col in range(0, len(filestr) - 14):
	prod = strProd(filestr[col:col+13])
	if prod > max:
		max = prod
		nums = filestr[col:col+13]

end = time.time()

print max
print nums
print end-start




