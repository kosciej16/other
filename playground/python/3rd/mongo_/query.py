from datetime import datetime
from pymongo import MongoClient
from sys import getsizeof


# Assuming you have set up your MongoDB client, database, and collection
client = MongoClient("mongodb://dowolkry:bJ5Ip7%7DC%7B%5D59U%3DkHb%232pTy%3DTH%5BL%5D@127.0.0.1:27017")
db = client.msknedle_prod_shadow
col = db.rawData

# Define the start and end date for July 2024
res = {}
for day in range(9, 11):
    print(f"processing day {day}")
    start_date = datetime(2024, 11, day)
    end_date = datetime(2024, 11, day + 1)

    query = col.find({"timestamp": {"$gte": start_date, "$lt": end_date}})

    size = 0
    mails = 0
    for document in query:
        size += getsizeof(document)
        mails += 1

    res[day] = {"size": size // 1024, "mails": mails}

__import__("pprint").pprint(res)
