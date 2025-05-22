import asyncio
from beanie import Document, init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from beanie.odm.bulk import BulkWriter


class MyModel(Document):
    field: str
    field2: str


async def main():
    client = AsyncIOMotorClient("mongodb://localhost:27017/kosciej")
    await init_beanie(database=client.db_name, document_models=[MyModel])
    db = client.get_default_database()
    collection = db["kolekcja"]
    # await collection.insert_one({"a": "b"})
    # await MyModel.find().delete_many()
    d = {"field": "haha", "field2": "hehe"}
    # model = MyModel(field="f", field2="f2")
    # setattr(model, "extra", 1)
    await MyModel.get_motor_collection().insert_one({"field": True, "field2": True})
    # await MyModel.delete_all()
    async for row in MyModel.get_motor_collection().find({"field": True}):
        print(type(row))
        print(row)
    # async for row in MyModel.find():
    #     print(row)
    #     await row.update({"$set": d})
    #
    # # await MyModel.find().update({"$set": {"field": "updated"}})
    # async for row in MyModel.find():
    #     print(row)


asyncio.run(main())
