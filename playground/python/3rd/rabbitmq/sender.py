import asyncio
from faststream.rabbit import RabbitBroker


async def pub(data) -> None:
    async with RabbitBroker("amqp://guest:guest@localhost:5672") as broker:
        await broker.publish(data, "test")


for i in range(1):
    data = {"a": i}
    asyncio.run(pub(data))
