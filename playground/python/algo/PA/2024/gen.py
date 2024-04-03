import random

# n = random.randint(5, 10)
n = 1000
# m = random.randint(5, 1000)


def gen():
    m = 0
    adj = {}
    for i in range(1, n):
        length = random.randint(1, min(50, n - i))
        adj[i] = random.sample(range(i + 1, n + 1), length)
        m += len(adj[i])
    return m, adj


print(n)
m, adj = gen()
print(m)
for i in range(1, n):
    for j in adj[i]:
        print(i, j)
m, adj = gen()
print(m)
for i in range(1, n):
    for j in adj[i]:
        print(i, j)
