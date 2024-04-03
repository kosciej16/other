from collections import Counter

n, m = [int(el) for el in input().split()]
cs = [Counter() for _ in range(m)]
for _ in range(n):
    for i, el in enumerate(s := input()):
        cs[i][el] += 1
    cs.append(Counter(s))


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
