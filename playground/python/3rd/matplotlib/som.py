import matplotlib.pyplot as plt

x = list(range(1, 10))
points = [3, 3, 5, 3, 5, 0, 1, 2, 5]

fig, ax = plt.subplots()
plt.xticks(x)
ax.bar(x, points, color="g")
plt.title("Bryza Wyzwań")
ax.set_xlabel("Zadanie")
ax.set_ylabel("Poprawne rozwiązania")
plt.savefig("podsumowanie.png")
# plt.savefig("podsumowanie.png")
