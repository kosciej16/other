import dis


def f():
    d = {0}
    for n, k in enumerate(d, 1):
        d.remove(k)
        d.add(n)

    print(d)


# x = dis.dis(f)
###


def three():
    print(5 in range(10) is True)


####
def exc():
    while True:
        try:
            raise Exception
        finally:
            break


####
def dic():
    x = {1: "a", 2: "b"}
    y = {}
    for k, y[k] in x.items():
        ...

    print(y)


def weird():
    print("⅐ↁⅣⅧↂⅪ".isnumeric())
    print("ⅬⅭⅮ⅟Ⅿ³₉ↀ".isnumeric())
    print("-3".isnumeric())


def timestamp():
    from datetime import datetime

    t = 1698544740
    assert datetime.fromtimestamp(t) == datetime.fromtimestamp(r - 3600)


x, y = 10, x - 1
# timestamp()
