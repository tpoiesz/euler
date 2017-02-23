from math import factorial

amounts = [0]


def sumOfFacDigits(x):
    return sum([factorial(int(a)) for a in str(x)])


def facChain(i):
    global amounts
    chain = [i]
    j = sumOfFacDigits(i)
    if j < len(amounts):
        return amounts[j] + 1
    while j not in chain:
        chain.append(j)
        j = sumOfFacDigits(j)
        if j < len(amounts):
            return amounts[j] + len(chain)
    return len(chain)


count = 0
for i in range(1, 1000000):
    if facChain(i) == 60:
        count += 1
        print i
print count
