import time
import asyncio


async def f():
    # time.sleep(3)
    await asyncio.sleep(3)
    print("F")


loop = asyncio.get_event_loop()
tasks = asyncio.gather(f(), f())
loop.run_until_complete(tasks)
