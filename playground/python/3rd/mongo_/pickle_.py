import pandas as pd
from pymongo import MongoClient
from pprint import pprint
import json


def get_cl():
    uri = "mongodb://127.0.0.1:27017"
    return MongoClient(uri)


cl = get_cl()
db = cl.get_database("test")
col = db.mail_decomposed
res = []
i = 0
# df = pd.DataFrame(col.find())
df = pd.read_pickle("./cascade_stats.pkl")
print(df)
# df.to_pickle("./cascade_stats.pkl")

# for el in col.find():
