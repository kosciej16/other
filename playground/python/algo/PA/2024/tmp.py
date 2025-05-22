from collections import defaultdict
from sys import stdin


d = defaultdict(int)
n, k = [int(el) for el in input().split()]


for line in stdin:
    for el in (int(el) for el in line.split()):
        d[el] += 1

elements, res = 0, 0
for heigh, nr in sorted(d.items(), reverse=True):
    res = max(res, nr + min(k, elements))
    elements += nr
print(res)
