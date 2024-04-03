size = 24
cube = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(size)]


def sur(i, j, k):
    if cube[i][j][k]:
        yield (i + 1, j, k)
        yield (i - 1, j, k)
        yield (i, j + 1, k)
        yield (i, j, k + 1)
        yield (i, j - 1, k)
        yield (i, j, k - 1)


with open("in2.txt") as f:
    for line in f.readlines():
        i, j, k = line.split(",")
        cube[int(i) + 1][int(j) + 1][int(k) + 1] = 1

print(cube)
res = 0
for i in range(1, size - 1):
    for j in range(1, size - 1):
        for k in range(1, size - 1):
            for s1, s2, s3 in sur(i, j, k):
                res += cube[s1][s2][s3] == 0

print(res)
