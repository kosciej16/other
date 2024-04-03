# Operators
class A:
    ...


# sum([A(), A(), A()])  # how to make it work

########

lt = ([1, 2, 3],)
lt[0] += (1,)


# type(1j)  # What's this
# type(...)  # And this
x = """" """
print(type(x))  # And this
print(x)

# OrderedDict
# interning

########

l = [10, 20, 30, 40, 50]
# write a code that counts elements greater than 20. Do not use len function

i = 4


def foo(x):
    def bar():
        print(i, end="")

    # ...
    # A bunch of code here
    # ...
    for i in x:  # Ah, i *is* local to foo, so this is what bar sees
        print(i, end="")
    bar()


# pylint: disable=redefined-outer-name
