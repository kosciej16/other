from operator import attrgetter
from dataclasses import dataclass, field
from typing import List


@dataclass
class Edge:
    v_from: "Vertex"
    v_to: "Vertex"
    weight: int

    @property
    def all_visited(self):
        return self.v_from.visited and self.v_to.visited

    def take(self):
        self.v_from.visited = True
        self.v_to.visited = True


@dataclass
class Vertex:
    value: int
    edges: List[Edge] = field(default_factory=list)
    visited: bool = False

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def __repr__(self):
        return str(self.value)


@dataclass
class Graph:
    vs: List[Vertex]
    edges: List[Edge]
    directed: bool = False

    def __init__(self, shape, directed=False):
        self.vs = [Vertex(i) for i in range(len(shape))]
        self.edges = []
        self.directed = directed
        for v_from, edges in shape.items():
            for v_to, weight in edges:
                self.add_edge(v_from, v_to, weight)

    def add_edge(self, v_from, v_to, weight):
        if isinstance(v_from, int):
            v_from = self.vs[v_from]
        if isinstance(v_to, int):
            v_to = self.vs[v_to]
        edge = Edge(v_from=v_from, v_to=v_to, weight=weight)
        self.vs[v_from.value].add_edge(edge)
        if not self.directed:
            self.vs[v_to.value].add_edge(edge)
        self.edges.append(edge)


shape = {
    0: [(1, 4), (7, 8)],
    1: [(2, 8), (7, 11)],
    2: [(3, 7), (5, 4), (8, 2)],
    3: [(4, 9), (5, 14)],
    4: [(5, 10)],
    5: [(6, 2)],
    6: [(7, 1), (8, 6)],
    7: [(8, 7)],
    8: [],
}

g = Graph(shape)
sorted_edges = sorted(g.edges, key=attrgetter("weight"))
res = []
for edge in sorted_edges:
    if not edge.all_visited:
        res.append(edge)
        edge.take()


print(res)
