low = range(97, 123)

file = open('../fixtures/euler059')
crypt = [int(numstring) for numstring in file.read().rstrip().split(',')]
print len(crypt)

for i in range(0, 3):
    print i
    for c in low:
        print c
        count = 0
        for c1 in crypt[i:len(crypt):3]:
            if chr(c1 ^ c).isalnum() or chr(c1 ^ c).isspace():
                count += 1
        print count
