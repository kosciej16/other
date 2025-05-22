import asyncio


async def foo2():
    await asyncio.sleep(1)
    print("FOO2")


async def foo():
    await asyncio.sleep(5)
    print("FOO")


async def main():
    for h in (foo2, foo2, foo):
        await h()
    # await asyncio.sleep(3)


asyncio.run(main())
