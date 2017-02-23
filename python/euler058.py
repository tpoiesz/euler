import euler as e

p = e.Primes(800000000)

pratio = 1
side = 1
diff = 0
end = 1
tprimes = 0.
total = 1

while pratio > 0.1:
    nprimes = 0
    diff += 2
    side += 2
    start = end + diff
    end = start + diff * 3
    for num in range(start, end + 1, diff):
        if p.isprime[num]:
            nprimes += 1
            tprimes += 1
        total += 1
    pratio = tprimes / total
    print nprimes
    print pratio

print side
