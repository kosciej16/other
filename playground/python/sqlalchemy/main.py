import pandas as pd
from model import Model, Session
import csv

s = Session()


# df = pd.read_csv("input.csv")
with open("input.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# print(rows[0])
print(type(rows[0]))
# for index, row in df.iterrows():
#     x = row["DeclaredIncomeAmount"]
#     print(x)
#     print(type(x))
#     row = df.loc[index]
#     for c in row:
#         print(c)
#     x = row["DeclaredIncomeAmount"]
#     print(x)
#     print(type(x))
#     break

#     # m = Model(num=int(row["col1"]))
#     # s.add(m)
#     # s.commit()
