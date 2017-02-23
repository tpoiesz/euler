def findLeftFrac(n, d):
    for num in range(12000, 0, -1):
        new_n = (n * num - 1.) / d
        if new_n.is_integer():
            return (new_n, num)
    return (0, 0)


count = 0
frac = (1, 2)

while frac != (1, 3):
    print frac
    frac = findLeftFrac(frac[0], frac[1])
    count += 1

print count
