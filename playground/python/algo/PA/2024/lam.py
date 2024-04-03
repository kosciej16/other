from array import array
from collections import Counter, defaultdict

a = array("u")

n, m = [int(el) for el in input().split()]
cr = [defaultdict(int) for _ in range(n)]
ck = [defaultdict(int) for _ in range(m)]
ll = []
for i in range(n):
    ll.append(input())

# i = 0
for i, sub in enumerate(ll):
    for c in sub:
        cr[i // m][c] += 1
        ck[i%m][c] += 1
        # i += 1
    # for i, el in enumerate(s := input()):
    # for c in input():
    # tmp[ord(el) - 65] += 1
    #     cs[i][el] += 1

# res = []
# iters = 0
# while any(cs):
#     # print(iters)
#     for i, c, k in ((i, c, next(iter(c.keys()))) for i, c in enumerate(cs) if len(c) == 1):
#         tmp = Counter([k])
#         for csv in cs[slice(*(m, None) if i < m else (0, m))]:
#             csv -= tmp
#         c.clear()
#         res.append(f"{'K' if i < m else 'R'} {i+1 if i < m else i - m + 1} {k}")
#     # iters += 1

# print(len(res))
# for r in res[::-1]:
#     print(r)
