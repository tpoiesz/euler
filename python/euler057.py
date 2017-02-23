numer = 1
denom = 1
count = 0

for i in range(0, 1000):
    h = denom
    denom += numer
    numer += 2 * h
    if len(str(numer)) > len(str(denom)):
        count += 1

print count
