cal = 0
with open("input.txt") as f:
    calories = []
    for line in f.readlines():
        if not line.strip():
            calories.append(cal)
            cal = 0
            continue
        cal += int(line)

calories.append(cal)
print(sum(sorted(calories[-3:])))
print(sum(sorted(calories)[-3:]))
# print((sorted(calories)[-1]))
