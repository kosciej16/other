from collections import Counter

n, m = [int(el) for el in input().split()]
cr = []
ll = []
for _ in range(n):
    s = input()
    cr.append(Counter(s))
    ll.append(s)

tmp = "".join(ll)
ck = [Counter(s) for s in (tmp[i::m] for i in range(m))]

res = []
while any(ck) or any(cr):
    for i, c, k in ((i, c, next(iter(c.keys()))) for i, c in enumerate(cr) if len(c) == 1):
        for cs in ck:
            if cs[k] == 1:
                del cs[k]
            elif cs:
                cs[k] -= 1
        res.append(f"R {i+1} {k}")
        c.clear()
    for i, c, k in ((i, c, next(iter(c.keys()))) for i, c in enumerate(ck) if len(c) == 1):
        for cs in cr:
            if cs[k] == 1:
                del cs[k]
            elif cs:
                cs[k] -= 1
        res.append(f"K {i+1} {k}")
        c.clear()

print(len(res))
for r in res[::-1]:
    print(r)
