def inc(fac):
    global num
    global den
    global tnum
    global tden
    global tempnum
    global tempden
    tempnum = num
    tempden = den
    num = fac * num + tnum
    den = fac * den + tden
    tnum = tempnum
    tden = tempden


num = 2
den = 1
tnum = 1
tden = 1
tempnum = 0
tempden = 0


for k in range(1, 34):
    inc(1)
    inc(2 * k)
    inc(1)

print num
