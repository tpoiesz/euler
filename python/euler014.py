pyr = []

file = open("../fixtures/euler014")
for line in file:
	pyr.append([int(n) for n in line.split()])

for i in range(len(pyr) - 2, -1, -1):
	line = pyr[i]
	for j in range(0, len(line)):
		line[j] += max(pyr[i+1][j], pyr[i+1][j+1])

print pyr
