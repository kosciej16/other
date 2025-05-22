from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import asyncio
from pathlib import Path

from tenacity import retry, wait_fixed, AsyncRetrying
import aio_pika
from faststream import ContextRepo, FastStream
from faststream.rabbit import RabbitBroker, RabbitExchange, RabbitQueue
from faststream.nats.annotations import NatsMessage

# from taskiq.schedule_sources import LabelScheduleSource
# from taskiq_faststream import AppWrapper, StreamScheduler

url = "amqp://localhost:5672"
broker = RabbitBroker(url=url, max_consumers=200, asyncapi_url="0.0.0.0:8000", timeout=5)

app = FastStream(broker)


queue = RabbitQueue(
    "main_queue",
    durable=True,
    arguments={
        "x-dead-letter-exchange": "",  # Default exchange
        "x-dead-letter-routing-key": "retry_queue",  # Route back to the main queue
    },
)
#
#
queue2 = RabbitQueue(
    "retry_queue",
    arguments={
        "x-message-ttl": 2 * 1000,  # 30 minutes in milliseconds
        # "x-dead-letter-exchange": "main_exchange",
        "x-dead-letter-exchange": "",
        "x-dead-letter-routing-key": "main_queue",
    },
    durable=True,
)


@app.on_startup
async def setup() -> None:
    # connection = await aio_pika.connect_robust(url)
    # channel = await connection.channel()

    await broker.connect()
    await broker.declare_queue(queue2)


MAX_WORKERS = 3  # Adjust this number based on your needs
thread_pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)


# def chain(


@dataclass
class Data:
    f1: int | None = None
    f2: str | None = None
    f3: str | None = None


async def foo1(data: Data):
    data.f1 = 10


async def foo2(data: Data):
    data.f2 = "xD"


async def foo3(data: Data):
    time.sleep(6)
    # await asyncio.to_thread(lambda: time.sleep(6))

    # await asyncio.sleep(6)
    data.f3 = "lol"


async def chain(steps, data):
    for step in steps:
        if asyncio.iscoroutinefunction(step):
            await step(data)
        else:
            await asyncio.to_thread(step, data)


async def process(steps, data):
    try:
        # await asyncio.wait_for(chain(steps, data), timeout=2)
        await asyncio.wait_for(asyncio.to_thread(lambda: asyncio.run(chain(steps, data))), timeout=2)
    except asyncio.TimeoutError:
        print("Process timed out")

    print(data)


@broker.subscriber(queue)
async def process_message(content, msg: NatsMessage):
    await process([foo1, foo2, foo3], Data())


#


# @broker.subscriber("in", retry=True)
# async def handle_msg(user: str, user_id: int) -> str:
#     await broker.publish("content", "test")
#     return f"User: {user_id} - {user} registered"


# @retry(wait=wait_fixed(10))
# async def tmp():
# raise Exception


@broker.subscriber("in", retry=True)
async def handle(content, msg: NatsMessage):
    print("IN")
    await asyncio.sleep(10)
    # await tmp()
    # print(user)
    # print(msg)
    # await msg.reject()
    # raise Exception


# async def async_chain(steps: List[Callable], data: Any):
#     for step in steps:
#         await step(data)
#
# def blocking_chain(steps: List[Callable], data: Any):
#     for step in steps:
#         if asyncio.iscoroutinefunction(step):
#             asyncio.run(step(data))
#         else:
#             step(data)
#
# async def process(steps: List[Callable], data: Any):
#     # Check if all steps are async
#     all_async = all(asyncio.iscoroutinefunction(step) for step in steps)
#
#     try:
#         if all_async:
#             # Use pure asyncio for all-async chains
#             await asyncio.wait_for(async_chain(steps, data), timeout=10)
#         else:
#             # Use thread for mixed chains
#             await asyncio.wait_for(
#                 asyncio.to_thread(partial(blocking_chain, steps, data)),
#                 timeout=10
#             )
#     except asyncio.TimeoutError:
#         print("Process timed out")
#
#     print(data)
#
#
