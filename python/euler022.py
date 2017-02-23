import csv

def namescore(name):
	sum = 0
	for char in name:
		sum += ord(char) - ord('A') + 1
	return sum

names = []
file = open("../fixtures/euler022")
filereader = csv.reader(file)
for row in filereader:
	for name in row:
		names.append(name)

names.sort()

index = 1
total = 0

for name in names:
	total += index * namescore(name)
	index += 1

print total


