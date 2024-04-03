import pandas as pd

df = pd.read_csv("b.csv")
print(df)
date = df.loc[:, "Date"]
print(date)
for d in date:
    date_object = datetime.strptime(d, "%Y-%m-%d").date()
    # print(date_object)
    weekdayidx = date_object.isoweekday()
    # print(weekdayidx)
    if weekdayidx == 6:
        date_final = date_object.replace(day=date_object.day + 2)
    elif weekdayidx == 7:
        date_final = date_object.replace(day=date_object.day + 1)
    else:
        date_final = date_object
    print(date_final)
    df["Date"] = df["Date"].replace({"d": "date_final"})
    df.to_csv("Book1.csv", index=False)
    print(df)
