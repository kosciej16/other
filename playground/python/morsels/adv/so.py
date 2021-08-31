from math import sqrt

from dunder_all import start_public_attributes

start_public_attributes()

root5 = sqrt(5)
phi = (1 + root5) / 2  # The golden ratio


def nth_lucas(n):
    """Return the n-th Lucas number."""
    return round(phi ** n + (-1 / phi) ** n)


def sum_of_squares(*numbers):
    return sum(n ** 2 for n in numbers)


print("A")
