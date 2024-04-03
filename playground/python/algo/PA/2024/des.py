from itertools import combinations


n, m = [int(el) for el in input().split()]
orders = [[int(el) for el in input().split()] for _ in range(m)]


def do_orders(prepared):
    soldiers = [False] * (n + 1)
    for p in prepared:
        soldiers[p] = True

    for a, b in orders:
        if soldiers[a] and not soldiers[b]:
            soldiers[a], soldiers[b] = soldiers[b], soldiers[a]
    first = soldiers.index(True)
    return all(soldiers[first : first + len(prepared)])


res = [f"{n % 2}"]
for k in range(2, n):
    tmp = 0
    for comb in combinations(range(1, n + 1), k):
        tmp += do_orders(comb)
    res.append(f"{tmp % 2}")
res.append("1")
print(" ".join(res))
