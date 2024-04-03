from glob import glob
import pandas as pd


def simple_df() -> pd.DataFrame:
    d = {"col1": [1, 2], "col2": [3, 4]}
    return pd.DataFrame(d)


def csv_df():
    files = glob("*.csv")
    ll = [pd.read_csv(f, index_col=None, header=0) for f in files]
    return pd.concat(ll)


df = simple_df()
print(df)
print(df.dtypes)
df2 = csv_df()
print(df2)
