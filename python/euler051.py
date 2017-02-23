import euler as e
from itertools import combinations

p = e.Primes(1000000)
print('ready')

for pr in [pr for pr in p.primes if pr > 50000and pr < 1000000]:
    prlist = [x for x in str(pr)]
    for idx in combinations(range(len(prlist) - 1), 3):
        prlistu = list(prlist)
        count = 0
        start = 0
        if 0 in idx:
            start = 1
        for c in range(start, 10):
            for i in idx:
                prlistu[i] = str(c)
            num = int(''.join(prlistu))
            if p.isprime[num]:
                count += 1
        if count > 7:
            print idx
            print pr
            exit()
