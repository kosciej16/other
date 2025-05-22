import asyncio
from datetime import datetime, timezone

from enum import Enum
import logging
from pymongo import IndexModel


from beanie import BulkWriter, Indexed, init_beanie, Document

from motor.core import AgnosticClient
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from functools import partial

from pydantic import Field


conn = "mongodb://localhost:27017/kosciej"
client = AsyncIOMotorClient(conn)


class MyEnum(str, Enum):
    A = "abc"


class Category(BaseModel):
    name: str
    description: str
    en: MyEnum


class Product(Document):  # This is the model
    name: str
    inserted_at: datetime = Field(default_factory=partial(datetime.now, timezone.utc))
    # description: str | None = None
    price: Indexed(float)
    # category: Category

    class Settings:
        indexes = [IndexModel(["created_at"], name="test_string_index_DESCENDING", expireAfterSeconds=10)]
        name = "products"


async def init():
    # Create Motor client

    # Initialize beanie with the Sample document class and a database
    await init_beanie(database=client.db, document_models=[Product])


db = client.db
collection = db.cl


async def insert():
    async with BulkWriter() as bulk_writer:
        for _ in range(1000):
            # await Product(name="Tony's", price=5.95)
            await Product(name="Tony's", price=5.95).insert()


async def test():
    to_update = []
    async with BulkWriter() as bulk_writer:
        async with BulkWriter() as bulk_writer2:
            async for row in Product.find_all():
                # print(row)
                # await Product.find_one({Product.id: row.id}).set({Product.price: 12345})
                # row.set({Product.price: 10})
                # print(prod)
                row.price = 7
                await row.save(bulk_writer=bulk_writer2)
                row.price = 8
                await row.save(bulk_writer=bulk_writer)
        # await bulk_writer.commit()


async def index():
    pass
    # a = client.create_index()
    # print(type(a))
    # print(a)


async def test2():
    to_update = []
    async for row in Product.find_all():
        # await Product.find_one({Product.id: row.id}).set({Product.price: 12345})
        # row.set({Product.price: 10})
        # print(prod)
        row.price = 3
        await row.replace()


# async def do_insert():
#     document = {"key": "value"}
#     result = await collection.insert_one(document)
#     print("result %s" % repr(result.inserted_id))


loop = client.get_io_loop()
loop.run_until_complete(init())
# loop.run_until_complete(insert())
# chocolate = Category(name="Chocolate", description="A preparation of roasted and ground cacao seeds.", en=MyEnum.A)
# tonybar = Product(name="Tony's", price=5.95, category=chocolate)
# marsbar = Product(name="Mars", price=1, category=chocolate)
loop.run_until_complete(insert())
loop.run_until_complete(test())
# loop.run_until_complete(test2())
# async def dev_delete_collections() -> None:
#     log.info("Deleting documents from mongo...")
#     res = await EmlStat.find().delete_many()
#     if res:
#         log.info(f"Deleted {res.deleted_count} stat docs")
