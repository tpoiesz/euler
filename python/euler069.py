import euler as e
from operator import mul

p = e.Primes(1000000)
maxphi = 0
maxarg = 0

for num in range(4, 100000, 2):
    factors = p.prime_factors(num)
    a = [1 - 1. / pr for pr in factors]
    phi = 1 / reduce(mul, a)
    if phi > maxphi:
        maxphi = phi
        maxarg = num

print maxarg
print maxphi
