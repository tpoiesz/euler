number_lengths = 1001*[0]
number_lengths[0:20] = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

number_lengths[20] = 6
number_lengths[30] = 6
number_lengths[40] = 5
number_lengths[50] = 5
number_lengths[60] = 5
number_lengths[70] = 7
number_lengths[80] = 6
number_lengths[90] = 6
print len(number_lengths)
number_lengths[1000] = 11
hundred = 7

#start with numbers smaller then 100
for num in range(21, 100):
	ones = num % 10
	number_lengths[num] = number_lengths[num - ones] + number_lengths[ones]

#do numbers between 100 and 1000
for num in range(100, 1000):
	tens = num % 100
	andWord = 3 if tens > 0 else 0
	number_lengths[num] = number_lengths[(num//100)] + hundred + andWord + number_lengths[tens]

