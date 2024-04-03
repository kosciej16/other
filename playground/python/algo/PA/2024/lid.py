from collections import Counter
from itertools import accumulate, takewhile


input()
c = Counter(int(el) for el in input().split())
sum_ = sum(c.values())
tups = ((-occ, occ - 1) for _, occ in c.most_common())
li = accumulate(tups, lambda *args: tuple(sum(x) for x in zip(*args)), initial=(sum_, 0))
print(len(list(takewhile(lambda p: p[0] > p[1], li))))
