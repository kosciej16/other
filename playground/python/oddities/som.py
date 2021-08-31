import dis


def f():
    d = {0}
    for n, k in enumerate(d, 1):
        d.remove(k)
        d.add(n)

    print(d)


x = dis.dis(f)
###

print(5 in range(10) == True)


####
while True:
    try:
        raise Exception
    finally:
        break

####
x = {1: "a", 2: "b"}
y = {}
for k, y[k] in x.items():
    ...

# print(y)

print("⅐ↁⅣⅧↂⅪ".isnumeric())
print("ⅬⅭⅮ⅟Ⅿ³₉ↀ".isnumeric())
print("-3".isnumeric())
