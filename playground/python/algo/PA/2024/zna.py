from collections import Counter
from itertools import accumulate

n = int(input())
res = [0] * n
c = Counter(int(el) for el in input().split())
for val in c.values():
    for i in range(1, val // 2 + 1):
        res[val // i - 1] += 1

for el in [n, *[k * el for k, el in zip(range(n, 1, -1), accumulate(res[::-1]))][::-1]]:
    print(el, end=" ")
