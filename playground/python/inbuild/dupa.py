import csv

with open("som.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        print(type(row))
