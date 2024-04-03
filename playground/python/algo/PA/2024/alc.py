from collections import defaultdict, deque


def add_edge(g, i, j):
    g[int(i)].add(int(j))
    g[int(j)].add(int(i))


def rem_edge(g, i, j):
    g[int(i)].remove(int(j))
    g[int(j)].remove(int(i))


g1, g2 = defaultdict(set), defaultdict(set)
n = int(input())
for _ in range(int(input())):
    add_edge(g1, *input().split())
for _ in range(int(input())):
    add_edge(g2, *input().split())
res = []


def BFS(g, add_edges=False):
    visited = [False, True, *(True if i in g[1] else False for i in range(2, n + 1))]
    d = deque(set().union(*[g[adj] for adj in g[1]]))
    order = deque()
    while d:
        el = d.popleft()
        if not visited[el]:
            order.appendleft(el)
            if add_edges:
                res.append(f"+ 1 {el}")
            add_edge(g, 1, el)
            d.extend(g[el])
            visited[el] = True
    return order


BFS(g1, add_edges=True)
for i in range(2, n + 1):
    for to_add in g2[i] - g1[i]:
        res.append(f"+ {i} {to_add}")
        add_edge(g1, i, to_add)
    for to_rem in g1[i] - g2[i] - {1}:
        res.append(f"- {i} {to_rem}")
        rem_edge(g1, i, to_rem)

to_rem = g1[1] - g2[1]
for v in (v for v in BFS(g2) if v in to_rem):
    res.append(f"- {1} {v}")
print(len(res))
for op in res:
    print(op)
