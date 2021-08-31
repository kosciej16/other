from collections import deque
import typing as t
from dataclasses import dataclass


@dataclass
class V:
    v: int
    edges: t.List[int]
    visited: bool = False


v0 = V(v=0, edges=[1, 2])
v1 = V(v=1, edges=[3])
v2 = V(v=2, edges=[0, 1, 3])
v3 = V(v=3, edges=[0])

graph = [v0, v1, v2, v3]


def dfs(v: V):
    q = deque([v])
    v.visited = True
    while q:
        v = q.popleft()
        print(v)
        for e in v.edges:
            new_v = graph[e]
            if not new_v.visited:
                q.appendleft(new_v)
                new_v.visited = True


dfs(v0)
