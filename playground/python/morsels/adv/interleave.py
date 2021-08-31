def interleave(*args):
    arr = [iter(a) for a in args]
    index = nones = 0
    while True:
        try:
            yield next(arr[index])
            nones = 0
        except StopIteration:
            nones += 1
            if nones == len(args):
                break
        index = (index + 1) % len(arr)


numbers = [1, 2, 3, 4]
x = interleave(numbers, range(5, 9))
y = interleave([1, 2, 3, 4, 5], [4, 5, 6], [7, 8, 9])
print(list(x))
print(list(y))
