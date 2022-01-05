import pandas as pd


def f(p):
    # print(type(p))
    # return {"a": p * 10, "b": p * 20}
    return (p * 10, p * 20)


x = pd.read_csv("som.csv")
# print(x)
# x["x1"], x["x2"] = zip(*x.map(f))
x[["p1", "p2"]] = x.apply(f, result_type="expand")
print(x)
# print(x["col1"])
