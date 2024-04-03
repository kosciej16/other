from functools import reduce

h, w = [int(el) for el in input().split()]
n = int(input())
imgs = dict.fromkeys((int(el) for el in input().split()[::-1]), 0)

w_res = reduce(lambda acc, el: ({k: v if k < el else v + (acc[1] if k != el else w) // el * k // el for k, v in acc[0].items()}, acc[1] % el), imgs, (imgs, w))
h_res = reduce(lambda acc, el: (acc[0] + w_res[0][el] * (acc[1] // el), acc[1] % el), imgs, (0, h))
print(-1 if h_res[1] or w_res[1] else h_res[0])
