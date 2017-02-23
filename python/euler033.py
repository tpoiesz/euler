def isCancelable(a, b):
	quot = float(a) / float(b)
	if a % 10 == 0 or b % 10 == 0:
		return False
	stra = str(a)
	strb = str(b)
	if stra[0] == stra[1] or strb[0] == strb[1]:
		return False
	if stra[0] == strb[1] and stra[1] == strb[0]:
		return False
	if stra[0] == strb[1]:
		return float(stra[1])/float(strb[0]) == quot
	if stra[1] == strb[0]:
		return float(stra[0])/float(strb[1]) == quot
	return False

num = 1
den = 1

for a in range(10, 100):
	for b in range(a, 100):
		if isCancelable(a, b):
			num *= a
			den *= b

print num, den
