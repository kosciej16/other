import time
import asyncio

from faststream import FastStream
from faststream.rabbit import RabbitQueue

# from brok import broker
from tmp import foo

from faststream.rabbit import RabbitBroker


url = "amqp://localhost:5672"
broker = RabbitBroker(url=url, max_consumers=200, asyncapi_url="0.0.0.0:8000", timeout=5)


app = FastStream(broker)


queue = RabbitQueue("test")


@app.on_startup
async def setup() -> None:
    pass
    # connection = await aio_pika.connect_robust(url)
    # channel = await connection.channel()

    # await broker.connect()
    # await broker.declare_queue(queue2)


@broker.subscriber(queue)
async def process_message(content):
    await foo()
    print("GOT MESSAGE", content)
    time.sleep(2)
    # await broker.publish(content, "test2")


async def run() -> None:
    await app.run()


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()
