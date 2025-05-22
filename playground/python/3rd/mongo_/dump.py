from datetime import datetime
from pymongo import MongoClient
from pprint import pprint
import json


def get_cl():
    uri = "mongodb://dowolkry:bJ5Ip7%7DC%7B%5D59U%3DkHb%232pTy%3DTH%5BL%5D@127.0.0.1:27017"
    return MongoClient(uri)


cl = get_cl()
# db = cl.get_database("msknedle_prod_shadow")
# col = db.returnData
db = cl.get_database("ORLICA_MAIL_TEST")
col = db.extracted_mails
res = []
i = 0
ids = [
    "000DKaK76QVU0HGX",
    "000DKaK76QVU0HHJ",
    "000DKaK76QVU0HHA",
    "000DKaK76QVU0HHC",
    "000DKaK76QVU0HJN",
    "000DKaK76QVU0HJK",
    "000DKaK76QVU0HJQ",
    "000DKaK76QVU0HJS",
    "000DKaK76QVU0HBH",
    "000DKaK76QVU0HPF",
    "000DKaK76QVU0HKW",
    "000DKaK76QVU0HKY",
    "000DKaK76QVU0HM3",
    "000DKaK76QVU0HNC",
    "000DKaK76QVU0HNE",
    "000DKaK76QVU0HNG",
    "000DKaK76QVU0HM5",
    "000DKaK76QVU0HNJ",
    "000DKaK76QVU0HPD",
    "000DKaK76QVU0HKS",
]
# for el in col.find({"InteractionId": {"$in": ids}}):

start_date = datetime(2024, 7, 1)
end_date = datetime(2024, 8, 1)

# Perform the query
query = col.find({"SentDatetime": {"$gte": start_date, "$lt": end_date}})
query = col.find()

r50, r100, r200, r400 = [], [], [], []

r = r50
cap = 50
for i, el in enumerate(query):
    print(i)
    if len(r) == cap:
        if cap == 50:
            cap = 100
            r = r100
        elif cap == 100:
            cap = 200
            r = r200
        elif cap == 200:
            cap = 400
            r = r400
        elif cap == 400:
            break

    if el["mail_info"]["mail_type"] != "IsAutoRe":
        el.pop("_id")
        el["interactionId"] = el.pop("interaction_id")
        el["mailInfo"] = el.pop("mail_info")
        r.append(el)


with open("/home/kosciej/work/pom/repos/mml_cascade_deco/cascade_service/data/test_50.json", "w+") as f:
    json.dump(r50, f, indent=4, sort_keys=True, default=str)
with open("/home/kosciej/work/pom/repos/mml_cascade_deco/cascade_service/data/test_100.json", "w+") as f:
    json.dump(r100, f, indent=4, sort_keys=True, default=str)
with open("/home/kosciej/work/pom/repos/mml_cascade_deco/cascade_service/data/test_200.json", "w+") as f:
    json.dump(r200, f, indent=4, sort_keys=True, default=str)
with open("/home/kosciej/work/pom/repos/mml_cascade_deco/cascade_service/data/test_400.json", "w+") as f:
    json.dump(r400, f, indent=4, sort_keys=True, default=str)
