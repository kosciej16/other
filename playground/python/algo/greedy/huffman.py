from dataclasses import dataclass
import heapq
from typing import Optional


@dataclass
class Node:
    freq: int
    char: str
    huff: int = 0
    parent: Optional["Node"] = None

    def __lt__(self, other):
        return (self.freq, self.char) < (other.freq, other.char)


chars = ["a", "b", "c", "d", "e", "f"]
freq = [5, 9, 12, 13, 16, 45]
ll = [Node(freq=f, char=c) for f, c in zip(freq, chars)]
d = {n.char: n for n in ll}

heapq.heapify(ll)
while True:
    if len(ll) == 1:
        break
    print(ll)
    left, right = heapq.heappop(ll), heapq.heappop(ll)
    right.huff = 1
    new = Node(left.freq + right.freq, left.char + right.char)
    left.parent = new
    right.parent = new
    heapq.heappush(ll, new)


def print_code(c):
    root = d[c]
    res = [root.huff]
    while root := root.parent:
        res.append(root.huff)
    return res[-2::-1]


for c in chars:
    print(c, print_code(c))
