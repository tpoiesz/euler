arr = []
file = open('../fixtures/euler081')
for line in file:
    numrow = [int(numstring) for numstring in line.rstrip().split(',')]
    arr.append(numrow)

rlen = len(arr)
clen = len(arr[0])

for j in range(rlen - 1, -1, -1):
    for i in range(clen - 1, -1, -1):
        if j == clen - 1 and i == rlen - 1:
            continue
        if j == clen - 1:
            arr[i][j] += arr[i + 1][j]
            continue
        if i == rlen - 1:
            arr[i][j] += arr[i][j + 1]
            continue
        arr[i][j] += min(arr[i + 1][j], arr[i][j + 1])

print arr
