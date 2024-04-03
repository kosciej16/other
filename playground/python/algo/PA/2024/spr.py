from collections import defaultdict

g1, g2 = defaultdict(set), defaultdict(set)


def assert_op(i, j, add=True):
    # print(g1, i, j, add)
    if add:
        assert j not in g1[i], j
        assert i not in g1[j], i
    else:
        assert j in g1[i], j
        assert i in g1[j], i
    adj = set().union(*[g1[adj] for adj in g1[i]])
    assert j in adj, (adj, g1)


def add_edge(g, i, j, ver=True):
    if ver:
        assert_op(int(i), int(j))
    g[int(i)].add(int(j))
    g[int(j)].add(int(i))


def rem_edge(g, i, j, ver=True):
    if ver:
        assert_op(int(i), int(j), add=False)
    g[int(i)].remove(int(j))
    g[int(j)].remove(int(i))


with open("in") as f:
    n = int(f.readline())
    for _ in range(int(f.readline())):
        add_edge(g1, *f.readline().split(), ver=False)
    for _ in range(int(f.readline())):
        add_edge(g2, *f.readline().split(), ver=False)

with open("out") as f:
    assert int(f.readline()) <= 200000
    for line in f.readlines():
        # print(line)
        sign, i, j = line.split()
        if sign.startswith("+"):
            add_edge(g1, i, j)
        elif sign.startswith("-"):
            rem_edge(g1, i, j)
        else:
            raise RuntimeError()

for i in range(1, n + 1):
    assert g1[i] == g2[i]
