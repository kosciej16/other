import itertools


def window(gen, n):
    ll = list(gen)
    return [tuple(itertools.islice(ll, i, i + n)) for i in range(len(ll) - n)]


ll = [1, 2, 3, 4]
print(list(window(ll, 2)))
numbers = [1, 2, 3, 4, 5, 6]
squares = (n ** 2 for n in numbers)
print(window(squares, 4))
