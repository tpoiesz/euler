import Euler

isAmicable x = (sum $ divisors sumDiv) == x && sumDiv /= x where sumDiv = sum $ divisors x