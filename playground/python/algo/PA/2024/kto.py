res = {0: "Algosia", 1: "Bajtek"}
a = [0] * 11
b = [0] * 11
for points in (int(el) for el in input().split()):
    a[10 - points] += points
for points in (int(el) for el in input().split()):
    b[10 - points] += points

if sum(a) == sum(b):
    if a == b:
        print("remis")
    else:
        print(res[a < b])
else:
    print(res[sum(a) < sum(b)])
