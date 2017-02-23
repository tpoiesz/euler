import euler as e

p = e.Primes(1000)
seqs = 1000*[0]
seqs[2] = 1

max_sequence = 1
max_arg = 2

for num in range(2, 1000):
	max_seq = 0
	for s_prime in [x for x in p.primes  if x < num]:
		h_prime = num - s_prime
		if seqs[h_prime] > max_seq:
			max_seq = seqs[h_prime]
	seqs[num] = max_seq + 1
	if p.isprime[num] and max_seq > max_sequence:
		max_sequence = max_seq
		max_arg = num

print max_arg
print max_sequence



