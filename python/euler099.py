from math import log

file = open('../fixtures/euler099')
i = 1
maxnum = 0
maxi = 0
for line in file:
    nums = line.rstrip().split(',')
    appr = int(nums[1]) * log(int(nums[0]))
    if appr > maxnum:
        maxnum = appr
        maxi = i
    i += 1
print maxi
