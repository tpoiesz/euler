import sys
num = 193993800
done = False
while not done:
	done = True
	for i in range(20, 3, -1):
		done = done and num % i == 0
	num += num

print num - 20
