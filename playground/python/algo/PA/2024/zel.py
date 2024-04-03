from math import inf

n, k, m = [int(el) for el in input().split()]
res = [inf] * m
res[0] = 0
tmp_res = [inf] * m
bank = {el: [] for el in range(1, k + 1)}
for _ in range(n):
    ki, mi, ci = [int(el) for el in input().split()]
    bank[ki].append((ki, mi, ci))


indexes = {0}
new_indexes = set()
for col in bank.values():
    while indexes:
        ind = indexes.pop()
        for ki, mi, ci in col:
            new_ind = (ind + mi) % m
            tmp_res[new_ind] = min(tmp_res[new_ind], res[ind] + ci)
            new_indexes.add(new_ind)

    indexes, new_indexes = new_indexes, indexes
    res, tmp_res = tmp_res, [inf] * m

changed = set(ind for ind, el in enumerate(res) if el != inf)
new_changed = set()

while changed:
    for c in changed:
        for i, v in enumerate(res):
            if res[(c + i) % m] > res[c] + res[i]:
                new_changed.add((c + i) % m)
                res[(c + i) % m] = res[c] + res[i]
    changed, new_changed = new_changed, changed
    new_changed.clear()

res[0] = 0
for el in res:
    print(el if el != inf else -1)
