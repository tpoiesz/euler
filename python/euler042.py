from bitarray import bitarray

def triWord(word):
	return sum([ord(char) - ord('A') + 1 for char in word])

isTriangle = 1000 * bitarray([False])
diff = 1
num = 0
for i in range(1, 30):
	num += diff
	isTriangle[num] = True
	diff += 1

file = open('../fixtures/euler042')
words = [word.strip('"') for word in file.read().split(',')]
am = len([word for word in words if isTriangle[triWord(word)]])
print am
