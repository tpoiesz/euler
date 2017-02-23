maxv = 0
maxp = 0
for p in range(10, 1000, 2):
	vl = 0
	lim = 2*p//3
	for b in range(10, p // 2):
		a = 10
		while a+b < lim and a < b:
			if p*p//2 - p * (a+b) + a*b == 0:
				vl += 1
			a += 1
	if vl > maxv:
		maxv = vl
		maxp = p
	print p
print maxp
