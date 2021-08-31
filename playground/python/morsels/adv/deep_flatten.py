from typing import Iterable
from functools import reduce
from operator import add


def deep_flatten(ll):
    # return [k for l in ll for k in l]
    for l in ll:
        if isinstance(l, Iterable) and not isinstance(l, str):
            for x in deep_flatten(l):
                yield x
            # return reduce(add, [deep_flatten(el) for el in ll], [])
        # print(ll)
        else:
            yield l


# numbers_and_words = enumerate([99, 98, 97])
# flattened = deep_flatten(numbers_and_words)
# print(next(flattened))
# print(next(flattened))
# print(next(numbers_and_words))
# print([1, 2] + [3])
# print(reduce(add, [[1, 2], [3]]))
# print(sum([[1, 2], [3]]))
# res = deep_flatten([[1, [2, 3]], 4, 5])
res = list(deep_flatten([["apple", "pickle"], ["pear", "avocado"]]))
print(res)
# res = deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
# print(res)
# res = deep_flaten([[1]])
# print(res)
Or
