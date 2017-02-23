import euler as e

p = e.Primes(100)

nums = []

for i in xrange(2, 100):
    nums.extend([(j, i)for j in xrange(1, i) if p.isRelativePrime(i, j)])

nums.sort(key=lambda pair: pair[0] / float(pair[1]))


def sortFrac(l1, l2):
    if l1[1] / l1[0] > l2[1] / l2[0]:
        return 1
    if l1[1] / l1[0] == l2[1] / l2[0]:
        return 0
    else:
        return 1
