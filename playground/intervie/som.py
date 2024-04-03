from collections import defaultdict
from dataclasses import dataclass
from typing import Any


sentinel = object()


@dataclass
class Operation:
    key: str
    before: Any
    after: Any = sentinel


class MemoryDatabase(dict):
    def __init__(self):
        print("NEW CASE")
        self.transactions = []
        self.in_transaction = False
        self.counter = defaultdict(int)

    def get(self, key):
        print(super().get(key))

    def set(self, key, value, prev=None):
        prev = prev if prev is not None else super().get(key)
        if prev is not None:
            self.counter[prev] -= 1
        if self.transactions:
            self.transactions[-1].append(Operation(key=key, before=prev, after=value))

        self.counter[value] += 1
        self[key] = value

    def delete(self, key):
        prev = super().get(key)
        del self[key]
        if self.transactions:
            self.transactions[-1].append(Operation(key=key, before=prev))

        self.counter[prev] -= 1

    def count(self, value):
        print(self.counter[value])

    def begin(self):
        self.transactions.append([])

    def commit(self):
        if not self.transactions:
            print("NO TRANSACTION")
            return

        self.transactions.clear()

    def rollback(self):
        if not self.transactions:
            print("NO TRANSACTION")
            return

        for change in self.transactions.pop()[::-1]:
            self.set(change.key, change.before, change.after)
